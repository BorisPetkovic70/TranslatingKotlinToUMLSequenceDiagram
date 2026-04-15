import re
from typing import Dict, List, Any
try:
    from gen.KotlinParserVisitor import KotlinParserVisitor
    from gen.KotlinParser import KotlinParser
except:
    from KotlinParserVisitor import KotlinParserVisitor
    from KotlinParser import KotlinParser

class KotlinSemanticAnalyzer(KotlinParserVisitor):
    def __init__(self):
        self.objects = {}              
        self.creation_order = []       
        self.var_types = {}            
        self.instance_vars = {}        
        self.sequence_flow = []
        self.current_class = None
        self.current_method = None
        self.inside_main = False
        self.pending_var = None
        self.call_depth = 0
        self.debug = True
        self.method_return_types = {}
        self.local_vars = {}
        self.method_returns = {}
        self.parsing_classes = False
        self.method_bodies = {}  # Stores method blocks for later inlining
        self.current_caller = None

    def log(self, msg):
        if self.debug:
            print(f"[DEBUG] {msg}")

    def visitKotlinFile(self, ctx: KotlinParser.KotlinFileContext):
        # Initial pass to identify top-level objects
        self.log(f"KotlinFile has {len(ctx.topLevelObject())} top-level objects")
        
        for i, child in enumerate(ctx.topLevelObject()):
            if child.classDeclaration():
                class_name = child.classDeclaration().IDENTIFIER().getText()
                self.log(f"  Top-level {i}: Class {class_name}")
            elif child.functionDeclaration():
                func_name = child.functionDeclaration().IDENTIFIER().getText()
                self.log(f"  Top-level {i}: Function {func_name}")
        
        # Pass 1: Visit classes to store their method structures for inlining
        for child in ctx.topLevelObject():
            if child.classDeclaration():
                self.parsing_classes = True
                self.visit(child)
                self.parsing_classes = False
        
        # Pass 2: Visit the main function to trigger the sequence trace
        for child in ctx.topLevelObject():
            if child.functionDeclaration():
                func = child.functionDeclaration()
                if func.IDENTIFIER().getText() == "main":
                    self.parsing_classes = False
                    self.inside_main = True
                    self.current_method = "main"
                    self.call_depth = 0
                    self.log(f"Starting MAIN function traversal")
                    
                    if func.block():
                        self.visit(func.block())
                    
                    self.inside_main = False
                    self.current_method = None
                    break
        
        return None
    
    def visitClassDeclaration(self, ctx: KotlinParser.ClassDeclarationContext):
        class_name = ctx.IDENTIFIER().getText()
        old_class = self.current_class
        self.current_class = class_name
        self.instance_vars[class_name] = {}
        
        self.log(f"Entering Class: {class_name}")
        
        if ctx.primaryConstructor():
            self.visit(ctx.primaryConstructor())
        
        if ctx.classBody():
            body = ctx.classBody()
            if body.classMemberDeclarations():
                for member in body.classMemberDeclarations().classMemberDeclaration():
                    if member.functionDeclaration():
                        self.visit(member.functionDeclaration())
        
        self.current_class = old_class
        return None

    def visitPrimaryConstructor(self, ctx: KotlinParser.PrimaryConstructorContext):
        # Extract properties declared in the primary constructor
        if self.current_class and ctx.primaryConstructorParameterList():
            for param in ctx.primaryConstructorParameterList().primaryConstructorParameter():
                if param.VAL() or param.VAR():
                    var_name = param.IDENTIFIER().getText()
                    type_ctx = param.type_()
                    if type_ctx:
                        type_name = type_ctx.getText()
                        self.instance_vars[self.current_class][var_name] = type_name
        return None

    def visitFunctionDeclaration(self, ctx: KotlinParser.FunctionDeclarationContext):
        func_name = ctx.IDENTIFIER().getText()
        old_method = self.current_method
        old_depth = self.call_depth
        
        return_type = "Unit"
        if ctx.COLON() and ctx.type_():
            return_type = ctx.type_().getText()
        
        full_name = f"{self.current_class}.{func_name}" if self.current_class else func_name
        self.method_return_types[full_name] = return_type
        
        # Store method body for inlining when a call is detected
        if ctx.block():
            self.method_bodies[full_name] = ctx.block()
        
        # If tracing execution (not just mapping classes), visit the body
        if not self.parsing_classes:
            if self.current_class:
                self.call_depth = old_depth + 1
            
            self.current_method = func_name
            self.log(f"  Method: {func_name}, depth={self.call_depth}")
            
            if ctx.block():
                self.visit(ctx.block())
            
            self.current_method = old_method
            self.call_depth = old_depth
        
        return None

    def visitPropertyDeclaration(self, ctx: KotlinParser.PropertyDeclarationContext):
        # Handle object creation and method calls assigned to variables
        if self.inside_main:
            var_name = ctx.IDENTIFIER().getText()
            
            if ctx.expression():
                expr = ctx.expression()
                expr_text = expr.getText()
                
                # Filter out standard collection helpers
                if any(x in expr_text for x in ['listOf', 'mutableListOf', 'mapOf', 'setOf', 'arrayOf']):
                    return None
                
                # Pattern: val result = obj.method(args)
                match = re.search(r'(\w+)\.(\w+)\s*\(([^)]+)\)', expr_text)
                if match:
                    receiver = match.group(1)
                    method_name = match.group(2)
                    params = match.group(3)
                    
                    self.sequence_flow.append({
                        'type': 'call',
                        'caller': "User",
                        'receiver': receiver,
                        'method': method_name,
                        'params': params,
                        'depth': self.call_depth,
                        'return_var': var_name,
                        'line': ctx.start.line
                    })
                    self.method_returns[method_name] = var_name
                    return None
                
                # Pattern: val obj = ClassName()
                match = re.search(r'([A-Z]\w*)', expr_text)
                if match:
                    class_name = match.group(1)
                    params_match = re.search(r'\(([^)]*)\)', expr_text)
                    if params_match:
                        self._finalize_object_creation(var_name, class_name, params_match.group(1).strip(), ctx.start.line)
                    else:
                        self.pending_var = {'name': var_name, 'class': class_name, 'line': ctx.start.line}
        
        return None

    def visitStatement(self, ctx: KotlinParser.StatementContext):
        # Handle Control Flow structures (If, While, For)
        if ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        
        text = ctx.getText().strip()
        if 'println' in text or self.parsing_classes:
            return None
        
        # Determine caller context
        caller = self.current_caller if self.current_caller else ("User" if self.inside_main else self.current_class.lower() if self.current_class else "User")
        
        # Handle return statements and capture return variables
        if text.startswith('return'):
            clean_text = text[6:].strip()
            if clean_text in ['true', 'false'] and self.current_method:
                self.method_returns[self.current_method] = clean_text
            return None
        
        # Generic method call detection (receiver.method(params))
        match = re.search(r'(\w+)\.(\w+)\s*\(([^)]*)\)', text)
        if match:
            receiver, method_name, params = match.groups()
            self.sequence_flow.append({
                'type': 'call', 'caller': caller, 'receiver': receiver, 
                'method': method_name, 'params': params, 
                'depth': self.call_depth, 'return_var': None, 'line': ctx.start.line
            })
            
            # Inline the body of the called method to track nested calls
            old_caller = self.current_caller
            self.current_caller = receiver
            self._inline_method_call(receiver, method_name)
            self.current_caller = old_caller
            return None
        
        return self.visitChildren(ctx)

    def _inline_method_call(self, receiver: str, method_name: str):
        # Logic to jump into a method's body while maintaining sequence context
        class_name = self.var_types.get(receiver)
        if not class_name and self.current_class:
            class_name = self.instance_vars.get(self.current_class, {}).get(receiver)
            
        if not class_name or f"{class_name}.{method_name}" not in self.method_bodies:
            return
        
        full_name = f"{class_name}.{method_name}"
        
        # Save current context to allow recursion/deep nesting
        ctx_save = (self.parsing_classes, self.current_class, self.current_method, 
                    self.call_depth, self.inside_main, getattr(self, 'current_caller', None))
        
        self.parsing_classes, self.current_class, self.current_method = False, class_name, method_name
        self.current_caller, self.call_depth, self.inside_main = receiver, self.call_depth + 1, False
        
        self.visit(self.method_bodies[full_name])
        
        # Restore context
        self.parsing_classes, self.current_class, self.current_method, self.call_depth, self.inside_main, self.current_caller = ctx_save

    def _finalize_object_creation(self, var_name, class_name, params, line):
        # Record object instantiation for PlantUML participant list
        self.objects[var_name] = class_name
        self.var_types[var_name] = class_name
        if var_name not in self.creation_order:
            self.creation_order.append(var_name)
        
        self.sequence_flow.append({
            'type': 'create', 'caller': 'User', 'object': var_name,
            'class': class_name, 'params': params, 'line': line
        })

    def get_sequence_data(self):
        # Deduplicate and prepare data for the generator
        seen, unique_flow = set(), []
        
        for step in self.sequence_flow:
            key = (step['type'], step.get('object', ''), step.get('method', ''), step['line'])
            if key not in seen:
                seen.add(key)
                unique_flow.append(step)
        
        # Dynamic depth calculation based on call nesting
        stack = []
        for step in unique_flow:
            if step['type'] == 'call':
                while stack and stack[-1] != step['caller']:
                    stack.pop()
                step['depth'] = len(stack)
                stack.append(step['receiver'])
        
        # Map return values stored during traversal
        for step in unique_flow:
            if step['type'] == 'call' and not step.get('return_var'):
                step['return_var'] = self.method_returns.get(step['method'])
        
        return {
            'objects': self.objects, 'creation_order': self.creation_order,
            'var_types': self.var_types, 'instance_vars': self.instance_vars,
            'sequence_flow': unique_flow
        }

    def visitIfStatement(self, ctx: KotlinParser.IfStatementContext):
        # Map Kotlin 'if' to PlantUML 'alt' block
        self.sequence_flow.append({'type': 'alt_start', 'condition': ctx.expression().getText(), 'line': ctx.start.line})
        if ctx.block(0): self.visit(ctx.block(0))
        
        if ctx.ELSE():
            self.sequence_flow.append({'type': 'else_start', 'line': ctx.ELSE().getSymbol().line})
            if len(ctx.block()) > 1: self.visit(ctx.block(1))
                
        self.sequence_flow.append({'type': 'alt_end', 'line': ctx.stop.line})
        return None

    def visitWhileStatement(self, ctx: KotlinParser.WhileStatementContext):
        # Map Kotlin 'while' to PlantUML 'loop' block
        self.sequence_flow.append({'type': 'loop_start', 'condition': f"while ({ctx.expression().getText()})", 'line': ctx.start.line})
        if ctx.block(): self.visit(ctx.block())
        self.sequence_flow.append({'type': 'loop_end', 'line': ctx.stop.line})
        return None

    def visitForStatement(self, ctx: KotlinParser.ForStatementContext):
        # Map Kotlin 'for' to PlantUML 'loop' block
        self.sequence_flow.append({'type': 'loop_start', 'condition': f"for ({ctx.IDENTIFIER().getText() if ctx.IDENTIFIER() else 'item'} in ...)", 'line': ctx.start.line})
        if ctx.block(): self.visit(ctx.block())
        self.sequence_flow.append({'type': 'loop_end', 'line': ctx.stop.line})
        return None