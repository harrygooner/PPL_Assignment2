# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr.
    def visitArr(self, ctx:MT22Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayList.
    def visitArrayList(self, ctx:MT22Parser.ArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_arrayList.
    def visitNon_null_arrayList(self, ctx:MT22Parser.Non_null_arrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayEle.
    def visitArrayEle(self, ctx:MT22Parser.ArrayEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#noninitVardecl.
    def visitNoninitVardecl(self, ctx:MT22Parser.NoninitVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initVardecl.
    def visitInitVardecl(self, ctx:MT22Parser.InitVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initVardeclEle.
    def visitInitVardeclEle(self, ctx:MT22Parser.InitVardeclEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayDecl.
    def visitArrayDecl(self, ctx:MT22Parser.ArrayDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initAardecl.
    def visitInitAardecl(self, ctx:MT22Parser.InitAardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initAardeclEle.
    def visitInitAardeclEle(self, ctx:MT22Parser.InitAardeclEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#noninitAardecl.
    def visitNoninitAardecl(self, ctx:MT22Parser.NoninitAardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intList.
    def visitIntList(self, ctx:MT22Parser.IntListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_exprlist.
    def visitNon_null_exprlist(self, ctx:MT22Parser.Non_null_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl_noInherit.
    def visitFuncdecl_noInherit(self, ctx:MT22Parser.Funcdecl_noInheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl_Inherit.
    def visitFuncdecl_Inherit(self, ctx:MT22Parser.Funcdecl_InheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functyp.
    def visitFunctyp(self, ctx:MT22Parser.FunctypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_params.
    def visitNon_null_params(self, ctx:MT22Parser.Non_null_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_EQ_op.
    def visitRelational_EQ_op(self, ctx:MT22Parser.Relational_EQ_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_noEQ_op.
    def visitRelational_noEQ_op(self, ctx:MT22Parser.Relational_noEQ_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_op.
    def visitLogical_op(self, ctx:MT22Parser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_expr.
    def visitAdd_expr(self, ctx:MT22Parser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_expr.
    def visitMul_expr(self, ctx:MT22Parser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_op.
    def visitMul_op(self, ctx:MT22Parser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nega_expr.
    def visitNega_expr(self, ctx:MT22Parser.Nega_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_list.
    def visitIndex_list(self, ctx:MT22Parser.Index_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall_expr.
    def visitFuncall_expr(self, ctx:MT22Parser.Funcall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unmatchStmt.
    def visitUnmatchStmt(self, ctx:MT22Parser.UnmatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#matchStmt.
    def visitMatchStmt(self, ctx:MT22Parser.MatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockelements.
    def visitBlockelements(self, ctx:MT22Parser.BlockelementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_blockelements.
    def visitNon_null_blockelements(self, ctx:MT22Parser.Non_null_blockelementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockelement.
    def visitBlockelement(self, ctx:MT22Parser.BlockelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_function.
    def visitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_integer.
    def visitRead_integer(self, ctx:MT22Parser.Read_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_integer.
    def visitPrint_integer(self, ctx:MT22Parser.Print_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_float.
    def visitRead_float(self, ctx:MT22Parser.Read_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#write_float.
    def visitWrite_float(self, ctx:MT22Parser.Write_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_boolean.
    def visitRead_boolean(self, ctx:MT22Parser.Read_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_boolean.
    def visitPrint_boolean(self, ctx:MT22Parser.Print_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_string.
    def visitRead_string(self, ctx:MT22Parser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_string.
    def visitPrint_string(self, ctx:MT22Parser.Print_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#super_func.
    def visitSuper_func(self, ctx:MT22Parser.Super_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prevent_default.
    def visitPrevent_default(self, ctx:MT22Parser.Prevent_defaultContext):
        return self.visitChildren(ctx)



del MT22Parser