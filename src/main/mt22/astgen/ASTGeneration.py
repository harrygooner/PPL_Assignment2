"""
Họ và tên: Trần Huy Nam Hưng
MSSV: 2052119

"""

from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decls EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        # print("hello")
        return Program(self.visit(ctx.decls()))


    ## Visit a parse tree produced by MT22Parser#decls.
    ## decls: decl decls | decl;
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        if(ctx.getChildCount()==1): return self.visit(ctx.decl())
        else:
            # print(self.visit(ctx.decl()))
            return self.visit(ctx.decl()) + self.visit(ctx.decls())

    # Visit a parse tree produced by MT22Parser#decl.
    # decl: vardecl | funcdecl | arrayDecl;
    def visitDecl(self, ctx:MT22Parser.DeclContext):       
        if(ctx.vardecl()): return self.visit(ctx.vardecl()) #return list of VarDecl
        elif(ctx.funcdecl()): return self.visit(ctx.funcdecl())
        elif(ctx.arrayDecl()): return self.visit(ctx.arrayDecl())


    # Visit a parse tree produced by MT22Parser#arr.
    # arr: LEFT_CURBRACK arrayList RIGHT_CURBRACK;
    def visitArr(self, ctx:MT22Parser.ArrContext):
        exprList = self.visit(ctx.arrayList())
        return ArrayLit(exprList)


    # Visit a parse tree produced by MT22Parser#arrayList.
    # arrayList: non_null_arrayList |;
    def visitArrayList(self, ctx:MT22Parser.ArrayListContext):
        if (ctx.getChildCount()==1): return self.visit(ctx.non_null_arrayList())
        return []


    # Visit a parse tree produced by MT22Parser#non_null_arrayList.
    """
    non_null_arrayList:
	arrayEle COMMA non_null_arrayList
	| arrayEle;
    """
    def visitNon_null_arrayList(self, ctx:MT22Parser.Non_null_arrayListContext):
        if (ctx.getChildCount()==1):return [self.visit(ctx.arrayEle())]
        else: 
            return [self.visit(ctx.arrayEle())] + self.visit(ctx.non_null_arrayList())


    # Visit a parse tree produced by MT22Parser#arrayEle.
    # arrayEle: expr;
    def visitArrayEle(self, ctx:MT22Parser.ArrayEleContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MT22Parser#vardecl.
    ## vardecl: initVardecl | noninitVardecl;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if(ctx.noninitVardecl()): return self.visit(ctx.noninitVardecl())
        else: return self.visit(ctx.initVardecl())


    # Visit a parse tree produced by MT22Parser#noninitVardecl.
    ## noninitVardecl: idlist COLON typ SEMICOLON;
    def visitNoninitVardecl(self, ctx:MT22Parser.NoninitVardeclContext):
        idl = self.visit(ctx.idlist())
        idTyp = self.visit(ctx.typ())
        return list(map(lambda x: VarDecl(x,idTyp),idl))
        #return a list of VarDecl

    # Visit a parse tree produced by MT22Parser#initVardecl.
    ## initVardecl: IDENTIFIER initVardeclEle expr SEMICOLON;
    idTempList = []
    exprTempList = []
    def visitInitVardecl(self, ctx:MT22Parser.InitVardeclContext):
        firstID = ctx.IDENTIFIER().getText()
        lastExpr = self.visit(ctx.expr())
        # print(lastExpr)
        typ = self.visit(ctx.initVardeclEle())
        ASTGeneration.idTempList = [firstID] + ASTGeneration.idTempList
        ASTGeneration.exprTempList+=[lastExpr]
        # print(ASTGeneration.exprTempList)
        result = list(map(lambda name,init: VarDecl(name,typ,init), ASTGeneration.idTempList, ASTGeneration.exprTempList))
        ASTGeneration.idTempList = []
        ASTGeneration.exprTempList = []
        return result
        #return a list of VarDecl
    """
    initVardeclEle: (COMMA IDENTIFIER initVardeclEle expr COMMA)
	| COLON typ ASSIG_OP;
    """
    ## Visit a parse tree produced by MT22Parser#initVardeclEle.
    def visitInitVardeclEle(self, ctx:MT22Parser.InitVardeclEleContext):
        if (ctx.getChildCount() == 3):
            # print('Haha')
            return self.visit(ctx.typ())
        else:
            id = ctx.IDENTIFIER().getText()
            ASTGeneration.idTempList += [id]
            ASTGeneration.exprTempList = [self.visit(ctx.expr())] + ASTGeneration.exprTempList 
            return self.visit(ctx.initVardeclEle())


    # Visit a parse tree produced by MT22Parser#arrayDecl.
    # arrayDecl: initAardecl | noninitAardecl;
    def visitArrayDecl(self, ctx:MT22Parser.ArrayDeclContext):
        if(ctx.noninitAardecl()): return self.visit(ctx.noninitAardecl())
        else: return self.visit(ctx.initAardecl())


    # Visit a parse tree produced by MT22Parser#initAardecl.
    # initAardecl: IDENTIFIER initAardeclEle arr SEMICOLON;

    def visitInitAardecl(self, ctx:MT22Parser.InitAardeclContext):
        firstID = ctx.IDENTIFIER().getText()
        lastInitArr = self.visit(ctx.expr())
        typ = self.visit(ctx.initAardeclEle())
        ASTGeneration.idArrTempList = [firstID] + ASTGeneration.idArrTempList
        ASTGeneration.initArrTempList += [lastInitArr]
        # print(ASTGeneration.exprTempList)
        result = list(map(lambda name,init: VarDecl(name,typ,init), ASTGeneration.idArrTempList, ASTGeneration.initArrTempList))
        ASTGeneration.idArrTempList = []
        ASTGeneration.initArrTempList = []
        return result

    # Visit a parse tree produced by MT22Parser#initAardeclEle.
    """
    initAardeclEle: (COMMA IDENTIFIER initAardeclEle arr COMMA)
	| (
		COLON ARRAY_TYP LEFT_SQUAREBRACK (intList /*dimension*/) RIGHT_SQUAREBRACK OF typ ASSIG_OP
	);
    """
    idArrTempList = []
    initArrTempList = []
    def visitInitAardeclEle(self, ctx:MT22Parser.InitAardeclEleContext):
        if (ctx.getChildCount() == 8):
            dimen = self.visit(ctx.intList()) # dimension
            typ = self.visit(ctx.typ())
            arrayTyp = ArrayType(dimen,typ)
            return arrayTyp
        else:
            id = ctx.IDENTIFIER().getText()
            ASTGeneration.idArrTempList += [id]
            ASTGeneration.initArrTempList = [self.visit(ctx.expr())] + ASTGeneration.initArrTempList 
            return self.visit(ctx.initAardeclEle())

        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#noninitAardecl.
    """
    noninitAardecl:
	idlist COLON ARRAY_TYP LEFT_SQUAREBRACK (intList) RIGHT_SQUAREBRACK OF typ SEMICOLON;
    """
    def visitNoninitAardecl(self, ctx:MT22Parser.NoninitAardeclContext):
        idlist = self.visit(ctx.idlist()) #list of id
        dimen = self.visit(ctx.intList()) # dimension
        typ = self.visit(ctx.typ())
        arrayTyp = ArrayType(dimen,typ)
        return list(map(lambda x: VarDecl(x,arrayTyp),idlist))
        
    # Visit a parse tree produced by MT22Parser#intList.
    # intList: INT_LIT COMMA intList | INT_LIT;

    def visitIntList(self, ctx:MT22Parser.IntListContext):
        # print(type(ctx.INT_LIT().getText()))
        if(ctx.getChildCount()==1):return [str(ctx.INT_LIT().getText())]
        else:
            return [str(ctx.INT_LIT().getText())] + self.visit(ctx.intList())


    # Visit a parse tree produced by MT22Parser#idlist.
    # idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        firstID = ctx.IDENTIFIER().getText()
        if(ctx.getChildCount() == 3): return [firstID] + self.visit(ctx.idlist())
        else:
            return [firstID]


    # Visit a parse tree produced by MT22Parser#typ.
    # typ: BOOLEAN | INT | FLOAT | ARRAY_TYP | STRING | AUTO;
    def visitTyp(self, ctx:MT22Parser.TypContext):
        if (ctx.INT()): return IntegerType()
        elif(ctx.FLOAT()): return FloatType()
        elif(ctx.BOOLEAN()): return BooleanType()
        # elif(ctx.ARRAY_TYP()): return ArrayType()
        elif(ctx.AUTO()): return AutoType()
        elif(ctx.STRING()): return StringType()


    # Visit a parse tree produced by MT22Parser#exprlist.
    #   exprlist: non_null_exprlist |;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if(ctx.getChildCount()==0):return []
        return self.visit(ctx.non_null_exprlist())


    # Visit a parse tree produced by MT22Parser#non_null_exprlist.
    # non_null_exprlist: expr COMMA non_null_exprlist | expr;
    def visitNon_null_exprlist(self, ctx:MT22Parser.Non_null_exprlistContext):
        if(ctx.getChildCount()==1): return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.non_null_exprlist())


    # Visit a parse tree produced by MT22Parser#paradecl.
    """
    (INHERIT | OUT | INHERIT OUT |) (
		(
			(IDENTIFIER COLON typ)
			| (
				INHERIT COLON ARRAY_TYP LEFT_SQUAREBRACK (
					intList /*dimension*/
				) RIGHT_SQUAREBRACK OF typ
			)
		)
	);
    """
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        inheritTemp = False
        outTemp = False
        if(ctx.INHERIT()): inheritTemp = True
        if(ctx.OUT()): outTemp = True
        # print(inheritTemp, outTemp)
        if(ctx.getChildCount() <= 5):
            name = ctx.IDENTIFIER().getText()
            typo = self.visit(ctx.typ())
            return ParamDecl(name, typo, outTemp, inheritTemp)
        else: 
            name = ctx.IDENTIFIER().getText()
            dimen = self.visit(ctx.intList()) # dimension
            typo = self.visit(ctx.typ())
            arrayTyp = ArrayType(dimen,typo)
            return ParamDecl(name, arrayTyp, outTemp, inheritTemp)

    # Visit a parse tree produced by MT22Parser#funcdecl.
    ## *** funcdecl: funcdecl_noInherit | funcdecl_Inherit; ***
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        if(ctx.funcdecl_noInherit()): return [self.visit(ctx.funcdecl_noInherit())]
        elif(ctx.funcdecl_Inherit()): return [self.visit(ctx.funcdecl_Inherit())]


    # Visit a parse tree produced by MT22Parser#funcdecl_noInherit.
    """
    funcdecl_noInherit:
	IDENTIFIER COLON FUNCTION functyp paramlist block_stmt;
    """
    def visitFuncdecl_noInherit(self, ctx:MT22Parser.Funcdecl_noInheritContext):
        name = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.functyp())
        params = self.visit(ctx.paramlist())
        inheritTemp = None
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name,typ,params,inheritTemp,body)


    ## Visit a parse tree produced by MT22Parser#funcdecl_Inherit.
    """
    funcdecl_Inherit:
	IDENTIFIER COLON FUNCTION functyp paramlist INHERIT IDENTIFIER block_stmt;
    """
    def visitFuncdecl_Inherit(self, ctx:MT22Parser.Funcdecl_InheritContext):
        name = ctx.IDENTIFIER(0).getText()
        typ = self.visit(ctx.functyp())
        params = self.visit(ctx.paramlist())
        inheritTemp = ctx.IDENTIFIER(1).getText()
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name,typ,params,inheritTemp,body)

    ## Visit a parse tree produced by MT22Parser#functyp.
    """
    functyp:
	BOOLEAN
	| INT
	| FLOAT
	| ARRAY_TYP
	| STRING
	| VOID
	| AUTO
	| (
		ARRAY_TYP LEFT_SQUAREBRACK (intList /*dimension*/) RIGHT_SQUAREBRACK OF typ
	);
    """
    def visitFunctyp(self, ctx:MT22Parser.FunctypContext):
        if (ctx.INT()): return IntegerType()
        elif(ctx.FLOAT()): return FloatType()
        elif(ctx.BOOLEAN()): return BooleanType()
        elif(ctx.ARRAY_TYP()):
            dimen = self.visit(ctx.intList())
            typ = self.visit(ctx.typ())
            return ArrayType(dimen, typ)
        elif(ctx.AUTO()): return AutoType()
        elif(ctx.STRING()): return StringType()
        elif(ctx.VOID()): return VoidType()


    # Visit a parse tree produced by MT22Parser#paramlist.
    ## paramlist: LEFT_PAREN params RIGHT_PAREN;
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visit(ctx.params())


    # Visit a parse tree produced by MT22Parser#params.
    # params: non_null_params |;
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        if(ctx.getChildCount() == 1): return self.visit(ctx.non_null_params())
        return[] #return list of paraDecl


    # Visit a parse tree produced by MT22Parser#non_null_params.
    # non_null_params: paradecl COMMA non_null_params | paradecl;
    def visitNon_null_params(self, ctx:MT22Parser.Non_null_paramsContext):
        if (ctx.getChildCount() == 1): return [self.visit(ctx.paradecl())]
        return [self.visit(ctx.paradecl())] + self.visit(ctx.non_null_params())



    # Visit a parse tree produced by MT22Parser#expr.
    """
    expr:
	relational_expr CONCAT_OP relational_expr
	| relational_expr;
    """
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if(ctx.getChildCount()==1): 
            return self.visit(ctx.relational_expr(0))
        else:
            left = self.visit(ctx.relational_expr(0))
            right = self.visit(ctx.relational_expr(1))
            op = ctx.CONCAT_OP().getText()
            return BinExpr(op,left,right)



    ## Visit a parse tree produced by MT22Parser#relational_expr.
    """
    relational_expr:
	logical_expr (relational_EQ_op | relational_noEQ_op) logical_expr
	| logical_expr;
    """
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        if(ctx.getChildCount()==1):
            return self.visit(ctx.logical_expr(0))
        else:
            left = self.visit(ctx.logical_expr(0))
            right = self.visit(ctx.logical_expr(1))
            op = 0
            if(ctx.relational_EQ_op()): op = self.visit(ctx.relational_EQ_op())
            else: op = self.visit(ctx.relational_noEQ_op())
            return BinExpr(op,left,right)



    # Visit a parse tree produced by MT22Parser#relational_EQ_op.
    ## relational_EQ_op: EQUAL_TO_OP | NOT_EQUAL_TO_OP;
    def visitRelational_EQ_op(self, ctx:MT22Parser.Relational_EQ_opContext):
        if(ctx.EQUAL_TO_OP()): return ctx.EQUAL_TO_OP().getText()
        elif(ctx.NOT_EQUAL_TO_OP()): return ctx.NOT_EQUAL_TO_OP().getText()
        


    ## Visit a parse tree produced by MT22Parser#relational_noEQ_op.
    """
    relational_noEQ_op:
	LESS_OP
	| EQ_LESS_OP
	| GREATER_OP
	| EQ_GREATER_OP;
    """
    def visitRelational_noEQ_op(self, ctx:MT22Parser.Relational_noEQ_opContext):
        if (ctx.LESS_OP()): return ctx.LESS_OP().getText()
        elif (ctx.EQ_LESS_OP()): return ctx.EQ_LESS_OP().getText()
        elif (ctx.GREATER_OP()): return ctx.GREATER_OP().getText()
        elif (ctx.EQ_GREATER_OP()): return ctx.EQ_GREATER_OP().getText()
        



    ## Visit a parse tree produced by MT22Parser#logical_expr.
    # logical_expr: logical_expr logical_op add_expr | add_expr;
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        if(ctx.getChildCount()==1):return self.visit(ctx.add_expr())
        else:
            left = self.visit(ctx.logical_expr())
            right = self.visit(ctx.add_expr())
            op = self.visit(ctx.logical_op())
            return BinExpr(op,left,right)

    ## Visit a parse tree produced by MT22Parser#logical_op.
    # logical_op: CONJ_OP | DISJ_OP;
    def visitLogical_op(self, ctx:MT22Parser.Logical_opContext):
        if(ctx.CONJ_OP()): return ctx.CONJ_OP().getText()
        elif(ctx.DISJ_OP()): return ctx.DISJ_OP().getText()



    ## Visit a parse tree produced by MT22Parser#add_expr.
    # add_expr: add_expr (ADD_OP | SUB_OP) mul_expr | mul_expr;
    def visitAdd_expr(self, ctx:MT22Parser.Add_exprContext):
        if(ctx.getChildCount()==1):return self.visit(ctx.mul_expr())
        else:
            left = self.visit(ctx.add_expr())
            right = self.visit(ctx.mul_expr())
            op = 0
            if(ctx.ADD_OP()): op = ctx.ADD_OP().getText()
            elif (ctx.SUB_OP()): op = ctx.SUB_OP().getText()
            return BinExpr(op,left,right)


    ## Visit a parse tree produced by MT22Parser#mul_expr.
    # mul_expr: mul_expr mul_op nega_expr | nega_expr;
    def visitMul_expr(self, ctx:MT22Parser.Mul_exprContext):
        if(ctx.getChildCount()==1):return self.visit(ctx.nega_expr())
        else:
            left = self.visit(ctx.mul_expr())
            right = self.visit(ctx.nega_expr())
            op = self.visit(ctx.mul_op())
            return BinExpr(op,left,right)


    ## Visit a parse tree produced by MT22Parser#mul_op.
    # mul_op: MUL_OP | DIV_OP | MOD_OP;
    def visitMul_op(self, ctx:MT22Parser.Mul_opContext):
        if(ctx.MUL_OP()):return ctx.MUL_OP().getText()
        elif(ctx.DIV_OP()):return ctx.DIV_OP().getText()
        elif(ctx.MOD_OP()):return ctx.MOD_OP().getText()


    # Visit a parse tree produced by MT22Parser#nega_expr.
    # nega_expr: NEGA_OP nega_expr | sign_expr;
    def visitNega_expr(self, ctx:MT22Parser.Nega_exprContext):
        if (ctx.getChildCount() == 2): 
            return UnExpr(ctx.NEGA_OP().getText(), self.visit(ctx.nega_expr()))        
        return self.visit(ctx.sign_expr())


    ## Visit a parse tree produced by MT22Parser#sign_expr.
    """
    sign_expr: SUB_OP sign_expr | index_expr;
    """
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        if (ctx.getChildCount() == 2): 
            return UnExpr(ctx.SUB_OP().getText(), self.visit(ctx.sign_expr()))
        return self.visit(ctx.index_expr())


    ## Visit a parse tree produced by MT22Parser#index_expr.
    """
    index_expr:
	IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK
	| funcall_expr;
    """
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        if (ctx.getChildCount()==1): return self.visit(ctx.funcall_expr())
        else:
            name = ctx.IDENTIFIER().getText()
            cellTemp = self.visit(ctx.index_list())
            return ArrayCell(name, cellTemp)

    ## Visit a parse tree produced by MT22Parser#index_list.
    #  index_list: expr COMMA index_list | expr;
    def visitIndex_list(self, ctx:MT22Parser.Index_listContext):
        if (ctx.getChildCount()==1): return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.index_list())


    ## Visit a parse tree produced by MT22Parser#funcall_expr.
    """
    funcall_expr:
	IDENTIFIER LEFT_PAREN exprlist RIGHT_PAREN
	| subexpr;
    """
    def visitFuncall_expr(self, ctx:MT22Parser.Funcall_exprContext):
        if(ctx.getChildCount()==1):return self.visit(ctx.subexpr())
        else:
            name = ctx.IDENTIFIER().getText()
            argsList = self.visit(ctx.exprlist())
            return FuncCall(name, argsList)
    
    ## Visit a parse tree produced by MT22Parser#subexpr.
    """
    subexpr:
        IDENTIFIER
        | BOOL_LIT
        | INT_LIT
        | FLOAT_LIT
        | STRING_LIT
        | arr
        | LEFT_PAREN expr RIGHT_PAREN
        | special_function;
    """
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        if(ctx.getChildCount()==3): return self.visit(ctx.expr())
        elif(ctx.IDENTIFIER()): return Id(ctx.IDENTIFIER().getText())
        elif(ctx.BOOL_LIT()): 
            if(ctx.BOOL_LIT().getText() == "true"): return BooleanLit(True)
            return BooleanLit(False)
        elif(ctx.INT_LIT()): return IntegerLit(int(ctx.INT_LIT().getText()))
        elif(ctx.FLOAT_LIT()): 
            text  = ctx.FLOAT_LIT().getText()
            if(text[0]=='.'):
                text = '0'+ text
            return FloatLit(float(text))
        elif(ctx.STRING_LIT()): return StringLit(ctx.STRING_LIT().getText())
        elif(ctx.special_function()): 
            lst = self.visit(ctx.special_function())
            return FuncCall(lst[0],lst[1])
        elif(ctx.arr()): return self.visit(ctx.arr())


    # Visit a parse tree produced by MT22Parser#stmt.
    # stmt: matchStmt | unmatchStmt;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if (ctx.matchStmt()):return self.visit(ctx.matchStmt())
        return self.visit(ctx.unmatchStmt())


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    # assign_stmt: lhs ASSIG_OP expr SEMICOLON;
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        lhsTemp = self.visit(ctx.lhs())
        rhsTemp = self.visit(ctx.expr())
        return AssignStmt(lhsTemp,rhsTemp)


    # Visit a parse tree produced by MT22Parser#lhs.
    """
    lhs:
	IDENTIFIER
	| (IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK);
    """
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if(ctx.getChildCount() == 1): return Id(ctx.IDENTIFIER().getText())
        else:
            name = ctx.IDENTIFIER().getText()
            index = self.visit(ctx.index_list())
            return ArrayCell(name, index)


    # Visit a parse tree produced by MT22Parser#unmatchStmt.
    """
    unmatchStmt:
	IF LEFT_PAREN expr RIGHT_PAREN stmt
	| IF LEFT_PAREN expr RIGHT_PAREN matchStmt ELSE unmatchStmt;
    """
    def visitUnmatchStmt(self, ctx:MT22Parser.UnmatchStmtContext):
        if ctx.ELSE(): 
            condTemp = self.visit(ctx.expr())
            tstmtTemp = self.visit(ctx.matchStmt())
            fstmtTemp = self.visit(ctx.unmatchStmt())
            return IfStmt(condTemp, tstmtTemp, fstmtTemp)
        else: 
            condTemp = self.visit(ctx.expr())
            tstmtTemp = self.visit(ctx.stmt())
            fstmtTemp = None
            return IfStmt(condTemp, tstmtTemp, fstmtTemp)



    # Visit a parse tree produced by MT22Parser#matchStmt.
    """
    matchStmt:
	IF LEFT_PAREN expr RIGHT_PAREN matchStmt ELSE matchStmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| block_stmt
	| assign_stmt;
    """
    def visitMatchStmt(self, ctx:MT22Parser.MatchStmtContext):
        if(ctx.getChildCount()==1):
            if(ctx.for_stmt()):return self.visit(ctx.for_stmt())
            elif(ctx.while_stmt()):return self.visit(ctx.while_stmt())
            elif(ctx.do_while_stmt()):return self.visit(ctx.do_while_stmt())
            elif(ctx.break_stmt()):return self.visit(ctx.break_stmt())
            elif(ctx.continue_stmt()):return self.visit(ctx.continue_stmt())
            elif(ctx.return_stmt()):return self.visit(ctx.return_stmt())
            elif(ctx.call_stmt()):return self.visit(ctx.call_stmt())
            elif(ctx.block_stmt()):return self.visit(ctx.block_stmt())
            elif(ctx.assign_stmt()):return self.visit(ctx.assign_stmt())
        else:
            condTemp = self.visit(ctx.expr())
            tstmtTemp = self.visit(ctx.matchStmt(0))
            fstmtTemp = self.visit(ctx.matchStmt(1))
            return IfStmt(condTemp, tstmtTemp, fstmtTemp)
            
    # Visit a parse tree produced by MT22Parser#for_stmt.
    """
    FOR LEFT_PAREN (
		IDENTIFIER
		| (
			IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK
		)
	) ASSIG_OP expr COMMA expr COMMA expr RIGHT_PAREN stmt;
    """
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        assignTemp = AssignStmt(name,self.visit(ctx.expr(0))) 
        if(ctx.index_list()):
            name = ctx.IDENTIFIER().getText()
            cellTemp = self.visit(ctx.index_list())
            assignTemp = AssignStmt(ArrayCell(name, cellTemp),self.visit(ctx.expr(0)))
        condTemp = self.visit(ctx.expr(1))
        updTemp = self.visit(ctx.expr(2))
        stmtTemp = self.visit(ctx.stmt())
        return ForStmt(assignTemp,condTemp,updTemp,stmtTemp)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    # while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        condTemp = self.visit(ctx.expr())
        stmtTemp = self.visit(ctx.stmt())
        return WhileStmt(condTemp,stmtTemp)

    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    """
    do_while_stmt:
	DO block_stmt WHILE LEFT_PAREN expr RIGHT_PAREN SEMICOLON;
    """
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        condTemp = self.visit(ctx.expr())
        block_stmtTemp = self.visit(ctx.block_stmt())
        return DoWhileStmt(condTemp,block_stmtTemp)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    # break_stmt: BREAK SEMICOLON;
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    # continue_stmt: CONTINUE SEMICOLON;
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_stmt.
    # return_stmt: (RETURN expr SEMICOLON) | (RETURN SEMICOLON);
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if(ctx.getChildCount()==2): return ReturnStmt(None)
        exprTemp = self.visit(ctx.expr())
        return ReturnStmt(exprTemp)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    """
    call_stmt:
	special_function SEMICOLON
	| IDENTIFIER LEFT_PAREN exprlist RIGHT_PAREN SEMICOLON;
    """
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        if (ctx.getChildCount()==2): 
            lst =  self.visit(ctx.special_function())
            return CallStmt(lst[0],lst[1])
        argsList = self.visit(ctx.exprlist())
        name = ctx.IDENTIFIER().getText()
        return CallStmt(name, argsList)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    # block_stmt: LEFT_CURBRACK blockelements RIGHT_CURBRACK;
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.blockelements()))


    # Visit a parse tree produced by MT22Parser#blockelements.
    # blockelements: non_null_blockelements |;
    
    def visitBlockelements(self, ctx:MT22Parser.BlockelementsContext):
        if (ctx.getChildCount() == 0): return []
        else:
            result = self.visit(ctx.non_null_blockelements())
            return result


    # Visit a parse tree produced by MT22Parser#non_null_blockelements.
    """
    non_null_blockelements:
	blockelement non_null_blockelements
	| blockelement;
    """
    def visitNon_null_blockelements(self, ctx:MT22Parser.Non_null_blockelementsContext):
        if (ctx.getChildCount() == 1): return self.visit(ctx.blockelement())
        return self.visit(ctx.blockelement()) + self.visit(ctx.non_null_blockelements())  


    # Visit a parse tree produced by MT22Parser#blockelement.
    """
    blockelement: stmt | vardecl | arrayDecl;
    """
    def visitBlockelement(self, ctx:MT22Parser.BlockelementContext):
        if (ctx.stmt()): return [self.visit(ctx.stmt())]
        elif (ctx.vardecl()): 
            return self.visit(ctx.vardecl())
        elif (ctx.arrayDecl()): return self.visit(ctx.arrayDecl())



    # Visit a parse tree produced by MT22Parser#special_function.
    """
    special_function:
	read_integer
	| print_integer
	| read_float
	| write_float
	| read_boolean
	| print_boolean
	| read_string
	| print_string
	| super_func
	| prevent_default;
    """
    def visitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        if (ctx.read_integer()): return self.visit(ctx.read_integer())
        elif (ctx.print_integer()): return self.visit(ctx.print_integer())
        elif (ctx.read_float()): return self.visit(ctx.read_float())
        elif (ctx.write_float()): return self.visit(ctx.write_float())
        elif (ctx.read_boolean()): return self.visit(ctx.read_boolean())
        elif (ctx.print_boolean()): return self.visit(ctx.print_boolean())
        elif (ctx.read_string()): return self.visit(ctx.read_string())
        elif (ctx.print_string()): return self.visit(ctx.print_string())
        elif (ctx.super_func()): return self.visit(ctx.super_func())
        elif (ctx.prevent_default()): return self.visit(ctx.prevent_default())



    # Visit a parse tree produced by MT22Parser#read_integer.
    # read_integer: READINT LEFT_PAREN RIGHT_PAREN;

    def visitRead_integer(self, ctx:MT22Parser.Read_integerContext):
        name = ctx.READINT().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]


    # Visit a parse tree produced by MT22Parser#print_integer.
    """
    print_integer:
	PRINTINT LEFT_PAREN expr RIGHT_PAREN;
    """
    def visitPrint_integer(self, ctx:MT22Parser.Print_integerContext):
        name = ctx.PRINTINT().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#read_float.
    # read_float: READFLOAT LEFT_PAREN RIGHT_PAREN;
    def visitRead_float(self, ctx:MT22Parser.Read_floatContext):
        name = ctx.READFLOAT().getText()
        exprTemp = []
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#write_float.
    # write_float: WRITEFLOAT LEFT_PAREN expr RIGHT_PAREN;
    def visitWrite_float(self, ctx:MT22Parser.Write_floatContext):
        name = ctx.WRITEFLOAT().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#read_boolean.
    # read_boolean: READBOOLEAN LEFT_PAREN RIGHT_PAREN;
    def visitRead_boolean(self, ctx:MT22Parser.Read_booleanContext):
        name = ctx.READBOOLEAN().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#print_boolean.
    # print_boolean: PRINTBOOL LEFT_PAREN expr RIGHT_PAREN;
    def visitPrint_boolean(self, ctx:MT22Parser.Print_booleanContext):
        name = ctx.PRINTBOOL().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#read_string.
    # read_string: READSTRING LEFT_PAREN RIGHT_PAREN;
    def visitRead_string(self, ctx:MT22Parser.Read_stringContext):
        name = ctx.READSTRING().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#print_string.
    # print_string: PRINTSTRING LEFT_PAREN expr RIGHT_PAREN;
    def visitPrint_string(self, ctx:MT22Parser.Print_stringContext):
        name = ctx.PRINTSTRING().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#super_func.
    # super_func: SUPERFUNC exprlist;
    def visitSuper_func(self, ctx:MT22Parser.Super_funcContext):
        name = ctx.SUPERFUNC().getText()
        exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]

    # Visit a parse tree produced by MT22Parser#prevent_default.
    # prevent_default: PREVENTDEFAULT LEFT_PAREN RIGHT_PAREN;
    def visitPrevent_default(self, ctx:MT22Parser.Prevent_defaultContext):
        name = ctx.PREVENTDEFAULT().getText()
        if(ctx.getChildCount()==3):
            exprTemp = []
        else: exprTemp = self.visit(ctx.exprlist())
        return [name, exprTemp]