# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0252\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0109\n\f\f\f")
        buf.write("\16\f\u010c\13\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0114\n\f")
        buf.write("\f\f\16\f\u0117\13\f\5\f\u0119\n\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0126\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\7;\u01d5\n;\f")
        buf.write(";\16;\u01d8\13;\3<\3<\7<\u01dc\n<\f<\16<\u01df\13<\3<")
        buf.write("\5<\u01e2\n<\3<\3<\7<\u01e6\n<\f<\16<\u01e9\13<\7<\u01eb")
        buf.write("\n<\f<\16<\u01ee\13<\3<\3<\3<\7<\u01f3\n<\f<\16<\u01f6")
        buf.write("\13<\3<\5<\u01f9\n<\3=\3=\3>\3>\7>\u01ff\n>\f>\16>\u0202")
        buf.write("\13>\3>\3>\3>\3?\3?\7?\u0209\n?\f?\16?\u020c\13?\3?\3")
        buf.write("?\3?\3@\3@\7@\u0213\n@\f@\16@\u0216\13@\3@\5@\u0219\n")
        buf.write("@\3@\3@\3A\3A\5A\u021f\nA\3B\3B\3B\3C\3C\3C\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\5D\u0237\nD\3E\3")
        buf.write("E\7E\u023b\nE\fE\16E\u023e\13E\3F\3F\5F\u0242\nF\3F\6")
        buf.write("F\u0245\nF\rF\16F\u0246\3G\6G\u024a\nG\rG\16G\u024b\3")
        buf.write("G\3G\3H\3H\3H\5\u010a\u01dd\u01e7\2I\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{>}?\177@\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087A\u0089\2\u008b\2\u008dB\u008f")
        buf.write("C\3\2\16\4\2\f\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62\62\3\2\62;\4\3\f\f\17\17\b\2\n\n\f\f\16\17$$")
        buf.write("))^^\n\2$$))^^ddhhppttvv\4\2GGgg\4\2--//\5\2\13\f\17\17")
        buf.write("\"\"\2\u0262\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u009d")
        buf.write("\3\2\2\2\7\u00aa\3\2\2\2\t\u00b4\3\2\2\2\13\u00bf\3\2")
        buf.write("\2\2\r\u00cb\3\2\2\2\17\u00d8\3\2\2\2\21\u00e3\3\2\2\2")
        buf.write("\23\u00ef\3\2\2\2\25\u00f5\3\2\2\2\27\u0118\3\2\2\2\31")
        buf.write("\u0125\3\2\2\2\33\u0127\3\2\2\2\35\u012c\3\2\2\2\37\u0134")
        buf.write("\3\2\2\2!\u0139\3\2\2\2#\u013f\3\2\2\2%\u0145\3\2\2\2")
        buf.write("\'\u014b\3\2\2\2)\u0152\3\2\2\2+\u0156\3\2\2\2-\u015e")
        buf.write("\3\2\2\2/\u0165\3\2\2\2\61\u0169\3\2\2\2\63\u0172\3\2")
        buf.write("\2\2\65\u0175\3\2\2\2\67\u017e\3\2\2\29\u0181\3\2\2\2")
        buf.write(";\u0186\3\2\2\2=\u0189\3\2\2\2?\u018f\3\2\2\2A\u0197\3")
        buf.write("\2\2\2C\u0199\3\2\2\2E\u019b\3\2\2\2G\u019d\3\2\2\2I\u019f")
        buf.write("\3\2\2\2K\u01a1\3\2\2\2M\u01a3\3\2\2\2O\u01a6\3\2\2\2")
        buf.write("Q\u01a9\3\2\2\2S\u01ac\3\2\2\2U\u01af\3\2\2\2W\u01b1\3")
        buf.write("\2\2\2Y\u01b4\3\2\2\2[\u01b6\3\2\2\2]\u01b9\3\2\2\2_\u01bc")
        buf.write("\3\2\2\2a\u01be\3\2\2\2c\u01c0\3\2\2\2e\u01c2\3\2\2\2")
        buf.write("g\u01c4\3\2\2\2i\u01c6\3\2\2\2k\u01c8\3\2\2\2m\u01ca\3")
        buf.write("\2\2\2o\u01cc\3\2\2\2q\u01ce\3\2\2\2s\u01d0\3\2\2\2u\u01d2")
        buf.write("\3\2\2\2w\u01f8\3\2\2\2y\u01fa\3\2\2\2{\u01fc\3\2\2\2")
        buf.write("}\u0206\3\2\2\2\177\u0210\3\2\2\2\u0081\u021e\3\2\2\2")
        buf.write("\u0083\u0220\3\2\2\2\u0085\u0223\3\2\2\2\u0087\u0236\3")
        buf.write("\2\2\2\u0089\u0238\3\2\2\2\u008b\u023f\3\2\2\2\u008d\u0249")
        buf.write("\3\2\2\2\u008f\u024f\3\2\2\2\u0091\u0092\7t\2\2\u0092")
        buf.write("\u0093\7g\2\2\u0093\u0094\7c\2\2\u0094\u0095\7f\2\2\u0095")
        buf.write("\u0096\7K\2\2\u0096\u0097\7p\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write("\u0099\7g\2\2\u0099\u009a\7i\2\2\u009a\u009b\7g\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\4\3\2\2\2\u009d\u009e\7r\2\2\u009e")
        buf.write("\u009f\7t\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7p\2\2\u00a1")
        buf.write("\u00a2\7v\2\2\u00a2\u00a3\7K\2\2\u00a3\u00a4\7p\2\2\u00a4")
        buf.write("\u00a5\7v\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7i\2\2\u00a7")
        buf.write("\u00a8\7g\2\2\u00a8\u00a9\7t\2\2\u00a9\6\3\2\2\2\u00aa")
        buf.write("\u00ab\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad")
        buf.write("\u00ae\7f\2\2\u00ae\u00af\7H\2\2\u00af\u00b0\7n\2\2\u00b0")
        buf.write("\u00b1\7q\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7v\2\2\u00b3")
        buf.write("\b\3\2\2\2\u00b4\u00b5\7y\2\2\u00b5\u00b6\7t\2\2\u00b6")
        buf.write("\u00b7\7k\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7g\2\2\u00b9")
        buf.write("\u00ba\7H\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7q\2\2\u00bc")
        buf.write("\u00bd\7c\2\2\u00bd\u00be\7v\2\2\u00be\n\3\2\2\2\u00bf")
        buf.write("\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7c\2\2\u00c2")
        buf.write("\u00c3\7f\2\2\u00c3\u00c4\7D\2\2\u00c4\u00c5\7q\2\2\u00c5")
        buf.write("\u00c6\7q\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\u00c9\7c\2\2\u00c9\u00ca\7p\2\2\u00ca\f\3\2\2\2\u00cb")
        buf.write("\u00cc\7r\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce")
        buf.write("\u00cf\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7D\2\2\u00d1")
        buf.write("\u00d2\7q\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7n\2\2\u00d4")
        buf.write("\u00d5\7g\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\16\3\2\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da")
        buf.write("\u00db\7c\2\2\u00db\u00dc\7f\2\2\u00dc\u00dd\7U\2\2\u00dd")
        buf.write("\u00de\7v\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7k\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\u00e2\7i\2\2\u00e2\20\3\2\2\2\u00e3")
        buf.write("\u00e4\7r\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7k\2\2\u00e6")
        buf.write("\u00e7\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7U\2\2\u00e9")
        buf.write("\u00ea\7v\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7k\2\2\u00ec")
        buf.write("\u00ed\7p\2\2\u00ed\u00ee\7i\2\2\u00ee\22\3\2\2\2\u00ef")
        buf.write("\u00f0\7u\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7r\2\2\u00f2")
        buf.write("\u00f3\7g\2\2\u00f3\u00f4\7t\2\2\u00f4\24\3\2\2\2\u00f5")
        buf.write("\u00f6\7r\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7g\2\2\u00f8")
        buf.write("\u00f9\7x\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7p\2\2\u00fb")
        buf.write("\u00fc\7v\2\2\u00fc\u00fd\7F\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write("\u00ff\7h\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7w\2\2\u0101")
        buf.write("\u0102\7n\2\2\u0102\u0103\7v\2\2\u0103\26\3\2\2\2\u0104")
        buf.write("\u0105\7\61\2\2\u0105\u0106\7,\2\2\u0106\u010a\3\2\2\2")
        buf.write("\u0107\u0109\13\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7,\2\2")
        buf.write("\u010e\u0119\7\61\2\2\u010f\u0110\7\61\2\2\u0110\u0111")
        buf.write("\7\61\2\2\u0111\u0115\3\2\2\2\u0112\u0114\n\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3")
        buf.write("\2\2\2\u0118\u0104\3\2\2\2\u0118\u010f\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u011b\b\f\2\2\u011b\30\3\2\2\2\u011c\u011d")
        buf.write("\7h\2\2\u011d\u011e\7c\2\2\u011e\u011f\7n\2\2\u011f\u0120")
        buf.write("\7u\2\2\u0120\u0126\7g\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123\u0124\7w\2\2\u0124\u0126\7g\2\2\u0125\u011c")
        buf.write("\3\2\2\2\u0125\u0121\3\2\2\2\u0126\32\3\2\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7w\2\2\u0129\u012a\7v\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\34\3\2\2\2\u012c\u012d\7k\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\u012f\7v\2\2\u012f\u0130\7g\2\2\u0130\u0131")
        buf.write("\7i\2\2\u0131\u0132\7g\2\2\u0132\u0133\7t\2\2\u0133\36")
        buf.write("\3\2\2\2\u0134\u0135\7x\2\2\u0135\u0136\7q\2\2\u0136\u0137")
        buf.write("\7k\2\2\u0137\u0138\7f\2\2\u0138 \3\2\2\2\u0139\u013a")
        buf.write("\7c\2\2\u013a\u013b\7t\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7c\2\2\u013d\u013e\7{\2\2\u013e\"\3\2\2\2\u013f\u0140")
        buf.write("\7d\2\2\u0140\u0141\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7m\2\2\u0144$\3\2\2\2\u0145\u0146")
        buf.write("\7h\2\2\u0146\u0147\7n\2\2\u0147\u0148\7q\2\2\u0148\u0149")
        buf.write("\7c\2\2\u0149\u014a\7v\2\2\u014a&\3\2\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\u014d\7g\2\2\u014d\u014e\7v\2\2\u014e\u014f")
        buf.write("\7w\2\2\u014f\u0150\7t\2\2\u0150\u0151\7p\2\2\u0151(\3")
        buf.write("\2\2\2\u0152\u0153\7q\2\2\u0153\u0154\7w\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155*\3\2\2\2\u0156\u0157\7d\2\2\u0157\u0158")
        buf.write("\7q\2\2\u0158\u0159\7q\2\2\u0159\u015a\7n\2\2\u015a\u015b")
        buf.write("\7g\2\2\u015b\u015c\7c\2\2\u015c\u015d\7p\2\2\u015d,\3")
        buf.write("\2\2\2\u015e\u015f\7u\2\2\u015f\u0160\7v\2\2\u0160\u0161")
        buf.write("\7t\2\2\u0161\u0162\7k\2\2\u0162\u0163\7p\2\2\u0163\u0164")
        buf.write("\7i\2\2\u0164.\3\2\2\2\u0165\u0166\7h\2\2\u0166\u0167")
        buf.write("\7q\2\2\u0167\u0168\7t\2\2\u0168\60\3\2\2\2\u0169\u016a")
        buf.write("\7e\2\2\u016a\u016b\7q\2\2\u016b\u016c\7p\2\2\u016c\u016d")
        buf.write("\7v\2\2\u016d\u016e\7k\2\2\u016e\u016f\7p\2\2\u016f\u0170")
        buf.write("\7w\2\2\u0170\u0171\7g\2\2\u0171\62\3\2\2\2\u0172\u0173")
        buf.write("\7f\2\2\u0173\u0174\7q\2\2\u0174\64\3\2\2\2\u0175\u0176")
        buf.write("\7h\2\2\u0176\u0177\7w\2\2\u0177\u0178\7p\2\2\u0178\u0179")
        buf.write("\7e\2\2\u0179\u017a\7v\2\2\u017a\u017b\7k\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017c\u017d\7p\2\2\u017d\66\3\2\2\2\u017e\u017f")
        buf.write("\7q\2\2\u017f\u0180\7h\2\2\u01808\3\2\2\2\u0181\u0182")
        buf.write("\7g\2\2\u0182\u0183\7n\2\2\u0183\u0184\7u\2\2\u0184\u0185")
        buf.write("\7g\2\2\u0185:\3\2\2\2\u0186\u0187\7k\2\2\u0187\u0188")
        buf.write("\7h\2\2\u0188<\3\2\2\2\u0189\u018a\7y\2\2\u018a\u018b")
        buf.write("\7j\2\2\u018b\u018c\7k\2\2\u018c\u018d\7n\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e>\3\2\2\2\u018f\u0190\7k\2\2\u0190\u0191")
        buf.write("\7p\2\2\u0191\u0192\7j\2\2\u0192\u0193\7g\2\2\u0193\u0194")
        buf.write("\7t\2\2\u0194\u0195\7k\2\2\u0195\u0196\7v\2\2\u0196@\3")
        buf.write("\2\2\2\u0197\u0198\7-\2\2\u0198B\3\2\2\2\u0199\u019a\7")
        buf.write("/\2\2\u019aD\3\2\2\2\u019b\u019c\7,\2\2\u019cF\3\2\2\2")
        buf.write("\u019d\u019e\7\61\2\2\u019eH\3\2\2\2\u019f\u01a0\7\'\2")
        buf.write("\2\u01a0J\3\2\2\2\u01a1\u01a2\7#\2\2\u01a2L\3\2\2\2\u01a3")
        buf.write("\u01a4\7(\2\2\u01a4\u01a5\7(\2\2\u01a5N\3\2\2\2\u01a6")
        buf.write("\u01a7\7~\2\2\u01a7\u01a8\7~\2\2\u01a8P\3\2\2\2\u01a9")
        buf.write("\u01aa\7?\2\2\u01aa\u01ab\7?\2\2\u01abR\3\2\2\2\u01ac")
        buf.write("\u01ad\7#\2\2\u01ad\u01ae\7?\2\2\u01aeT\3\2\2\2\u01af")
        buf.write("\u01b0\7>\2\2\u01b0V\3\2\2\2\u01b1\u01b2\7>\2\2\u01b2")
        buf.write("\u01b3\7?\2\2\u01b3X\3\2\2\2\u01b4\u01b5\7@\2\2\u01b5")
        buf.write("Z\3\2\2\2\u01b6\u01b7\7@\2\2\u01b7\u01b8\7?\2\2\u01b8")
        buf.write("\\\3\2\2\2\u01b9\u01ba\7<\2\2\u01ba\u01bb\7<\2\2\u01bb")
        buf.write("^\3\2\2\2\u01bc\u01bd\7*\2\2\u01bd`\3\2\2\2\u01be\u01bf")
        buf.write("\7+\2\2\u01bfb\3\2\2\2\u01c0\u01c1\7.\2\2\u01c1d\3\2\2")
        buf.write("\2\u01c2\u01c3\7=\2\2\u01c3f\3\2\2\2\u01c4\u01c5\7<\2")
        buf.write("\2\u01c5h\3\2\2\2\u01c6\u01c7\7}\2\2\u01c7j\3\2\2\2\u01c8")
        buf.write("\u01c9\7\177\2\2\u01c9l\3\2\2\2\u01ca\u01cb\7?\2\2\u01cb")
        buf.write("n\3\2\2\2\u01cc\u01cd\7]\2\2\u01cdp\3\2\2\2\u01ce\u01cf")
        buf.write("\7_\2\2\u01cfr\3\2\2\2\u01d0\u01d1\7\60\2\2\u01d1t\3\2")
        buf.write("\2\2\u01d2\u01d6\t\3\2\2\u01d3\u01d5\t\4\2\2\u01d4\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7v\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9")
        buf.write("\u01dd\t\5\2\2\u01da\u01dc\5y=\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01de\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01de\u01ec\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e2\7")
        buf.write("a\2\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e7\5y=\2\u01e4\u01e6\5y=\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01ea\u01e1\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3")
        buf.write("\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ef\u01f9\b<\3\2\u01f0\u01f4\t\5\2\2\u01f1")
        buf.write("\u01f3\5y=\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f9\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f7\u01f9\t\6\2\2\u01f8\u01d9\3")
        buf.write("\2\2\2\u01f8\u01f0\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9x")
        buf.write("\3\2\2\2\u01fa\u01fb\t\7\2\2\u01fbz\3\2\2\2\u01fc\u0200")
        buf.write("\7$\2\2\u01fd\u01ff\5\u0081A\2\u01fe\u01fd\3\2\2\2\u01ff")
        buf.write("\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201\u0203\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\7")
        buf.write("$\2\2\u0204\u0205\b>\4\2\u0205|\3\2\2\2\u0206\u020a\7")
        buf.write("$\2\2\u0207\u0209\5\u0081A\2\u0208\u0207\3\2\2\2\u0209")
        buf.write("\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020e\5")
        buf.write("\u0085C\2\u020e\u020f\b?\5\2\u020f~\3\2\2\2\u0210\u0214")
        buf.write("\7$\2\2\u0211\u0213\5\u0081A\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0219\t")
        buf.write("\b\2\2\u0218\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b")
        buf.write("\b@\6\2\u021b\u0080\3\2\2\2\u021c\u021f\n\t\2\2\u021d")
        buf.write("\u021f\5\u0083B\2\u021e\u021c\3\2\2\2\u021e\u021d\3\2")
        buf.write("\2\2\u021f\u0082\3\2\2\2\u0220\u0221\7^\2\2\u0221\u0222")
        buf.write("\t\n\2\2\u0222\u0084\3\2\2\2\u0223\u0224\7^\2\2\u0224")
        buf.write("\u0225\n\n\2\2\u0225\u0086\3\2\2\2\u0226\u0227\5w<\2\u0227")
        buf.write("\u0228\5\u0089E\2\u0228\u0229\5\u008bF\2\u0229\u022a\b")
        buf.write("D\7\2\u022a\u0237\3\2\2\2\u022b\u022c\5\u0089E\2\u022c")
        buf.write("\u022d\5\u008bF\2\u022d\u0237\3\2\2\2\u022e\u022f\5w<")
        buf.write("\2\u022f\u0230\5\u008bF\2\u0230\u0231\bD\b\2\u0231\u0237")
        buf.write("\3\2\2\2\u0232\u0233\5w<\2\u0233\u0234\5\u0089E\2\u0234")
        buf.write("\u0235\bD\t\2\u0235\u0237\3\2\2\2\u0236\u0226\3\2\2\2")
        buf.write("\u0236\u022b\3\2\2\2\u0236\u022e\3\2\2\2\u0236\u0232\3")
        buf.write("\2\2\2\u0237\u0088\3\2\2\2\u0238\u023c\7\60\2\2\u0239")
        buf.write("\u023b\t\7\2\2\u023a\u0239\3\2\2\2\u023b\u023e\3\2\2\2")
        buf.write("\u023c\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u008a\3")
        buf.write("\2\2\2\u023e\u023c\3\2\2\2\u023f\u0241\t\13\2\2\u0240")
        buf.write("\u0242\t\f\2\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2\2\2")
        buf.write("\u0242\u0244\3\2\2\2\u0243\u0245\t\7\2\2\u0244\u0243\3")
        buf.write("\2\2\2\u0245\u0246\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0247\u008c\3\2\2\2\u0248\u024a\t\r\2\2\u0249")
        buf.write("\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u0249\3\2\2\2")
        buf.write("\u024b\u024c\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024e\b")
        buf.write("G\2\2\u024e\u008e\3\2\2\2\u024f\u0250\13\2\2\2\u0250\u0251")
        buf.write("\bH\n\2\u0251\u0090\3\2\2\2\30\2\u010a\u0115\u0118\u0125")
        buf.write("\u01d6\u01dd\u01e1\u01e7\u01ec\u01f4\u01f8\u0200\u020a")
        buf.write("\u0214\u0218\u021e\u0236\u023c\u0241\u0246\u024b\13\b")
        buf.write("\2\2\3<\2\3>\3\3?\4\3@\5\3D\6\3D\7\3D\b\3H\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    READINT = 1
    PRINTINT = 2
    READFLOAT = 3
    WRITEFLOAT = 4
    READBOOLEAN = 5
    PRINTBOOL = 6
    READSTRING = 7
    PRINTSTRING = 8
    SUPERFUNC = 9
    PREVENTDEFAULT = 10
    COMMENT = 11
    BOOL_LIT = 12
    AUTO = 13
    INT = 14
    VOID = 15
    ARRAY_TYP = 16
    BREAK = 17
    FLOAT = 18
    RETURN = 19
    OUT = 20
    BOOLEAN = 21
    STRING = 22
    FOR = 23
    CONTINUE = 24
    DO = 25
    FUNCTION = 26
    OF = 27
    ELSE = 28
    IF = 29
    WHILE = 30
    INHERIT = 31
    ADD_OP = 32
    SUB_OP = 33
    MUL_OP = 34
    DIV_OP = 35
    MOD_OP = 36
    NEGA_OP = 37
    CONJ_OP = 38
    DISJ_OP = 39
    EQUAL_TO_OP = 40
    NOT_EQUAL_TO_OP = 41
    LESS_OP = 42
    EQ_LESS_OP = 43
    GREATER_OP = 44
    EQ_GREATER_OP = 45
    CONCAT_OP = 46
    LEFT_PAREN = 47
    RIGHT_PAREN = 48
    COMMA = 49
    SEMICOLON = 50
    COLON = 51
    LEFT_CURBRACK = 52
    RIGHT_CURBRACK = 53
    ASSIG_OP = 54
    LEFT_SQUAREBRACK = 55
    RIGHT_SQUAREBRACK = 56
    DOT = 57
    IDENTIFIER = 58
    INT_LIT = 59
    STRING_LIT = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    FLOAT_LIT = 63
    WS = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'integer'", "'void'", 
            "'array'", "'break'", "'float'", "'return'", "'out'", "'boolean'", 
            "'string'", "'for'", "'continue'", "'do'", "'function'", "'of'", 
            "'else'", "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'::'", "'('", "')'", "','", "';'", "':'", 
            "'{'", "'}'", "'='", "'['", "']'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "READINT", "PRINTINT", "READFLOAT", "WRITEFLOAT", "READBOOLEAN", 
            "PRINTBOOL", "READSTRING", "PRINTSTRING", "SUPERFUNC", "PREVENTDEFAULT", 
            "COMMENT", "BOOL_LIT", "AUTO", "INT", "VOID", "ARRAY_TYP", "BREAK", 
            "FLOAT", "RETURN", "OUT", "BOOLEAN", "STRING", "FOR", "CONTINUE", 
            "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADD_OP", 
            "SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NEGA_OP", "CONJ_OP", 
            "DISJ_OP", "EQUAL_TO_OP", "NOT_EQUAL_TO_OP", "LESS_OP", "EQ_LESS_OP", 
            "GREATER_OP", "EQ_GREATER_OP", "CONCAT_OP", "LEFT_PAREN", "RIGHT_PAREN", 
            "COMMA", "SEMICOLON", "COLON", "LEFT_CURBRACK", "RIGHT_CURBRACK", 
            "ASSIG_OP", "LEFT_SQUAREBRACK", "RIGHT_SQUAREBRACK", "DOT", 
            "IDENTIFIER", "INT_LIT", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "FLOAT_LIT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "READINT", "PRINTINT", "READFLOAT", "WRITEFLOAT", "READBOOLEAN", 
                  "PRINTBOOL", "READSTRING", "PRINTSTRING", "SUPERFUNC", 
                  "PREVENTDEFAULT", "COMMENT", "BOOL_LIT", "AUTO", "INT", 
                  "VOID", "ARRAY_TYP", "BREAK", "FLOAT", "RETURN", "OUT", 
                  "BOOLEAN", "STRING", "FOR", "CONTINUE", "DO", "FUNCTION", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "ADD_OP", "SUB_OP", 
                  "MUL_OP", "DIV_OP", "MOD_OP", "NEGA_OP", "CONJ_OP", "DISJ_OP", 
                  "EQUAL_TO_OP", "NOT_EQUAL_TO_OP", "LESS_OP", "EQ_LESS_OP", 
                  "GREATER_OP", "EQ_GREATER_OP", "CONCAT_OP", "LEFT_PAREN", 
                  "RIGHT_PAREN", "COMMA", "SEMICOLON", "COLON", "LEFT_CURBRACK", 
                  "RIGHT_CURBRACK", "ASSIG_OP", "LEFT_SQUAREBRACK", "RIGHT_SQUAREBRACK", 
                  "DOT", "IDENTIFIER", "INT_LIT", "DIGIT", "STRING_LIT", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING_CHAR", "ESCAPEFRAG", 
                  "ILLEGALFRAG", "FLOAT_LIT", "DECPART", "EXPPART", "WS", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.INT_LIT_action 
            actions[60] = self.STRING_LIT_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[66] = self.FLOAT_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = "".join(self.text.split("_"))
            		
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	if (self.text.find('\n') != -1) :
            		raise UncloseString(self.text[1:(self.text.find('\n')-1)])
            	elif (self.text.find('\r') != -1):
            		raise UncloseString(self.text[1:self.text.find('\r')])	
            	elif(self.text[-1]=='\"'):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])	

     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = "".join(self.text.split("_"))
     

        if actionIndex == 5:
            self.text = "".join(self.text.split("_"))
     

        if actionIndex == 6:
            self.text = "".join(self.text.split("_"))
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


