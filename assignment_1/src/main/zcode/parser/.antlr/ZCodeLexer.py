# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/Assignment 232/assignment_1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,0,58,474,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,193,8,6,1,7,1,7,
        3,7,197,8,7,1,7,3,7,200,8,7,1,7,1,7,1,7,3,7,205,8,7,1,8,1,8,1,8,
        5,8,210,8,8,10,8,12,8,213,9,8,3,8,215,8,8,1,9,1,9,5,9,219,8,9,10,
        9,12,9,222,9,9,1,10,1,10,3,10,226,8,10,1,10,4,10,229,8,10,11,10,
        12,10,230,1,11,1,11,1,11,1,11,1,11,5,11,238,8,11,10,11,12,11,241,
        9,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,15,
        1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,
        1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,27,
        1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,31,1,31,
        1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,
        1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,
        1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,
        1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,48,
        1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,
        1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,54,
        1,54,1,54,1,55,1,55,1,55,1,55,5,55,417,8,55,10,55,12,55,420,9,55,
        1,55,1,55,1,56,1,56,5,56,426,8,56,10,56,12,56,429,9,56,1,57,3,57,
        432,8,57,1,57,1,57,1,57,1,58,4,58,438,8,58,11,58,12,58,439,1,58,
        1,58,1,59,1,59,1,59,1,59,1,59,5,59,449,8,59,10,59,12,59,452,9,59,
        1,59,3,59,455,8,59,1,59,1,59,1,60,1,60,1,60,1,60,1,60,5,60,464,8,
        60,10,60,12,60,467,9,60,1,60,1,60,1,60,1,61,1,61,1,61,0,0,62,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,0,21,0,23,10,25,0,27,0,29,
        11,31,12,33,13,35,14,37,15,39,16,41,17,43,18,45,19,47,20,49,21,51,
        22,53,23,55,24,57,25,59,26,61,27,63,28,65,29,67,30,69,31,71,32,73,
        33,75,34,77,35,79,36,81,37,83,38,85,39,87,40,89,41,91,42,93,43,95,
        44,97,45,99,46,101,47,103,48,105,49,107,50,109,51,111,52,113,53,
        115,54,117,55,119,56,121,57,123,58,1,0,10,1,0,48,57,2,0,69,69,101,
        101,2,0,43,43,45,45,3,0,10,10,34,34,92,92,7,0,39,39,92,92,98,98,
        102,102,110,110,114,114,116,116,2,0,10,10,13,13,3,0,65,90,95,95,
        97,122,4,0,48,57,65,90,95,95,97,122,3,0,8,9,12,12,32,32,2,1,10,10,
        13,13,491,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,
        0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,23,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,
        0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,
        0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,
        0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,1,125,1,
        0,0,0,3,136,1,0,0,0,5,148,1,0,0,0,7,157,1,0,0,0,9,167,1,0,0,0,11,
        178,1,0,0,0,13,192,1,0,0,0,15,204,1,0,0,0,17,214,1,0,0,0,19,216,
        1,0,0,0,21,223,1,0,0,0,23,232,1,0,0,0,25,245,1,0,0,0,27,248,1,0,
        0,0,29,251,1,0,0,0,31,253,1,0,0,0,33,255,1,0,0,0,35,257,1,0,0,0,
        37,259,1,0,0,0,39,261,1,0,0,0,41,263,1,0,0,0,43,265,1,0,0,0,45,267,
        1,0,0,0,47,269,1,0,0,0,49,271,1,0,0,0,51,273,1,0,0,0,53,276,1,0,
        0,0,55,279,1,0,0,0,57,281,1,0,0,0,59,284,1,0,0,0,61,287,1,0,0,0,
        63,289,1,0,0,0,65,293,1,0,0,0,67,296,1,0,0,0,69,301,1,0,0,0,71,307,
        1,0,0,0,73,314,1,0,0,0,75,319,1,0,0,0,77,326,1,0,0,0,79,333,1,0,
        0,0,81,337,1,0,0,0,83,345,1,0,0,0,85,350,1,0,0,0,87,354,1,0,0,0,
        89,360,1,0,0,0,91,363,1,0,0,0,93,369,1,0,0,0,95,378,1,0,0,0,97,381,
        1,0,0,0,99,386,1,0,0,0,101,391,1,0,0,0,103,397,1,0,0,0,105,401,1,
        0,0,0,107,405,1,0,0,0,109,409,1,0,0,0,111,412,1,0,0,0,113,423,1,
        0,0,0,115,431,1,0,0,0,117,437,1,0,0,0,119,443,1,0,0,0,121,458,1,
        0,0,0,123,471,1,0,0,0,125,126,5,114,0,0,126,127,5,101,0,0,127,128,
        5,97,0,0,128,129,5,100,0,0,129,130,5,78,0,0,130,131,5,117,0,0,131,
        132,5,109,0,0,132,133,5,98,0,0,133,134,5,101,0,0,134,135,5,114,0,
        0,135,2,1,0,0,0,136,137,5,119,0,0,137,138,5,114,0,0,138,139,5,105,
        0,0,139,140,5,116,0,0,140,141,5,101,0,0,141,142,5,78,0,0,142,143,
        5,117,0,0,143,144,5,109,0,0,144,145,5,98,0,0,145,146,5,101,0,0,146,
        147,5,114,0,0,147,4,1,0,0,0,148,149,5,114,0,0,149,150,5,101,0,0,
        150,151,5,97,0,0,151,152,5,100,0,0,152,153,5,66,0,0,153,154,5,111,
        0,0,154,155,5,111,0,0,155,156,5,108,0,0,156,6,1,0,0,0,157,158,5,
        119,0,0,158,159,5,114,0,0,159,160,5,105,0,0,160,161,5,116,0,0,161,
        162,5,101,0,0,162,163,5,66,0,0,163,164,5,111,0,0,164,165,5,111,0,
        0,165,166,5,108,0,0,166,8,1,0,0,0,167,168,5,114,0,0,168,169,5,101,
        0,0,169,170,5,97,0,0,170,171,5,100,0,0,171,172,5,83,0,0,172,173,
        5,116,0,0,173,174,5,114,0,0,174,175,5,105,0,0,175,176,5,110,0,0,
        176,177,5,103,0,0,177,10,1,0,0,0,178,179,5,119,0,0,179,180,5,114,
        0,0,180,181,5,105,0,0,181,182,5,116,0,0,182,183,5,101,0,0,183,184,
        5,83,0,0,184,185,5,116,0,0,185,186,5,114,0,0,186,187,5,105,0,0,187,
        188,5,110,0,0,188,189,5,103,0,0,189,12,1,0,0,0,190,193,3,67,33,0,
        191,193,3,69,34,0,192,190,1,0,0,0,192,191,1,0,0,0,193,14,1,0,0,0,
        194,196,3,17,8,0,195,197,3,19,9,0,196,195,1,0,0,0,196,197,1,0,0,
        0,197,199,1,0,0,0,198,200,3,21,10,0,199,198,1,0,0,0,199,200,1,0,
        0,0,200,205,1,0,0,0,201,202,3,17,8,0,202,203,3,21,10,0,203,205,1,
        0,0,0,204,194,1,0,0,0,204,201,1,0,0,0,205,16,1,0,0,0,206,215,5,48,
        0,0,207,211,7,0,0,0,208,210,7,0,0,0,209,208,1,0,0,0,210,213,1,0,
        0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,215,1,0,0,0,213,211,1,0,
        0,0,214,206,1,0,0,0,214,207,1,0,0,0,215,18,1,0,0,0,216,220,5,46,
        0,0,217,219,7,0,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,
        0,0,220,221,1,0,0,0,221,20,1,0,0,0,222,220,1,0,0,0,223,225,7,1,0,
        0,224,226,7,2,0,0,225,224,1,0,0,0,225,226,1,0,0,0,226,228,1,0,0,
        0,227,229,7,0,0,0,228,227,1,0,0,0,229,230,1,0,0,0,230,228,1,0,0,
        0,230,231,1,0,0,0,231,22,1,0,0,0,232,239,5,34,0,0,233,238,3,25,12,
        0,234,238,8,3,0,0,235,236,5,39,0,0,236,238,5,34,0,0,237,233,1,0,
        0,0,237,234,1,0,0,0,237,235,1,0,0,0,238,241,1,0,0,0,239,237,1,0,
        0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,239,1,0,0,0,242,243,5,34,
        0,0,243,244,6,11,0,0,244,24,1,0,0,0,245,246,5,92,0,0,246,247,7,4,
        0,0,247,26,1,0,0,0,248,249,5,92,0,0,249,250,8,4,0,0,250,28,1,0,0,
        0,251,252,5,40,0,0,252,30,1,0,0,0,253,254,5,41,0,0,254,32,1,0,0,
        0,255,256,5,91,0,0,256,34,1,0,0,0,257,258,5,93,0,0,258,36,1,0,0,
        0,259,260,5,44,0,0,260,38,1,0,0,0,261,262,5,43,0,0,262,40,1,0,0,
        0,263,264,5,45,0,0,264,42,1,0,0,0,265,266,5,42,0,0,266,44,1,0,0,
        0,267,268,5,47,0,0,268,46,1,0,0,0,269,270,5,37,0,0,270,48,1,0,0,
        0,271,272,5,61,0,0,272,50,1,0,0,0,273,274,5,60,0,0,274,275,5,45,
        0,0,275,52,1,0,0,0,276,277,5,33,0,0,277,278,5,61,0,0,278,54,1,0,
        0,0,279,280,5,60,0,0,280,56,1,0,0,0,281,282,5,60,0,0,282,283,5,61,
        0,0,283,58,1,0,0,0,284,285,5,62,0,0,285,286,5,61,0,0,286,60,1,0,
        0,0,287,288,5,62,0,0,288,62,1,0,0,0,289,290,5,46,0,0,290,291,5,46,
        0,0,291,292,5,46,0,0,292,64,1,0,0,0,293,294,5,61,0,0,294,295,5,61,
        0,0,295,66,1,0,0,0,296,297,5,116,0,0,297,298,5,114,0,0,298,299,5,
        117,0,0,299,300,5,101,0,0,300,68,1,0,0,0,301,302,5,102,0,0,302,303,
        5,97,0,0,303,304,5,108,0,0,304,305,5,115,0,0,305,306,5,101,0,0,306,
        70,1,0,0,0,307,308,5,110,0,0,308,309,5,117,0,0,309,310,5,109,0,0,
        310,311,5,98,0,0,311,312,5,101,0,0,312,313,5,114,0,0,313,72,1,0,
        0,0,314,315,5,98,0,0,315,316,5,111,0,0,316,317,5,111,0,0,317,318,
        5,108,0,0,318,74,1,0,0,0,319,320,5,115,0,0,320,321,5,116,0,0,321,
        322,5,114,0,0,322,323,5,105,0,0,323,324,5,110,0,0,324,325,5,103,
        0,0,325,76,1,0,0,0,326,327,5,114,0,0,327,328,5,101,0,0,328,329,5,
        116,0,0,329,330,5,117,0,0,330,331,5,114,0,0,331,332,5,110,0,0,332,
        78,1,0,0,0,333,334,5,118,0,0,334,335,5,97,0,0,335,336,5,114,0,0,
        336,80,1,0,0,0,337,338,5,100,0,0,338,339,5,121,0,0,339,340,5,110,
        0,0,340,341,5,97,0,0,341,342,5,109,0,0,342,343,5,105,0,0,343,344,
        5,99,0,0,344,82,1,0,0,0,345,346,5,102,0,0,346,347,5,117,0,0,347,
        348,5,110,0,0,348,349,5,99,0,0,349,84,1,0,0,0,350,351,5,102,0,0,
        351,352,5,111,0,0,352,353,5,114,0,0,353,86,1,0,0,0,354,355,5,117,
        0,0,355,356,5,110,0,0,356,357,5,116,0,0,357,358,5,105,0,0,358,359,
        5,108,0,0,359,88,1,0,0,0,360,361,5,98,0,0,361,362,5,121,0,0,362,
        90,1,0,0,0,363,364,5,98,0,0,364,365,5,114,0,0,365,366,5,101,0,0,
        366,367,5,97,0,0,367,368,5,107,0,0,368,92,1,0,0,0,369,370,5,99,0,
        0,370,371,5,111,0,0,371,372,5,110,0,0,372,373,5,116,0,0,373,374,
        5,105,0,0,374,375,5,110,0,0,375,376,5,117,0,0,376,377,5,101,0,0,
        377,94,1,0,0,0,378,379,5,105,0,0,379,380,5,102,0,0,380,96,1,0,0,
        0,381,382,5,101,0,0,382,383,5,108,0,0,383,384,5,115,0,0,384,385,
        5,101,0,0,385,98,1,0,0,0,386,387,5,101,0,0,387,388,5,108,0,0,388,
        389,5,105,0,0,389,390,5,102,0,0,390,100,1,0,0,0,391,392,5,98,0,0,
        392,393,5,101,0,0,393,394,5,103,0,0,394,395,5,105,0,0,395,396,5,
        110,0,0,396,102,1,0,0,0,397,398,5,101,0,0,398,399,5,110,0,0,399,
        400,5,100,0,0,400,104,1,0,0,0,401,402,5,110,0,0,402,403,5,111,0,
        0,403,404,5,116,0,0,404,106,1,0,0,0,405,406,5,97,0,0,406,407,5,110,
        0,0,407,408,5,100,0,0,408,108,1,0,0,0,409,410,5,111,0,0,410,411,
        5,114,0,0,411,110,1,0,0,0,412,413,5,35,0,0,413,414,5,35,0,0,414,
        418,1,0,0,0,415,417,8,5,0,0,416,415,1,0,0,0,417,420,1,0,0,0,418,
        416,1,0,0,0,418,419,1,0,0,0,419,421,1,0,0,0,420,418,1,0,0,0,421,
        422,6,55,1,0,422,112,1,0,0,0,423,427,7,6,0,0,424,426,7,7,0,0,425,
        424,1,0,0,0,426,429,1,0,0,0,427,425,1,0,0,0,427,428,1,0,0,0,428,
        114,1,0,0,0,429,427,1,0,0,0,430,432,5,13,0,0,431,430,1,0,0,0,431,
        432,1,0,0,0,432,433,1,0,0,0,433,434,5,10,0,0,434,435,6,57,2,0,435,
        116,1,0,0,0,436,438,7,8,0,0,437,436,1,0,0,0,438,439,1,0,0,0,439,
        437,1,0,0,0,439,440,1,0,0,0,440,441,1,0,0,0,441,442,6,58,1,0,442,
        118,1,0,0,0,443,450,5,34,0,0,444,449,8,3,0,0,445,449,3,25,12,0,446,
        447,5,39,0,0,447,449,5,34,0,0,448,444,1,0,0,0,448,445,1,0,0,0,448,
        446,1,0,0,0,449,452,1,0,0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,
        454,1,0,0,0,452,450,1,0,0,0,453,455,7,9,0,0,454,453,1,0,0,0,455,
        456,1,0,0,0,456,457,6,59,3,0,457,120,1,0,0,0,458,465,5,34,0,0,459,
        464,8,3,0,0,460,464,3,25,12,0,461,462,5,39,0,0,462,464,5,34,0,0,
        463,459,1,0,0,0,463,460,1,0,0,0,463,461,1,0,0,0,464,467,1,0,0,0,
        465,463,1,0,0,0,465,466,1,0,0,0,466,468,1,0,0,0,467,465,1,0,0,0,
        468,469,3,27,13,0,469,470,6,60,4,0,470,122,1,0,0,0,471,472,9,0,0,
        0,472,473,6,61,5,0,473,124,1,0,0,0,21,0,192,196,199,204,211,214,
        220,225,230,237,239,418,427,431,439,448,450,454,463,465,6,1,11,0,
        6,0,0,1,57,1,1,59,2,1,60,3,1,61,4
    ]

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
        self.checkVersion("4.13.1")
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
            	
     


