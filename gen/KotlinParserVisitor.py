# Generated from grammars/KotlinParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .KotlinParser import KotlinParser
else:
    from KotlinParser import KotlinParser

# This class defines a complete generic visitor for a parse tree produced by KotlinParser.

class KotlinParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by KotlinParser#kotlinFile.
    def visitKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#packageHeader.
    def visitPackageHeader(self, ctx:KotlinParser.PackageHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#importList.
    def visitImportList(self, ctx:KotlinParser.ImportListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#topLevelObject.
    def visitTopLevelObject(self, ctx:KotlinParser.TopLevelObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classDeclaration.
    def visitClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#primaryConstructor.
    def visitPrimaryConstructor(self, ctx:KotlinParser.PrimaryConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#primaryConstructorParameterList.
    def visitPrimaryConstructorParameterList(self, ctx:KotlinParser.PrimaryConstructorParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#primaryConstructorParameter.
    def visitPrimaryConstructorParameter(self, ctx:KotlinParser.PrimaryConstructorParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:KotlinParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:KotlinParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:KotlinParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#modifiers.
    def visitModifiers(self, ctx:KotlinParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#modifier.
    def visitModifier(self, ctx:KotlinParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#parameterList.
    def visitParameterList(self, ctx:KotlinParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#parameter.
    def visitParameter(self, ctx:KotlinParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#superTypes.
    def visitSuperTypes(self, ctx:KotlinParser.SuperTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#superType.
    def visitSuperType(self, ctx:KotlinParser.SuperTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeParameters.
    def visitTypeParameters(self, ctx:KotlinParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeParameter.
    def visitTypeParameter(self, ctx:KotlinParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#typeArguments.
    def visitTypeArguments(self, ctx:KotlinParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#type_.
    def visitType_(self, ctx:KotlinParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classBody.
    def visitClassBody(self, ctx:KotlinParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#interfaceBody.
    def visitInterfaceBody(self, ctx:KotlinParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumBody.
    def visitEnumBody(self, ctx:KotlinParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classMemberDeclarations.
    def visitClassMemberDeclarations(self, ctx:KotlinParser.ClassMemberDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#classMemberDeclaration.
    def visitClassMemberDeclaration(self, ctx:KotlinParser.ClassMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#interfaceMemberDeclarations.
    def visitInterfaceMemberDeclarations(self, ctx:KotlinParser.InterfaceMemberDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx:KotlinParser.InterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#secondaryConstructor.
    def visitSecondaryConstructor(self, ctx:KotlinParser.SecondaryConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#initBlock.
    def visitInitBlock(self, ctx:KotlinParser.InitBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#constructorDelegationCall.
    def visitConstructorDelegationCall(self, ctx:KotlinParser.ConstructorDelegationCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumEntries.
    def visitEnumEntries(self, ctx:KotlinParser.EnumEntriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#enumEntry.
    def visitEnumEntry(self, ctx:KotlinParser.EnumEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#propertyDeclaration.
    def visitPropertyDeclaration(self, ctx:KotlinParser.PropertyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#propertyDelegate.
    def visitPropertyDelegate(self, ctx:KotlinParser.PropertyDelegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#getter.
    def visitGetter(self, ctx:KotlinParser.GetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#setter.
    def visitSetter(self, ctx:KotlinParser.SetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#block.
    def visitBlock(self, ctx:KotlinParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#statements.
    def visitStatements(self, ctx:KotlinParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#statement.
    def visitStatement(self, ctx:KotlinParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#ifStatement.
    def visitIfStatement(self, ctx:KotlinParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#whileStatement.
    def visitWhileStatement(self, ctx:KotlinParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#forStatement.
    def visitForStatement(self, ctx:KotlinParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#returnStatement.
    def visitReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#declaration.
    def visitDeclaration(self, ctx:KotlinParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#argumentList.
    def visitArgumentList(self, ctx:KotlinParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#expression.
    def visitExpression(self, ctx:KotlinParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:KotlinParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:KotlinParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#equalityExpression.
    def visitEqualityExpression(self, ctx:KotlinParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#relationalExpression.
    def visitRelationalExpression(self, ctx:KotlinParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:KotlinParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:KotlinParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#unaryExpression.
    def visitUnaryExpression(self, ctx:KotlinParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:KotlinParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#functionCall.
    def visitFunctionCall(self, ctx:KotlinParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by KotlinParser#literal.
    def visitLiteral(self, ctx:KotlinParser.LiteralContext):
        return self.visitChildren(ctx)



del KotlinParser