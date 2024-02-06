# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/Assignment 232/assignment_1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,58,481,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,5,0,112,8,0,10,0,12,0,115,9,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,124,8,1,1,2,1,2,3,2,128,8,2,1,3,1,3,1,3,3,
        3,133,8,3,1,3,4,3,136,8,3,11,3,12,3,137,1,4,1,4,1,4,1,4,1,4,1,5,
        1,5,3,5,147,8,5,1,5,1,5,1,5,3,5,152,8,5,1,6,1,6,1,6,3,6,157,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,5,7,165,8,7,10,7,12,7,168,9,7,1,7,1,7,1,
        7,3,7,173,8,7,1,8,1,8,1,8,3,8,178,8,8,1,9,1,9,3,9,182,8,9,1,10,1,
        10,1,10,1,10,1,10,3,10,189,8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,
        11,197,8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,234,
        8,18,1,19,1,19,1,19,1,19,4,19,240,8,19,11,19,12,19,241,1,20,1,20,
        1,20,1,20,1,20,5,20,249,8,20,10,20,12,20,252,9,20,1,20,1,20,5,20,
        256,8,20,10,20,12,20,259,9,20,1,20,3,20,262,8,20,1,21,1,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        4,23,280,8,23,11,23,12,23,281,1,24,1,24,4,24,286,8,24,11,24,12,24,
        287,1,25,1,25,3,25,292,8,25,1,25,4,25,295,8,25,11,25,12,25,296,1,
        26,1,26,1,26,1,26,1,26,4,26,304,8,26,11,26,12,26,305,1,26,1,26,4,
        26,310,8,26,11,26,12,26,311,3,26,314,8,26,1,27,1,27,4,27,318,8,27,
        11,27,12,27,319,1,27,1,27,1,27,4,27,325,8,27,11,27,12,27,326,1,28,
        1,28,1,28,1,28,3,28,333,8,28,1,29,1,29,3,29,337,8,29,1,30,1,30,3,
        30,341,8,30,1,31,1,31,1,32,1,32,3,32,347,8,32,1,33,1,33,1,33,1,33,
        1,33,3,33,354,8,33,1,34,1,34,1,34,1,34,1,34,3,34,361,8,34,1,35,1,
        35,1,35,1,35,1,35,3,35,368,8,35,1,36,1,36,1,36,1,36,1,36,1,36,5,
        36,376,8,36,10,36,12,36,379,9,36,1,37,1,37,1,37,1,37,1,37,1,37,5,
        37,387,8,37,10,37,12,37,390,9,37,1,38,1,38,1,38,1,38,1,38,1,38,5,
        38,398,8,38,10,38,12,38,401,9,38,1,39,1,39,1,39,3,39,406,8,39,1,
        40,1,40,1,40,3,40,411,8,40,1,41,1,41,1,41,1,41,1,41,1,41,3,41,419,
        8,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,3,43,430,8,43,
        1,44,1,44,1,44,1,44,1,45,1,45,3,45,438,8,45,1,45,1,45,1,46,1,46,
        1,46,1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,3,48,455,
        8,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,
        1,51,3,51,470,8,51,1,52,1,52,1,53,1,53,1,53,3,53,477,8,53,1,54,1,
        54,1,54,0,3,72,74,76,55,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,0,6,3,
        0,21,21,23,27,29,29,1,0,50,51,1,0,16,17,1,0,18,20,1,0,32,34,1,0,
        8,9,489,0,113,1,0,0,0,2,123,1,0,0,0,4,127,1,0,0,0,6,132,1,0,0,0,
        8,139,1,0,0,0,10,146,1,0,0,0,12,153,1,0,0,0,14,158,1,0,0,0,16,174,
        1,0,0,0,18,181,1,0,0,0,20,188,1,0,0,0,22,196,1,0,0,0,24,198,1,0,
        0,0,26,203,1,0,0,0,28,207,1,0,0,0,30,212,1,0,0,0,32,216,1,0,0,0,
        34,221,1,0,0,0,36,233,1,0,0,0,38,235,1,0,0,0,40,243,1,0,0,0,42,263,
        1,0,0,0,44,268,1,0,0,0,46,277,1,0,0,0,48,283,1,0,0,0,50,289,1,0,
        0,0,52,313,1,0,0,0,54,315,1,0,0,0,56,332,1,0,0,0,58,336,1,0,0,0,
        60,338,1,0,0,0,62,342,1,0,0,0,64,346,1,0,0,0,66,353,1,0,0,0,68,360,
        1,0,0,0,70,367,1,0,0,0,72,369,1,0,0,0,74,380,1,0,0,0,76,391,1,0,
        0,0,78,405,1,0,0,0,80,410,1,0,0,0,82,418,1,0,0,0,84,420,1,0,0,0,
        86,429,1,0,0,0,88,431,1,0,0,0,90,437,1,0,0,0,92,441,1,0,0,0,94,445,
        1,0,0,0,96,454,1,0,0,0,98,456,1,0,0,0,100,460,1,0,0,0,102,469,1,
        0,0,0,104,471,1,0,0,0,106,476,1,0,0,0,108,478,1,0,0,0,110,112,5,
        54,0,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,
        0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,3,2,1,0,117,118,5,
        0,0,1,118,1,1,0,0,0,119,120,3,4,2,0,120,121,3,2,1,0,121,124,1,0,
        0,0,122,124,3,4,2,0,123,119,1,0,0,0,123,122,1,0,0,0,124,3,1,0,0,
        0,125,128,3,6,3,0,126,128,3,14,7,0,127,125,1,0,0,0,127,126,1,0,0,
        0,128,5,1,0,0,0,129,133,3,10,5,0,130,133,3,8,4,0,131,133,3,12,6,
        0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,135,1,0,0,
        0,134,136,5,54,0,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,0,
        0,137,138,1,0,0,0,138,7,1,0,0,0,139,140,5,36,0,0,140,141,5,53,0,
        0,141,142,5,22,0,0,142,143,3,62,31,0,143,9,1,0,0,0,144,147,3,104,
        52,0,145,147,5,37,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,148,1,
        0,0,0,148,151,5,53,0,0,149,150,5,22,0,0,150,152,3,62,31,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,11,1,0,0,0,153,156,3,98,49,0,154,155,
        5,22,0,0,155,157,3,94,47,0,156,154,1,0,0,0,156,157,1,0,0,0,157,13,
        1,0,0,0,158,159,5,38,0,0,159,160,5,53,0,0,160,161,5,11,0,0,161,162,
        3,18,9,0,162,166,5,12,0,0,163,165,5,54,0,0,164,163,1,0,0,0,165,168,
        1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,172,1,0,0,0,168,166,
        1,0,0,0,169,173,5,54,0,0,170,173,3,54,27,0,171,173,3,50,25,0,172,
        169,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,15,1,0,0,0,174,175,
        3,104,52,0,175,177,5,53,0,0,176,178,3,100,50,0,177,176,1,0,0,0,177,
        178,1,0,0,0,178,17,1,0,0,0,179,182,3,20,10,0,180,182,1,0,0,0,181,
        179,1,0,0,0,181,180,1,0,0,0,182,19,1,0,0,0,183,184,3,16,8,0,184,
        185,5,15,0,0,185,186,3,20,10,0,186,189,1,0,0,0,187,189,3,16,8,0,
        188,183,1,0,0,0,188,187,1,0,0,0,189,21,1,0,0,0,190,197,3,34,17,0,
        191,197,3,32,16,0,192,197,3,30,15,0,193,197,3,28,14,0,194,197,3,
        26,13,0,195,197,3,24,12,0,196,190,1,0,0,0,196,191,1,0,0,0,196,192,
        1,0,0,0,196,193,1,0,0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,23,1,
        0,0,0,198,199,5,6,0,0,199,200,5,11,0,0,200,201,3,62,31,0,201,202,
        5,12,0,0,202,25,1,0,0,0,203,204,5,5,0,0,204,205,5,11,0,0,205,206,
        5,12,0,0,206,27,1,0,0,0,207,208,5,4,0,0,208,209,5,11,0,0,209,210,
        3,62,31,0,210,211,5,12,0,0,211,29,1,0,0,0,212,213,5,3,0,0,213,214,
        5,11,0,0,214,215,5,12,0,0,215,31,1,0,0,0,216,217,5,2,0,0,217,218,
        5,11,0,0,218,219,3,62,31,0,219,220,5,12,0,0,220,33,1,0,0,0,221,222,
        5,1,0,0,222,223,5,11,0,0,223,224,5,12,0,0,224,35,1,0,0,0,225,234,
        3,38,19,0,226,234,3,40,20,0,227,234,3,44,22,0,228,234,3,54,27,0,
        229,234,3,46,23,0,230,234,3,48,24,0,231,234,3,50,25,0,232,234,3,
        52,26,0,233,225,1,0,0,0,233,226,1,0,0,0,233,227,1,0,0,0,233,228,
        1,0,0,0,233,229,1,0,0,0,233,230,1,0,0,0,233,231,1,0,0,0,233,232,
        1,0,0,0,234,37,1,0,0,0,235,236,3,60,30,0,236,237,5,22,0,0,237,239,
        3,62,31,0,238,240,5,54,0,0,239,238,1,0,0,0,240,241,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,39,1,0,0,0,243,244,5,44,0,0,244,245,
        3,88,44,0,245,246,3,106,53,0,246,250,3,36,18,0,247,249,3,42,21,0,
        248,247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,
        251,261,1,0,0,0,252,250,1,0,0,0,253,257,5,45,0,0,254,256,5,54,0,
        0,255,254,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,
        0,258,260,1,0,0,0,259,257,1,0,0,0,260,262,3,36,18,0,261,253,1,0,
        0,0,261,262,1,0,0,0,262,41,1,0,0,0,263,264,5,46,0,0,264,265,3,88,
        44,0,265,266,3,106,53,0,266,267,3,36,18,0,267,43,1,0,0,0,268,269,
        5,39,0,0,269,270,5,53,0,0,270,271,5,40,0,0,271,272,3,62,31,0,272,
        273,5,41,0,0,273,274,3,62,31,0,274,275,3,106,53,0,275,276,3,36,18,
        0,276,45,1,0,0,0,277,279,5,42,0,0,278,280,5,54,0,0,279,278,1,0,0,
        0,280,281,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,47,1,0,0,0,
        283,285,5,43,0,0,284,286,5,54,0,0,285,284,1,0,0,0,286,287,1,0,0,
        0,287,285,1,0,0,0,287,288,1,0,0,0,288,49,1,0,0,0,289,291,5,35,0,
        0,290,292,3,62,31,0,291,290,1,0,0,0,291,292,1,0,0,0,292,294,1,0,
        0,0,293,295,5,54,0,0,294,293,1,0,0,0,295,296,1,0,0,0,296,294,1,0,
        0,0,296,297,1,0,0,0,297,51,1,0,0,0,298,299,5,53,0,0,299,300,5,11,
        0,0,300,301,3,64,32,0,301,303,5,12,0,0,302,304,5,54,0,0,303,302,
        1,0,0,0,304,305,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,314,
        1,0,0,0,307,309,3,22,11,0,308,310,5,54,0,0,309,308,1,0,0,0,310,311,
        1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,314,1,0,0,0,313,298,
        1,0,0,0,313,307,1,0,0,0,314,53,1,0,0,0,315,317,5,47,0,0,316,318,
        5,54,0,0,317,316,1,0,0,0,318,319,1,0,0,0,319,317,1,0,0,0,319,320,
        1,0,0,0,320,321,1,0,0,0,321,322,3,56,28,0,322,324,5,48,0,0,323,325,
        5,54,0,0,324,323,1,0,0,0,325,326,1,0,0,0,326,324,1,0,0,0,326,327,
        1,0,0,0,327,55,1,0,0,0,328,329,3,58,29,0,329,330,3,56,28,0,330,333,
        1,0,0,0,331,333,1,0,0,0,332,328,1,0,0,0,332,331,1,0,0,0,333,57,1,
        0,0,0,334,337,3,36,18,0,335,337,3,6,3,0,336,334,1,0,0,0,336,335,
        1,0,0,0,337,59,1,0,0,0,338,340,5,53,0,0,339,341,3,92,46,0,340,339,
        1,0,0,0,340,341,1,0,0,0,341,61,1,0,0,0,342,343,3,68,34,0,343,63,
        1,0,0,0,344,347,3,66,33,0,345,347,1,0,0,0,346,344,1,0,0,0,346,345,
        1,0,0,0,347,65,1,0,0,0,348,349,3,62,31,0,349,350,5,15,0,0,350,351,
        3,66,33,0,351,354,1,0,0,0,352,354,3,62,31,0,353,348,1,0,0,0,353,
        352,1,0,0,0,354,67,1,0,0,0,355,356,3,70,35,0,356,357,5,28,0,0,357,
        358,3,70,35,0,358,361,1,0,0,0,359,361,3,70,35,0,360,355,1,0,0,0,
        360,359,1,0,0,0,361,69,1,0,0,0,362,363,3,72,36,0,363,364,7,0,0,0,
        364,365,3,72,36,0,365,368,1,0,0,0,366,368,3,72,36,0,367,362,1,0,
        0,0,367,366,1,0,0,0,368,71,1,0,0,0,369,370,6,36,-1,0,370,371,3,74,
        37,0,371,377,1,0,0,0,372,373,10,2,0,0,373,374,7,1,0,0,374,376,3,
        74,37,0,375,372,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,
        1,0,0,0,378,73,1,0,0,0,379,377,1,0,0,0,380,381,6,37,-1,0,381,382,
        3,76,38,0,382,388,1,0,0,0,383,384,10,2,0,0,384,385,7,2,0,0,385,387,
        3,76,38,0,386,383,1,0,0,0,387,390,1,0,0,0,388,386,1,0,0,0,388,389,
        1,0,0,0,389,75,1,0,0,0,390,388,1,0,0,0,391,392,6,38,-1,0,392,393,
        3,78,39,0,393,399,1,0,0,0,394,395,10,2,0,0,395,396,7,3,0,0,396,398,
        3,78,39,0,397,394,1,0,0,0,398,401,1,0,0,0,399,397,1,0,0,0,399,400,
        1,0,0,0,400,77,1,0,0,0,401,399,1,0,0,0,402,403,5,49,0,0,403,406,
        3,78,39,0,404,406,3,80,40,0,405,402,1,0,0,0,405,404,1,0,0,0,406,
        79,1,0,0,0,407,408,5,17,0,0,408,411,3,80,40,0,409,411,3,82,41,0,
        410,407,1,0,0,0,410,409,1,0,0,0,411,81,1,0,0,0,412,419,5,53,0,0,
        413,419,3,86,43,0,414,419,3,84,42,0,415,419,3,88,44,0,416,419,3,
        90,45,0,417,419,3,22,11,0,418,412,1,0,0,0,418,413,1,0,0,0,418,414,
        1,0,0,0,418,415,1,0,0,0,418,416,1,0,0,0,418,417,1,0,0,0,419,83,1,
        0,0,0,420,421,5,53,0,0,421,422,5,11,0,0,422,423,3,64,32,0,423,424,
        5,12,0,0,424,85,1,0,0,0,425,430,3,108,54,0,426,430,5,7,0,0,427,430,
        5,10,0,0,428,430,3,94,47,0,429,425,1,0,0,0,429,426,1,0,0,0,429,427,
        1,0,0,0,429,428,1,0,0,0,430,87,1,0,0,0,431,432,5,11,0,0,432,433,
        3,62,31,0,433,434,5,12,0,0,434,89,1,0,0,0,435,438,5,53,0,0,436,438,
        3,84,42,0,437,435,1,0,0,0,437,436,1,0,0,0,438,439,1,0,0,0,439,440,
        3,92,46,0,440,91,1,0,0,0,441,442,5,13,0,0,442,443,3,66,33,0,443,
        444,5,14,0,0,444,93,1,0,0,0,445,446,5,13,0,0,446,447,3,96,48,0,447,
        448,5,14,0,0,448,95,1,0,0,0,449,450,3,62,31,0,450,451,5,15,0,0,451,
        452,3,96,48,0,452,455,1,0,0,0,453,455,3,62,31,0,454,449,1,0,0,0,
        454,453,1,0,0,0,455,97,1,0,0,0,456,457,3,104,52,0,457,458,5,53,0,
        0,458,459,3,100,50,0,459,99,1,0,0,0,460,461,5,13,0,0,461,462,3,102,
        51,0,462,463,5,14,0,0,463,101,1,0,0,0,464,465,3,108,54,0,465,466,
        5,15,0,0,466,467,3,102,51,0,467,470,1,0,0,0,468,470,3,108,54,0,469,
        464,1,0,0,0,469,468,1,0,0,0,470,103,1,0,0,0,471,472,7,4,0,0,472,
        105,1,0,0,0,473,474,5,54,0,0,474,477,3,106,53,0,475,477,1,0,0,0,
        476,473,1,0,0,0,476,475,1,0,0,0,477,107,1,0,0,0,478,479,7,5,0,0,
        479,109,1,0,0,0,46,113,123,127,132,137,146,151,156,166,172,177,181,
        188,196,233,241,250,257,261,281,287,291,296,305,311,313,319,326,
        332,336,340,346,353,360,367,377,388,399,405,410,418,429,437,454,
        469,476
    ]

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
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33, 34, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.vardecl()
                pass
            elif token in [38]:
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
                if not (_la==54):
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




    def vardecl_not_full(self):

        localctx = ZCodeParser.Vardecl_not_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl_not_full)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33, 34]:
                self.state = 144
                self.atomic_types()
                pass
            elif token in [37]:
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
            if _la==22:
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
            if _la==22:
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
            if token in [54]:
                self.state = 169
                self.match(ZCodeParser.NEW_LINE)
                pass
            elif token in [47]:
                self.state = 170
                self.block_stmt()
                pass
            elif token in [35]:
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
            if _la==13:
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




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.param_prime()
                pass
            elif token in [12]:
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




    def spec_func(self):

        localctx = ZCodeParser.Spec_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_spec_func)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.read_number()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.write_number()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.read_bool()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.write()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 194
                self.read_string()
                pass
            elif token in [6]:
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
                if not (_la==54):
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
                while _la==54:
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
                if not (_la==54):
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
                if not (_la==54):
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
        self.enterRule(localctx, 50, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.RETURN)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9570149208305662) != 0):
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
                if not (_la==54):
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




    def call_stmt(self):

        localctx = ZCodeParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
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
                    if not (_la==54):
                        break

                pass
            elif token in [1, 2, 3, 4, 5, 6]:
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
                    if not (_la==54):
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
                if not (_la==54):
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
                if not (_la==54):
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
        self.enterRule(localctx, 56, self.RULE_blocked_list)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 32, 33, 34, 35, 36, 37, 39, 42, 43, 44, 47, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.stmt_plus_vardecl()
                self.state = 329
                self.blocked_list()
                pass
            elif token in [48]:
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
        self.enterRule(localctx, 58, self.RULE_stmt_plus_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 35, 39, 42, 43, 44, 47, 53]:
                self.state = 334
                self.stmt()
                pass
            elif token in [32, 33, 34, 36, 37]:
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
            if _la==13:
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




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr_list)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 49, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.exprprime()
                pass
            elif token in [12]:
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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 799014912) != 0)):
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
                    if not(_la==50 or _la==51):
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
                    if not(_la==16 or _la==17):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
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




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp5)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(ZCodeParser.NOT)
                self.state = 403
                self.exp5()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 53]:
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




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp6)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ZCodeParser.SUB)
                self.state = 408
                self.exp6()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 53]:
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




    def constant(self):

        localctx = ZCodeParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_constant)
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.number_lit()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [13]:
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




    def atomic_types(self):

        localctx = ZCodeParser.Atomic_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_atomic_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
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
        self.enterRule(localctx, 106, self.RULE_newline_list)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(ZCodeParser.NEW_LINE)
                self.state = 474
                self.newline_list()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 35, 39, 42, 43, 44, 47, 53]:
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




    def number_lit(self):

        localctx = ZCodeParser.Number_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_number_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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
         




