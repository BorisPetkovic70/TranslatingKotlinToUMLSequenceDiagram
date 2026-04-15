# Generated from grammars/KotlinParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .KotlinParser import KotlinParser
else:
    from KotlinParser import KotlinParser

# This class defines a complete listener for a parse tree produced by KotlinParser.
class KotlinParserListener(ParseTreeListener):

    # Enter a parse tree produced by KotlinParser#kotlinFile.
    def enterKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        pass

    # Exit a parse tree produced by KotlinParser#kotlinFile.
    def exitKotlinFile(self, ctx:KotlinParser.KotlinFileContext):
        pass


    # Enter a parse tree produced by KotlinParser#packageHeader.
    def enterPackageHeader(self, ctx:KotlinParser.PackageHeaderContext):
        pass

    # Exit a parse tree produced by KotlinParser#packageHeader.
    def exitPackageHeader(self, ctx:KotlinParser.PackageHeaderContext):
        pass


    # Enter a parse tree produced by KotlinParser#importList.
    def enterImportList(self, ctx:KotlinParser.ImportListContext):
        pass

    # Exit a parse tree produced by KotlinParser#importList.
    def exitImportList(self, ctx:KotlinParser.ImportListContext):
        pass


    # Enter a parse tree produced by KotlinParser#topLevelObject.
    def enterTopLevelObject(self, ctx:KotlinParser.TopLevelObjectContext):
        pass

    # Exit a parse tree produced by KotlinParser#topLevelObject.
    def exitTopLevelObject(self, ctx:KotlinParser.TopLevelObjectContext):
        pass


    # Enter a parse tree produced by KotlinParser#classDeclaration.
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#classDeclaration.
    def exitClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#primaryConstructor.
    def enterPrimaryConstructor(self, ctx:KotlinParser.PrimaryConstructorContext):
        pass

    # Exit a parse tree produced by KotlinParser#primaryConstructor.
    def exitPrimaryConstructor(self, ctx:KotlinParser.PrimaryConstructorContext):
        pass


    # Enter a parse tree produced by KotlinParser#primaryConstructorParameterList.
    def enterPrimaryConstructorParameterList(self, ctx:KotlinParser.PrimaryConstructorParameterListContext):
        pass

    # Exit a parse tree produced by KotlinParser#primaryConstructorParameterList.
    def exitPrimaryConstructorParameterList(self, ctx:KotlinParser.PrimaryConstructorParameterListContext):
        pass


    # Enter a parse tree produced by KotlinParser#primaryConstructorParameter.
    def enterPrimaryConstructorParameter(self, ctx:KotlinParser.PrimaryConstructorParameterContext):
        pass

    # Exit a parse tree produced by KotlinParser#primaryConstructorParameter.
    def exitPrimaryConstructorParameter(self, ctx:KotlinParser.PrimaryConstructorParameterContext):
        pass


    # Enter a parse tree produced by KotlinParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:KotlinParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:KotlinParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#objectDeclaration.
    def enterObjectDeclaration(self, ctx:KotlinParser.ObjectDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#objectDeclaration.
    def exitObjectDeclaration(self, ctx:KotlinParser.ObjectDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:KotlinParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:KotlinParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#modifiers.
    def enterModifiers(self, ctx:KotlinParser.ModifiersContext):
        pass

    # Exit a parse tree produced by KotlinParser#modifiers.
    def exitModifiers(self, ctx:KotlinParser.ModifiersContext):
        pass


    # Enter a parse tree produced by KotlinParser#modifier.
    def enterModifier(self, ctx:KotlinParser.ModifierContext):
        pass

    # Exit a parse tree produced by KotlinParser#modifier.
    def exitModifier(self, ctx:KotlinParser.ModifierContext):
        pass


    # Enter a parse tree produced by KotlinParser#parameterList.
    def enterParameterList(self, ctx:KotlinParser.ParameterListContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameterList.
    def exitParameterList(self, ctx:KotlinParser.ParameterListContext):
        pass


    # Enter a parse tree produced by KotlinParser#parameter.
    def enterParameter(self, ctx:KotlinParser.ParameterContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameter.
    def exitParameter(self, ctx:KotlinParser.ParameterContext):
        pass


    # Enter a parse tree produced by KotlinParser#superTypes.
    def enterSuperTypes(self, ctx:KotlinParser.SuperTypesContext):
        pass

    # Exit a parse tree produced by KotlinParser#superTypes.
    def exitSuperTypes(self, ctx:KotlinParser.SuperTypesContext):
        pass


    # Enter a parse tree produced by KotlinParser#superType.
    def enterSuperType(self, ctx:KotlinParser.SuperTypeContext):
        pass

    # Exit a parse tree produced by KotlinParser#superType.
    def exitSuperType(self, ctx:KotlinParser.SuperTypeContext):
        pass


    # Enter a parse tree produced by KotlinParser#typeParameters.
    def enterTypeParameters(self, ctx:KotlinParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeParameters.
    def exitTypeParameters(self, ctx:KotlinParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by KotlinParser#typeParameter.
    def enterTypeParameter(self, ctx:KotlinParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeParameter.
    def exitTypeParameter(self, ctx:KotlinParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by KotlinParser#typeArguments.
    def enterTypeArguments(self, ctx:KotlinParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by KotlinParser#typeArguments.
    def exitTypeArguments(self, ctx:KotlinParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by KotlinParser#type_.
    def enterType_(self, ctx:KotlinParser.Type_Context):
        pass

    # Exit a parse tree produced by KotlinParser#type_.
    def exitType_(self, ctx:KotlinParser.Type_Context):
        pass


    # Enter a parse tree produced by KotlinParser#classBody.
    def enterClassBody(self, ctx:KotlinParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by KotlinParser#classBody.
    def exitClassBody(self, ctx:KotlinParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by KotlinParser#interfaceBody.
    def enterInterfaceBody(self, ctx:KotlinParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by KotlinParser#interfaceBody.
    def exitInterfaceBody(self, ctx:KotlinParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by KotlinParser#enumBody.
    def enterEnumBody(self, ctx:KotlinParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by KotlinParser#enumBody.
    def exitEnumBody(self, ctx:KotlinParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by KotlinParser#classMemberDeclarations.
    def enterClassMemberDeclarations(self, ctx:KotlinParser.ClassMemberDeclarationsContext):
        pass

    # Exit a parse tree produced by KotlinParser#classMemberDeclarations.
    def exitClassMemberDeclarations(self, ctx:KotlinParser.ClassMemberDeclarationsContext):
        pass


    # Enter a parse tree produced by KotlinParser#classMemberDeclaration.
    def enterClassMemberDeclaration(self, ctx:KotlinParser.ClassMemberDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#classMemberDeclaration.
    def exitClassMemberDeclaration(self, ctx:KotlinParser.ClassMemberDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#interfaceMemberDeclarations.
    def enterInterfaceMemberDeclarations(self, ctx:KotlinParser.InterfaceMemberDeclarationsContext):
        pass

    # Exit a parse tree produced by KotlinParser#interfaceMemberDeclarations.
    def exitInterfaceMemberDeclarations(self, ctx:KotlinParser.InterfaceMemberDeclarationsContext):
        pass


    # Enter a parse tree produced by KotlinParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:KotlinParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:KotlinParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#secondaryConstructor.
    def enterSecondaryConstructor(self, ctx:KotlinParser.SecondaryConstructorContext):
        pass

    # Exit a parse tree produced by KotlinParser#secondaryConstructor.
    def exitSecondaryConstructor(self, ctx:KotlinParser.SecondaryConstructorContext):
        pass


    # Enter a parse tree produced by KotlinParser#initBlock.
    def enterInitBlock(self, ctx:KotlinParser.InitBlockContext):
        pass

    # Exit a parse tree produced by KotlinParser#initBlock.
    def exitInitBlock(self, ctx:KotlinParser.InitBlockContext):
        pass


    # Enter a parse tree produced by KotlinParser#constructorDelegationCall.
    def enterConstructorDelegationCall(self, ctx:KotlinParser.ConstructorDelegationCallContext):
        pass

    # Exit a parse tree produced by KotlinParser#constructorDelegationCall.
    def exitConstructorDelegationCall(self, ctx:KotlinParser.ConstructorDelegationCallContext):
        pass


    # Enter a parse tree produced by KotlinParser#enumEntries.
    def enterEnumEntries(self, ctx:KotlinParser.EnumEntriesContext):
        pass

    # Exit a parse tree produced by KotlinParser#enumEntries.
    def exitEnumEntries(self, ctx:KotlinParser.EnumEntriesContext):
        pass


    # Enter a parse tree produced by KotlinParser#enumEntry.
    def enterEnumEntry(self, ctx:KotlinParser.EnumEntryContext):
        pass

    # Exit a parse tree produced by KotlinParser#enumEntry.
    def exitEnumEntry(self, ctx:KotlinParser.EnumEntryContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#propertyDeclaration.
    def enterPropertyDeclaration(self, ctx:KotlinParser.PropertyDeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#propertyDeclaration.
    def exitPropertyDeclaration(self, ctx:KotlinParser.PropertyDeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#propertyDelegate.
    def enterPropertyDelegate(self, ctx:KotlinParser.PropertyDelegateContext):
        pass

    # Exit a parse tree produced by KotlinParser#propertyDelegate.
    def exitPropertyDelegate(self, ctx:KotlinParser.PropertyDelegateContext):
        pass


    # Enter a parse tree produced by KotlinParser#getter.
    def enterGetter(self, ctx:KotlinParser.GetterContext):
        pass

    # Exit a parse tree produced by KotlinParser#getter.
    def exitGetter(self, ctx:KotlinParser.GetterContext):
        pass


    # Enter a parse tree produced by KotlinParser#setter.
    def enterSetter(self, ctx:KotlinParser.SetterContext):
        pass

    # Exit a parse tree produced by KotlinParser#setter.
    def exitSetter(self, ctx:KotlinParser.SetterContext):
        pass


    # Enter a parse tree produced by KotlinParser#block.
    def enterBlock(self, ctx:KotlinParser.BlockContext):
        pass

    # Exit a parse tree produced by KotlinParser#block.
    def exitBlock(self, ctx:KotlinParser.BlockContext):
        pass


    # Enter a parse tree produced by KotlinParser#statements.
    def enterStatements(self, ctx:KotlinParser.StatementsContext):
        pass

    # Exit a parse tree produced by KotlinParser#statements.
    def exitStatements(self, ctx:KotlinParser.StatementsContext):
        pass


    # Enter a parse tree produced by KotlinParser#statement.
    def enterStatement(self, ctx:KotlinParser.StatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#statement.
    def exitStatement(self, ctx:KotlinParser.StatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#ifStatement.
    def enterIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#ifStatement.
    def exitIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#whileStatement.
    def enterWhileStatement(self, ctx:KotlinParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#whileStatement.
    def exitWhileStatement(self, ctx:KotlinParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#forStatement.
    def enterForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#forStatement.
    def exitForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#returnStatement.
    def enterReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#returnStatement.
    def exitReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#declaration.
    def enterDeclaration(self, ctx:KotlinParser.DeclarationContext):
        pass

    # Exit a parse tree produced by KotlinParser#declaration.
    def exitDeclaration(self, ctx:KotlinParser.DeclarationContext):
        pass


    # Enter a parse tree produced by KotlinParser#argumentList.
    def enterArgumentList(self, ctx:KotlinParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by KotlinParser#argumentList.
    def exitArgumentList(self, ctx:KotlinParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by KotlinParser#expression.
    def enterExpression(self, ctx:KotlinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#expression.
    def exitExpression(self, ctx:KotlinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:KotlinParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:KotlinParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:KotlinParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:KotlinParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#equalityExpression.
    def enterEqualityExpression(self, ctx:KotlinParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#equalityExpression.
    def exitEqualityExpression(self, ctx:KotlinParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#relationalExpression.
    def enterRelationalExpression(self, ctx:KotlinParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#relationalExpression.
    def exitRelationalExpression(self, ctx:KotlinParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:KotlinParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:KotlinParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:KotlinParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:KotlinParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#unaryExpression.
    def enterUnaryExpression(self, ctx:KotlinParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#unaryExpression.
    def exitUnaryExpression(self, ctx:KotlinParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:KotlinParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:KotlinParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionCall.
    def enterFunctionCall(self, ctx:KotlinParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionCall.
    def exitFunctionCall(self, ctx:KotlinParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by KotlinParser#literal.
    def enterLiteral(self, ctx:KotlinParser.LiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#literal.
    def exitLiteral(self, ctx:KotlinParser.LiteralContext):
        pass



del KotlinParser