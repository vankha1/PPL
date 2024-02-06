# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00c3\n\b\3\t\3\t\5\t")
        buf.write("\u00c7\n\t\3\t\5\t\u00ca\n\t\3\t\3\t\3\t\5\t\u00cf\n\t")
        buf.write("\3\n\3\n\3\n\7\n\u00d4\n\n\f\n\16\n\u00d7\13\n\5\n\u00d9")
        buf.write("\n\n\3\13\3\13\7\13\u00dd\n\13\f\13\16\13\u00e0\13\13")
        buf.write("\3\f\3\f\5\f\u00e4\n\f\3\f\6\f\u00e7\n\f\r\f\16\f\u00e8")
        buf.write("\3\r\3\r\3\r\3\r\3\r\7\r\u00f0\n\r\f\r\16\r\u00f3\13\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\7")
        buf.write("9\u01a3\n9\f9\169\u01a6\139\39\39\3:\3:\7:\u01ac\n:\f")
        buf.write(":\16:\u01af\13:\3;\5;\u01b2\n;\3;\3;\3;\3<\6<\u01b8\n")
        buf.write("<\r<\16<\u01b9\3<\3<\3=\3=\3=\3=\3=\7=\u01c3\n=\f=\16")
        buf.write("=\u01c6\13=\3=\5=\u01c9\n=\3=\3=\3>\3>\3>\3>\3>\7>\u01d2")
        buf.write("\n>\f>\16>\u01d5\13>\3>\3>\3>\3?\3?\3?\2\2@\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2\31\f\33\2\35")
        buf.write("\2\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27\65")
        buf.write("\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(")
        buf.write("W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u8w9y:{")
        buf.write(";}<\3\2\f\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\t\2))^^")
        buf.write("ddhhppttvv\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\n\13\16\16\"\"\4\3\f\f\17\17\2\u01ed\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\3\177\3\2\2\2\5\u008a\3\2\2\2\7\u0096\3\2\2\2\t")
        buf.write("\u009f\3\2\2\2\13\u00a9\3\2\2\2\r\u00b4\3\2\2\2\17\u00c2")
        buf.write("\3\2\2\2\21\u00ce\3\2\2\2\23\u00d8\3\2\2\2\25\u00da\3")
        buf.write("\2\2\2\27\u00e1\3\2\2\2\31\u00ea\3\2\2\2\33\u00f7\3\2")
        buf.write("\2\2\35\u00fa\3\2\2\2\37\u00fd\3\2\2\2!\u00ff\3\2\2\2")
        buf.write("#\u0101\3\2\2\2%\u0103\3\2\2\2\'\u0105\3\2\2\2)\u0107")
        buf.write("\3\2\2\2+\u0109\3\2\2\2-\u010b\3\2\2\2/\u010d\3\2\2\2")
        buf.write("\61\u010f\3\2\2\2\63\u0111\3\2\2\2\65\u0113\3\2\2\2\67")
        buf.write("\u0116\3\2\2\29\u0119\3\2\2\2;\u011b\3\2\2\2=\u011e\3")
        buf.write("\2\2\2?\u0121\3\2\2\2A\u0123\3\2\2\2C\u0127\3\2\2\2E\u012a")
        buf.write("\3\2\2\2G\u012f\3\2\2\2I\u0135\3\2\2\2K\u013c\3\2\2\2")
        buf.write("M\u0141\3\2\2\2O\u0148\3\2\2\2Q\u014f\3\2\2\2S\u0153\3")
        buf.write("\2\2\2U\u015b\3\2\2\2W\u0160\3\2\2\2Y\u0164\3\2\2\2[\u016a")
        buf.write("\3\2\2\2]\u016d\3\2\2\2_\u0173\3\2\2\2a\u017c\3\2\2\2")
        buf.write("c\u017f\3\2\2\2e\u0184\3\2\2\2g\u0189\3\2\2\2i\u018f\3")
        buf.write("\2\2\2k\u0193\3\2\2\2m\u0197\3\2\2\2o\u019b\3\2\2\2q\u019e")
        buf.write("\3\2\2\2s\u01a9\3\2\2\2u\u01b1\3\2\2\2w\u01b7\3\2\2\2")
        buf.write("y\u01bd\3\2\2\2{\u01cc\3\2\2\2}\u01d9\3\2\2\2\177\u0080")
        buf.write("\7t\2\2\u0080\u0081\7g\2\2\u0081\u0082\7c\2\2\u0082\u0083")
        buf.write("\7f\2\2\u0083\u0084\7P\2\2\u0084\u0085\7w\2\2\u0085\u0086")
        buf.write("\7o\2\2\u0086\u0087\7d\2\2\u0087\u0088\7g\2\2\u0088\u0089")
        buf.write("\7t\2\2\u0089\4\3\2\2\2\u008a\u008b\7y\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\u008d\7k\2\2\u008d\u008e\7v\2\2\u008e\u008f")
        buf.write("\7g\2\2\u008f\u0090\7P\2\2\u0090\u0091\7w\2\2\u0091\u0092")
        buf.write("\7o\2\2\u0092\u0093\7d\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\6\3\2\2\2\u0096\u0097\7t\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u0099\7c\2\2\u0099\u009a\7f\2\2\u009a\u009b")
        buf.write("\7D\2\2\u009b\u009c\7q\2\2\u009c\u009d\7q\2\2\u009d\u009e")
        buf.write("\7n\2\2\u009e\b\3\2\2\2\u009f\u00a0\7y\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7D\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\u00a8\7n\2\2\u00a8\n\3\2\2\2\u00a9\u00aa")
        buf.write("\7t\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write("\7f\2\2\u00ad\u00ae\7U\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3")
        buf.write("\7i\2\2\u00b3\f\3\2\2\2\u00b4\u00b5\7y\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7U\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7i\2\2\u00bf\16\3\2\2\2\u00c0\u00c3\5E#\2\u00c1\u00c3")
        buf.write("\5G$\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\20")
        buf.write("\3\2\2\2\u00c4\u00c6\5\23\n\2\u00c5\u00c7\5\25\13\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00ca\5\27\f\2\u00c9\u00c8\3\2\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cf\3\2\2\2\u00cb\u00cc\5\23\n\2\u00cc")
        buf.write("\u00cd\5\27\f\2\u00cd\u00cf\3\2\2\2\u00ce\u00c4\3\2\2")
        buf.write("\2\u00ce\u00cb\3\2\2\2\u00cf\22\3\2\2\2\u00d0\u00d9\7")
        buf.write("\62\2\2\u00d1\u00d5\t\2\2\2\u00d2\u00d4\t\2\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3")
        buf.write("\2\2\2\u00d8\u00d0\3\2\2\2\u00d8\u00d1\3\2\2\2\u00d9\24")
        buf.write("\3\2\2\2\u00da\u00de\7\60\2\2\u00db\u00dd\t\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\26\3\2\2\2\u00e0\u00de\3\2")
        buf.write("\2\2\u00e1\u00e3\t\3\2\2\u00e2\u00e4\t\4\2\2\u00e3\u00e2")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5")
        buf.write("\u00e7\t\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\30\3\2")
        buf.write("\2\2\u00ea\u00f1\7$\2\2\u00eb\u00f0\5\33\16\2\u00ec\u00f0")
        buf.write("\n\5\2\2\u00ed\u00ee\7)\2\2\u00ee\u00f0\7$\2\2\u00ef\u00eb")
        buf.write("\3\2\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\7")
        buf.write("$\2\2\u00f5\u00f6\b\r\2\2\u00f6\32\3\2\2\2\u00f7\u00f8")
        buf.write("\7^\2\2\u00f8\u00f9\t\6\2\2\u00f9\34\3\2\2\2\u00fa\u00fb")
        buf.write("\7^\2\2\u00fb\u00fc\n\6\2\2\u00fc\36\3\2\2\2\u00fd\u00fe")
        buf.write("\7*\2\2\u00fe \3\2\2\2\u00ff\u0100\7+\2\2\u0100\"\3\2")
        buf.write("\2\2\u0101\u0102\7]\2\2\u0102$\3\2\2\2\u0103\u0104\7_")
        buf.write("\2\2\u0104&\3\2\2\2\u0105\u0106\7.\2\2\u0106(\3\2\2\2")
        buf.write("\u0107\u0108\7-\2\2\u0108*\3\2\2\2\u0109\u010a\7/\2\2")
        buf.write("\u010a,\3\2\2\2\u010b\u010c\7,\2\2\u010c.\3\2\2\2\u010d")
        buf.write("\u010e\7\61\2\2\u010e\60\3\2\2\2\u010f\u0110\7\'\2\2\u0110")
        buf.write("\62\3\2\2\2\u0111\u0112\7?\2\2\u0112\64\3\2\2\2\u0113")
        buf.write("\u0114\7>\2\2\u0114\u0115\7/\2\2\u0115\66\3\2\2\2\u0116")
        buf.write("\u0117\7#\2\2\u0117\u0118\7?\2\2\u01188\3\2\2\2\u0119")
        buf.write("\u011a\7>\2\2\u011a:\3\2\2\2\u011b\u011c\7>\2\2\u011c")
        buf.write("\u011d\7?\2\2\u011d<\3\2\2\2\u011e\u011f\7@\2\2\u011f")
        buf.write("\u0120\7?\2\2\u0120>\3\2\2\2\u0121\u0122\7@\2\2\u0122")
        buf.write("@\3\2\2\2\u0123\u0124\7\60\2\2\u0124\u0125\7\60\2\2\u0125")
        buf.write("\u0126\7\60\2\2\u0126B\3\2\2\2\u0127\u0128\7?\2\2\u0128")
        buf.write("\u0129\7?\2\2\u0129D\3\2\2\2\u012a\u012b\7v\2\2\u012b")
        buf.write("\u012c\7t\2\2\u012c\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write("F\3\2\2\2\u012f\u0130\7h\2\2\u0130\u0131\7c\2\2\u0131")
        buf.write("\u0132\7n\2\2\u0132\u0133\7u\2\2\u0133\u0134\7g\2\2\u0134")
        buf.write("H\3\2\2\2\u0135\u0136\7p\2\2\u0136\u0137\7w\2\2\u0137")
        buf.write("\u0138\7o\2\2\u0138\u0139\7d\2\2\u0139\u013a\7g\2\2\u013a")
        buf.write("\u013b\7t\2\2\u013bJ\3\2\2\2\u013c\u013d\7d\2\2\u013d")
        buf.write("\u013e\7q\2\2\u013e\u013f\7q\2\2\u013f\u0140\7n\2\2\u0140")
        buf.write("L\3\2\2\2\u0141\u0142\7u\2\2\u0142\u0143\7v\2\2\u0143")
        buf.write("\u0144\7t\2\2\u0144\u0145\7k\2\2\u0145\u0146\7p\2\2\u0146")
        buf.write("\u0147\7i\2\2\u0147N\3\2\2\2\u0148\u0149\7t\2\2\u0149")
        buf.write("\u014a\7g\2\2\u014a\u014b\7v\2\2\u014b\u014c\7w\2\2\u014c")
        buf.write("\u014d\7t\2\2\u014d\u014e\7p\2\2\u014eP\3\2\2\2\u014f")
        buf.write("\u0150\7x\2\2\u0150\u0151\7c\2\2\u0151\u0152\7t\2\2\u0152")
        buf.write("R\3\2\2\2\u0153\u0154\7f\2\2\u0154\u0155\7{\2\2\u0155")
        buf.write("\u0156\7p\2\2\u0156\u0157\7c\2\2\u0157\u0158\7o\2\2\u0158")
        buf.write("\u0159\7k\2\2\u0159\u015a\7e\2\2\u015aT\3\2\2\2\u015b")
        buf.write("\u015c\7h\2\2\u015c\u015d\7w\2\2\u015d\u015e\7p\2\2\u015e")
        buf.write("\u015f\7e\2\2\u015fV\3\2\2\2\u0160\u0161\7h\2\2\u0161")
        buf.write("\u0162\7q\2\2\u0162\u0163\7t\2\2\u0163X\3\2\2\2\u0164")
        buf.write("\u0165\7w\2\2\u0165\u0166\7p\2\2\u0166\u0167\7v\2\2\u0167")
        buf.write("\u0168\7k\2\2\u0168\u0169\7n\2\2\u0169Z\3\2\2\2\u016a")
        buf.write("\u016b\7d\2\2\u016b\u016c\7{\2\2\u016c\\\3\2\2\2\u016d")
        buf.write("\u016e\7d\2\2\u016e\u016f\7t\2\2\u016f\u0170\7g\2\2\u0170")
        buf.write("\u0171\7c\2\2\u0171\u0172\7m\2\2\u0172^\3\2\2\2\u0173")
        buf.write("\u0174\7e\2\2\u0174\u0175\7q\2\2\u0175\u0176\7p\2\2\u0176")
        buf.write("\u0177\7v\2\2\u0177\u0178\7k\2\2\u0178\u0179\7p\2\2\u0179")
        buf.write("\u017a\7w\2\2\u017a\u017b\7g\2\2\u017b`\3\2\2\2\u017c")
        buf.write("\u017d\7k\2\2\u017d\u017e\7h\2\2\u017eb\3\2\2\2\u017f")
        buf.write("\u0180\7g\2\2\u0180\u0181\7n\2\2\u0181\u0182\7u\2\2\u0182")
        buf.write("\u0183\7g\2\2\u0183d\3\2\2\2\u0184\u0185\7g\2\2\u0185")
        buf.write("\u0186\7n\2\2\u0186\u0187\7k\2\2\u0187\u0188\7h\2\2\u0188")
        buf.write("f\3\2\2\2\u0189\u018a\7d\2\2\u018a\u018b\7g\2\2\u018b")
        buf.write("\u018c\7i\2\2\u018c\u018d\7k\2\2\u018d\u018e\7p\2\2\u018e")
        buf.write("h\3\2\2\2\u018f\u0190\7g\2\2\u0190\u0191\7p\2\2\u0191")
        buf.write("\u0192\7f\2\2\u0192j\3\2\2\2\u0193\u0194\7p\2\2\u0194")
        buf.write("\u0195\7q\2\2\u0195\u0196\7v\2\2\u0196l\3\2\2\2\u0197")
        buf.write("\u0198\7c\2\2\u0198\u0199\7p\2\2\u0199\u019a\7f\2\2\u019a")
        buf.write("n\3\2\2\2\u019b\u019c\7q\2\2\u019c\u019d\7t\2\2\u019d")
        buf.write("p\3\2\2\2\u019e\u019f\7%\2\2\u019f\u01a0\7%\2\2\u01a0")
        buf.write("\u01a4\3\2\2\2\u01a1\u01a3\n\7\2\2\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3")
        buf.write("\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a8")
        buf.write("\b9\3\2\u01a8r\3\2\2\2\u01a9\u01ad\t\b\2\2\u01aa\u01ac")
        buf.write("\t\t\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aet\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b2\7\17\2\2\u01b1\u01b0\3\2\2")
        buf.write("\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4")
        buf.write("\7\f\2\2\u01b4\u01b5\b;\4\2\u01b5v\3\2\2\2\u01b6\u01b8")
        buf.write("\t\n\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01bc\b<\3\2\u01bcx\3\2\2\2\u01bd\u01c4\7$\2\2")
        buf.write("\u01be\u01c3\n\5\2\2\u01bf\u01c3\5\33\16\2\u01c0\u01c1")
        buf.write("\7)\2\2\u01c1\u01c3\7$\2\2\u01c2\u01be\3\2\2\2\u01c2\u01bf")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c8\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c7\u01c9\t\13\2\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\b=\5\2\u01cb")
        buf.write("z\3\2\2\2\u01cc\u01d3\7$\2\2\u01cd\u01d2\n\5\2\2\u01ce")
        buf.write("\u01d2\5\33\16\2\u01cf\u01d0\7)\2\2\u01d0\u01d2\7$\2\2")
        buf.write("\u01d1\u01cd\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4")
        buf.write("\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6")
        buf.write("\u01d7\5\35\17\2\u01d7\u01d8\b>\6\2\u01d8|\3\2\2\2\u01d9")
        buf.write("\u01da\13\2\2\2\u01da\u01db\b?\7\2\u01db~\3\2\2\2\27\2")
        buf.write("\u00c2\u00c6\u00c9\u00ce\u00d5\u00d8\u00de\u00e3\u00e8")
        buf.write("\u00ef\u00f1\u01a4\u01ad\u01b1\u01b9\u01c2\u01c4\u01c8")
        buf.write("\u01d1\u01d3\b\3\r\2\b\2\2\3;\3\3=\4\3>\5\3?\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    READNUM = 1
    WRITENUM = 2
    READBOOL = 3
    WRITEBOOL = 4
    READSTRING = 5
    WRITESTRING = 6
    BOOL_LIT = 7
    FLOAT_LIT = 8
    INT_LIT = 9
    STRING_LIT = 10
    LP = 11
    RP = 12
    LS = 13
    RS = 14
    COMMA = 15
    ADD = 16
    SUB = 17
    MUL = 18
    DIV = 19
    MOD = 20
    EQUAL = 21
    ASSIGN = 22
    NOT_SAME = 23
    LESS_THAN = 24
    LESS_THAN_EQUAL = 25
    GREATER_THAN_EQUAL = 26
    GREATER_THAN = 27
    CONCAT = 28
    SAME = 29
    TRUE = 30
    FALSE = 31
    NUMBER = 32
    BOOL = 33
    STRING = 34
    RETURN = 35
    VAR = 36
    DYNAMIC = 37
    FUNC = 38
    FOR = 39
    UNTIL = 40
    BY = 41
    BREAK = 42
    CONTINUE = 43
    IF = 44
    ELSE = 45
    ELIF = 46
    BEGIN = 47
    END = 48
    NOT = 49
    AND = 50
    OR = 51
    LINE_COMMENT = 52
    ID = 53
    NEW_LINE = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readNumber'", "'writeNumber'", "'readBool'", "'writeBool'", 
            "'readString'", "'writeString'", "'('", "')'", "'['", "']'", 
            "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>='", "'>'", "'...'", "'=='", "'true'", "'false'", 
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
            "'or'" ]

    symbolicNames = [ "<INVALID>",
            "READNUM", "WRITENUM", "READBOOL", "WRITEBOOL", "READSTRING", 
            "WRITESTRING", "BOOL_LIT", "FLOAT_LIT", "INT_LIT", "STRING_LIT", 
            "LP", "RP", "LS", "RS", "COMMA", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "EQUAL", "ASSIGN", "NOT_SAME", "LESS_THAN", "LESS_THAN_EQUAL", 
            "GREATER_THAN_EQUAL", "GREATER_THAN", "CONCAT", "SAME", "TRUE", 
            "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
            "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
            "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "LINE_COMMENT", 
            "ID", "NEW_LINE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "READNUM", "WRITENUM", "READBOOL", "WRITEBOOL", "READSTRING", 
                  "WRITESTRING", "BOOL_LIT", "FLOAT_LIT", "INT_LIT", "DEC_PART", 
                  "EXP_PART", "STRING_LIT", "ESC", "ILLEGAL_ESC", "LP", 
                  "RP", "LS", "RS", "COMMA", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQUAL", "ASSIGN", "NOT_SAME", "LESS_THAN", "LESS_THAN_EQUAL", 
                  "GREATER_THAN_EQUAL", "GREATER_THAN", "CONCAT", "SAME", 
                  "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "LINE_COMMENT", "ID", "NEW_LINE", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.STRING_LIT_action 
            actions[57] = self.NEW_LINE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[61] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEW_LINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = '\n'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise UncloseString(self.text[1:].replace('\n', '').replace('\r', ''))

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		raise ErrorToken(self.text)
            	
     


