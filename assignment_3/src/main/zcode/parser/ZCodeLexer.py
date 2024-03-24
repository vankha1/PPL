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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\5\2v\n\2\3\3\3\3\5\3z\n\3\3\3\5\3}\n\3\3\3\3\3\3\3")
        buf.write("\5\3\u0082\n\3\3\4\3\4\3\4\7\4\u0087\n\4\f\4\16\4\u008a")
        buf.write("\13\4\5\4\u008c\n\4\3\5\3\5\7\5\u0090\n\5\f\5\16\5\u0093")
        buf.write("\13\5\3\6\3\6\5\6\u0097\n\6\3\6\6\6\u009a\n\6\r\6\16\6")
        buf.write("\u009b\3\7\3\7\3\7\3\7\3\7\7\7\u00a3\n\7\f\7\16\7\u00a6")
        buf.write("\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\7\63\u0156\n\63\f\63\16\63\u0159\13\63\3\63\3\63\3\64")
        buf.write("\3\64\7\64\u015f\n\64\f\64\16\64\u0162\13\64\3\65\5\65")
        buf.write("\u0165\n\65\3\65\3\65\3\65\3\66\6\66\u016b\n\66\r\66\16")
        buf.write("\66\u016c\3\66\3\66\3\67\3\67\3\67\7\67\u0174\n\67\f\67")
        buf.write("\16\67\u0177\13\67\3\67\5\67\u017a\n\67\3\67\3\67\38\3")
        buf.write("8\38\78\u0181\n8\f8\168\u0184\138\38\38\38\39\39\39\2")
        buf.write("\2:\3\3\5\4\7\2\t\2\13\2\r\5\17\2\21\2\23\6\25\7\27\b")
        buf.write("\31\t\33\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24")
        buf.write("\61\25\63\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G")
        buf.write(" I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64")
        buf.write("q\65\3\2\16\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$")
        buf.write("^^\t\2))^^ddhhppttvv\4\2\f\f\17\17\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\n\13\16\16\"\"\6\2\f\f$$))^^\4\3\f\f\17\17")
        buf.write("\2\u0199\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\3u\3\2\2\2\5\u0081\3\2\2\2\7\u008b\3\2\2\2\t")
        buf.write("\u008d\3\2\2\2\13\u0094\3\2\2\2\r\u009d\3\2\2\2\17\u00aa")
        buf.write("\3\2\2\2\21\u00ad\3\2\2\2\23\u00b0\3\2\2\2\25\u00b2\3")
        buf.write("\2\2\2\27\u00b4\3\2\2\2\31\u00b6\3\2\2\2\33\u00b8\3\2")
        buf.write("\2\2\35\u00ba\3\2\2\2\37\u00bc\3\2\2\2!\u00be\3\2\2\2")
        buf.write("#\u00c0\3\2\2\2%\u00c2\3\2\2\2\'\u00c4\3\2\2\2)\u00c6")
        buf.write("\3\2\2\2+\u00c9\3\2\2\2-\u00cc\3\2\2\2/\u00ce\3\2\2\2")
        buf.write("\61\u00d1\3\2\2\2\63\u00d4\3\2\2\2\65\u00d6\3\2\2\2\67")
        buf.write("\u00da\3\2\2\29\u00dd\3\2\2\2;\u00e2\3\2\2\2=\u00e8\3")
        buf.write("\2\2\2?\u00ef\3\2\2\2A\u00f4\3\2\2\2C\u00fb\3\2\2\2E\u0102")
        buf.write("\3\2\2\2G\u0106\3\2\2\2I\u010e\3\2\2\2K\u0113\3\2\2\2")
        buf.write("M\u0117\3\2\2\2O\u011d\3\2\2\2Q\u0120\3\2\2\2S\u0126\3")
        buf.write("\2\2\2U\u012f\3\2\2\2W\u0132\3\2\2\2Y\u0137\3\2\2\2[\u013c")
        buf.write("\3\2\2\2]\u0142\3\2\2\2_\u0146\3\2\2\2a\u014a\3\2\2\2")
        buf.write("c\u014e\3\2\2\2e\u0151\3\2\2\2g\u015c\3\2\2\2i\u0164\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u0170\3\2\2\2o\u017d\3\2\2\2q\u0188")
        buf.write("\3\2\2\2sv\59\35\2tv\5;\36\2us\3\2\2\2ut\3\2\2\2v\4\3")
        buf.write("\2\2\2wy\5\7\4\2xz\5\t\5\2yx\3\2\2\2yz\3\2\2\2z|\3\2\2")
        buf.write("\2{}\5\13\6\2|{\3\2\2\2|}\3\2\2\2}\u0082\3\2\2\2~\177")
        buf.write("\5\7\4\2\177\u0080\5\13\6\2\u0080\u0082\3\2\2\2\u0081")
        buf.write("w\3\2\2\2\u0081~\3\2\2\2\u0082\6\3\2\2\2\u0083\u008c\7")
        buf.write("\62\2\2\u0084\u0088\t\2\2\2\u0085\u0087\t\3\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3")
        buf.write("\2\2\2\u008b\u0083\3\2\2\2\u008b\u0084\3\2\2\2\u008c\b")
        buf.write("\3\2\2\2\u008d\u0091\7\60\2\2\u008e\u0090\t\3\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\n\3\2\2\2\u0093\u0091\3\2\2")
        buf.write("\2\u0094\u0096\t\4\2\2\u0095\u0097\t\5\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3\2\2\2\u0098")
        buf.write("\u009a\t\3\2\2\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\f\3\2\2")
        buf.write("\2\u009d\u00a4\7$\2\2\u009e\u00a3\5\17\b\2\u009f\u00a3")
        buf.write("\n\6\2\2\u00a0\u00a1\7)\2\2\u00a1\u00a3\7$\2\2\u00a2\u009e")
        buf.write("\3\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3")
        buf.write("\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\7")
        buf.write("$\2\2\u00a8\u00a9\b\7\2\2\u00a9\16\3\2\2\2\u00aa\u00ab")
        buf.write("\7^\2\2\u00ab\u00ac\t\7\2\2\u00ac\20\3\2\2\2\u00ad\u00ae")
        buf.write("\7^\2\2\u00ae\u00af\n\7\2\2\u00af\22\3\2\2\2\u00b0\u00b1")
        buf.write("\7*\2\2\u00b1\24\3\2\2\2\u00b2\u00b3\7+\2\2\u00b3\26\3")
        buf.write("\2\2\2\u00b4\u00b5\7]\2\2\u00b5\30\3\2\2\2\u00b6\u00b7")
        buf.write("\7_\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7.\2\2\u00b9\34\3")
        buf.write("\2\2\2\u00ba\u00bb\7-\2\2\u00bb\36\3\2\2\2\u00bc\u00bd")
        buf.write("\7/\2\2\u00bd \3\2\2\2\u00be\u00bf\7,\2\2\u00bf\"\3\2")
        buf.write("\2\2\u00c0\u00c1\7\61\2\2\u00c1$\3\2\2\2\u00c2\u00c3\7")
        buf.write("\'\2\2\u00c3&\3\2\2\2\u00c4\u00c5\7?\2\2\u00c5(\3\2\2")
        buf.write("\2\u00c6\u00c7\7>\2\2\u00c7\u00c8\7/\2\2\u00c8*\3\2\2")
        buf.write("\2\u00c9\u00ca\7#\2\2\u00ca\u00cb\7?\2\2\u00cb,\3\2\2")
        buf.write("\2\u00cc\u00cd\7>\2\2\u00cd.\3\2\2\2\u00ce\u00cf\7>\2")
        buf.write("\2\u00cf\u00d0\7?\2\2\u00d0\60\3\2\2\2\u00d1\u00d2\7@")
        buf.write("\2\2\u00d2\u00d3\7?\2\2\u00d3\62\3\2\2\2\u00d4\u00d5\7")
        buf.write("@\2\2\u00d5\64\3\2\2\2\u00d6\u00d7\7\60\2\2\u00d7\u00d8")
        buf.write("\7\60\2\2\u00d8\u00d9\7\60\2\2\u00d9\66\3\2\2\2\u00da")
        buf.write("\u00db\7?\2\2\u00db\u00dc\7?\2\2\u00dc8\3\2\2\2\u00dd")
        buf.write("\u00de\7v\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write("\u00e1\7g\2\2\u00e1:\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3")
        buf.write("\u00e4\7c\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7<\3\2\2\2\u00e8\u00e9\7p\2\2\u00e9")
        buf.write("\u00ea\7w\2\2\u00ea\u00eb\7o\2\2\u00eb\u00ec\7d\2\2\u00ec")
        buf.write("\u00ed\7g\2\2\u00ed\u00ee\7t\2\2\u00ee>\3\2\2\2\u00ef")
        buf.write("\u00f0\7d\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7q\2\2\u00f2")
        buf.write("\u00f3\7n\2\2\u00f3@\3\2\2\2\u00f4\u00f5\7u\2\2\u00f5")
        buf.write("\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7k\2\2\u00f8")
        buf.write("\u00f9\7p\2\2\u00f9\u00fa\7i\2\2\u00faB\3\2\2\2\u00fb")
        buf.write("\u00fc\7t\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7v\2\2\u00fe")
        buf.write("\u00ff\7w\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7p\2\2\u0101")
        buf.write("D\3\2\2\2\u0102\u0103\7x\2\2\u0103\u0104\7c\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105F\3\2\2\2\u0106\u0107\7f\2\2\u0107")
        buf.write("\u0108\7{\2\2\u0108\u0109\7p\2\2\u0109\u010a\7c\2\2\u010a")
        buf.write("\u010b\7o\2\2\u010b\u010c\7k\2\2\u010c\u010d\7e\2\2\u010d")
        buf.write("H\3\2\2\2\u010e\u010f\7h\2\2\u010f\u0110\7w\2\2\u0110")
        buf.write("\u0111\7p\2\2\u0111\u0112\7e\2\2\u0112J\3\2\2\2\u0113")
        buf.write("\u0114\7h\2\2\u0114\u0115\7q\2\2\u0115\u0116\7t\2\2\u0116")
        buf.write("L\3\2\2\2\u0117\u0118\7w\2\2\u0118\u0119\7p\2\2\u0119")
        buf.write("\u011a\7v\2\2\u011a\u011b\7k\2\2\u011b\u011c\7n\2\2\u011c")
        buf.write("N\3\2\2\2\u011d\u011e\7d\2\2\u011e\u011f\7{\2\2\u011f")
        buf.write("P\3\2\2\2\u0120\u0121\7d\2\2\u0121\u0122\7t\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123\u0124\7c\2\2\u0124\u0125\7m\2\2\u0125")
        buf.write("R\3\2\2\2\u0126\u0127\7e\2\2\u0127\u0128\7q\2\2\u0128")
        buf.write("\u0129\7p\2\2\u0129\u012a\7v\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7p\2\2\u012c\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write("T\3\2\2\2\u012f\u0130\7k\2\2\u0130\u0131\7h\2\2\u0131")
        buf.write("V\3\2\2\2\u0132\u0133\7g\2\2\u0133\u0134\7n\2\2\u0134")
        buf.write("\u0135\7u\2\2\u0135\u0136\7g\2\2\u0136X\3\2\2\2\u0137")
        buf.write("\u0138\7g\2\2\u0138\u0139\7n\2\2\u0139\u013a\7k\2\2\u013a")
        buf.write("\u013b\7h\2\2\u013bZ\3\2\2\2\u013c\u013d\7d\2\2\u013d")
        buf.write("\u013e\7g\2\2\u013e\u013f\7i\2\2\u013f\u0140\7k\2\2\u0140")
        buf.write("\u0141\7p\2\2\u0141\\\3\2\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\u0144\7p\2\2\u0144\u0145\7f\2\2\u0145^\3\2\2\2\u0146")
        buf.write("\u0147\7p\2\2\u0147\u0148\7q\2\2\u0148\u0149\7v\2\2\u0149")
        buf.write("`\3\2\2\2\u014a\u014b\7c\2\2\u014b\u014c\7p\2\2\u014c")
        buf.write("\u014d\7f\2\2\u014db\3\2\2\2\u014e\u014f\7q\2\2\u014f")
        buf.write("\u0150\7t\2\2\u0150d\3\2\2\2\u0151\u0152\7%\2\2\u0152")
        buf.write("\u0153\7%\2\2\u0153\u0157\3\2\2\2\u0154\u0156\n\b\2\2")
        buf.write("\u0155\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0157\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u015a\u015b\b\63\3\2\u015bf\3\2\2\2\u015c\u0160")
        buf.write("\t\t\2\2\u015d\u015f\t\n\2\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161h\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0165\7\17\2")
        buf.write("\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0167\7\f\2\2\u0167\u0168\b\65\4\2\u0168")
        buf.write("j\3\2\2\2\u0169\u016b\t\13\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u016f\b\66\3\2\u016fl\3\2\2")
        buf.write("\2\u0170\u0175\7$\2\2\u0171\u0174\n\f\2\2\u0172\u0174")
        buf.write("\5\17\b\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a\t")
        buf.write("\r\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c")
        buf.write("\b\67\5\2\u017cn\3\2\2\2\u017d\u0182\7$\2\2\u017e\u0181")
        buf.write("\n\6\2\2\u017f\u0181\5\17\b\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0185\u0186\5\21\t\2\u0186\u0187\b8\6\2\u0187p")
        buf.write("\3\2\2\2\u0188\u0189\13\2\2\2\u0189\u018a\b9\7\2\u018a")
        buf.write("r\3\2\2\2\27\2uy|\u0081\u0088\u008b\u0091\u0096\u009b")
        buf.write("\u00a2\u00a4\u0157\u0160\u0164\u016c\u0173\u0175\u0179")
        buf.write("\u0180\u0182\b\3\7\2\b\2\2\3\65\3\3\67\4\38\5\39\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
    NUMBER_LIT = 2
    STRING_LIT = 3
    LP = 4
    RP = 5
    LS = 6
    RS = 7
    COMMA = 8
    ADD = 9
    SUB = 10
    MUL = 11
    DIV = 12
    MOD = 13
    EQUAL = 14
    ASSIGN = 15
    NOT_SAME = 16
    LESS_THAN = 17
    LESS_THAN_EQUAL = 18
    GREATER_THAN_EQUAL = 19
    GREATER_THAN = 20
    CONCAT = 21
    SAME = 22
    TRUE = 23
    FALSE = 24
    NUMBER = 25
    BOOL = 26
    STRING = 27
    RETURN = 28
    VAR = 29
    DYNAMIC = 30
    FUNC = 31
    FOR = 32
    UNTIL = 33
    BY = 34
    BREAK = 35
    CONTINUE = 36
    IF = 37
    ELSE = 38
    ELIF = 39
    BEGIN = 40
    END = 41
    NOT = 42
    AND = 43
    OR = 44
    LINE_COMMENT = 45
    ID = 46
    NEW_LINE = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>='", "'>'", 
            "'...'", "'=='", "'true'", "'false'", "'number'", "'bool'", 
            "'string'", "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'if'", "'else'", 
            "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "NUMBER_LIT", "STRING_LIT", "LP", "RP", "LS", "RS", 
            "COMMA", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", 
            "NOT_SAME", "LESS_THAN", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", 
            "GREATER_THAN", "CONCAT", "SAME", "TRUE", "FALSE", "NUMBER", 
            "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "LINE_COMMENT", "ID", "NEW_LINE", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOL_LIT", "NUMBER_LIT", "INT_LIT", "DEC_PART", "EXP_PART", 
                  "STRING_LIT", "ESC", "ILLEGAL_ESC", "LP", "RP", "LS", 
                  "RS", "COMMA", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "ASSIGN", "NOT_SAME", "LESS_THAN", "LESS_THAN_EQUAL", 
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
            actions[5] = self.STRING_LIT_action 
            actions[51] = self.NEW_LINE_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
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

     


