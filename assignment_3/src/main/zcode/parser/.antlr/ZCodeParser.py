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
        4,1,49,398,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,101,8,1,1,2,1,2,3,2,105,8,2,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,118,8,4,1,4,1,4,1,5,
        1,5,3,5,124,8,5,1,6,1,6,3,6,128,8,6,1,7,1,7,1,7,1,7,3,7,134,8,7,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,143,8,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,157,8,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,3,11,176,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,194,8,11,1,12,1,12,1,12,
        3,12,199,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,3,14,212,8,14,1,15,1,15,3,15,216,8,15,1,16,1,16,1,16,1,16,1,
        16,3,16,223,8,16,1,17,1,17,1,17,3,17,228,8,17,1,18,1,18,1,18,3,18,
        233,8,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,244,8,
        20,1,21,1,21,1,21,3,21,249,8,21,1,21,1,21,3,21,253,8,21,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,266,8,24,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,3,26,277,8,26,1,27,1,27,
        1,27,1,27,1,27,3,27,284,8,27,1,28,1,28,1,28,1,28,1,28,1,28,5,28,
        292,8,28,10,28,12,28,295,9,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,
        303,8,29,10,29,12,29,306,9,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,
        314,8,30,10,30,12,30,317,9,30,1,31,1,31,1,31,3,31,322,8,31,1,32,
        1,32,1,32,3,32,327,8,32,1,33,1,33,3,33,331,8,33,1,34,1,34,1,34,1,
        34,1,34,3,34,338,8,34,1,35,1,35,1,35,1,35,1,35,1,35,3,35,346,8,35,
        1,36,1,36,3,36,350,8,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,1,38,1,39,1,39,1,39,1,39,1,39,3,39,367,8,39,1,40,1,40,1,40,
        1,40,1,40,1,41,1,41,3,41,376,8,41,1,42,1,42,1,42,1,42,1,42,3,42,
        383,8,42,1,43,1,43,3,43,387,8,43,1,44,1,44,3,44,391,8,44,1,45,1,
        45,1,45,3,45,396,8,45,1,45,0,3,56,58,60,46,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,5,1,0,4,6,2,0,34,
        35,37,41,1,0,22,23,1,0,29,30,1,0,31,33,402,0,92,1,0,0,0,2,100,1,
        0,0,0,4,104,1,0,0,0,6,106,1,0,0,0,8,109,1,0,0,0,10,123,1,0,0,0,12,
        127,1,0,0,0,14,133,1,0,0,0,16,135,1,0,0,0,18,142,1,0,0,0,20,144,
        1,0,0,0,22,193,1,0,0,0,24,198,1,0,0,0,26,200,1,0,0,0,28,205,1,0,
        0,0,30,215,1,0,0,0,32,222,1,0,0,0,34,224,1,0,0,0,36,232,1,0,0,0,
        38,234,1,0,0,0,40,239,1,0,0,0,42,245,1,0,0,0,44,254,1,0,0,0,46,256,
        1,0,0,0,48,265,1,0,0,0,50,267,1,0,0,0,52,276,1,0,0,0,54,283,1,0,
        0,0,56,285,1,0,0,0,58,296,1,0,0,0,60,307,1,0,0,0,62,321,1,0,0,0,
        64,326,1,0,0,0,66,330,1,0,0,0,68,337,1,0,0,0,70,345,1,0,0,0,72,349,
        1,0,0,0,74,351,1,0,0,0,76,356,1,0,0,0,78,366,1,0,0,0,80,368,1,0,
        0,0,82,375,1,0,0,0,84,382,1,0,0,0,86,386,1,0,0,0,88,390,1,0,0,0,
        90,395,1,0,0,0,92,93,3,88,44,0,93,94,3,2,1,0,94,95,5,0,0,1,95,1,
        1,0,0,0,96,97,3,4,2,0,97,98,3,2,1,0,98,101,1,0,0,0,99,101,3,4,2,
        0,100,96,1,0,0,0,100,99,1,0,0,0,101,3,1,0,0,0,102,105,3,8,4,0,103,
        105,3,6,3,0,104,102,1,0,0,0,104,103,1,0,0,0,105,5,1,0,0,0,106,107,
        3,36,18,0,107,108,3,90,45,0,108,7,1,0,0,0,109,110,5,10,0,0,110,111,
        5,46,0,0,111,112,5,24,0,0,112,113,3,30,15,0,113,117,5,25,0,0,114,
        115,3,88,44,0,115,116,3,10,5,0,116,118,1,0,0,0,117,114,1,0,0,0,117,
        118,1,0,0,0,118,119,1,0,0,0,119,120,3,90,45,0,120,9,1,0,0,0,121,
        124,3,26,13,0,122,124,3,28,14,0,123,121,1,0,0,0,123,122,1,0,0,0,
        124,11,1,0,0,0,125,128,3,14,7,0,126,128,1,0,0,0,127,125,1,0,0,0,
        127,126,1,0,0,0,128,13,1,0,0,0,129,130,3,16,8,0,130,131,3,14,7,0,
        131,134,1,0,0,0,132,134,3,16,8,0,133,129,1,0,0,0,133,132,1,0,0,0,
        134,15,1,0,0,0,135,136,3,22,11,0,136,137,3,90,45,0,137,17,1,0,0,
        0,138,139,3,20,10,0,139,140,3,18,9,0,140,143,1,0,0,0,141,143,1,0,
        0,0,142,138,1,0,0,0,142,141,1,0,0,0,143,19,1,0,0,0,144,145,3,90,
        45,0,145,146,5,18,0,0,146,147,5,24,0,0,147,148,3,52,26,0,148,149,
        5,25,0,0,149,150,1,0,0,0,150,151,3,88,44,0,151,152,3,24,12,0,152,
        21,1,0,0,0,153,194,3,36,18,0,154,157,3,74,37,0,155,157,5,46,0,0,
        156,154,1,0,0,0,156,155,1,0,0,0,157,158,1,0,0,0,158,159,5,36,0,0,
        159,194,3,52,26,0,160,194,3,26,13,0,161,194,3,28,14,0,162,163,5,
        16,0,0,163,164,5,24,0,0,164,165,3,52,26,0,165,166,5,25,0,0,166,167,
        1,0,0,0,167,168,3,88,44,0,168,169,3,24,12,0,169,175,3,18,9,0,170,
        171,3,90,45,0,171,172,5,17,0,0,172,173,3,88,44,0,173,174,3,24,12,
        0,174,176,1,0,0,0,175,170,1,0,0,0,175,176,1,0,0,0,176,194,1,0,0,
        0,177,178,5,11,0,0,178,179,5,46,0,0,179,180,5,12,0,0,180,181,3,52,
        26,0,181,182,5,13,0,0,182,183,3,52,26,0,183,184,3,88,44,0,184,185,
        3,24,12,0,185,194,1,0,0,0,186,194,5,14,0,0,187,194,5,15,0,0,188,
        189,5,46,0,0,189,190,5,24,0,0,190,191,3,82,41,0,191,192,5,25,0,0,
        192,194,1,0,0,0,193,153,1,0,0,0,193,156,1,0,0,0,193,160,1,0,0,0,
        193,161,1,0,0,0,193,162,1,0,0,0,193,177,1,0,0,0,193,186,1,0,0,0,
        193,187,1,0,0,0,193,188,1,0,0,0,194,23,1,0,0,0,195,199,3,26,13,0,
        196,199,3,28,14,0,197,199,3,22,11,0,198,195,1,0,0,0,198,196,1,0,
        0,0,198,197,1,0,0,0,199,25,1,0,0,0,200,201,5,19,0,0,201,202,3,90,
        45,0,202,203,3,12,6,0,203,204,5,20,0,0,204,27,1,0,0,0,205,211,5,
        7,0,0,206,207,5,24,0,0,207,208,3,52,26,0,208,209,5,25,0,0,209,212,
        1,0,0,0,210,212,3,52,26,0,211,206,1,0,0,0,211,210,1,0,0,0,211,212,
        1,0,0,0,212,29,1,0,0,0,213,216,3,32,16,0,214,216,1,0,0,0,215,213,
        1,0,0,0,215,214,1,0,0,0,216,31,1,0,0,0,217,218,3,34,17,0,218,219,
        5,28,0,0,219,220,3,32,16,0,220,223,1,0,0,0,221,223,3,34,17,0,222,
        217,1,0,0,0,222,221,1,0,0,0,223,33,1,0,0,0,224,227,3,44,22,0,225,
        228,5,46,0,0,226,228,3,46,23,0,227,225,1,0,0,0,227,226,1,0,0,0,228,
        35,1,0,0,0,229,233,3,38,19,0,230,233,3,40,20,0,231,233,3,42,21,0,
        232,229,1,0,0,0,232,230,1,0,0,0,232,231,1,0,0,0,233,37,1,0,0,0,234,
        235,5,8,0,0,235,236,5,46,0,0,236,237,5,36,0,0,237,238,3,52,26,0,
        238,39,1,0,0,0,239,240,5,9,0,0,240,243,5,46,0,0,241,242,5,36,0,0,
        242,244,3,52,26,0,243,241,1,0,0,0,243,244,1,0,0,0,244,41,1,0,0,0,
        245,248,3,44,22,0,246,249,3,46,23,0,247,249,5,46,0,0,248,246,1,0,
        0,0,248,247,1,0,0,0,249,252,1,0,0,0,250,251,5,36,0,0,251,253,3,52,
        26,0,252,250,1,0,0,0,252,253,1,0,0,0,253,43,1,0,0,0,254,255,7,0,
        0,0,255,45,1,0,0,0,256,257,5,46,0,0,257,258,5,26,0,0,258,259,3,48,
        24,0,259,260,5,27,0,0,260,47,1,0,0,0,261,262,5,43,0,0,262,263,5,
        28,0,0,263,266,3,48,24,0,264,266,5,43,0,0,265,261,1,0,0,0,265,264,
        1,0,0,0,266,49,1,0,0,0,267,268,5,26,0,0,268,269,3,78,39,0,269,270,
        5,27,0,0,270,51,1,0,0,0,271,272,3,54,27,0,272,273,5,42,0,0,273,274,
        3,54,27,0,274,277,1,0,0,0,275,277,3,54,27,0,276,271,1,0,0,0,276,
        275,1,0,0,0,277,53,1,0,0,0,278,279,3,56,28,0,279,280,7,1,0,0,280,
        281,3,56,28,0,281,284,1,0,0,0,282,284,3,56,28,0,283,278,1,0,0,0,
        283,282,1,0,0,0,284,55,1,0,0,0,285,286,6,28,-1,0,286,287,3,58,29,
        0,287,293,1,0,0,0,288,289,10,2,0,0,289,290,7,2,0,0,290,292,3,58,
        29,0,291,288,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,
        0,0,294,57,1,0,0,0,295,293,1,0,0,0,296,297,6,29,-1,0,297,298,3,60,
        30,0,298,304,1,0,0,0,299,300,10,2,0,0,300,301,7,3,0,0,301,303,3,
        60,30,0,302,299,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,59,1,0,0,0,306,304,1,0,0,0,307,308,6,30,-1,0,308,309,
        3,62,31,0,309,315,1,0,0,0,310,311,10,2,0,0,311,312,7,4,0,0,312,314,
        3,62,31,0,313,310,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,
        1,0,0,0,316,61,1,0,0,0,317,315,1,0,0,0,318,319,5,21,0,0,319,322,
        3,62,31,0,320,322,3,64,32,0,321,318,1,0,0,0,321,320,1,0,0,0,322,
        63,1,0,0,0,323,324,5,30,0,0,324,327,3,64,32,0,325,327,3,66,33,0,
        326,323,1,0,0,0,326,325,1,0,0,0,327,65,1,0,0,0,328,331,3,72,36,0,
        329,331,3,68,34,0,330,328,1,0,0,0,330,329,1,0,0,0,331,67,1,0,0,0,
        332,333,5,24,0,0,333,334,3,52,26,0,334,335,5,25,0,0,335,338,1,0,
        0,0,336,338,3,70,35,0,337,332,1,0,0,0,337,336,1,0,0,0,338,69,1,0,
        0,0,339,346,3,80,40,0,340,346,5,46,0,0,341,346,5,43,0,0,342,346,
        5,44,0,0,343,346,5,45,0,0,344,346,3,50,25,0,345,339,1,0,0,0,345,
        340,1,0,0,0,345,341,1,0,0,0,345,342,1,0,0,0,345,343,1,0,0,0,345,
        344,1,0,0,0,346,71,1,0,0,0,347,350,3,74,37,0,348,350,3,76,38,0,349,
        347,1,0,0,0,349,348,1,0,0,0,350,73,1,0,0,0,351,352,5,46,0,0,352,
        353,5,26,0,0,353,354,3,78,39,0,354,355,5,27,0,0,355,75,1,0,0,0,356,
        357,3,80,40,0,357,358,5,26,0,0,358,359,3,78,39,0,359,360,5,27,0,
        0,360,77,1,0,0,0,361,367,3,52,26,0,362,363,3,52,26,0,363,364,5,28,
        0,0,364,365,3,78,39,0,365,367,1,0,0,0,366,361,1,0,0,0,366,362,1,
        0,0,0,367,79,1,0,0,0,368,369,5,46,0,0,369,370,5,24,0,0,370,371,3,
        82,41,0,371,372,5,25,0,0,372,81,1,0,0,0,373,376,3,84,42,0,374,376,
        1,0,0,0,375,373,1,0,0,0,375,374,1,0,0,0,376,83,1,0,0,0,377,378,3,
        86,43,0,378,379,5,28,0,0,379,380,3,84,42,0,380,383,1,0,0,0,381,383,
        3,86,43,0,382,377,1,0,0,0,382,381,1,0,0,0,383,85,1,0,0,0,384,387,
        5,46,0,0,385,387,3,52,26,0,386,384,1,0,0,0,386,385,1,0,0,0,387,87,
        1,0,0,0,388,391,3,90,45,0,389,391,1,0,0,0,390,388,1,0,0,0,390,389,
        1,0,0,0,391,89,1,0,0,0,392,393,5,3,0,0,393,396,3,90,45,0,394,396,
        5,3,0,0,395,392,1,0,0,0,395,394,1,0,0,0,396,91,1,0,0,0,37,100,104,
        117,123,127,133,142,156,175,193,198,211,215,222,227,232,243,248,
        252,265,276,283,293,304,315,321,326,330,337,345,349,366,375,382,
        386,390,395
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'not'", "'and'", "'or'", "'('", 
                     "')'", "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'='", "'=='", "'<-'", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'...'" ]

    symbolicNames = [ "<INVALID>", "CMT", "WS", "NEWLINE", "NUMBER", "BOOL", 
                      "STRING_DEF", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONT", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "LB", 
                      "RB", "LBRACE", "RBRACE", "COMMA", "ADD", "MINUS", 
                      "MUL", "DIV", "MOD", "EQUAL_NUM", "EQUAL_STR", "ASS", 
                      "DIF", "SM", "SMOE", "BG", "BGOE", "CON", "NUMBER_LIT", 
                      "BOOL_LIT", "STR_LIT", "IDENTIFIER", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_var_decl_full = 3
    RULE_func_decl = 4
    RULE_function_body = 5
    RULE_statement_list = 6
    RULE_nonnull_statement = 7
    RULE_statement_full = 8
    RULE_elif_list = 9
    RULE_elif_stmt = 10
    RULE_stmt = 11
    RULE_all_stmt = 12
    RULE_block_stmt = 13
    RULE_return_stmt = 14
    RULE_parameter_list = 15
    RULE_nonnull_parameter = 16
    RULE_parameter = 17
    RULE_var_decl = 18
    RULE_varkey_decl = 19
    RULE_dykey_decl = 20
    RULE_prikey_decl = 21
    RULE_pri_type = 22
    RULE_arr_type = 23
    RULE_numlit_list = 24
    RULE_arr_value = 25
    RULE_expression1 = 26
    RULE_expression2 = 27
    RULE_expression3 = 28
    RULE_expression4 = 29
    RULE_expression5 = 30
    RULE_expression6 = 31
    RULE_expression7 = 32
    RULE_expression8 = 33
    RULE_expression9 = 34
    RULE_expression10 = 35
    RULE_acc_arr = 36
    RULE_arr_ele = 37
    RULE_arr_expr = 38
    RULE_index_operators = 39
    RULE_function_call = 40
    RULE_argurment_list = 41
    RULE_nonnull_argurment = 42
    RULE_argurment = 43
    RULE_newline_list = 44
    RULE_nonnull_newline = 45

    ruleNames =  [ "program", "decl_list", "decl", "var_decl_full", "func_decl", 
                   "function_body", "statement_list", "nonnull_statement", 
                   "statement_full", "elif_list", "elif_stmt", "stmt", "all_stmt", 
                   "block_stmt", "return_stmt", "parameter_list", "nonnull_parameter", 
                   "parameter", "var_decl", "varkey_decl", "dykey_decl", 
                   "prikey_decl", "pri_type", "arr_type", "numlit_list", 
                   "arr_value", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "expression8", "expression9", "expression10", "acc_arr", 
                   "arr_ele", "arr_expr", "index_operators", "function_call", 
                   "argurment_list", "nonnull_argurment", "argurment", "newline_list", 
                   "nonnull_newline" ]

    EOF = Token.EOF
    CMT=1
    WS=2
    NEWLINE=3
    NUMBER=4
    BOOL=5
    STRING_DEF=6
    RETURN=7
    VAR=8
    DYNAMIC=9
    FUNC=10
    FOR=11
    UNTIL=12
    BY=13
    BREAK=14
    CONT=15
    IF=16
    ELSE=17
    ELIF=18
    BEGIN=19
    END=20
    NOT=21
    AND=22
    OR=23
    LB=24
    RB=25
    LBRACE=26
    RBRACE=27
    COMMA=28
    ADD=29
    MINUS=30
    MUL=31
    DIV=32
    MOD=33
    EQUAL_NUM=34
    EQUAL_STR=35
    ASS=36
    DIF=37
    SM=38
    SMOE=39
    BG=40
    BGOE=41
    CON=42
    NUMBER_LIT=43
    BOOL_LIT=44
    STR_LIT=45
    IDENTIFIER=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    ERROR_CHAR=49

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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.newline_list()
            self.state = 93
            self.decl_list()
            self.state = 94
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.decl()
                self.state = 97
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
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

        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def var_decl_full(self):
            return self.getTypedRuleContext(ZCodeParser.Var_decl_fullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.func_decl()
                pass
            elif token in [4, 5, 6, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.var_decl_full()
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


    class Var_decl_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl_full




    def var_decl_full(self):

        localctx = ZCodeParser.Var_decl_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl_full)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.var_decl()
            self.state = 107
            self.nonnull_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZCodeParser.FUNC)
            self.state = 110
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 111
            self.match(ZCodeParser.LB)
            self.state = 112
            self.parameter_list()
            self.state = 113
            self.match(ZCodeParser.RB)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 114
                self.newline_list()
                self.state = 115
                self.function_body()


            self.state = 119
            self.nonnull_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_body)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.block_stmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
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


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonnull_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement_list)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 19, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.nonnull_statement()
                pass
            elif token in [20]:
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


    class Nonnull_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_full(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_fullContext,0)


        def nonnull_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nonnull_statement




    def nonnull_statement(self):

        localctx = ZCodeParser.Nonnull_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nonnull_statement)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.statement_full()
                self.state = 130
                self.nonnull_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.statement_full()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_full




    def statement_full(self):

        localctx = ZCodeParser.Statement_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement_full)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.stmt()
            self.state = 136
            self.nonnull_newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elif_list)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.elif_stmt()
                self.state = 139
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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

        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def all_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.All_stmtContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.nonnull_newline()
            self.state = 145
            self.match(ZCodeParser.ELIF)

            self.state = 146
            self.match(ZCodeParser.LB)
            self.state = 147
            self.expression1()
            self.state = 148
            self.match(ZCodeParser.RB)
            self.state = 150
            self.newline_list()
            self.state = 151
            self.all_stmt()
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

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def ASS(self):
            return self.getToken(ZCodeParser.ASS, 0)

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def arr_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_eleContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def all_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.All_stmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.All_stmtContext,i)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def CONT(self):
            return self.getToken(ZCodeParser.CONT, 0)

        def argurment_list(self):
            return self.getTypedRuleContext(ZCodeParser.Argurment_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 154
                    self.arr_ele()
                    pass

                elif la_ == 2:
                    self.state = 155
                    self.match(ZCodeParser.IDENTIFIER)
                    pass


                self.state = 158
                self.match(ZCodeParser.ASS)
                self.state = 159
                self.expression1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.match(ZCodeParser.IF)

                self.state = 163
                self.match(ZCodeParser.LB)
                self.state = 164
                self.expression1()
                self.state = 165
                self.match(ZCodeParser.RB)
                self.state = 167
                self.newline_list()
                self.state = 168
                self.all_stmt()
                self.state = 169
                self.elif_list()
                self.state = 175
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.nonnull_newline()
                    self.state = 171
                    self.match(ZCodeParser.ELSE)
                    self.state = 172
                    self.newline_list()
                    self.state = 173
                    self.all_stmt()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                self.match(ZCodeParser.FOR)
                self.state = 178
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 179
                self.match(ZCodeParser.UNTIL)
                self.state = 180
                self.expression1()
                self.state = 181
                self.match(ZCodeParser.BY)
                self.state = 182
                self.expression1()
                self.state = 183
                self.newline_list()
                self.state = 184
                self.all_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 186
                self.match(ZCodeParser.BREAK)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 187
                self.match(ZCodeParser.CONT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 188
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 189
                self.match(ZCodeParser.LB)
                self.state = 190
                self.argurment_list()
                self.state = 191
                self.match(ZCodeParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_all_stmt




    def all_stmt(self):

        localctx = ZCodeParser.All_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_all_stmt)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.return_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.stmt()
                pass


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

        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.BEGIN)
            self.state = 201
            self.nonnull_newline()
            self.state = 202
            self.statement_list()
            self.state = 203
            self.match(ZCodeParser.END)
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

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZCodeParser.RETURN)
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 206
                self.match(ZCodeParser.LB)
                self.state = 207
                self.expression1()
                self.state = 208
                self.match(ZCodeParser.RB)

            elif la_ == 2:
                self.state = 210
                self.expression1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonnull_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.nonnull_parameter()
                pass
            elif token in [25]:
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


    class Nonnull_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def nonnull_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nonnull_parameter




    def nonnull_parameter(self):

        localctx = ZCodeParser.Nonnull_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nonnull_parameter)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.parameter()
                self.state = 218
                self.match(ZCodeParser.COMMA)
                self.state = 219
                self.nonnull_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pri_type(self):
            return self.getTypedRuleContext(ZCodeParser.Pri_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arr_type(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.pri_type()
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 225
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 226
                self.arr_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varkey_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Varkey_declContext,0)


        def dykey_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Dykey_declContext,0)


        def prikey_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Prikey_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_decl)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.varkey_decl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.dykey_decl()
                pass
            elif token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.prikey_decl()
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


    class Varkey_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASS(self):
            return self.getToken(ZCodeParser.ASS, 0)

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varkey_decl




    def varkey_decl(self):

        localctx = ZCodeParser.Varkey_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_varkey_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ZCodeParser.VAR)
            self.state = 235
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 236
            self.match(ZCodeParser.ASS)
            self.state = 237
            self.expression1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dykey_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASS(self):
            return self.getToken(ZCodeParser.ASS, 0)

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dykey_decl




    def dykey_decl(self):

        localctx = ZCodeParser.Dykey_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dykey_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.DYNAMIC)
            self.state = 240
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 241
                self.match(ZCodeParser.ASS)
                self.state = 242
                self.expression1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prikey_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pri_type(self):
            return self.getTypedRuleContext(ZCodeParser.Pri_typeContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASS(self):
            return self.getToken(ZCodeParser.ASS, 0)

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prikey_decl




    def prikey_decl(self):

        localctx = ZCodeParser.Prikey_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_prikey_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.pri_type()
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 246
                self.arr_type()
                pass

            elif la_ == 2:
                self.state = 247
                self.match(ZCodeParser.IDENTIFIER)
                pass


            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 250
                self.match(ZCodeParser.ASS)
                self.state = 251
                self.expression1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pri_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING_DEF(self):
            return self.getToken(ZCodeParser.STRING_DEF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_pri_type




    def pri_type(self):

        localctx = ZCodeParser.Pri_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pri_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
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


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(ZCodeParser.LBRACE, 0)

        def numlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numlit_listContext,0)


        def RBRACE(self):
            return self.getToken(ZCodeParser.RBRACE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_type




    def arr_type(self):

        localctx = ZCodeParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 257
            self.match(ZCodeParser.LBRACE)
            self.state = 258
            self.numlit_list()
            self.state = 259
            self.match(ZCodeParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numlit_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numlit_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlit_list




    def numlit_list(self):

        localctx = ZCodeParser.Numlit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_numlit_list)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 262
                self.match(ZCodeParser.COMMA)
                self.state = 263
                self.numlit_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ZCodeParser.LBRACE, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RBRACE(self):
            return self.getToken(ZCodeParser.RBRACE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_value




    def arr_value(self):

        localctx = ZCodeParser.Arr_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arr_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(ZCodeParser.LBRACE)
            self.state = 268
            self.index_operators()
            self.state = 269
            self.match(ZCodeParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def CON(self):
            return self.getToken(ZCodeParser.CON, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression1)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.expression2()
                self.state = 272
                self.match(ZCodeParser.CON)
                self.state = 273
                self.expression2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expression2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression3Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression3Context,i)


        def DIF(self):
            return self.getToken(ZCodeParser.DIF, 0)

        def BGOE(self):
            return self.getToken(ZCodeParser.BGOE, 0)

        def SMOE(self):
            return self.getToken(ZCodeParser.SMOE, 0)

        def BG(self):
            return self.getToken(ZCodeParser.BG, 0)

        def SM(self):
            return self.getToken(ZCodeParser.SM, 0)

        def EQUAL_NUM(self):
            return self.getToken(ZCodeParser.EQUAL_NUM, 0)

        def EQUAL_STR(self):
            return self.getToken(ZCodeParser.EQUAL_STR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2




    def expression2(self):

        localctx = ZCodeParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression2)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.expression3(0)
                self.state = 279
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4312147165184) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 280
                self.expression3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.expression3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.expression4(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.expression5(0) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.expression6() 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expression6)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ZCodeParser.NOT)
                self.state = 319
                self.expression6()
                pass
            elif token in [24, 26, 30, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.expression7()
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression7)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(ZCodeParser.MINUS)
                self.state = 324
                self.expression7()
                pass
            elif token in [24, 26, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.expression8()
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


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acc_arr(self):
            return self.getTypedRuleContext(ZCodeParser.Acc_arrContext,0)


        def expression9(self):
            return self.getTypedRuleContext(ZCodeParser.Expression9Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8




    def expression8(self):

        localctx = ZCodeParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression8)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.acc_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.expression9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def expression10(self):
            return self.getTypedRuleContext(ZCodeParser.Expression10Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression9




    def expression9(self):

        localctx = ZCodeParser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression9)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(ZCodeParser.LB)
                self.state = 333
                self.expression1()
                self.state = 334
                self.match(ZCodeParser.RB)
                pass
            elif token in [26, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.expression10()
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


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def arr_value(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression10




    def expression10(self):

        localctx = ZCodeParser.Expression10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression10)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.match(ZCodeParser.BOOL_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 343
                self.match(ZCodeParser.STR_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 344
                self.arr_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Acc_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_eleContext,0)


        def arr_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_acc_arr




    def acc_arr(self):

        localctx = ZCodeParser.Acc_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_acc_arr)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.arr_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(ZCodeParser.LBRACE, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RBRACE(self):
            return self.getToken(ZCodeParser.RBRACE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_ele




    def arr_ele(self):

        localctx = ZCodeParser.Arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 352
            self.match(ZCodeParser.LBRACE)
            self.state = 353
            self.index_operators()
            self.state = 354
            self.match(ZCodeParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def LBRACE(self):
            return self.getToken(ZCodeParser.LBRACE, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RBRACE(self):
            return self.getToken(ZCodeParser.RBRACE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_expr




    def arr_expr(self):

        localctx = ZCodeParser.Arr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arr_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.function_call()
            self.state = 357
            self.match(ZCodeParser.LBRACE)
            self.state = 358
            self.index_operators()
            self.state = 359
            self.match(ZCodeParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_operators)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.expression1()

                self.state = 363
                self.match(ZCodeParser.COMMA)
                self.state = 364
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def argurment_list(self):
            return self.getTypedRuleContext(ZCodeParser.Argurment_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 369
            self.match(ZCodeParser.LB)
            self.state = 370
            self.argurment_list()
            self.state = 371
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argurment_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonnull_argurment(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_argurmentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argurment_list




    def argurment_list(self):

        localctx = ZCodeParser.Argurment_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_argurment_list)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 24, 26, 30, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.nonnull_argurment()
                pass
            elif token in [25]:
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


    class Nonnull_argurmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argurment(self):
            return self.getTypedRuleContext(ZCodeParser.ArgurmentContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def nonnull_argurment(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_argurmentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nonnull_argurment




    def nonnull_argurment(self):

        localctx = ZCodeParser.Nonnull_argurmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_nonnull_argurment)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.argurment()
                self.state = 378
                self.match(ZCodeParser.COMMA)
                self.state = 379
                self.nonnull_argurment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.argurment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgurmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expression1(self):
            return self.getTypedRuleContext(ZCodeParser.Expression1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argurment




    def argurment(self):

        localctx = ZCodeParser.ArgurmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argurment)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.expression1()
                pass


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

        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_newline_list)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.nonnull_newline()
                pass
            elif token in [4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 19, 46]:
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


    class Nonnull_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nonnull_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Nonnull_newlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nonnull_newline




    def nonnull_newline(self):

        localctx = ZCodeParser.Nonnull_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_nonnull_newline)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(ZCodeParser.NEWLINE)
                self.state = 393
                self.nonnull_newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(ZCodeParser.NEWLINE)
                pass


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
        self._predicates[28] = self.expression3_sempred
        self._predicates[29] = self.expression4_sempred
        self._predicates[30] = self.expression5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




