# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/Assignment 232/assignment_3/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,425,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,5,0,98,8,0,10,0,12,0,101,9,0,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,110,8,1,1,2,1,2,3,2,114,8,2,1,3,1,3,1,3,3,3,119,
        8,3,1,3,4,3,122,8,3,11,3,12,3,123,1,4,1,4,1,4,1,4,1,4,1,5,1,5,3,
        5,133,8,5,1,5,1,5,1,5,3,5,138,8,5,1,6,1,6,1,6,1,6,1,6,3,6,145,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,153,8,7,10,7,12,7,156,9,7,1,7,1,7,
        1,7,3,7,161,8,7,1,8,1,8,3,8,165,8,8,1,9,1,9,1,9,1,9,1,9,3,9,172,
        8,9,1,10,1,10,1,10,3,10,177,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,3,11,188,8,11,1,12,1,12,1,12,1,12,4,12,194,8,12,11,
        12,12,12,195,1,13,1,13,1,13,1,13,1,13,5,13,203,8,13,10,13,12,13,
        206,9,13,1,13,3,13,209,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,5,
        15,218,8,15,10,15,12,15,221,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,17,1,17,4,17,236,8,17,11,17,12,17,237,1,
        18,1,18,4,18,242,8,18,11,18,12,18,243,1,19,1,19,3,19,248,8,19,1,
        19,4,19,251,8,19,11,19,12,19,252,1,20,1,20,1,20,1,20,1,20,4,20,260,
        8,20,11,20,12,20,261,1,21,1,21,4,21,266,8,21,11,21,12,21,267,1,21,
        1,21,1,21,4,21,273,8,21,11,21,12,21,274,1,22,1,22,1,22,1,22,3,22,
        281,8,22,1,23,1,23,3,23,285,8,23,1,24,1,24,3,24,289,8,24,1,25,1,
        25,1,26,1,26,3,26,295,8,26,1,27,1,27,1,27,1,27,1,27,3,27,302,8,27,
        1,28,1,28,1,28,1,28,1,28,3,28,309,8,28,1,29,1,29,1,29,1,29,1,29,
        3,29,316,8,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,324,8,30,10,30,
        12,30,327,9,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,335,8,31,10,31,
        12,31,338,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,346,8,32,10,32,
        12,32,349,9,32,1,33,1,33,1,33,3,33,354,8,33,1,34,1,34,1,34,3,34,
        359,8,34,1,35,1,35,1,35,1,35,3,35,365,8,35,1,35,1,35,3,35,369,8,
        35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,3,37,380,8,37,1,
        38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,
        41,1,41,1,42,1,42,1,42,1,42,1,42,3,42,402,8,42,1,43,1,43,1,43,1,
        43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,3,45,416,8,45,1,46,1,
        46,1,47,1,47,1,47,3,47,423,8,47,1,47,0,3,60,62,64,48,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,0,5,
        3,0,14,14,16,20,22,22,1,0,43,44,1,0,9,10,1,0,11,13,1,0,25,27,433,
        0,99,1,0,0,0,2,109,1,0,0,0,4,113,1,0,0,0,6,118,1,0,0,0,8,125,1,0,
        0,0,10,132,1,0,0,0,12,139,1,0,0,0,14,146,1,0,0,0,16,164,1,0,0,0,
        18,171,1,0,0,0,20,173,1,0,0,0,22,187,1,0,0,0,24,189,1,0,0,0,26,197,
        1,0,0,0,28,210,1,0,0,0,30,215,1,0,0,0,32,224,1,0,0,0,34,233,1,0,
        0,0,36,239,1,0,0,0,38,245,1,0,0,0,40,254,1,0,0,0,42,263,1,0,0,0,
        44,280,1,0,0,0,46,284,1,0,0,0,48,286,1,0,0,0,50,290,1,0,0,0,52,294,
        1,0,0,0,54,301,1,0,0,0,56,308,1,0,0,0,58,315,1,0,0,0,60,317,1,0,
        0,0,62,328,1,0,0,0,64,339,1,0,0,0,66,353,1,0,0,0,68,358,1,0,0,0,
        70,368,1,0,0,0,72,370,1,0,0,0,74,379,1,0,0,0,76,381,1,0,0,0,78,385,
        1,0,0,0,80,388,1,0,0,0,82,392,1,0,0,0,84,401,1,0,0,0,86,403,1,0,
        0,0,88,407,1,0,0,0,90,415,1,0,0,0,92,417,1,0,0,0,94,422,1,0,0,0,
        96,98,5,47,0,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,
        1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,103,3,2,1,0,103,104,5,
        0,0,1,104,1,1,0,0,0,105,106,3,4,2,0,106,107,3,2,1,0,107,110,1,0,
        0,0,108,110,3,4,2,0,109,105,1,0,0,0,109,108,1,0,0,0,110,3,1,0,0,
        0,111,114,3,6,3,0,112,114,3,14,7,0,113,111,1,0,0,0,113,112,1,0,0,
        0,114,5,1,0,0,0,115,119,3,10,5,0,116,119,3,8,4,0,117,119,3,12,6,
        0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,1,0,0,0,119,121,1,0,0,
        0,120,122,5,47,0,0,121,120,1,0,0,0,122,123,1,0,0,0,123,121,1,0,0,
        0,123,124,1,0,0,0,124,7,1,0,0,0,125,126,5,29,0,0,126,127,5,46,0,
        0,127,128,5,15,0,0,128,129,3,50,25,0,129,9,1,0,0,0,130,133,3,92,
        46,0,131,133,5,30,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,134,1,
        0,0,0,134,137,5,46,0,0,135,136,5,15,0,0,136,138,3,50,25,0,137,135,
        1,0,0,0,137,138,1,0,0,0,138,11,1,0,0,0,139,140,3,92,46,0,140,141,
        5,46,0,0,141,144,3,88,44,0,142,143,5,15,0,0,143,145,3,82,41,0,144,
        142,1,0,0,0,144,145,1,0,0,0,145,13,1,0,0,0,146,147,5,31,0,0,147,
        148,5,46,0,0,148,149,5,4,0,0,149,150,3,16,8,0,150,154,5,5,0,0,151,
        153,5,47,0,0,152,151,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,160,1,0,0,0,156,154,1,0,0,0,157,161,5,47,0,0,158,
        161,3,42,21,0,159,161,3,38,19,0,160,157,1,0,0,0,160,158,1,0,0,0,
        160,159,1,0,0,0,161,15,1,0,0,0,162,165,3,18,9,0,163,165,1,0,0,0,
        164,162,1,0,0,0,164,163,1,0,0,0,165,17,1,0,0,0,166,167,3,20,10,0,
        167,168,5,8,0,0,168,169,3,18,9,0,169,172,1,0,0,0,170,172,3,20,10,
        0,171,166,1,0,0,0,171,170,1,0,0,0,172,19,1,0,0,0,173,174,3,92,46,
        0,174,176,5,46,0,0,175,177,3,88,44,0,176,175,1,0,0,0,176,177,1,0,
        0,0,177,21,1,0,0,0,178,188,3,6,3,0,179,188,3,24,12,0,180,188,3,26,
        13,0,181,188,3,32,16,0,182,188,3,42,21,0,183,188,3,34,17,0,184,188,
        3,36,18,0,185,188,3,38,19,0,186,188,3,40,20,0,187,178,1,0,0,0,187,
        179,1,0,0,0,187,180,1,0,0,0,187,181,1,0,0,0,187,182,1,0,0,0,187,
        183,1,0,0,0,187,184,1,0,0,0,187,185,1,0,0,0,187,186,1,0,0,0,188,
        23,1,0,0,0,189,190,3,48,24,0,190,191,5,15,0,0,191,193,3,50,25,0,
        192,194,5,47,0,0,193,192,1,0,0,0,194,195,1,0,0,0,195,193,1,0,0,0,
        195,196,1,0,0,0,196,25,1,0,0,0,197,198,5,37,0,0,198,199,3,76,38,
        0,199,200,3,94,47,0,200,204,3,22,11,0,201,203,3,28,14,0,202,201,
        1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,208,
        1,0,0,0,206,204,1,0,0,0,207,209,3,30,15,0,208,207,1,0,0,0,208,209,
        1,0,0,0,209,27,1,0,0,0,210,211,5,39,0,0,211,212,3,76,38,0,212,213,
        3,94,47,0,213,214,3,22,11,0,214,29,1,0,0,0,215,219,5,38,0,0,216,
        218,5,47,0,0,217,216,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,
        220,1,0,0,0,220,222,1,0,0,0,221,219,1,0,0,0,222,223,3,22,11,0,223,
        31,1,0,0,0,224,225,5,32,0,0,225,226,5,46,0,0,226,227,5,33,0,0,227,
        228,3,50,25,0,228,229,5,34,0,0,229,230,3,50,25,0,230,231,3,94,47,
        0,231,232,3,22,11,0,232,33,1,0,0,0,233,235,5,35,0,0,234,236,5,47,
        0,0,235,234,1,0,0,0,236,237,1,0,0,0,237,235,1,0,0,0,237,238,1,0,
        0,0,238,35,1,0,0,0,239,241,5,36,0,0,240,242,5,47,0,0,241,240,1,0,
        0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,37,1,0,0,
        0,245,247,5,28,0,0,246,248,3,50,25,0,247,246,1,0,0,0,247,248,1,0,
        0,0,248,250,1,0,0,0,249,251,5,47,0,0,250,249,1,0,0,0,251,252,1,0,
        0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,39,1,0,0,0,254,255,5,46,
        0,0,255,256,5,4,0,0,256,257,3,52,26,0,257,259,5,5,0,0,258,260,5,
        47,0,0,259,258,1,0,0,0,260,261,1,0,0,0,261,259,1,0,0,0,261,262,1,
        0,0,0,262,41,1,0,0,0,263,265,5,40,0,0,264,266,5,47,0,0,265,264,1,
        0,0,0,266,267,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,269,1,
        0,0,0,269,270,3,44,22,0,270,272,5,41,0,0,271,273,5,47,0,0,272,271,
        1,0,0,0,273,274,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,43,1,
        0,0,0,276,277,3,46,23,0,277,278,3,44,22,0,278,281,1,0,0,0,279,281,
        1,0,0,0,280,276,1,0,0,0,280,279,1,0,0,0,281,45,1,0,0,0,282,285,3,
        22,11,0,283,285,3,6,3,0,284,282,1,0,0,0,284,283,1,0,0,0,285,47,1,
        0,0,0,286,288,5,46,0,0,287,289,3,80,40,0,288,287,1,0,0,0,288,289,
        1,0,0,0,289,49,1,0,0,0,290,291,3,56,28,0,291,51,1,0,0,0,292,295,
        3,54,27,0,293,295,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,53,
        1,0,0,0,296,297,3,50,25,0,297,298,5,8,0,0,298,299,3,54,27,0,299,
        302,1,0,0,0,300,302,3,50,25,0,301,296,1,0,0,0,301,300,1,0,0,0,302,
        55,1,0,0,0,303,304,3,58,29,0,304,305,5,21,0,0,305,306,3,58,29,0,
        306,309,1,0,0,0,307,309,3,58,29,0,308,303,1,0,0,0,308,307,1,0,0,
        0,309,57,1,0,0,0,310,311,3,60,30,0,311,312,7,0,0,0,312,313,3,60,
        30,0,313,316,1,0,0,0,314,316,3,60,30,0,315,310,1,0,0,0,315,314,1,
        0,0,0,316,59,1,0,0,0,317,318,6,30,-1,0,318,319,3,62,31,0,319,325,
        1,0,0,0,320,321,10,2,0,0,321,322,7,1,0,0,322,324,3,62,31,0,323,320,
        1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,0,325,326,1,0,0,0,326,61,1,
        0,0,0,327,325,1,0,0,0,328,329,6,31,-1,0,329,330,3,64,32,0,330,336,
        1,0,0,0,331,332,10,2,0,0,332,333,7,2,0,0,333,335,3,64,32,0,334,331,
        1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,0,337,63,1,
        0,0,0,338,336,1,0,0,0,339,340,6,32,-1,0,340,341,3,66,33,0,341,347,
        1,0,0,0,342,343,10,2,0,0,343,344,7,3,0,0,344,346,3,66,33,0,345,342,
        1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,65,1,
        0,0,0,349,347,1,0,0,0,350,351,5,42,0,0,351,354,3,66,33,0,352,354,
        3,68,34,0,353,350,1,0,0,0,353,352,1,0,0,0,354,67,1,0,0,0,355,356,
        5,10,0,0,356,359,3,68,34,0,357,359,3,70,35,0,358,355,1,0,0,0,358,
        357,1,0,0,0,359,69,1,0,0,0,360,369,5,46,0,0,361,369,3,74,37,0,362,
        364,3,72,36,0,363,365,3,80,40,0,364,363,1,0,0,0,364,365,1,0,0,0,
        365,369,1,0,0,0,366,369,3,76,38,0,367,369,3,78,39,0,368,360,1,0,
        0,0,368,361,1,0,0,0,368,362,1,0,0,0,368,366,1,0,0,0,368,367,1,0,
        0,0,369,71,1,0,0,0,370,371,5,46,0,0,371,372,5,4,0,0,372,373,3,52,
        26,0,373,374,5,5,0,0,374,73,1,0,0,0,375,380,5,2,0,0,376,380,5,1,
        0,0,377,380,5,3,0,0,378,380,3,82,41,0,379,375,1,0,0,0,379,376,1,
        0,0,0,379,377,1,0,0,0,379,378,1,0,0,0,380,75,1,0,0,0,381,382,5,4,
        0,0,382,383,3,50,25,0,383,384,5,5,0,0,384,77,1,0,0,0,385,386,5,46,
        0,0,386,387,3,80,40,0,387,79,1,0,0,0,388,389,5,6,0,0,389,390,3,54,
        27,0,390,391,5,7,0,0,391,81,1,0,0,0,392,393,5,6,0,0,393,394,3,84,
        42,0,394,395,5,7,0,0,395,83,1,0,0,0,396,397,3,50,25,0,397,398,5,
        8,0,0,398,399,3,84,42,0,399,402,1,0,0,0,400,402,3,50,25,0,401,396,
        1,0,0,0,401,400,1,0,0,0,402,85,1,0,0,0,403,404,3,92,46,0,404,405,
        5,46,0,0,405,406,3,88,44,0,406,87,1,0,0,0,407,408,5,6,0,0,408,409,
        3,90,45,0,409,410,5,7,0,0,410,89,1,0,0,0,411,412,5,2,0,0,412,413,
        5,8,0,0,413,416,3,90,45,0,414,416,5,2,0,0,415,411,1,0,0,0,415,414,
        1,0,0,0,416,91,1,0,0,0,417,418,7,4,0,0,418,93,1,0,0,0,419,420,5,
        47,0,0,420,423,3,94,47,0,421,423,1,0,0,0,422,419,1,0,0,0,422,421,
        1,0,0,0,423,95,1,0,0,0,43,99,109,113,118,123,132,137,144,154,160,
        164,171,176,187,195,204,208,219,237,243,247,252,261,267,274,280,
        284,288,294,301,308,315,325,336,347,353,358,364,368,379,401,415,
        422
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "','", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", 
                     "'>='", "'>'", "'...'", "'=='", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "BOOL_LIT", "NUMBER_LIT", "STRING_LIT", 
                      "LP", "RP", "LS", "RS", "COMMA", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQUAL", "ASSIGN", "NOT_SAME", "LESS_THAN", 
                      "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", "GREATER_THAN", 
                      "CONCAT", "SAME", "TRUE", "FALSE", "NUMBER", "BOOL", 
                      "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "LINE_COMMENT", 
                      "ID", "NEW_LINE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_vardecl_full = 4
    RULE_vardecl_not_full = 5
    RULE_vardecl_array = 6
    RULE_funcdecl = 7
    RULE_param_list = 8
    RULE_param_prime = 9
    RULE_paramdecl = 10
    RULE_stmt = 11
    RULE_assign_stmt = 12
    RULE_if_stmt = 13
    RULE_elif_stmt = 14
    RULE_else_stmt = 15
    RULE_for_stmt = 16
    RULE_break_stmt = 17
    RULE_continue_stmt = 18
    RULE_return_stmt = 19
    RULE_call_stmt = 20
    RULE_block_stmt = 21
    RULE_blocked_list = 22
    RULE_stmt_plus_vardecl = 23
    RULE_lhs = 24
    RULE_exp = 25
    RULE_expr_list = 26
    RULE_exprprime = 27
    RULE_exp0 = 28
    RULE_exp1 = 29
    RULE_exp2 = 30
    RULE_exp3 = 31
    RULE_exp4 = 32
    RULE_exp5 = 33
    RULE_exp6 = 34
    RULE_exp7 = 35
    RULE_func_call = 36
    RULE_constant = 37
    RULE_sub_exp = 38
    RULE_index_expr = 39
    RULE_index_operator = 40
    RULE_array_lit = 41
    RULE_non_empty_expr_list = 42
    RULE_array_type = 43
    RULE_dimensions = 44
    RULE_number_lits = 45
    RULE_atomic_types = 46
    RULE_newline_list = 47

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "vardecl_full", 
                   "vardecl_not_full", "vardecl_array", "funcdecl", "param_list", 
                   "param_prime", "paramdecl", "stmt", "assign_stmt", "if_stmt", 
                   "elif_stmt", "else_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "call_stmt", "block_stmt", "blocked_list", 
                   "stmt_plus_vardecl", "lhs", "exp", "expr_list", "exprprime", 
                   "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "func_call", "constant", "sub_exp", "index_expr", 
                   "index_operator", "array_lit", "non_empty_expr_list", 
                   "array_type", "dimensions", "number_lits", "atomic_types", 
                   "newline_list" ]

    EOF = Token.EOF
    BOOL_LIT=1
    NUMBER_LIT=2
    STRING_LIT=3
    LP=4
    RP=5
    LS=6
    RS=7
    COMMA=8
    ADD=9
    SUB=10
    MUL=11
    DIV=12
    MOD=13
    EQUAL=14
    ASSIGN=15
    NOT_SAME=16
    LESS_THAN=17
    LESS_THAN_EQUAL=18
    GREATER_THAN_EQUAL=19
    GREATER_THAN=20
    CONCAT=21
    SAME=22
    TRUE=23
    FALSE=24
    NUMBER=25
    BOOL=26
    STRING=27
    RETURN=28
    VAR=29
    DYNAMIC=30
    FUNC=31
    FOR=32
    UNTIL=33
    BY=34
    BREAK=35
    CONTINUE=36
    IF=37
    ELSE=38
    ELIF=39
    BEGIN=40
    END=41
    NOT=42
    AND=43
    OR=44
    LINE_COMMENT=45
    ID=46
    NEW_LINE=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 96
                self.match(ZCodeParser.NEW_LINE)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.decllist()
            self.state = 103
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




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.decl()
                self.state = 106
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.vardecl()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
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




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 115
                self.vardecl_not_full()
                pass

            elif la_ == 2:
                self.state = 116
                self.vardecl_full()
                pass

            elif la_ == 3:
                self.state = 117
                self.vardecl_array()
                pass


            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.match(ZCodeParser.NEW_LINE)
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
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




    def vardecl_full(self):

        localctx = ZCodeParser.Vardecl_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl_full)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ZCodeParser.VAR)
            self.state = 126
            self.match(ZCodeParser.ID)
            self.state = 127
            self.match(ZCodeParser.ASSIGN)
            self.state = 128
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




    def vardecl_not_full(self):

        localctx = ZCodeParser.Vardecl_not_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl_not_full)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27]:
                self.state = 130
                self.atomic_types()
                pass
            elif token in [30]:
                self.state = 131
                self.match(ZCodeParser.DYNAMIC)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 134
            self.match(ZCodeParser.ID)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 135
                self.match(ZCodeParser.ASSIGN)
                self.state = 136
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

        def atomic_types(self):
            return self.getTypedRuleContext(ZCodeParser.Atomic_typesContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_array




    def vardecl_array(self):

        localctx = ZCodeParser.Vardecl_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.atomic_types()
            self.state = 140
            self.match(ZCodeParser.ID)
            self.state = 141
            self.dimensions()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 142
                self.match(ZCodeParser.ASSIGN)
                self.state = 143
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




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.FUNC)
            self.state = 147
            self.match(ZCodeParser.ID)
            self.state = 148
            self.match(ZCodeParser.LP)
            self.state = 149
            self.param_list()
            self.state = 150
            self.match(ZCodeParser.RP)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.match(ZCodeParser.NEW_LINE) 
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.state = 157
                self.match(ZCodeParser.NEW_LINE)
                pass
            elif token in [40]:
                self.state = 158
                self.block_stmt()
                pass
            elif token in [28]:
                self.state = 159
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


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param_list)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.param_prime()
                pass
            elif token in [5]:
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




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_prime)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.paramdecl()
                self.state = 167
                self.match(ZCodeParser.COMMA)
                self.state = 168
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.paramdecl()
                pass


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




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.atomic_types()
            self.state = 174
            self.match(ZCodeParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 175
                self.dimensions()


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

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


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




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 178
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 179
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 180
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 181
                self.for_stmt()
                pass

            elif la_ == 5:
                self.state = 182
                self.block_stmt()
                pass

            elif la_ == 6:
                self.state = 183
                self.break_stmt()
                pass

            elif la_ == 7:
                self.state = 184
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.state = 185
                self.return_stmt()
                pass

            elif la_ == 9:
                self.state = 186
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




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.lhs()
            self.state = 190
            self.match(ZCodeParser.ASSIGN)
            self.state = 191
            self.exp()
            self.state = 193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                self.match(ZCodeParser.NEW_LINE)
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
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


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_stmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ZCodeParser.IF)
            self.state = 198
            self.sub_exp()
            self.state = 199
            self.newline_list()
            self.state = 200
            self.stmt()
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self.elif_stmt() 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 207
                self.else_stmt()


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




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ZCodeParser.ELIF)
            self.state = 211
            self.sub_exp()
            self.state = 212
            self.newline_list()
            self.state = 213
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEW_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEW_LINE)
            else:
                return self.getToken(ZCodeParser.NEW_LINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ZCodeParser.ELSE)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 216
                self.match(ZCodeParser.NEW_LINE)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
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




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ZCodeParser.FOR)
            self.state = 225
            self.match(ZCodeParser.ID)
            self.state = 226
            self.match(ZCodeParser.UNTIL)
            self.state = 227
            self.exp()
            self.state = 228
            self.match(ZCodeParser.BY)
            self.state = 229
            self.exp()
            self.state = 230
            self.newline_list()
            self.state = 231
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




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_break_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ZCodeParser.BREAK)
            self.state = 235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.match(ZCodeParser.NEW_LINE)
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
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




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_continue_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.CONTINUE)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240
                self.match(ZCodeParser.NEW_LINE)
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
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




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZCodeParser.RETURN)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 74766790689886) != 0):
                self.state = 246
                self.exp()


            self.state = 250 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 249
                self.match(ZCodeParser.NEW_LINE)
                self.state = 252 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_call_stmt




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ZCodeParser.ID)
            self.state = 255
            self.match(ZCodeParser.LP)
            self.state = 256
            self.expr_list()
            self.state = 257
            self.match(ZCodeParser.RP)
            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258
                self.match(ZCodeParser.NEW_LINE)
                self.state = 261 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
                    break

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




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ZCodeParser.BEGIN)
            self.state = 265 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 264
                self.match(ZCodeParser.NEW_LINE)
                self.state = 267 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
                    break

            self.state = 269
            self.blocked_list()
            self.state = 270
            self.match(ZCodeParser.END)
            self.state = 272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.match(ZCodeParser.NEW_LINE)
                self.state = 274 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==47):
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




    def blocked_list(self):

        localctx = ZCodeParser.Blocked_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blocked_list)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27, 28, 29, 30, 32, 35, 36, 37, 40, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.stmt_plus_vardecl()
                self.state = 277
                self.blocked_list()
                pass
            elif token in [41]:
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




    def stmt_plus_vardecl(self):

        localctx = ZCodeParser.Stmt_plus_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt_plus_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 282
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 283
                self.vardecl()
                pass


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




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.ID)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 287
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




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
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




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr_list)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 6, 10, 42, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.exprprime()
                pass
            elif token in [5]:
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




    def exprprime(self):

        localctx = ZCodeParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprprime)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.exp()
                self.state = 297
                self.match(ZCodeParser.COMMA)
                self.state = 298
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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




    def exp0(self):

        localctx = ZCodeParser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp0)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.exp1()
                self.state = 304
                self.match(ZCodeParser.CONCAT)
                self.state = 305
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
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




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.exp2(0)
                self.state = 311
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6242304) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 312
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 320
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(_la==43 or _la==44):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 322
                    self.exp3(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 333
                    self.exp4(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 344
                    self.exp5() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp5)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(ZCodeParser.NOT)
                self.state = 351
                self.exp5()
                pass
            elif token in [1, 2, 3, 4, 6, 10, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp6)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(ZCodeParser.SUB)
                self.state = 356
                self.exp6()
                pass
            elif token in [1, 2, 3, 4, 6, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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


        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def sub_exp(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_expContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp7)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
                self.func_call()
                self.state = 364
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 363
                    self.index_operator()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 366
                self.sub_exp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 367
                self.index_expr()
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




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(ZCodeParser.ID)
            self.state = 371
            self.match(ZCodeParser.LP)
            self.state = 372
            self.expr_list()
            self.state = 373
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

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_constant




    def constant(self):

        localctx = ZCodeParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_constant)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
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




    def sub_exp(self):

        localctx = ZCodeParser.Sub_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sub_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(ZCodeParser.LP)
            self.state = 382
            self.exp()
            self.state = 383
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

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(ZCodeParser.ID)
            self.state = 386
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




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.LS)
            self.state = 389
            self.exprprime()
            self.state = 390
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




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(ZCodeParser.LS)
            self.state = 393
            self.non_empty_expr_list()
            self.state = 394
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




    def non_empty_expr_list(self):

        localctx = ZCodeParser.Non_empty_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_non_empty_expr_list)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.exp()
                self.state = 397
                self.match(ZCodeParser.COMMA)
                self.state = 398
                self.non_empty_expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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




    def array_type(self):

        localctx = ZCodeParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.atomic_types()
            self.state = 404
            self.match(ZCodeParser.ID)
            self.state = 405
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




    def dimensions(self):

        localctx = ZCodeParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(ZCodeParser.LS)
            self.state = 408
            self.number_lits()
            self.state = 409
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

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def number_lits(self):
            return self.getTypedRuleContext(ZCodeParser.Number_litsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_lits




    def number_lits(self):

        localctx = ZCodeParser.Number_litsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_number_lits)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 412
                self.match(ZCodeParser.COMMA)
                self.state = 413
                self.number_lits()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.match(ZCodeParser.NUMBER_LIT)
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




    def atomic_types(self):

        localctx = ZCodeParser.Atomic_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_atomic_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
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




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_newline_list)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(ZCodeParser.NEW_LINE)
                self.state = 420
                self.newline_list()
                pass
            elif token in [25, 26, 27, 28, 29, 30, 32, 35, 36, 37, 40, 46]:
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.exp2_sempred
        self._predicates[31] = self.exp3_sempred
        self._predicates[32] = self.exp4_sempred
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
         




