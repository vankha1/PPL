# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u01e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\7\2r\n\2\f\2")
        buf.write("\16\2u\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3~\n\3\3\4\3")
        buf.write("\4\5\4\u0082\n\4\3\5\3\5\3\5\5\5\u0087\n\5\3\5\6\5\u008a")
        buf.write("\n\5\r\5\16\5\u008b\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u0095")
        buf.write("\n\7\3\7\3\7\3\7\5\7\u009a\n\7\3\b\3\b\3\b\5\b\u009f\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00a7\n\t\f\t\16\t\u00aa")
        buf.write("\13\t\3\t\3\t\3\t\5\t\u00af\n\t\3\n\3\n\3\n\5\n\u00b4")
        buf.write("\n\n\3\13\3\13\5\13\u00b8\n\13\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00bf\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c7\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00ec\n\24\3\25\3\25\3\25\3\25\6\25\u00f2\n")
        buf.write("\25\r\25\16\25\u00f3\3\26\3\26\3\26\3\26\3\26\7\26\u00fb")
        buf.write("\n\26\f\26\16\26\u00fe\13\26\3\26\3\26\7\26\u0102\n\26")
        buf.write("\f\26\16\26\u0105\13\26\3\26\5\26\u0108\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\6\31\u011a\n\31\r\31\16\31\u011b\3\32")
        buf.write("\3\32\6\32\u0120\n\32\r\32\16\32\u0121\3\33\3\33\5\33")
        buf.write("\u0126\n\33\3\33\6\33\u0129\n\33\r\33\16\33\u012a\3\34")
        buf.write("\3\34\3\34\3\34\3\34\6\34\u0132\n\34\r\34\16\34\u0133")
        buf.write("\3\34\3\34\6\34\u0138\n\34\r\34\16\34\u0139\5\34\u013c")
        buf.write("\n\34\3\35\3\35\6\35\u0140\n\35\r\35\16\35\u0141\3\35")
        buf.write("\3\35\3\35\6\35\u0147\n\35\r\35\16\35\u0148\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u014f\n\36\3\37\3\37\5\37\u0153\n\37\3")
        buf.write(" \3 \5 \u0157\n \3!\3!\3\"\3\"\5\"\u015d\n\"\3#\3#\3#")
        buf.write("\3#\3#\5#\u0164\n#\3$\3$\3$\3$\3$\5$\u016b\n$\3%\3%\3")
        buf.write("%\3%\3%\5%\u0172\n%\3&\3&\3&\3&\3&\3&\7&\u017a\n&\f&\16")
        buf.write("&\u017d\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0185\n\'\f\'")
        buf.write("\16\'\u0188\13\'\3(\3(\3(\3(\3(\3(\7(\u0190\n(\f(\16(")
        buf.write("\u0193\13(\3)\3)\3)\5)\u0198\n)\3*\3*\3*\5*\u019d\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\5+\u01a5\n+\3,\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\5-\u01b0\n-\3.\3.\3.\3.\3/\3/\5/\u01b8\n/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\5\62\u01c9\n\62\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\64\3\65\3\65\3\65\3\65\3\65\5\65\u01d8\n\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\5\67\u01df\n\67\38\38\38\2\5JLN9")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\b\5\2\27\27\31\35")
        buf.write("\37\37\3\2\64\65\3\2\22\23\3\2\24\26\3\2\"$\3\2\n\13\2")
        buf.write("\u01eb\2s\3\2\2\2\4}\3\2\2\2\6\u0081\3\2\2\2\b\u0086\3")
        buf.write("\2\2\2\n\u008d\3\2\2\2\f\u0094\3\2\2\2\16\u009b\3\2\2")
        buf.write("\2\20\u00a0\3\2\2\2\22\u00b0\3\2\2\2\24\u00b7\3\2\2\2")
        buf.write("\26\u00be\3\2\2\2\30\u00c6\3\2\2\2\32\u00c8\3\2\2\2\34")
        buf.write("\u00cd\3\2\2\2\36\u00d1\3\2\2\2 \u00d6\3\2\2\2\"\u00da")
        buf.write("\3\2\2\2$\u00df\3\2\2\2&\u00eb\3\2\2\2(\u00ed\3\2\2\2")
        buf.write("*\u00f5\3\2\2\2,\u0109\3\2\2\2.\u010e\3\2\2\2\60\u0117")
        buf.write("\3\2\2\2\62\u011d\3\2\2\2\64\u0123\3\2\2\2\66\u013b\3")
        buf.write("\2\2\28\u013d\3\2\2\2:\u014e\3\2\2\2<\u0152\3\2\2\2>\u0154")
        buf.write("\3\2\2\2@\u0158\3\2\2\2B\u015c\3\2\2\2D\u0163\3\2\2\2")
        buf.write("F\u016a\3\2\2\2H\u0171\3\2\2\2J\u0173\3\2\2\2L\u017e\3")
        buf.write("\2\2\2N\u0189\3\2\2\2P\u0197\3\2\2\2R\u019c\3\2\2\2T\u01a4")
        buf.write("\3\2\2\2V\u01a6\3\2\2\2X\u01af\3\2\2\2Z\u01b1\3\2\2\2")
        buf.write("\\\u01b7\3\2\2\2^\u01bb\3\2\2\2`\u01bf\3\2\2\2b\u01c8")
        buf.write("\3\2\2\2d\u01ca\3\2\2\2f\u01ce\3\2\2\2h\u01d7\3\2\2\2")
        buf.write("j\u01d9\3\2\2\2l\u01de\3\2\2\2n\u01e0\3\2\2\2pr\78\2\2")
        buf.write("qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3")
        buf.write("\2\2\2vw\5\4\3\2wx\7\2\2\3x\3\3\2\2\2yz\5\6\4\2z{\5\4")
        buf.write("\3\2{~\3\2\2\2|~\5\6\4\2}y\3\2\2\2}|\3\2\2\2~\5\3\2\2")
        buf.write("\2\177\u0082\5\b\5\2\u0080\u0082\5\20\t\2\u0081\177\3")
        buf.write("\2\2\2\u0081\u0080\3\2\2\2\u0082\7\3\2\2\2\u0083\u0087")
        buf.write("\5\f\7\2\u0084\u0087\5\n\6\2\u0085\u0087\5\16\b\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u0089\3\2\2\2\u0088\u008a\78\2\2\u0089\u0088\3")
        buf.write("\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\t\3\2\2\2\u008d\u008e\7&\2\2\u008e\u008f")
        buf.write("\7\67\2\2\u008f\u0090\7\30\2\2\u0090\u0091\5@!\2\u0091")
        buf.write("\13\3\2\2\2\u0092\u0095\5j\66\2\u0093\u0095\7\'\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0099\7\67\2\2\u0097\u0098\7\30\2\2\u0098\u009a")
        buf.write("\5@!\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\r")
        buf.write("\3\2\2\2\u009b\u009e\5d\63\2\u009c\u009d\7\30\2\2\u009d")
        buf.write("\u009f\5`\61\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\17\3\2\2\2\u00a0\u00a1\7(\2\2\u00a1\u00a2\7\67")
        buf.write("\2\2\u00a2\u00a3\7\r\2\2\u00a3\u00a4\5\24\13\2\u00a4\u00a8")
        buf.write("\7\16\2\2\u00a5\u00a7\78\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00ae\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00af\7")
        buf.write("8\2\2\u00ac\u00af\58\35\2\u00ad\u00af\5\64\33\2\u00ae")
        buf.write("\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00af\21\3\2\2\2\u00b0\u00b1\5j\66\2\u00b1\u00b3\7\67")
        buf.write("\2\2\u00b2\u00b4\5f\64\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\23\3\2\2\2\u00b5\u00b8\5\26\f\2\u00b6\u00b8")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("\25\3\2\2\2\u00b9\u00ba\5\22\n\2\u00ba\u00bb\7\21\2\2")
        buf.write("\u00bb\u00bc\5\26\f\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf")
        buf.write("\5\22\n\2\u00be\u00b9\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\27\3\2\2\2\u00c0\u00c7\5$\23\2\u00c1\u00c7\5\"\22\2\u00c2")
        buf.write("\u00c7\5 \21\2\u00c3\u00c7\5\36\20\2\u00c4\u00c7\5\34")
        buf.write("\17\2\u00c5\u00c7\5\32\16\2\u00c6\u00c0\3\2\2\2\u00c6")
        buf.write("\u00c1\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c6\u00c3\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\31\3\2")
        buf.write("\2\2\u00c8\u00c9\7\b\2\2\u00c9\u00ca\7\r\2\2\u00ca\u00cb")
        buf.write("\5@!\2\u00cb\u00cc\7\16\2\2\u00cc\33\3\2\2\2\u00cd\u00ce")
        buf.write("\7\7\2\2\u00ce\u00cf\7\r\2\2\u00cf\u00d0\7\16\2\2\u00d0")
        buf.write("\35\3\2\2\2\u00d1\u00d2\7\6\2\2\u00d2\u00d3\7\r\2\2\u00d3")
        buf.write("\u00d4\5@!\2\u00d4\u00d5\7\16\2\2\u00d5\37\3\2\2\2\u00d6")
        buf.write("\u00d7\7\5\2\2\u00d7\u00d8\7\r\2\2\u00d8\u00d9\7\16\2")
        buf.write("\2\u00d9!\3\2\2\2\u00da\u00db\7\4\2\2\u00db\u00dc\7\r")
        buf.write("\2\2\u00dc\u00dd\5@!\2\u00dd\u00de\7\16\2\2\u00de#\3\2")
        buf.write("\2\2\u00df\u00e0\7\3\2\2\u00e0\u00e1\7\r\2\2\u00e1\u00e2")
        buf.write("\7\16\2\2\u00e2%\3\2\2\2\u00e3\u00ec\5(\25\2\u00e4\u00ec")
        buf.write("\5*\26\2\u00e5\u00ec\5.\30\2\u00e6\u00ec\58\35\2\u00e7")
        buf.write("\u00ec\5\60\31\2\u00e8\u00ec\5\62\32\2\u00e9\u00ec\5\64")
        buf.write("\33\2\u00ea\u00ec\5\66\34\2\u00eb\u00e3\3\2\2\2\u00eb")
        buf.write("\u00e4\3\2\2\2\u00eb\u00e5\3\2\2\2\u00eb\u00e6\3\2\2\2")
        buf.write("\u00eb\u00e7\3\2\2\2\u00eb\u00e8\3\2\2\2\u00eb\u00e9\3")
        buf.write("\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\'\3\2\2\2\u00ed\u00ee")
        buf.write("\5> \2\u00ee\u00ef\7\30\2\2\u00ef\u00f1\5@!\2\u00f0\u00f2")
        buf.write("\78\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4)\3\2\2\2\u00f5")
        buf.write("\u00f6\7.\2\2\u00f6\u00f7\5Z.\2\u00f7\u00f8\5l\67\2\u00f8")
        buf.write("\u00fc\5&\24\2\u00f9\u00fb\5,\27\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u0107\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0103")
        buf.write("\7/\2\2\u0100\u0102\78\2\2\u0101\u0100\3\2\2\2\u0102\u0105")
        buf.write("\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108\5&\24\2")
        buf.write("\u0107\u00ff\3\2\2\2\u0107\u0108\3\2\2\2\u0108+\3\2\2")
        buf.write("\2\u0109\u010a\7\60\2\2\u010a\u010b\5Z.\2\u010b\u010c")
        buf.write("\5l\67\2\u010c\u010d\5&\24\2\u010d-\3\2\2\2\u010e\u010f")
        buf.write("\7)\2\2\u010f\u0110\7\67\2\2\u0110\u0111\7*\2\2\u0111")
        buf.write("\u0112\5@!\2\u0112\u0113\7+\2\2\u0113\u0114\5@!\2\u0114")
        buf.write("\u0115\5l\67\2\u0115\u0116\5&\24\2\u0116/\3\2\2\2\u0117")
        buf.write("\u0119\7,\2\2\u0118\u011a\78\2\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\61\3\2\2\2\u011d\u011f\7-\2\2\u011e\u0120\78\2")
        buf.write("\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\63\3\2\2\2\u0123\u0125")
        buf.write("\7%\2\2\u0124\u0126\5@!\2\u0125\u0124\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0129\78\2\2\u0128")
        buf.write("\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\65\3\2\2\2\u012c\u012d\7\67")
        buf.write("\2\2\u012d\u012e\7\r\2\2\u012e\u012f\5B\"\2\u012f\u0131")
        buf.write("\7\16\2\2\u0130\u0132\78\2\2\u0131\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u013c\3\2\2\2\u0135\u0137\5\30\r\2\u0136\u0138")
        buf.write("\78\2\2\u0137\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2")
        buf.write("\u013b\u012c\3\2\2\2\u013b\u0135\3\2\2\2\u013c\67\3\2")
        buf.write("\2\2\u013d\u013f\7\61\2\2\u013e\u0140\78\2\2\u013f\u013e")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\5:\36\2")
        buf.write("\u0144\u0146\7\62\2\2\u0145\u0147\78\2\2\u0146\u0145\3")
        buf.write("\2\2\2\u0147\u0148\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149")
        buf.write("\3\2\2\2\u01499\3\2\2\2\u014a\u014b\5<\37\2\u014b\u014c")
        buf.write("\5:\36\2\u014c\u014f\3\2\2\2\u014d\u014f\3\2\2\2\u014e")
        buf.write("\u014a\3\2\2\2\u014e\u014d\3\2\2\2\u014f;\3\2\2\2\u0150")
        buf.write("\u0153\5&\24\2\u0151\u0153\5\b\5\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0151\3\2\2\2\u0153=\3\2\2\2\u0154\u0156\7\67\2")
        buf.write("\2\u0155\u0157\5^\60\2\u0156\u0155\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157?\3\2\2\2\u0158\u0159\5F$\2\u0159A\3\2\2")
        buf.write("\2\u015a\u015d\5D#\2\u015b\u015d\3\2\2\2\u015c\u015a\3")
        buf.write("\2\2\2\u015c\u015b\3\2\2\2\u015dC\3\2\2\2\u015e\u015f")
        buf.write("\5@!\2\u015f\u0160\7\21\2\2\u0160\u0161\5D#\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0164\5@!\2\u0163\u015e\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164E\3\2\2\2\u0165\u0166\5H%\2\u0166\u0167")
        buf.write("\7\36\2\2\u0167\u0168\5H%\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u016b\5H%\2\u016a\u0165\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("G\3\2\2\2\u016c\u016d\5J&\2\u016d\u016e\t\2\2\2\u016e")
        buf.write("\u016f\5J&\2\u016f\u0172\3\2\2\2\u0170\u0172\5J&\2\u0171")
        buf.write("\u016c\3\2\2\2\u0171\u0170\3\2\2\2\u0172I\3\2\2\2\u0173")
        buf.write("\u0174\b&\1\2\u0174\u0175\5L\'\2\u0175\u017b\3\2\2\2\u0176")
        buf.write("\u0177\f\4\2\2\u0177\u0178\t\3\2\2\u0178\u017a\5L\'\2")
        buf.write("\u0179\u0176\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017c\3\2\2\2\u017cK\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\b\'\1\2\u017f\u0180\5N(\2\u0180\u0186")
        buf.write("\3\2\2\2\u0181\u0182\f\4\2\2\u0182\u0183\t\4\2\2\u0183")
        buf.write("\u0185\5N(\2\u0184\u0181\3\2\2\2\u0185\u0188\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187M\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0189\u018a\b(\1\2\u018a\u018b\5P)\2\u018b")
        buf.write("\u0191\3\2\2\2\u018c\u018d\f\4\2\2\u018d\u018e\t\5\2\2")
        buf.write("\u018e\u0190\5P)\2\u018f\u018c\3\2\2\2\u0190\u0193\3\2")
        buf.write("\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192O\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195\7\63\2\2\u0195")
        buf.write("\u0198\5P)\2\u0196\u0198\5R*\2\u0197\u0194\3\2\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198Q\3\2\2\2\u0199\u019a\7\23\2\2\u019a")
        buf.write("\u019d\5R*\2\u019b\u019d\5T+\2\u019c\u0199\3\2\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019dS\3\2\2\2\u019e\u01a5\7\67\2\2\u019f")
        buf.write("\u01a5\5X-\2\u01a0\u01a5\5V,\2\u01a1\u01a5\5Z.\2\u01a2")
        buf.write("\u01a5\5\\/\2\u01a3\u01a5\5\30\r\2\u01a4\u019e\3\2\2\2")
        buf.write("\u01a4\u019f\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a4\u01a1\3")
        buf.write("\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5U")
        buf.write("\3\2\2\2\u01a6\u01a7\7\67\2\2\u01a7\u01a8\7\r\2\2\u01a8")
        buf.write("\u01a9\5B\"\2\u01a9\u01aa\7\16\2\2\u01aaW\3\2\2\2\u01ab")
        buf.write("\u01b0\5n8\2\u01ac\u01b0\7\t\2\2\u01ad\u01b0\7\f\2\2\u01ae")
        buf.write("\u01b0\5`\61\2\u01af\u01ab\3\2\2\2\u01af\u01ac\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0Y\3\2\2")
        buf.write("\2\u01b1\u01b2\7\r\2\2\u01b2\u01b3\5@!\2\u01b3\u01b4\7")
        buf.write("\16\2\2\u01b4[\3\2\2\2\u01b5\u01b8\7\67\2\2\u01b6\u01b8")
        buf.write("\5V,\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9\u01ba\5^\60\2\u01ba]\3\2\2\2\u01bb\u01bc")
        buf.write("\7\17\2\2\u01bc\u01bd\5D#\2\u01bd\u01be\7\20\2\2\u01be")
        buf.write("_\3\2\2\2\u01bf\u01c0\7\17\2\2\u01c0\u01c1\5b\62\2\u01c1")
        buf.write("\u01c2\7\20\2\2\u01c2a\3\2\2\2\u01c3\u01c4\5@!\2\u01c4")
        buf.write("\u01c5\7\21\2\2\u01c5\u01c6\5b\62\2\u01c6\u01c9\3\2\2")
        buf.write("\2\u01c7\u01c9\5@!\2\u01c8\u01c3\3\2\2\2\u01c8\u01c7\3")
        buf.write("\2\2\2\u01c9c\3\2\2\2\u01ca\u01cb\5j\66\2\u01cb\u01cc")
        buf.write("\7\67\2\2\u01cc\u01cd\5f\64\2\u01cde\3\2\2\2\u01ce\u01cf")
        buf.write("\7\17\2\2\u01cf\u01d0\5h\65\2\u01d0\u01d1\7\20\2\2\u01d1")
        buf.write("g\3\2\2\2\u01d2\u01d3\5n8\2\u01d3\u01d4\7\21\2\2\u01d4")
        buf.write("\u01d5\5h\65\2\u01d5\u01d8\3\2\2\2\u01d6\u01d8\5n8\2\u01d7")
        buf.write("\u01d2\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8i\3\2\2\2\u01d9")
        buf.write("\u01da\t\6\2\2\u01dak\3\2\2\2\u01db\u01dc\78\2\2\u01dc")
        buf.write("\u01df\5l\67\2\u01dd\u01df\3\2\2\2\u01de\u01db\3\2\2\2")
        buf.write("\u01de\u01dd\3\2\2\2\u01dfm\3\2\2\2\u01e0\u01e1\t\7\2")
        buf.write("\2\u01e1o\3\2\2\2\60s}\u0081\u0086\u008b\u0094\u0099\u009e")
        buf.write("\u00a8\u00ae\u00b3\u00b7\u00be\u00c6\u00eb\u00f3\u00fc")
        buf.write("\u0103\u0107\u011b\u0121\u0125\u012a\u0133\u0139\u013b")
        buf.write("\u0141\u0148\u014e\u0152\u0156\u015c\u0163\u016a\u0171")
        buf.write("\u017b\u0186\u0191\u0197\u019c\u01a4\u01af\u01b7\u01c8")
        buf.write("\u01d7\u01de")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'writeBool'", "'readString'", "'writeString'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>='", "'>'", 
                     "'...'", "'=='", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "READNUM", "WRITENUM", "READBOOL", "WRITEBOOL", 
                      "READSTRING", "WRITESTRING", "BOOL_LIT", "FLOAT_LIT", 
                      "INT_LIT", "STRING_LIT", "LP", "RP", "LS", "RS", "COMMA", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", 
                      "NOT_SAME", "LESS_THAN", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", 
                      "GREATER_THAN", "CONCAT", "SAME", "TRUE", "FALSE", 
                      "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
                      "OR", "LINE_COMMENT", "ID", "NEW_LINE", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_vardecl_full = 4
    RULE_vardecl_not_full = 5
    RULE_vardecl_array = 6
    RULE_funcdecl = 7
    RULE_paramdecl = 8
    RULE_param_list = 9
    RULE_param_prime = 10
    RULE_spec_func = 11
    RULE_write_string = 12
    RULE_read_string = 13
    RULE_write = 14
    RULE_read_bool = 15
    RULE_write_number = 16
    RULE_read_number = 17
    RULE_stmt = 18
    RULE_assign_stmt = 19
    RULE_if_stmt = 20
    RULE_elif_stmt = 21
    RULE_for_stmt = 22
    RULE_break_stmt = 23
    RULE_continue_stmt = 24
    RULE_return_stmt = 25
    RULE_call_stmt = 26
    RULE_block_stmt = 27
    RULE_blocked_list = 28
    RULE_stmt_plus_vardecl = 29
    RULE_lhs = 30
    RULE_exp = 31
    RULE_expr_list = 32
    RULE_exprprime = 33
    RULE_exp0 = 34
    RULE_exp1 = 35
    RULE_exp2 = 36
    RULE_exp3 = 37
    RULE_exp4 = 38
    RULE_exp5 = 39
    RULE_exp6 = 40
    RULE_exp7 = 41
    RULE_func_call = 42
    RULE_constant = 43
    RULE_sub_exp = 44
    RULE_index_expr = 45
    RULE_index_operator = 46
    RULE_array_lit = 47
    RULE_non_empty_expr_list = 48
    RULE_array_type = 49
    RULE_dimensions = 50
    RULE_number_lits = 51
    RULE_atomic_types = 52
    RULE_newline_list = 53
    RULE_number_lit = 54

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "vardecl_full", 
                   "vardecl_not_full", "vardecl_array", "funcdecl", "paramdecl", 
                   "param_list", "param_prime", "spec_func", "write_string", 
                   "read_string", "write", "read_bool", "write_number", 
                   "read_number", "stmt", "assign_stmt", "if_stmt", "elif_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "block_stmt", "blocked_list", "stmt_plus_vardecl", 
                   "lhs", "exp", "expr_list", "exprprime", "exp0", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "func_call", 
                   "constant", "sub_exp", "index_expr", "index_operator", 
                   "array_lit", "non_empty_expr_list", "array_type", "dimensions", 
                   "number_lits", "atomic_types", "newline_list", "number_lit" ]

    EOF = Token.EOF
    READNUM=1
    WRITENUM=2
    READBOOL=3
    WRITEBOOL=4
    READSTRING=5
    WRITESTRING=6
    BOOL_LIT=7
    FLOAT_LIT=8
    INT_LIT=9
    STRING_LIT=10
    LP=11
    RP=12
    LS=13
    RS=14
    COMMA=15
    ADD=16
    SUB=17
    MUL=18
    DIV=19
    MOD=20
    EQUAL=21
    ASSIGN=22
    NOT_SAME=23
    LESS_THAN=24
    LESS_THAN_EQUAL=25
    GREATER_THAN_EQUAL=26
    GREATER_THAN=27
    CONCAT=28
    SAME=29
    TRUE=30
    FALSE=31
    NUMBER=32
    BOOL=33
    STRING=34
    RETURN=35
    VAR=36
    DYNAMIC=37
    FUNC=38
    FOR=39
    UNTIL=40
    BY=41
    BREAK=42
    CONTINUE=43
    IF=44
    ELSE=45
    ELIF=46
    BEGIN=47
    END=48
    NOT=49
    AND=50
    OR=51
    LINE_COMMENT=52
    ID=53
    NEW_LINE=54
    WS=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57
    ERROR_CHAR=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEW_LINE:
                self.state = 110
                self.match(ZCodeParser.NEW_LINE)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.decllist()
            self.state = 117
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.decl()
                self.state = 120
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl_not_full(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_not_fullContext,0)


        def vardecl_full(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_fullContext,0)


        def vardecl_array(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_arrayContext,0)


        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 129
                self.vardecl_not_full()
                pass

            elif la_ == 2:
                self.state = 130
                self.vardecl_full()
                pass

            elif la_ == 3:
                self.state = 131
                self.vardecl_array()
                pass


            self.state = 135 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 134
                self.match(ZCodeParser.NEW_LINE)
                self.state = 137 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_full

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_full" ):
                return visitor.visitVardecl_full(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_full(self):

        localctx = ZCodeParser.Vardecl_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl_full)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ZCodeParser.VAR)
            self.state = 140
            self.match(ZCodeParser.ID)
            self.state = 141
            self.match(ZCodeParser.ASSIGN)
            self.state = 142
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_not_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def atomic_types(self):
            return self.getTypedRuleContext(ZCodeParser.Atomic_typesContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_not_full

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_not_full" ):
                return visitor.visitVardecl_not_full(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_not_full(self):

        localctx = ZCodeParser.Vardecl_not_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl_not_full)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 144
                self.atomic_types()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 145
                self.match(ZCodeParser.DYNAMIC)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 148
            self.match(ZCodeParser.ID)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 149
                self.match(ZCodeParser.ASSIGN)
                self.state = 150
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_array" ):
                return visitor.visitVardecl_array(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_array(self):

        localctx = ZCodeParser.Vardecl_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.array_type()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 154
                self.match(ZCodeParser.ASSIGN)
                self.state = 155
                self.array_lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.FUNC)
            self.state = 159
            self.match(ZCodeParser.ID)
            self.state = 160
            self.match(ZCodeParser.LP)
            self.state = 161
            self.param_list()
            self.state = 162
            self.match(ZCodeParser.RP)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 163
                    self.match(ZCodeParser.NEW_LINE) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEW_LINE]:
                self.state = 169
                self.match(ZCodeParser.NEW_LINE)
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.state = 170
                self.block_stmt()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.state = 171
                self.return_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_types(self):
            return self.getTypedRuleContext(ZCodeParser.Atomic_typesContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.atomic_types()
            self.state = 175
            self.match(ZCodeParser.ID)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LS:
                self.state = 176
                self.dimensions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.param_prime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_prime" ):
                return visitor.visitParam_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_prime)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.paramdecl()
                self.state = 184
                self.match(ZCodeParser.COMMA)
                self.state = 185
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.paramdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spec_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def read_number(self):
            return self.getTypedRuleContext(ZCodeParser.Read_numberContext,0)


        def write_number(self):
            return self.getTypedRuleContext(ZCodeParser.Write_numberContext,0)


        def read_bool(self):
            return self.getTypedRuleContext(ZCodeParser.Read_boolContext,0)


        def write(self):
            return self.getTypedRuleContext(ZCodeParser.WriteContext,0)


        def read_string(self):
            return self.getTypedRuleContext(ZCodeParser.Read_stringContext,0)


        def write_string(self):
            return self.getTypedRuleContext(ZCodeParser.Write_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_spec_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpec_func" ):
                return visitor.visitSpec_func(self)
            else:
                return visitor.visitChildren(self)




    def spec_func(self):

        localctx = ZCodeParser.Spec_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_spec_func)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.READNUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.read_number()
                pass
            elif token in [ZCodeParser.WRITENUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.write_number()
                pass
            elif token in [ZCodeParser.READBOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.read_bool()
                pass
            elif token in [ZCodeParser.WRITEBOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.write()
                pass
            elif token in [ZCodeParser.READSTRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 194
                self.read_string()
                pass
            elif token in [ZCodeParser.WRITESTRING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 195
                self.write_string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITESTRING(self):
            return self.getToken(ZCodeParser.WRITESTRING, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_string" ):
                return visitor.visitWrite_string(self)
            else:
                return visitor.visitChildren(self)




    def write_string(self):

        localctx = ZCodeParser.Write_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_write_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ZCodeParser.WRITESTRING)
            self.state = 199
            self.match(ZCodeParser.LP)
            self.state = 200
            self.exp()
            self.state = 201
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READSTRING(self):
            return self.getToken(ZCodeParser.READSTRING, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_read_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_string" ):
                return visitor.visitRead_string(self)
            else:
                return visitor.visitChildren(self)




    def read_string(self):

        localctx = ZCodeParser.Read_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_read_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ZCodeParser.READSTRING)
            self.state = 204
            self.match(ZCodeParser.LP)
            self.state = 205
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITEBOOL(self):
            return self.getToken(ZCodeParser.WRITEBOOL, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = ZCodeParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.WRITEBOOL)
            self.state = 208
            self.match(ZCodeParser.LP)
            self.state = 209
            self.exp()
            self.state = 210
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READBOOL(self):
            return self.getToken(ZCodeParser.READBOOL, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_read_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_bool" ):
                return visitor.visitRead_bool(self)
            else:
                return visitor.visitChildren(self)




    def read_bool(self):

        localctx = ZCodeParser.Read_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_read_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ZCodeParser.READBOOL)
            self.state = 213
            self.match(ZCodeParser.LP)
            self.state = 214
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITENUM(self):
            return self.getToken(ZCodeParser.WRITENUM, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_write_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite_number" ):
                return visitor.visitWrite_number(self)
            else:
                return visitor.visitChildren(self)




    def write_number(self):

        localctx = ZCodeParser.Write_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_write_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(ZCodeParser.WRITENUM)
            self.state = 217
            self.match(ZCodeParser.LP)
            self.state = 218
            self.exp()
            self.state = 219
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READNUM(self):
            return self.getToken(ZCodeParser.READNUM, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_read_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_number" ):
                return visitor.visitRead_number(self)
            else:
                return visitor.visitChildren(self)




    def read_number(self):

        localctx = ZCodeParser.Read_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_read_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ZCodeParser.READNUM)
            self.state = 222
            self.match(ZCodeParser.LP)
            self.state = 223
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Call_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 225
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.state = 226
                self.if_stmt()
                pass

            elif la_ == 3:
                self.state = 227
                self.for_stmt()
                pass

            elif la_ == 4:
                self.state = 228
                self.block_stmt()
                pass

            elif la_ == 5:
                self.state = 229
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 230
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 231
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 232
                self.call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.lhs()
            self.state = 236
            self.match(ZCodeParser.ASSIGN)
            self.state = 237
            self.exp()
            self.state = 239 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 238
                self.match(ZCodeParser.NEW_LINE)
                self.state = 241 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def sub_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_expContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def elif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_stmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.IF)
            self.state = 244
            self.sub_exp()
            self.state = 245
            self.newline_list()
            self.state = 246
            self.stmt()
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 247
                    self.elif_stmt() 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(ZCodeParser.ELSE)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEW_LINE:
                    self.state = 254
                    self.match(ZCodeParser.NEW_LINE)
                    self.state = 259
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 260
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def sub_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_expContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ZCodeParser.ELIF)
            self.state = 264
            self.sub_exp()
            self.state = 265
            self.newline_list()
            self.state = 266
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ZCodeParser.FOR)
            self.state = 269
            self.match(ZCodeParser.ID)
            self.state = 270
            self.match(ZCodeParser.UNTIL)
            self.state = 271
            self.exp()
            self.state = 272
            self.match(ZCodeParser.BY)
            self.state = 273
            self.exp()
            self.state = 274
            self.newline_list()
            self.state = 275
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_break_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(ZCodeParser.BREAK)
            self.state = 279 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.match(ZCodeParser.NEW_LINE)
                self.state = 281 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continue_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ZCodeParser.CONTINUE)
            self.state = 285 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 284
                self.match(ZCodeParser.NEW_LINE)
                self.state = 287 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.RETURN)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.READNUM) | (1 << ZCodeParser.WRITENUM) | (1 << ZCodeParser.READBOOL) | (1 << ZCodeParser.WRITEBOOL) | (1 << ZCodeParser.READSTRING) | (1 << ZCodeParser.WRITESTRING) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.FLOAT_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 290
                self.exp()


            self.state = 294 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 293
                self.match(ZCodeParser.NEW_LINE)
                self.state = 296 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def spec_func(self):
            return self.getTypedRuleContext(ZCodeParser.Spec_funcContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(ZCodeParser.ID)
                self.state = 299
                self.match(ZCodeParser.LP)
                self.state = 300
                self.expr_list()
                self.state = 301
                self.match(ZCodeParser.RP)
                self.state = 303 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 302
                    self.match(ZCodeParser.NEW_LINE)
                    self.state = 305 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEW_LINE):
                        break

                pass
            elif token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.spec_func()
                self.state = 309 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 308
                    self.match(ZCodeParser.NEW_LINE)
                    self.state = 311 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NEW_LINE):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def blocked_list(self):
            return self.getTypedRuleContext(ZCodeParser.Blocked_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.BEGIN)
            self.state = 317 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 316
                self.match(ZCodeParser.NEW_LINE)
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

            self.state = 321
            self.blocked_list()
            self.state = 322
            self.match(ZCodeParser.END)
            self.state = 324 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 323
                self.match(ZCodeParser.NEW_LINE)
                self.state = 326 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEW_LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Blocked_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_plus_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_plus_vardeclContext,0)


        def blocked_list(self):
            return self.getTypedRuleContext(ZCodeParser.Blocked_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blocked_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocked_list" ):
                return visitor.visitBlocked_list(self)
            else:
                return visitor.visitChildren(self)




    def blocked_list(self):

        localctx = ZCodeParser.Blocked_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_blocked_list)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.stmt_plus_vardecl()
                self.state = 329
                self.blocked_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_plus_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_plus_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_plus_vardecl" ):
                return visitor.visitStmt_plus_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def stmt_plus_vardecl(self):

        localctx = ZCodeParser.Stmt_plus_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_plus_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.state = 334
                self.stmt()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 335
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.ID)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LS:
                self.state = 339
                self.index_operator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(ZCodeParser.Exp0Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.exp0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr_list)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING, ZCodeParser.BOOL_LIT, ZCodeParser.FLOAT_LIT, ZCodeParser.INT_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.exprprime()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = ZCodeParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exprprime)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.exp()
                self.state = 349
                self.match(ZCodeParser.COMMA)
                self.state = 350
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp0" ):
                return visitor.visitExp0(self)
            else:
                return visitor.visitChildren(self)




    def exp0(self):

        localctx = ZCodeParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp0)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.exp1()
                self.state = 356
                self.match(ZCodeParser.CONCAT)
                self.state = 357
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOT_SAME(self):
            return self.getToken(ZCodeParser.NOT_SAME, 0)

        def SAME(self):
            return self.getToken(ZCodeParser.SAME, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.exp2(0)
                self.state = 363
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_SAME) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_THAN_EQUAL) | (1 << ZCodeParser.GREATER_THAN_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.SAME))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 364
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 374
                    self.exp3(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 385
                    self.exp4(0) 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 396
                    self.exp5() 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp5)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(ZCodeParser.NOT)
                self.state = 403
                self.exp5()
                pass
            elif token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING, ZCodeParser.BOOL_LIT, ZCodeParser.FLOAT_LIT, ZCodeParser.INT_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.SUB, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp6)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ZCodeParser.SUB)
                self.state = 408
                self.exp6()
                pass
            elif token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING, ZCodeParser.BOOL_LIT, ZCodeParser.FLOAT_LIT, ZCodeParser.INT_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def constant(self):
            return self.getTypedRuleContext(ZCodeParser.ConstantContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def sub_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_expContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def spec_func(self):
            return self.getTypedRuleContext(ZCodeParser.Spec_funcContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp7)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.sub_exp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.index_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 417
                self.spec_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(ZCodeParser.ID)
            self.state = 421
            self.match(ZCodeParser.LP)
            self.state = 422
            self.expr_list()
            self.state = 423
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Number_litContext,0)


        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = ZCodeParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_constant)
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FLOAT_LIT, ZCodeParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.number_lit()
                pass
            elif token in [ZCodeParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.LS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 428
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sub_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_exp" ):
                return visitor.visitSub_exp(self)
            else:
                return visitor.visitChildren(self)




    def sub_exp(self):

        localctx = ZCodeParser.Sub_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_sub_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(ZCodeParser.LP)
            self.state = 432
            self.exp()
            self.state = 433
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 435
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 436
                self.func_call()
                pass


            self.state = 439
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.LS)
            self.state = 442
            self.exprprime()
            self.state = 443
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def non_empty_expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Non_empty_expr_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(ZCodeParser.LS)
            self.state = 446
            self.non_empty_expr_list()
            self.state = 447
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_empty_expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def non_empty_expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Non_empty_expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_non_empty_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_empty_expr_list" ):
                return visitor.visitNon_empty_expr_list(self)
            else:
                return visitor.visitChildren(self)




    def non_empty_expr_list(self):

        localctx = ZCodeParser.Non_empty_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_non_empty_expr_list)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.exp()
                self.state = 450
                self.match(ZCodeParser.COMMA)
                self.state = 451
                self.non_empty_expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_types(self):
            return self.getTypedRuleContext(ZCodeParser.Atomic_typesContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = ZCodeParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.atomic_types()
            self.state = 457
            self.match(ZCodeParser.ID)
            self.state = 458
            self.dimensions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def number_lits(self):
            return self.getTypedRuleContext(ZCodeParser.Number_litsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = ZCodeParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(ZCodeParser.LS)
            self.state = 461
            self.number_lits()
            self.state = 462
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_litsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Number_litContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def number_lits(self):
            return self.getTypedRuleContext(ZCodeParser.Number_litsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_lits

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_lits" ):
                return visitor.visitNumber_lits(self)
            else:
                return visitor.visitChildren(self)




    def number_lits(self):

        localctx = ZCodeParser.Number_litsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_number_lits)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.number_lit()
                self.state = 465
                self.match(ZCodeParser.COMMA)
                self.state = 466
                self.number_lits()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.number_lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_atomic_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_types" ):
                return visitor.visitAtomic_types(self)
            else:
                return visitor.visitChildren(self)




    def atomic_types(self):

        localctx = ZCodeParser.Atomic_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_atomic_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_newline_list)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEW_LINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(ZCodeParser.NEW_LINE)
                self.state = 474
                self.newline_list()
                pass
            elif token in [ZCodeParser.READNUM, ZCodeParser.WRITENUM, ZCodeParser.READBOOL, ZCodeParser.WRITEBOOL, ZCodeParser.READSTRING, ZCodeParser.WRITESTRING, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(ZCodeParser.FLOAT_LIT, 0)

        def INT_LIT(self):
            return self.getToken(ZCodeParser.INT_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_number_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_lit" ):
                return visitor.visitNumber_lit(self)
            else:
                return visitor.visitChildren(self)




    def number_lit(self):

        localctx = ZCodeParser.Number_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_number_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.FLOAT_LIT or _la==ZCodeParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.exp2_sempred
        self._predicates[37] = self.exp3_sempred
        self._predicates[38] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




