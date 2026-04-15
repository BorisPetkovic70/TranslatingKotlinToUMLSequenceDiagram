class PlantUMLSequenceGenerator:
    def __init__(self):
        # Maps object names to PlantUML aliases (e.g., 'pump' -> 'O0')
        self.participants = {}
        self.aliases = {}
        self.created_objects = set()

    def generate(self, data):
        # Reset state and initialize the User actor
        self.participants = {"User": "U"}
        self.aliases = {"User": "U"}
        self.created_objects = set()
        
        lines = []
        lines.append("@startuml")
        lines.append("!theme plain")
        lines.append("autonumber")
        lines.append("")
        lines.append("actor User as U")
        
        # Define participants based on the order they were created in the code
        alias_counter = 0
        for obj in data.get('creation_order', []):
            class_name = data['objects'].get(obj, "Unknown")
            alias = f"O{alias_counter}"
            self.participants[obj] = alias
            self.aliases[obj] = alias
            self.aliases[class_name.lower()] = alias
            lines.append(f'participant "{obj}:{class_name}" as {alias}')
            alias_counter += 1
        
        lines.append("")
        
        flow = data.get('sequence_flow', [])
        
        # Handle initial object instantiations (<<create>> messages)
        for step in flow:
            if step['type'] == 'create':
                caller = step['caller']
                caller_alias = self.aliases.get(caller, "U")
                obj = step['object']
                obj_alias = self.aliases.get(obj, obj)
                class_name = step['class']
                params = step.get('params', '')
                
                if params:
                    lines.append(f"{caller_alias} -> {obj_alias} : <<create>> {class_name}({params})")
                else:
                    lines.append(f"{caller_alias} -> {obj_alias} : <<create>> {class_name}()")
                self.created_objects.add(obj)
                lines.append("")
        
        # Process calls, loops, and conditional blocks
        self._generate_structured(lines, flow)
        
        lines.append("@enduml")
        return "\n".join(lines)
    
    def _generate_structured(self, lines, flow):
            indent = 0
            call_stack = [] # Tracks active calls for proper return arrows and deactivation
            block_stack = [] # Tracks the number of active calls at the start of a block
            
            i = 0
            while i < len(flow):
                step = flow[i]
                indent_str = "    " * indent
                
                if step['type'] == 'create':
                    i += 1
                    continue
                
                # Handle the start of logical blocks (alt/if or loop/while)
                elif step['type'] in ['alt_start', 'loop_start']:
                    # Record the current call stack size to close nested calls later
                    block_stack.append(len(call_stack))
                    
                    if step['type'] == 'alt_start':
                        lines.append(f"{indent_str}alt {step.get('condition', 'condition')}")
                    else:
                        lines.append(f"{indent_str}loop {step.get('condition', 'loop')}")
                    
                    indent += 1
                    i += 1
                    
                # Handle the 'else' part of an alternative block
                elif step['type'] == 'else_start':
                    # Forcefully close any activations started within the 'if' branch
                    target_len = block_stack[-1] if block_stack else 0
                    while len(call_stack) > target_len:
                        old_call = call_stack.pop()
                        indent -= 1
                        lines.append(f"{'    ' * indent}{old_call['receiver_alias']} --> {old_call['caller_alias']} : {old_call['return_var'] if old_call['return_var'] else ''}")
                        lines.append(f"{'    ' * indent}deactivate {old_call['receiver_alias']}")
                    
                    indent -= 1
                    lines.append(f"{'    ' * indent}else")
                    indent += 1
                    i += 1
                    
                # Handle the end of a block (closes the loop or alt)
                elif step['type'] in ['alt_end', 'loop_end']:
                    # Forcefully close any activations remaining in the block before ending it
                    target_len = block_stack.pop() if block_stack else 0
                    while len(call_stack) > target_len:
                        old_call = call_stack.pop()
                        indent -= 1
                        lines.append(f"{'    ' * indent}{old_call['receiver_alias']} --> {old_call['caller_alias']} : {old_call['return_var'] if old_call['return_var'] else ''}")
                        lines.append(f"{'    ' * indent}deactivate {old_call['receiver_alias']}")
                    
                    indent = max(0, indent - 1)
                    lines.append(f"{'    ' * indent}end")
                    i += 1
                    
                # Handle standard method calls
                elif step['type'] == 'call':
                    caller = step['caller']
                    receiver = step['receiver']
                    method = step['method']
                    params = step['params']
                    return_var = step.get('return_var')
                    depth = step.get('depth', 0)
                    
                    caller_alias = self.aliases.get(caller, "U") if caller != "User" else "U"
                    receiver_alias = self.aliases.get(receiver, receiver)
                    
                    # Close previous calls if the current call is at a shallower depth
                    while call_stack and call_stack[-1]['depth'] >= depth:
                        old_call = call_stack.pop()
                        old_indent = old_call['indent']
                        old_indent_str = "    " * old_indent
                        if old_call['return_var']:
                            lines.append(f"{old_indent_str}{old_call['receiver_alias']} --> {old_call['caller_alias']} : {old_call['return_var']}")
                        else:
                            lines.append(f"{old_indent_str}{old_call['receiver_alias']} --> {old_call['caller_alias']}")
                        lines.append(f"{old_indent_str}deactivate {old_call['receiver_alias']}")
                        indent = old_indent

                    # Check if the next step is a block boundary to decide if we should close the call immediately
                    next_is_boundary = False
                    if i + 1 < len(flow):
                        next_step = flow[i+1]
                        if next_step['type'] in ['else_start', 'alt_end', 'loop_end']:
                            next_is_boundary = True

                    # Generate activation and call message
                    current_indent = indent
                    lines.append(f"{'    ' * current_indent}{caller_alias} -> {receiver_alias} : {method}({params})")
                    lines.append(f"{'    ' * current_indent}activate {receiver_alias}")
                    
                    if next_is_boundary:
                        # If a boundary follows, return and deactivate immediately
                        if return_var:
                            lines.append(f"{'    ' * current_indent}{receiver_alias} --> {caller_alias} : {return_var}")
                        else:
                            lines.append(f"{'    ' * current_indent}{receiver_alias} --> {caller_alias}")
                        lines.append(f"{'    ' * current_indent}deactivate {receiver_alias}")
                    else:
                        # Push call metadata to stack to close it later
                        call_stack.append({
                            'caller_alias': caller_alias,
                            'receiver_alias': receiver_alias,
                            'return_var': return_var,
                            'depth': depth,
                            'indent': current_indent
                        })
                        indent = current_indent + 1
                    
                    i += 1
                    
                else:
                    i += 1
            
            # Final cleanup: close all calls that were not explicitly deactivated
            while call_stack:
                old_call = call_stack.pop()
                indent = old_call['indent']
                lines.append(f"{'    ' * indent}{old_call['receiver_alias']} --> {old_call['caller_alias']} : {old_call['return_var'] if old_call['return_var'] else ''}")
                lines.append(f"{'    ' * indent}deactivate {old_call['receiver_alias']}")