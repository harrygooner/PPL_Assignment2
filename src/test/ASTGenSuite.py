"""
Họ và tên: Trần Huy Nam Hưng
MSSV: 2052119
"""


import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def testcase5(self):
        # test vardecl with no init of array
        input = """x: array[2,3] of integer;"""
        expect = str(Program([
            VarDecl("x", ArrayType([2, 3], IntegerType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def testcase6(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def testcase7(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";
                    a: integer = a[1+2, 1*5];"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(a, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def testcase8(self):
        # test vardecl with init of expression
        input = """x, y: integer = 1*2, 2+3;
                    a: string = "abc" :: "def";
                    d: integer = a[1+2, 1*5];
                    c: string = a(1, f("abc"));"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(*, IntegerLit(1), IntegerLit(2)))
	VarDecl(y, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(a, StringType, BinExpr(::, StringLit(abc), StringLit(def)))
	VarDecl(d, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(5))]))
	VarDecl(c, StringType, FuncCall(a, [IntegerLit(1), FuncCall(f, [StringLit(abc)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def testcase9(self):
        # test vardecl with no init of array
        input = """x: array[2,3] of integer = {1,2,3};"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def testcase10(self):
        # test basic funcdecls
        input = """
    foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    main: function void () {
        printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def testcase11(self):
        # test funcdecls
        input = """main: function void () {
        x: integer;
        x = (3+4)*2;
        b: array [2] of float;
        b[0] = 4.5;
        preventDefault();
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(*, BinExpr(+, IntegerLit(3), IntegerLit(4)), IntegerLit(2))), VarDecl(b, ArrayType([2], FloatType)), AssignStmt(ArrayCell(b, [IntegerLit(0)]), FloatLit(4.5)), CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def testcase12(self):
        # ifstmt without blockstmt and else
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello world";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def testcase13(self):
        # ifstmt without blockstmt but have else
        input = """
    main: function void () {
        if (3 > 4 + 5) a[0] = "hello world";
        else a[0] = "hello world in else";
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, IntegerLit(3), BinExpr(+, IntegerLit(4), IntegerLit(5))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(hello world in else)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def testcase14(self):
        # forstmt without block
        input = """
    main: function void () {
        for (i=1,i<100,i+1) break;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def testcase15(self):
        # forstmt with block
        input = """
    main: function void () {
        for (i=1,i<100,i+1) {
            if (a<1) continue;
            a: boolean = false;
        }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(1)), ContinueStmt()), VarDecl(a, BooleanType, BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def testcase16(self):
        # whilestmt without block
        input = """
    testfunc: function integer (a: integer) {
        while (a < 10) a = a + 1;
        return a + 3;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))), ReturnStmt(BinExpr(+, Id(a), IntegerLit(3)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def testcase17(self):
        # whilestmt with block
        input = """
    testfunc: function integer (a: integer) {
        while (a < 10) {
            for (i=1,i<10,i+1) a = a + 1;
        }
        readBoolean(a==10);
        return a + 3;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))])), CallStmt(readBoolean, BinExpr(==, Id(a), IntegerLit(10))), ReturnStmt(BinExpr(+, Id(a), IntegerLit(3)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def testcase18(self):
        # dowhile
        input = """
    testfunc: function integer (c: string) {
        do {
            readString("abc");
            c = c :: "abc";
            printString(c);
        } while (c != "" );
        return 1;
    }
    main: function void () {
        testfunc();
}"""
        expect = """Program([
	FuncDecl(testfunc, IntegerType, [Param(c, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(c), StringLit()), BlockStmt([CallStmt(readString, StringLit(abc)), AssignStmt(Id(c), BinExpr(::, Id(c), StringLit(abc))), CallStmt(printString, Id(c))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(testfunc, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def testcase19(self):
        input = """
    testfunc: function auto (a: boolean) {
        while (a < 10) {
            {
                a = a + 1;
            }
        }
    }
"""
        expect = """Program([
	FuncDecl(testfunc, AutoType, [Param(a, BooleanType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def testcase20(self):
        input = """
    testfunc: function string (a: boolean) {
        x: float = 1.5e-10 + x + y;
    }
"""
        expect = """Program([
	FuncDecl(testfunc, StringType, [Param(a, BooleanType)], None, BlockStmt([VarDecl(x, FloatType, BinExpr(+, BinExpr(+, FloatLit(1.5e-10), Id(x)), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    
    
    def testcase21(self):
        input = """
    testfunc: function void (inherit out a: array[1] of boolean) {
        if(a[1, 2] == "true")
            super(printInteger(a[1*2, 3+4]), x%2);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([1], BooleanType))], None, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(true)), CallStmt(super, FuncCall(printInteger, [ArrayCell(a, [BinExpr(*, IntegerLit(1), IntegerLit(2)), BinExpr(+, IntegerLit(3), IntegerLit(4))])]), BinExpr(%, Id(x), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def testcase22(self):
        input = """main: function void() {
    c = true;
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(c), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def testcase23(self):
        input = """
    testfunc: function void (inherit out a: array[2, 3] of boolean) inherit foo {
        if(a[a[1, 2], 2] == "true") {
            {
                {
                    a[a[a[1, 2], 3], 2] = "false";
                }
            }
        }
            
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([2, 3], BooleanType))], foo, BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(2)]), StringLit(true)), BlockStmt([BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3)]), IntegerLit(2)]), StringLit(false))])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    def testcase24(self):
        input = """
    testfunc: function void (inherit out a: array[2, 3] of float) inherit foo {
        do {
            for (a[2,3] = 4.5, (!!b && a[10] == true) || a[10] == false, b >= !b) {
                while (a_bss[2]) {
                    x: float = 1.5e-10 * --x;
                    x = 2.5 % a[2,2];
                    continue;
                }
                
                if (a[1] != !("false")) {
                    readFloat();
                    break;
                }
            }
            
            main(2+5.5, "55" :: b);
        } while (true) ;
                    
        main: array[2 , 4] of boolean = {true, "223"};
        
        a = test(a[2, 23 ,23], !!aa, --a);
    }
"""
        expect = """Program([
	FuncDecl(testfunc, VoidType, [InheritOutParam(a, ArrayType([2, 3], FloatType))], foo, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(2), IntegerLit(3)]), FloatLit(4.5)), BinExpr(==, BinExpr(||, BinExpr(==, BinExpr(&&, UnExpr(!, UnExpr(!, Id(b))), ArrayCell(a, [IntegerLit(10)])), BooleanLit(True)), ArrayCell(a, [IntegerLit(10)])), BooleanLit(False)), BinExpr(>=, Id(b), UnExpr(!, Id(b))), BlockStmt([WhileStmt(ArrayCell(a_bss, [IntegerLit(2)]), BlockStmt([VarDecl(x, FloatType, BinExpr(*, FloatLit(1.5e-10), UnExpr(-, UnExpr(-, Id(x))))), AssignStmt(Id(x), BinExpr(%, FloatLit(2.5), ArrayCell(a, [IntegerLit(2), IntegerLit(2)]))), ContinueStmt()])), IfStmt(BinExpr(!=, ArrayCell(a, [IntegerLit(1)]), UnExpr(!, StringLit(false))), BlockStmt([CallStmt(readFloat, ), BreakStmt()]))])), CallStmt(main, BinExpr(+, IntegerLit(2), FloatLit(5.5)), BinExpr(::, StringLit(55), Id(b)))])), VarDecl(main, ArrayType([2, 4], BooleanType), ArrayLit([BooleanLit(True), StringLit(223)])), AssignStmt(Id(a), FuncCall(test, [ArrayCell(a, [IntegerLit(2), IntegerLit(23), IntegerLit(23)]), UnExpr(!, UnExpr(!, Id(aa))), UnExpr(-, UnExpr(-, Id(a)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    def testcase25(self):
        prog = """dd: integer;"""
        expect = str(Program([VarDecl("dd", typ=IntegerType())]))
        self.assertTrue(TestAST.test(prog, expect, 325))

    def testcase26(self):
        prog = """a, b, c, d, e, f, g, h: integer;"""
        expect = str(
            Program(
                [
                    VarDecl("a", typ=IntegerType()),
                    VarDecl("b", typ=IntegerType()),
                    VarDecl("c", typ=IntegerType()),
                    VarDecl("d", typ=IntegerType()),
                    VarDecl("e", typ=IntegerType()),
                    VarDecl("f", typ=IntegerType()),
                    VarDecl("g", typ=IntegerType()),
                    VarDecl("h", typ=IntegerType()),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 326))

    def testcase27(self):
        prog = """a: integer = 2023;"""
        expect = str(Program([VarDecl("a", typ=IntegerType(), init=IntegerLit(2023))]))
        self.assertTrue(TestAST.test(prog, expect, 327))

    def testcase28(self):
        prog = "a: auto = arr[1, foo(), three, 2*2];"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        ArrayCell(
                            "arr",
                            [
                                IntegerLit(1),
                                FuncCall("foo", []),
                                Id("three"),
                                BinExpr("*", IntegerLit(2), IntegerLit(2)),
                            ],
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 328), f"Correct {expect}")

    def testcase29(self):
        prog = """a: integer = -404;
b: boolean = !true;"""
        expect = str(
            Program(
                [
                    VarDecl("a", typ=IntegerType(), init=UnExpr("-", IntegerLit(404))),
                    VarDecl("b", typ=BooleanType(), init=UnExpr("!", BooleanLit(True))),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 329), f"Correct: \n{expect}")

    def testcase30(self):
        prog = """a: integer = -101 * -4;"""
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        typ=IntegerType(),
                        init=BinExpr(
                            "*", UnExpr("-", IntegerLit(101)), UnExpr("-", IntegerLit(4))
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 330), f"Correct: \n{expect}")


    def testcase31(self):
        prog = "lol: integer = 11 + - 2;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="lol",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="+",
                            left=IntegerLit(11),
                            right=UnExpr(op="-", val=IntegerLit(2)),
                        ),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 331), f"Correct {expect}")

    def testcase32(self):
        prog = "a: integer = 100 + 100 * -100 - 100 / 100 + 100 % 100;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        IntegerType(),
                        init=BinExpr(
                            op="+",
                            left=BinExpr(
                                op="-",
                                left=BinExpr(
                                    op="+",
                                    left=IntegerLit(100),
                                    right=BinExpr(
                                        op="*",
                                        left=IntegerLit(100),
                                        right=UnExpr(op="-", val=IntegerLit(100)),
                                    ),
                                ),
                                right=BinExpr(
                                    op="/", left=IntegerLit(100), right=IntegerLit(100)
                                ),
                            ),
                            right=BinExpr(
                                op="%", left=IntegerLit(100), right=IntegerLit(100)
                            ),
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 332), f"Correct: {expect}")





    def testcase33(self):
        prog = "a: integer = two() || three;"
        expect = str(
            Program(
                [
                    VarDecl(
                        name="a",
                        typ=IntegerType(),
                        init=BinExpr(
                            op="||", left=FuncCall("two", []), right=Id("three")
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 333), f"Correct {expect}")

    def testcase34(self):
        prog = "a: auto = two() != three;"
        expect = str(
            Program(
                [
                    VarDecl(
                        "a",
                        AutoType(),
                        init=BinExpr("!=", FuncCall("two", []), Id("three")),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 334), f"Correct {expect}")

    def testcase35(self):
        prog = """main: function void() {
callFunc(1, "String", foo());
}"""
        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                CallStmt(
                                    "callFunc",
                                    [
                                        IntegerLit(1),
                                        StringLit("String"),
                                        FuncCall("foo", []),
                                    ],
                                )
                            ]
                        ),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(prog, expect, 335), f"Correct {expect}")

    def testcase36(self):
        prog = """main: function void() {
    if (foo == barz)
        if (barz == bar)
            call();
        else
            dontCall();
    else
        callAPI();
}"""

        expect = str(
            Program(
                [
                    FuncDecl(
                        "main",
                        VoidType(),
                        [],
                        None,
                        BlockStmt(
                            [
                                IfStmt(
                                    BinExpr("==", Id("foo"), Id("barz")),
                                    IfStmt(
                                        BinExpr("==", Id("barz"), Id("bar")),
                                        CallStmt("call", []),
                                        CallStmt("dontCall", []),
                                    ),
                                    CallStmt("callAPI", []),
                                )
                            ]
                        ),
                    )
                ]
            )
        )

        self.assertTrue(TestAST.test(prog, expect, 336), f"Correct {expect}")

    def testcase37(self):
        input = """
      main:function void() {
        foo(5*3-12);
        foobar("hiiii");
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(-, BinExpr(*, IntegerLit(5), IntegerLit(3)), IntegerLit(12))), CallStmt(foobar, StringLit(hiiii))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def testcase38(self):
        input = """main: function void() {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def testcase39(self):
        input = """
      test: function integer() {
        return 2+3;
      }
      """
        expect = """Program([
	FuncDecl(test, IntegerType, [], None, BlockStmt([ReturnStmt(BinExpr(+, IntegerLit(2), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def testcase40(self):
        input = """test: function float(){return 2_3e+3;}"""
        expect = """Program([
	FuncDecl(test, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(23000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def testcase41(self):
        input = """asd: function void(){
        return 2_3 + 3.2 - 49;
      }"""
        expect = """Program([
	FuncDecl(asd, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(+, IntegerLit(23), FloatLit(3.2)), IntegerLit(49)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def testcase42(self):
        input = """
      lol: function integer() {
        a = arr[0];
        return a+3-2%2;
      }
      """
        expect = """Program([
	FuncDecl(lol, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(arr, [IntegerLit(0)])), ReturnStmt(BinExpr(-, BinExpr(+, Id(a), IntegerLit(3)), BinExpr(%, IntegerLit(2), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def testcase43(self):
        input = """
      str_ret: function string(){
        return "abc ";
      }"""
        expect = """Program([
	FuncDecl(str_ret, StringType, [], None, BlockStmt([ReturnStmt(StringLit(abc ))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def testcase44(self):
        input = """
      str_ret: function string(){
        return "abc"::"NICE";
      }"""
        expect = """Program([
	FuncDecl(str_ret, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(::, StringLit(abc), StringLit(NICE)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def testcase45(self):
        input = """
      str_ret: function string(){
        return "abc";
      }"""
        expect = """Program([
	FuncDecl(str_ret, StringType, [], None, BlockStmt([ReturnStmt(StringLit(abc))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def testcase46(self):
        input = """
      str_ret: function integer(){
        a: integer = 12_32323232323232323;
        b: array [1] of integer = {123};
        return a+23-23231123%123*9999;
      }"""
        expect = """Program([
	FuncDecl(str_ret, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1232323232323232323)), VarDecl(b, ArrayType([1], IntegerType), ArrayLit([IntegerLit(123)])), ReturnStmt(BinExpr(-, BinExpr(+, Id(a), IntegerLit(23)), BinExpr(*, BinExpr(%, IntegerLit(23231123), IntegerLit(123)), IntegerLit(9999))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def testcase48(self):
        input = """
      str_ret: function void(){
        a: float = 12.0;
        c: integer;
        b: boolean;
        return;
      }"""
        expect = """Program([
	FuncDecl(str_ret, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(12.0)), VarDecl(c, IntegerType), VarDecl(b, BooleanType), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def testcase49(self):
        input = """
        a: integer;
        b,c: integer;
        e,f,g: float;
        d: array [1] of integer;
      """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(e, FloatType)
	VarDecl(f, FloatType)
	VarDecl(g, FloatType)
	VarDecl(d, ArrayType([1], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def testcase50(self):
        input = """
      a,b: string = "hi", "YO bro";
      """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hi))
	VarDecl(b, StringType, StringLit(YO bro))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def testcase51(self):
        input = """
      // hey
      a: integer = 123_123123_123123123213123;
      """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(123123123123123123213123))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def testcase52(self):
        input = """
        main:function void(){
      for (i = 1, i < 10, i + 1) {
        writeInt(i);
      }
        }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def testcase53(self):
        input = """
        /* masdjaskd jklasjdk ljaklsjdlk jslkajdl jasd */
        ///
        ///////
        //sad asd/ as/d
        // 123 123
        main: function void(){}
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def testcase54(self):
        input = """
        x: integer = 65;
          fact: function integer (n: integer) {
              if (n == 0) return 1;
              else return n * fact(n - 1);
          }
          inc: function void(out n: integer, delta: integer) {
              n = n + delta;
          }
          main: function void() {
              delta: integer = fact(3);
              inc(x, delta);
              printInteger(x);
          }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def testcase55(self):
        input = """
      x: string = "ahsdkjashdkahkdads";
      """
        expect = """Program([
	VarDecl(x, StringType, StringLit(ahsdkjashdkahkdads))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def testcase56(self):
        input = """
        main: function void() {
          result: integer = fact(5);
          printInteger(result);
          str: string = "yo bro, such a nice day";
        }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType, FuncCall(fact, [IntegerLit(5)])), CallStmt(printInteger, Id(result)), VarDecl(str, StringType, StringLit(yo bro, such a nice day))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def testcase57(self):
        input = """
      main: function void(){
        x: integer = 12;
        if(x+2==0) return;
        else x = x+1;
        for(i=1,i<10,i+1){
          writeInt(i);
        }
        return;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(12)), IfStmt(BinExpr(==, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(0)), ReturnStmt(), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def testcase58(self):
        input = """
      main: function void(){
        x: string = "HI BRP asdasdasd";
        if(x=="TEST") return;
        else x = "HAHAHAHHA";
        for(i=1,i<10,i+1){
          foo(i);
        }
        return;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(HI BRP asdasdasd)), IfStmt(BinExpr(==, Id(x), StringLit(TEST)), ReturnStmt(), AssignStmt(Id(x), StringLit(HAHAHAHHA))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(foo, Id(i))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def testcase59(self):
        input = """
          main: function integer(){
            x: integer = readInt();
            if(x+2%3-11+99!=0) return;
            else x = x+1;
            for(i=1,i<10,i+1){
              printInteger(arr[i,i]);
            }
            return x+3;
          }
          """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(readInt, [])), IfStmt(BinExpr(!=, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), BinExpr(%, IntegerLit(2), IntegerLit(3))), IntegerLit(11)), IntegerLit(99)), IntegerLit(0)), ReturnStmt(), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(i)]))])), ReturnStmt(BinExpr(+, Id(x), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def testcase60(self):
        input = """
          main: function integer(){
            x: boolean = readInt();
            if(!x) return;
            else x = x+1;
            for(i=1,i<10,i+1){
              printInteger(arr[i,i]);
            }
            return x+3;
          }
          """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(x, BooleanType, FuncCall(readInt, [])), IfStmt(UnExpr(!, Id(x)), ReturnStmt(), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(i)]))])), ReturnStmt(BinExpr(+, Id(x), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def testcase61(self):
        input = """
      foo: function integer(x: integer){
        return x*2;
      }
      main: function void(){
        foo(23);
      }
      """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), IntegerLit(2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(23))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def testcase62(self):
        input = """
      main:function void(){
        x: integer = -2+3-123*12_9;
        y: float = 2e13-23;
        a: integer = 12;
        z: string = "NICE NICE NICE";
        s: boolean = !false && true;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, UnExpr(-, IntegerLit(2)), IntegerLit(3)), BinExpr(*, IntegerLit(123), IntegerLit(129)))), VarDecl(y, FloatType, BinExpr(-, FloatLit(20000000000000.0), IntegerLit(23))), VarDecl(a, IntegerType, IntegerLit(12)), VarDecl(z, StringType, StringLit(NICE NICE NICE)), VarDecl(s, BooleanType, BinExpr(&&, UnExpr(!, BooleanLit(False)), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def testcase63(self):
        input = """
      main: function void(){
        if(true) return;
        else return;
        x: array [2] of integer = {123_232323,-232323_23232};
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(), ReturnStmt()), VarDecl(x, ArrayType([2], IntegerType), ArrayLit([IntegerLit(123232323), UnExpr(-, IntegerLit(23232323232))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))



    def testcase64(self):
        input = """
    main: function void(){
        a: float = .e23;
    }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
        self.assertTrue(TestAST.test(input, expect, 364))

    def testcase65(self):
        input = """main: function void() {
    do {_tttt = 1 + 2;} while (expr + expr);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, Id(expr), Id(expr)), BlockStmt([AssignStmt(Id(_tttt), BinExpr(+, IntegerLit(1), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def testcase66(self):
        input = """main: function void() {
    do {return 1;} while (a && b);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(&&, Id(a), Id(b)), BlockStmt([ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def testcase67(self):
        input = """main: function void() {
    do {break;} while (foo(abc));
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(FuncCall(foo, [Id(abc)]), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def testcase68(self):
        input = """main: function void() {
    do {while (t+z*a) {}} while (2 + a);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, IntegerLit(2), Id(a)), BlockStmt([WhileStmt(BinExpr(+, Id(t), BinExpr(*, Id(z), Id(a))), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def testcase69(self):
        input = """main: function void() {
    do {call(22,11,33); continue; return 1;} while (aa);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(aa), BlockStmt([CallStmt(call, IntegerLit(22), IntegerLit(11), IntegerLit(33)), ContinueStmt(), ReturnStmt(IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def testcase70(self):
        input = """main: function void() {
    do {{{{return 1;} return 2;} return 3;} return 4;} while (z);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(Id(z), BlockStmt([BlockStmt([BlockStmt([BlockStmt([ReturnStmt(IntegerLit(1))]), ReturnStmt(IntegerLit(2))]), ReturnStmt(IntegerLit(3))]), ReturnStmt(IntegerLit(4))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    # Combine all declarations and statements
    def testcase71(self):
        input = """main: function void() {
    pi: float = 3.14;
    n: float;
    n = 5.0;
    S = pi * square(n);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(pi, FloatType, FloatLit(3.14)), VarDecl(n, FloatType), AssignStmt(Id(n), FloatLit(5.0)), AssignStmt(Id(S), BinExpr(*, Id(pi), FuncCall(square, [Id(n)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def testcase72(self):
        input = """main: function void() {
    sum: integer = 0;
    arr: array[5] of integer;
    arr = {5,6,7,8,9};
    for (i = 0, i < 5, i+1) {
        print(cube(arr[i]));
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(arr, ArrayType([5], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, FuncCall(cube, [ArrayCell(arr, [Id(i)])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def testcase73(self):
        input = """main: function void() {
    x = x + 1;
    y = y + 1;
    z = z + 1;
    a, b, c: string = "How", "are", "you";
    if (x == y) {
        a = b;
        b = c;
    }
    else if (y == z) {
        b = c;
        c = a;
    }
    else {
        c = a;
        a = b;
    }
    concat(a, b, c);    
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), AssignStmt(Id(y), BinExpr(+, Id(y), IntegerLit(1))), AssignStmt(Id(z), BinExpr(+, Id(z), IntegerLit(1))), VarDecl(a, StringType, StringLit(How)), VarDecl(b, StringType, StringLit(are)), VarDecl(c, StringType, StringLit(you)), IfStmt(BinExpr(==, Id(x), Id(y)), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(c))]), IfStmt(BinExpr(==, Id(y), Id(z)), BlockStmt([AssignStmt(Id(b), Id(c)), AssignStmt(Id(c), Id(a))]), BlockStmt([AssignStmt(Id(c), Id(a)), AssignStmt(Id(a), Id(b))]))), CallStmt(concat, Id(a), Id(b), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def testcase74(self):
        input = """main: function void() {
    while (a) {
        do {
            a = a + 1;
        }
        while (i + 1);
        return a;
    }
    for (a = 2, tg + wer, df + a) {
        for (j = 0, j < 5, j+1) {
            if (j == 2) continue;
            else if (j == 4) return j;
        }
        return "abc";
    }
    t = f + z;
    print(t);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(Id(a), BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(Id(a))])), ForStmt(AssignStmt(Id(a), IntegerLit(2)), BinExpr(+, Id(tg), Id(wer)), BinExpr(+, Id(df), Id(a)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(j), IntegerLit(2)), ContinueStmt(), IfStmt(BinExpr(==, Id(j), IntegerLit(4)), ReturnStmt(Id(j))))])), ReturnStmt(StringLit(abc))])), AssignStmt(Id(t), BinExpr(+, Id(f), Id(z))), CallStmt(print, Id(t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def testcase75(self):
        input = """main: function void() {
    y = (a + z) && (t || y) :: (z / r % iopd);
    for (j = z, t < n, io / 5) break;
    foo(123);
    call(xsdf,ysdadfs,zdsasfd);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(y), BinExpr(::, BinExpr(&&, BinExpr(+, Id(a), Id(z)), BinExpr(||, Id(t), Id(y))), BinExpr(%, BinExpr(/, Id(z), Id(r)), Id(iopd)))), ForStmt(AssignStmt(Id(j), Id(z)), BinExpr(<, Id(t), Id(n)), BinExpr(/, Id(io), IntegerLit(5)), BreakStmt()), CallStmt(foo, IntegerLit(123)), CallStmt(call, Id(xsdf), Id(ysdadfs), Id(zdsasfd))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def testcase76(self):
        input = """main: function void() {
    sdffds(sadlfsd, sdfljfsdh, dsfhjsfda);
    y = a * b[1,2] + fdsfsd / sdffds;
    z[0,2,3] = sdflk(sfdsjsdl, wqheol);
    do {
        adfsfsd = adsffsd - 12123321 + {sdfd, fsdfdsdfs};
        continue;
    } while (safsaf + dslhfsd - dfshkfd);
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(sdffds, Id(sadlfsd), Id(sdfljfsdh), Id(dsfhjsfda)), AssignStmt(Id(y), BinExpr(+, BinExpr(*, Id(a), ArrayCell(b, [IntegerLit(1), IntegerLit(2)])), BinExpr(/, Id(fdsfsd), Id(sdffds)))), AssignStmt(ArrayCell(z, [IntegerLit(0), IntegerLit(2), IntegerLit(3)]), FuncCall(sdflk, [Id(sfdsjsdl), Id(wqheol)])), DoWhileStmt(BinExpr(-, BinExpr(+, Id(safsaf), Id(dslhfsd)), Id(dfshkfd)), BlockStmt([AssignStmt(Id(adfsfsd), BinExpr(+, BinExpr(-, Id(adsffsd), IntegerLit(12123321)), ArrayLit([Id(sdfd), Id(fsdfdsdfs)]))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def testcase77(self):
        input = """main: function void() {
    { aa = 1; } {
        sfaldfsdf = sdfhdfsfds + sdlffdhs - sdfksdfsdf;
        sjdffsd: integer = 5232;
        if (asdfdfs < ttt + fds) {
            do {i = i+1;} while (i+1);
            return fdfds+fdfdsdf[0,-1] + wssdf[9];
        }
        return fdsfd[0,2,3,4] * xcvs[0,0] / dfsdf[0,1];
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([AssignStmt(Id(aa), IntegerLit(1))]), BlockStmt([AssignStmt(Id(sfaldfsdf), BinExpr(-, BinExpr(+, Id(sdfhdfsfds), Id(sdlffdhs)), Id(sdfksdfsdf))), VarDecl(sjdffsd, IntegerType, IntegerLit(5232)), IfStmt(BinExpr(<, Id(asdfdfs), BinExpr(+, Id(ttt), Id(fds))), BlockStmt([DoWhileStmt(BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(BinExpr(+, BinExpr(+, Id(fdfds), ArrayCell(fdfdsdf, [IntegerLit(0), UnExpr(-, IntegerLit(1))])), ArrayCell(wssdf, [IntegerLit(9)])))])), ReturnStmt(BinExpr(/, BinExpr(*, ArrayCell(fdsfd, [IntegerLit(0), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayCell(xcvs, [IntegerLit(0), IntegerLit(0)])), ArrayCell(dfsdf, [IntegerLit(0), IntegerLit(1)])))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def testcase78(self):
        input = """main: function void() {
    ewr: string = "343dsfsd";
    fdsfsdfds, sdfsdffdosv: float = 12332, "strings";
    rtrwuepa, odsfodew, sohqodls: string = 123321, 12321, {"Stroihsd", fdsfds, dfsfsd};
    break; {
        if (dsfhfdsl + fsdkfdsfdcv > dsffdfdsfd) {
            return sdflfhewlfh;
        }
        else {
            return sdfoqrpsdp;
        }
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(ewr, StringType, StringLit(343dsfsd)), VarDecl(fdsfsdfds, FloatType, IntegerLit(12332)), VarDecl(sdfsdffdosv, FloatType, StringLit(strings)), VarDecl(rtrwuepa, StringType, IntegerLit(123321)), VarDecl(odsfodew, StringType, IntegerLit(12321)), VarDecl(sohqodls, StringType, ArrayLit([StringLit(Stroihsd), Id(fdsfds), Id(dfsfsd)])), BreakStmt(), BlockStmt([IfStmt(BinExpr(>, BinExpr(+, Id(dsfhfdsl), Id(fsdkfdsfdcv)), Id(dsffdfdsfd)), BlockStmt([ReturnStmt(Id(sdflfhewlfh))]), BlockStmt([ReturnStmt(Id(sdfoqrpsdp))]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def testcase79(self):
        input = """main: function void() {
    dsffsd: string = sdfdfsfsd;
    wofewp = dflfd + dfskhdos && 312973 / hdsofd :: ofdfdf;
    sdfdsdfssdf = dsflhfdlhfdshfld + sfdslfdkhlsdf - fdskhiwqds;
    continue; {
        ewrwhro[0,1,2] = fdshlfshdlfds + 123465464 / 546461;
        sdfhds: boolean = "sdhfdsfd";
        fdsfds = 165461;
        return fdsjfwp;
        return 4213165;
        return {1,2,3,4};
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(dsffsd, StringType, Id(sdfdfsfsd)), AssignStmt(Id(wofewp), BinExpr(::, BinExpr(&&, BinExpr(+, Id(dflfd), Id(dfskhdos)), BinExpr(/, IntegerLit(312973), Id(hdsofd))), Id(ofdfdf))), AssignStmt(Id(sdfdsdfssdf), BinExpr(-, BinExpr(+, Id(dsflhfdlhfdshfld), Id(sfdslfdkhlsdf)), Id(fdskhiwqds))), ContinueStmt(), BlockStmt([AssignStmt(ArrayCell(ewrwhro, [IntegerLit(0), IntegerLit(1), IntegerLit(2)]), BinExpr(+, Id(fdshlfshdlfds), BinExpr(/, IntegerLit(123465464), IntegerLit(546461)))), VarDecl(sdfhds, BooleanType, StringLit(sdhfdsfd)), AssignStmt(Id(fdsfds), IntegerLit(165461)), ReturnStmt(Id(fdsjfwp)), ReturnStmt(IntegerLit(4213165)), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def testcase80(self):
        input = """main: function void() {
    do {return 132213;} while (dsfdw / dfsfdsl + (sdfds - fdbkfds));
    rewdsjfewp = dfshdfsfds + _dfshdfs_sdfhdfssdf;
    fdfdhwf(sdfdsf,{123,213,13,aaa,weew});
    for (i = 0, i > 5, i - 1) {
        for (i = 0, i > 5, i - 1) {
            for (i = 0, i > 5, i - 1) {
                for (i = 0, i > 5, i - 1) {
                    return;
                }
            }
        }
    }
}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(+, BinExpr(/, Id(dsfdw), Id(dfsfdsl)), BinExpr(-, Id(sdfds), Id(fdbkfds))), BlockStmt([ReturnStmt(IntegerLit(132213))])), AssignStmt(Id(rewdsjfewp), BinExpr(+, Id(dfshdfsfds), Id(_dfshdfs_sdfhdfssdf))), CallStmt(fdfdhwf, Id(sdfdsf), ArrayLit([IntegerLit(123), IntegerLit(213), IntegerLit(13), Id(aaa), Id(weew)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(>, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt()]))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    # Catch errors
    def testcase81(self):
        input = """dsfhfdslfds: integer = false;
fsdffsdsdf: float = fdsfdsfds;
sfw, sdfhsdfo, dsfodsfhw: string = {1,2,3,4}, sdhfowe, "sfsdhow";
fhslfdsf: function array [1,1,1,1,1,1,1,1,1] of string (inherit out dshfsdldsffd: float) inherit main {
    return;
    return;
    return;
    return;
    dfdsfds = fdslfdsf + dsjkfkds;
    eqwr = fdshlfw[0,1,fdsfdsfds] + fdslfdldfsjlfd;
}
fsdhdfsdf, sdfwe, fwewro: integer = 432, 324432, "adsfsfad";
dfsfsd: function string () {
    sdfdsfds[1,2,2+3,(223+22+dsafr)] = dfshfdsl + fdshlfdsf[0,1,{2.4}];
    call(dsfhfdsldsf,rewro,"123213");
}
"""
        expect = """Program([
	VarDecl(dsfhfdslfds, IntegerType, BooleanLit(False))
	VarDecl(fsdffsdsdf, FloatType, Id(fdsfdsfds))
	VarDecl(sfw, StringType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(sdfhsdfo, StringType, Id(sdhfowe))
	VarDecl(dsfodsfhw, StringType, StringLit(sfsdhow))
	FuncDecl(fhslfdsf, ArrayType([1, 1, 1, 1, 1, 1, 1, 1, 1], StringType), [InheritOutParam(dshfsdldsffd, FloatType)], main, BlockStmt([ReturnStmt(), ReturnStmt(), ReturnStmt(), ReturnStmt(), AssignStmt(Id(dfdsfds), BinExpr(+, Id(fdslfdsf), Id(dsjkfkds))), AssignStmt(Id(eqwr), BinExpr(+, ArrayCell(fdshlfw, [IntegerLit(0), IntegerLit(1), Id(fdsfdsfds)]), Id(fdslfdldfsjlfd)))]))
	VarDecl(fsdhdfsdf, IntegerType, IntegerLit(432))
	VarDecl(sdfwe, IntegerType, IntegerLit(324432))
	VarDecl(fwewro, IntegerType, StringLit(adsfsfad))
	FuncDecl(dfsfsd, StringType, [], None, BlockStmt([AssignStmt(ArrayCell(sdfdsfds, [IntegerLit(1), IntegerLit(2), BinExpr(+, IntegerLit(2), IntegerLit(3)), BinExpr(+, BinExpr(+, IntegerLit(223), IntegerLit(22)), Id(dsafr))]), BinExpr(+, Id(dfshfdsl), ArrayCell(fdshlfdsf, [IntegerLit(0), IntegerLit(1), ArrayLit([FloatLit(2.4)])]))), CallStmt(call, Id(dsfhfdsldsf), Id(rewro), StringLit(123213))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def testcase82(self):
        input = """wfdwfupwe_2g3o : function void () {
    eqrspsf, whfe, dsdwp: array [2] of integer = {1123,123214,13232132132}, 42143, "SDhoreht";
    return 13124;
    do {
        e3prwf = ewp1 / dfofhdq + fdjspfew * hdshfdwf;
        return;
        return;
        break;
        continue;
        wqp, aa: string = 43243, 324324;
    }
    while (1 + 2);
    qewqwe = csfwwef + dfjsfwe / eepfpm * hofdsfho - fdhsfd * (132 + dsf);
    aaaf_sfew = 3243240;
    return 432 - 7432 - 432403;
}
dsfsdffd: integer = 5;
dsfweewree: function void(a: string) {
    return;
}
"""
        expect = """Program([
	FuncDecl(wfdwfupwe_2g3o, VoidType, [], None, BlockStmt([VarDecl(eqrspsf, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1123), IntegerLit(123214), IntegerLit(13232132132)])), VarDecl(whfe, ArrayType([2], IntegerType), IntegerLit(42143)), VarDecl(dsdwp, ArrayType([2], IntegerType), StringLit(SDhoreht)), ReturnStmt(IntegerLit(13124)), DoWhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)), BlockStmt([AssignStmt(Id(e3prwf), BinExpr(+, BinExpr(/, Id(ewp1), Id(dfofhdq)), BinExpr(*, Id(fdjspfew), Id(hdshfdwf)))), ReturnStmt(), ReturnStmt(), BreakStmt(), ContinueStmt(), VarDecl(wqp, StringType, IntegerLit(43243)), VarDecl(aa, StringType, IntegerLit(324324))])), AssignStmt(Id(qewqwe), BinExpr(-, BinExpr(+, Id(csfwwef), BinExpr(*, BinExpr(/, Id(dfjsfwe), Id(eepfpm)), Id(hofdsfho))), BinExpr(*, Id(fdhsfd), BinExpr(+, IntegerLit(132), Id(dsf))))), AssignStmt(Id(aaaf_sfew), IntegerLit(3243240)), ReturnStmt(BinExpr(-, BinExpr(-, IntegerLit(432), IntegerLit(7432)), IntegerLit(432403)))]))
	VarDecl(dsfsdffd, IntegerType, IntegerLit(5))
	FuncDecl(dsfweewree, VoidType, [Param(a, StringType)], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def testcase83(self):
        input = """sdfdsf, sdfsd, dsfsdfsfd: integer = 2,3,4;
reerwrewr: string = 324324432;
ffddsfdssdsdfdsf: function void() {

}"""
        expect = """Program([
	VarDecl(sdfdsf, IntegerType, IntegerLit(2))
	VarDecl(sdfsd, IntegerType, IntegerLit(3))
	VarDecl(dsfsdfsfd, IntegerType, IntegerLit(4))
	VarDecl(reerwrewr, StringType, IntegerLit(324324432))
	FuncDecl(ffddsfdssdsdfdsf, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def testcase84(self):
        input = """sdfddsfd: function void() {
    return;
}"""
        expect = """Program([
	FuncDecl(sdfddsfd, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def testcase85(self):
        input = """sdffwfwef: function boolean(out dfwew: string, fddsf: boolean) {
    ewrewewrwerrew = dsffsd + fwqrdsf;
    return;
}"""
        expect = """Program([
	FuncDecl(sdffwfwef, BooleanType, [OutParam(dfwew, StringType), Param(fddsf, BooleanType)], None, BlockStmt([AssignStmt(Id(ewrewewrwerrew), BinExpr(+, Id(dsffsd), Id(fwqrdsf))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def testcase86(self):
        input = """abc: function string(inherit out sdd: string) inherit a123 {
    dsfd = fsdferwer + fsdlhfep / fdsofdsf;
    for (idwewr = 1, fdsfewpfew, fdspwer) {
        {
            ohohohohohohohohoho = 111111;
        }
    }
    rewrpwer, sdfsfdsfd: string = "32432434", {13232,{2133,21321},{abdfgfgf}};
}"""
        expect = """Program([
	FuncDecl(abc, StringType, [InheritOutParam(sdd, StringType)], a123, BlockStmt([AssignStmt(Id(dsfd), BinExpr(+, Id(fsdferwer), BinExpr(/, Id(fsdlhfep), Id(fdsofdsf)))), ForStmt(AssignStmt(Id(idwewr), IntegerLit(1)), Id(fdsfewpfew), Id(fdspwer), BlockStmt([BlockStmt([AssignStmt(Id(ohohohohohohohohoho), IntegerLit(111111))])])), VarDecl(rewrpwer, StringType, StringLit(32432434)), VarDecl(sdfsfdsfd, StringType, ArrayLit([IntegerLit(13232), ArrayLit([IntegerLit(2133), IntegerLit(21321)]), ArrayLit([Id(abdfgfgf)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def testcase87(self):
        input = """aaa123: function string(out trrtet: string) inherit trrtetre {
    return fgwedewrrew;
}"""
        expect = """Program([
	FuncDecl(aaa123, StringType, [OutParam(trrtet, StringType)], trrtetre, BlockStmt([ReturnStmt(Id(fgwedewrrew))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def testcase88(self):
        input = """aaaa: function string(out a: integer) {
    do {
        return;
    } while (asdffsd);
    while (i+i) a = 5;
    sdfdwwprew();
    aaaa, bnbbb, sdfdssdf: string = "a123213", dfsfde, 123214;
    return wer_123abfds;
}"""
        expect = """Program([
	FuncDecl(aaaa, StringType, [OutParam(a, IntegerType)], None, BlockStmt([DoWhileStmt(Id(asdffsd), BlockStmt([ReturnStmt()])), WhileStmt(BinExpr(+, Id(i), Id(i)), AssignStmt(Id(a), IntegerLit(5))), CallStmt(sdfdwwprew, ), VarDecl(aaaa, StringType, StringLit(a123213)), VarDecl(bnbbb, StringType, Id(dfsfde)), VarDecl(sdfdssdf, StringType, IntegerLit(123214)), ReturnStmt(Id(wer_123abfds))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def testcase89(self):
        input = """fewrewrewrewrewr: function void() {
    a = ewwerewr * 11;
    return;
    return;
    return;
    sdfdfdww = fgdshsfdsdffsd + fdsfsdsdf;
    fssdfdsf, rewrerewwer: string = 1,2;
}"""
        expect = """Program([
	FuncDecl(fewrewrewrewrewr, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(*, Id(ewwerewr), IntegerLit(11))), ReturnStmt(), ReturnStmt(), ReturnStmt(), AssignStmt(Id(sdfdfdww), BinExpr(+, Id(fgdshsfdsdffsd), Id(fdsfsdsdf))), VarDecl(fssdfdsf, StringType, IntegerLit(1)), VarDecl(rewrerewwer, StringType, IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """wrewprsd: function array [1,1,1,1,1,2] of string() {}"""
        expect = """Program([
	FuncDecl(wrewprsd, ArrayType([1, 1, 1, 1, 1, 2], StringType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """sdfdsfdsf: function string() {
    a = dfsfwer / 34324 ;
    wqeqe = 1234 * ab + fdsfd2 ;
    {
        return;
        return;
    }
    if (a == 2) {} else {}
}"""
        expect = """Program([
	FuncDecl(sdfdsfdsf, StringType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(dfsfwer), IntegerLit(34324))), AssignStmt(Id(wqeqe), BinExpr(+, BinExpr(*, IntegerLit(1234), Id(ab)), Id(fdsfd2))), BlockStmt([ReturnStmt(), ReturnStmt()]), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([]), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """aaa: boolean = {123213,213213};
fdewew, strings: string = {2313,213123}, 123213;
aaaa, aaaaa, bbbb: string = 111, 23112, 32_42_34.1321;
fdsfsdfsdfds, rewwer: string = 24234, 32432432.213321;"""
        expect = """Program([
	VarDecl(aaa, BooleanType, ArrayLit([IntegerLit(123213), IntegerLit(213213)]))
	VarDecl(fdewew, StringType, ArrayLit([IntegerLit(2313), IntegerLit(213123)]))
	VarDecl(strings, StringType, IntegerLit(123213))
	VarDecl(aaaa, StringType, IntegerLit(111))
	VarDecl(aaaaa, StringType, IntegerLit(23112))
	VarDecl(bbbb, StringType, FloatLit(324234.1321))
	VarDecl(fdsfsdfsdfds, StringType, IntegerLit(24234))
	VarDecl(rewwer, StringType, FloatLit(32432432.213321))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """aaaa3324, stringgg: float = 43432234432, {123,123+1123,52.432};
aaa32132121312: function auto () {
    aaaa2432, treter, were: string = "321321213", 12321, 12312321_2333;
    dsfff = f24324432;
}"""
        expect = """Program([
	VarDecl(aaaa3324, FloatType, IntegerLit(43432234432))
	VarDecl(stringgg, FloatType, ArrayLit([IntegerLit(123), BinExpr(+, IntegerLit(123), IntegerLit(1123)), FloatLit(52.432)]))
	FuncDecl(aaa32132121312, AutoType, [], None, BlockStmt([VarDecl(aaaa2432, StringType, StringLit(321321213)), VarDecl(treter, StringType, IntegerLit(12321)), VarDecl(were, StringType, IntegerLit(123123212333)), AssignStmt(Id(dsfff), Id(f24324432))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """dsrwewre, fdssfd: integer = 213214_213213, dffdsb;
ewqrew: function void() {}
dsffwer: boolean = 324324;
ewrerwerw: function auto(inherit out asadf: string) {

}"""
        expect = """Program([
	VarDecl(dsrwewre, IntegerType, IntegerLit(213214213213))
	VarDecl(fdssfd, IntegerType, Id(dffdsb))
	FuncDecl(ewqrew, VoidType, [], None, BlockStmt([]))
	VarDecl(dsffwer, BooleanType, IntegerLit(324324))
	FuncDecl(ewrerwerw, AutoType, [InheritOutParam(asadf, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """mainnn: function auto(inherit aaaaaaa: string) {
    return;
}"""
        expect = """Program([
	FuncDecl(mainnn, AutoType, [InheritParam(aaaaaaa, StringType)], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """rrewrerw: integer = 432432234+234324342342;
aaaaaa: float = 32442343 / 23423443 * 234324234 :: 1213;
"""
        expect = """Program([
	VarDecl(rrewrerw, IntegerType, BinExpr(+, IntegerLit(432432234), IntegerLit(234324342342)))
	VarDecl(aaaaaa, FloatType, BinExpr(::, BinExpr(*, BinExpr(/, IntegerLit(32442343), IntegerLit(23423443)), IntegerLit(234324234)), IntegerLit(1213)))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """abcxyz: function string(fsdffsdfsd: string) {
    return;
    return;
    break;
    continue;
}"""
        expect = """Program([
	FuncDecl(abcxyz, StringType, [Param(fsdffsdfsd, StringType)], None, BlockStmt([ReturnStmt(), ReturnStmt(), BreakStmt(), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """main: function void () {
            if (true)
                if (false) a = 4;
            else b = 5;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(False), AssignStmt(Id(a), IntegerLit(4)), AssignStmt(Id(b), IntegerLit(5))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def testcase99(self):
        input = """a : boolean = {1_2, .E-003, false, \"string\"};
        a : boolean = {a+b, _40 == c, !false, \"string\\nline\"};
        """
        expect = r"""Program([
	VarDecl(a, BooleanType, ArrayLit([IntegerLit(12), FloatLit(0.0), BooleanLit(False), StringLit(string)]))
	VarDecl(a, BooleanType, ArrayLit([BinExpr(+, Id(a), Id(b)), BinExpr(==, Id(_40), Id(c)), UnExpr(!, BooleanLit(False)), StringLit(string\nline)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def testcase100(self):
        input = """main: function void () {
            arrOfArr = { {1+1, a<=b}, {!true, \"string1\"::\"string\\\"2\\\"\"}, {2e-2 * 1_1.E+3, a[2e-2 * 1_1.E+3]} };
            arrOfArrOfArr = { {{1+1, a<=b}, {!true, \"string1\"::\"string\\\"2\\\"\"}} , {{2e-2 * 1_1.E+3, {a[2e-2 * 1_1.E+3]}}} };
            empArr =  {};
        }"""
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arrOfArr), ArrayLit([ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(<=, Id(a), Id(b))]), ArrayLit([UnExpr(!, BooleanLit(True)), BinExpr(::, StringLit(string1), StringLit(string\"2\"))]), ArrayLit([BinExpr(*, FloatLit(0.02), FloatLit(11000.0)), ArrayCell(a, [BinExpr(*, FloatLit(0.02), FloatLit(11000.0))])])])), AssignStmt(Id(arrOfArrOfArr), ArrayLit([ArrayLit([ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(<=, Id(a), Id(b))]), ArrayLit([UnExpr(!, BooleanLit(True)), BinExpr(::, StringLit(string1), StringLit(string\"2\"))])]), ArrayLit([ArrayLit([BinExpr(*, FloatLit(0.02), FloatLit(11000.0)), ArrayLit([ArrayCell(a, [BinExpr(*, FloatLit(0.02), FloatLit(11000.0))])])])])])), AssignStmt(Id(empArr), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
    def testcase101(self):
        input = """a: array [3] of integer = c;"""
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType), Id(c))
])"""
        self.assertTrue(TestAST.test(input, expect, 401))
    