# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/Assignment 232/assignment2-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,51,393,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,3,0,116,8,0,1,1,1,
        1,3,1,120,8,1,1,1,3,1,123,8,1,1,1,1,1,1,1,3,1,128,8,1,1,2,1,2,1,
        2,5,2,133,8,2,10,2,12,2,136,9,2,3,2,138,8,2,1,3,1,3,5,3,142,8,3,
        10,3,12,3,145,9,3,1,4,1,4,3,4,149,8,4,1,4,4,4,152,8,4,11,4,12,4,
        153,1,5,1,5,1,5,1,5,1,5,5,5,161,8,5,10,5,12,5,164,9,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,
        12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,
        18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,23,1,
        23,1,23,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,
        27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,
        36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,
        39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,
        43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,46,1,
        46,1,46,1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,
        49,5,49,340,8,49,10,49,12,49,343,9,49,1,49,1,49,1,50,1,50,5,50,349,
        8,50,10,50,12,50,352,9,50,1,51,3,51,355,8,51,1,51,1,51,1,51,1,52,
        4,52,361,8,52,11,52,12,52,362,1,52,1,52,1,53,1,53,1,53,5,53,370,
        8,53,10,53,12,53,373,9,53,1,53,3,53,376,8,53,1,53,1,53,1,54,1,54,
        1,54,5,54,383,8,54,10,54,12,54,386,9,54,1,54,1,54,1,54,1,55,1,55,
        1,55,0,0,56,1,1,3,2,5,0,7,0,9,0,11,3,13,0,15,0,17,4,19,5,21,6,23,
        7,25,8,27,9,29,10,31,11,33,12,35,13,37,14,39,15,41,16,43,17,45,18,
        47,19,49,20,51,21,53,22,55,23,57,24,59,25,61,26,63,27,65,28,67,29,
        69,30,71,31,73,32,75,33,77,34,79,35,81,36,83,37,85,38,87,39,89,40,
        91,41,93,42,95,43,97,44,99,45,101,46,103,47,105,48,107,49,109,50,
        111,51,1,0,12,1,0,49,57,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,
        45,3,0,10,10,34,34,92,92,7,0,39,39,92,92,98,98,102,102,110,110,114,
        114,116,116,2,0,10,10,13,13,3,0,65,90,95,95,97,122,4,0,48,57,65,
        90,95,95,97,122,3,0,8,9,12,12,32,32,4,0,10,10,34,34,39,39,92,92,
        2,1,10,10,13,13,407,0,1,1,0,0,0,0,3,1,0,0,0,0,11,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,
        0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,
        0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,1,115,1,0,0,0,3,127,1,0,0,0,
        5,137,1,0,0,0,7,139,1,0,0,0,9,146,1,0,0,0,11,155,1,0,0,0,13,168,
        1,0,0,0,15,171,1,0,0,0,17,174,1,0,0,0,19,176,1,0,0,0,21,178,1,0,
        0,0,23,180,1,0,0,0,25,182,1,0,0,0,27,184,1,0,0,0,29,186,1,0,0,0,
        31,188,1,0,0,0,33,190,1,0,0,0,35,192,1,0,0,0,37,194,1,0,0,0,39,196,
        1,0,0,0,41,199,1,0,0,0,43,202,1,0,0,0,45,204,1,0,0,0,47,207,1,0,
        0,0,49,210,1,0,0,0,51,212,1,0,0,0,53,216,1,0,0,0,55,219,1,0,0,0,
        57,224,1,0,0,0,59,230,1,0,0,0,61,237,1,0,0,0,63,242,1,0,0,0,65,249,
        1,0,0,0,67,256,1,0,0,0,69,260,1,0,0,0,71,268,1,0,0,0,73,273,1,0,
        0,0,75,277,1,0,0,0,77,283,1,0,0,0,79,286,1,0,0,0,81,292,1,0,0,0,
        83,301,1,0,0,0,85,304,1,0,0,0,87,309,1,0,0,0,89,314,1,0,0,0,91,320,
        1,0,0,0,93,324,1,0,0,0,95,328,1,0,0,0,97,332,1,0,0,0,99,335,1,0,
        0,0,101,346,1,0,0,0,103,354,1,0,0,0,105,360,1,0,0,0,107,366,1,0,
        0,0,109,379,1,0,0,0,111,390,1,0,0,0,113,116,3,55,27,0,114,116,3,
        57,28,0,115,113,1,0,0,0,115,114,1,0,0,0,116,2,1,0,0,0,117,119,3,
        5,2,0,118,120,3,7,3,0,119,118,1,0,0,0,119,120,1,0,0,0,120,122,1,
        0,0,0,121,123,3,9,4,0,122,121,1,0,0,0,122,123,1,0,0,0,123,128,1,
        0,0,0,124,125,3,5,2,0,125,126,3,9,4,0,126,128,1,0,0,0,127,117,1,
        0,0,0,127,124,1,0,0,0,128,4,1,0,0,0,129,138,5,48,0,0,130,134,7,0,
        0,0,131,133,7,1,0,0,132,131,1,0,0,0,133,136,1,0,0,0,134,132,1,0,
        0,0,134,135,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,137,129,1,0,
        0,0,137,130,1,0,0,0,138,6,1,0,0,0,139,143,5,46,0,0,140,142,7,1,0,
        0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,
        0,144,8,1,0,0,0,145,143,1,0,0,0,146,148,7,2,0,0,147,149,7,3,0,0,
        148,147,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,152,7,1,0,0,
        151,150,1,0,0,0,152,153,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,
        154,10,1,0,0,0,155,162,5,34,0,0,156,161,3,13,6,0,157,161,8,4,0,0,
        158,159,5,39,0,0,159,161,5,34,0,0,160,156,1,0,0,0,160,157,1,0,0,
        0,160,158,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,
        0,163,165,1,0,0,0,164,162,1,0,0,0,165,166,5,34,0,0,166,167,6,5,0,
        0,167,12,1,0,0,0,168,169,5,92,0,0,169,170,7,5,0,0,170,14,1,0,0,0,
        171,172,5,92,0,0,172,173,8,5,0,0,173,16,1,0,0,0,174,175,5,40,0,0,
        175,18,1,0,0,0,176,177,5,41,0,0,177,20,1,0,0,0,178,179,5,91,0,0,
        179,22,1,0,0,0,180,181,5,93,0,0,181,24,1,0,0,0,182,183,5,44,0,0,
        183,26,1,0,0,0,184,185,5,43,0,0,185,28,1,0,0,0,186,187,5,45,0,0,
        187,30,1,0,0,0,188,189,5,42,0,0,189,32,1,0,0,0,190,191,5,47,0,0,
        191,34,1,0,0,0,192,193,5,37,0,0,193,36,1,0,0,0,194,195,5,61,0,0,
        195,38,1,0,0,0,196,197,5,60,0,0,197,198,5,45,0,0,198,40,1,0,0,0,
        199,200,5,33,0,0,200,201,5,61,0,0,201,42,1,0,0,0,202,203,5,60,0,
        0,203,44,1,0,0,0,204,205,5,60,0,0,205,206,5,61,0,0,206,46,1,0,0,
        0,207,208,5,62,0,0,208,209,5,61,0,0,209,48,1,0,0,0,210,211,5,62,
        0,0,211,50,1,0,0,0,212,213,5,46,0,0,213,214,5,46,0,0,214,215,5,46,
        0,0,215,52,1,0,0,0,216,217,5,61,0,0,217,218,5,61,0,0,218,54,1,0,
        0,0,219,220,5,116,0,0,220,221,5,114,0,0,221,222,5,117,0,0,222,223,
        5,101,0,0,223,56,1,0,0,0,224,225,5,102,0,0,225,226,5,97,0,0,226,
        227,5,108,0,0,227,228,5,115,0,0,228,229,5,101,0,0,229,58,1,0,0,0,
        230,231,5,110,0,0,231,232,5,117,0,0,232,233,5,109,0,0,233,234,5,
        98,0,0,234,235,5,101,0,0,235,236,5,114,0,0,236,60,1,0,0,0,237,238,
        5,98,0,0,238,239,5,111,0,0,239,240,5,111,0,0,240,241,5,108,0,0,241,
        62,1,0,0,0,242,243,5,115,0,0,243,244,5,116,0,0,244,245,5,114,0,0,
        245,246,5,105,0,0,246,247,5,110,0,0,247,248,5,103,0,0,248,64,1,0,
        0,0,249,250,5,114,0,0,250,251,5,101,0,0,251,252,5,116,0,0,252,253,
        5,117,0,0,253,254,5,114,0,0,254,255,5,110,0,0,255,66,1,0,0,0,256,
        257,5,118,0,0,257,258,5,97,0,0,258,259,5,114,0,0,259,68,1,0,0,0,
        260,261,5,100,0,0,261,262,5,121,0,0,262,263,5,110,0,0,263,264,5,
        97,0,0,264,265,5,109,0,0,265,266,5,105,0,0,266,267,5,99,0,0,267,
        70,1,0,0,0,268,269,5,102,0,0,269,270,5,117,0,0,270,271,5,110,0,0,
        271,272,5,99,0,0,272,72,1,0,0,0,273,274,5,102,0,0,274,275,5,111,
        0,0,275,276,5,114,0,0,276,74,1,0,0,0,277,278,5,117,0,0,278,279,5,
        110,0,0,279,280,5,116,0,0,280,281,5,105,0,0,281,282,5,108,0,0,282,
        76,1,0,0,0,283,284,5,98,0,0,284,285,5,121,0,0,285,78,1,0,0,0,286,
        287,5,98,0,0,287,288,5,114,0,0,288,289,5,101,0,0,289,290,5,97,0,
        0,290,291,5,107,0,0,291,80,1,0,0,0,292,293,5,99,0,0,293,294,5,111,
        0,0,294,295,5,110,0,0,295,296,5,116,0,0,296,297,5,105,0,0,297,298,
        5,110,0,0,298,299,5,117,0,0,299,300,5,101,0,0,300,82,1,0,0,0,301,
        302,5,105,0,0,302,303,5,102,0,0,303,84,1,0,0,0,304,305,5,101,0,0,
        305,306,5,108,0,0,306,307,5,115,0,0,307,308,5,101,0,0,308,86,1,0,
        0,0,309,310,5,101,0,0,310,311,5,108,0,0,311,312,5,105,0,0,312,313,
        5,102,0,0,313,88,1,0,0,0,314,315,5,98,0,0,315,316,5,101,0,0,316,
        317,5,103,0,0,317,318,5,105,0,0,318,319,5,110,0,0,319,90,1,0,0,0,
        320,321,5,101,0,0,321,322,5,110,0,0,322,323,5,100,0,0,323,92,1,0,
        0,0,324,325,5,110,0,0,325,326,5,111,0,0,326,327,5,116,0,0,327,94,
        1,0,0,0,328,329,5,97,0,0,329,330,5,110,0,0,330,331,5,100,0,0,331,
        96,1,0,0,0,332,333,5,111,0,0,333,334,5,114,0,0,334,98,1,0,0,0,335,
        336,5,35,0,0,336,337,5,35,0,0,337,341,1,0,0,0,338,340,8,6,0,0,339,
        338,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,342,
        344,1,0,0,0,343,341,1,0,0,0,344,345,6,49,1,0,345,100,1,0,0,0,346,
        350,7,7,0,0,347,349,7,8,0,0,348,347,1,0,0,0,349,352,1,0,0,0,350,
        348,1,0,0,0,350,351,1,0,0,0,351,102,1,0,0,0,352,350,1,0,0,0,353,
        355,5,13,0,0,354,353,1,0,0,0,354,355,1,0,0,0,355,356,1,0,0,0,356,
        357,5,10,0,0,357,358,6,51,2,0,358,104,1,0,0,0,359,361,7,9,0,0,360,
        359,1,0,0,0,361,362,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,
        364,1,0,0,0,364,365,6,52,1,0,365,106,1,0,0,0,366,371,5,34,0,0,367,
        370,8,10,0,0,368,370,3,13,6,0,369,367,1,0,0,0,369,368,1,0,0,0,370,
        373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,375,1,0,0,0,373,
        371,1,0,0,0,374,376,7,11,0,0,375,374,1,0,0,0,376,377,1,0,0,0,377,
        378,6,53,3,0,378,108,1,0,0,0,379,384,5,34,0,0,380,383,8,4,0,0,381,
        383,3,13,6,0,382,380,1,0,0,0,382,381,1,0,0,0,383,386,1,0,0,0,384,
        382,1,0,0,0,384,385,1,0,0,0,385,387,1,0,0,0,386,384,1,0,0,0,387,
        388,3,15,7,0,388,389,6,54,4,0,389,110,1,0,0,0,390,391,9,0,0,0,391,
        392,6,55,5,0,392,112,1,0,0,0,21,0,115,119,122,127,134,137,143,148,
        153,160,162,341,350,354,362,369,371,375,382,384,6,1,5,0,6,0,0,1,
        51,1,1,53,2,1,54,3,1,55,4
    ]

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
        self.checkVersion("4.13.1")
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

     


