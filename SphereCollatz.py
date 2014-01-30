#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

import sys

meta_cache = [119, 128,144, 142, 137,171,179,174,169,182,177,172,167,180,175,175,170,183,183,209,178,191,173,217,186,199,181,181,194,238,176,189,189,202,202,215,184,184,197,210,179,179,192,192,236,205,218,187,187,262,200,200,244,182,182,257,195,195,195,239,208,177,221,252,190,190,234,203,203,203,216,247,185,229,260,198,198,185,211,242,224,242,180,255,255,193,206,268,206,237,206,206,237,219,188,250,188,250,263,263,263,201,201,201,201,245,276,245,245,214,227,258,196,196,196,209,196,271,240,209,271,222,240,209,253,178,222,253,235,191,204,266,235,235,266,204,217,235,235,204,248,279,217,248,186,248,199,230,261,199,261,230,199,199,212,199,274,212,243,274,243,243,243,243,212,181,256,256,225,256,256,238,194,207,238,269,269,238,269,207,269,220,238,194,238,207,220,251,282,251,220,251,251,251,251,202,233,264,264,233,233,264,233,246,215,233,202,233,202,171,246,277,308,215,246,246,246,259,246,215,184,228,259,259,197,228,259,228,197,197,228,210,228,241,272,272,210,241,272,241,272,241,223,241,197,254,210,210,210,254,254,285,223,285,254,236,254,236,254,267,223,192,236,267,267,236,236,236,267,236,267,205,218,311,236,174,249,280,205,205,218,249,280,311,218,324,249,218,249,249,249,249,218,218,187,231,262,262,262,231,306,262,262,231,244,200,213,231,231,213,244,244,275,275,200,244,244,275,275,306,275,244,244,213,213,257,213,288,244,213,182,226,226,257,257,182,226,288,226,257,239,257,239,195,195,257,226,226,195,239,239,270,270,195,239,239,239,270,239,239,283,314,239,221,239,239,239,208,252,239,208,283,177,252,252,252,283,283,314,221,283,221,252,252,252,252,221,252,265,190,221,296,190,234,265,265,296,190,265,203,234,234,265,234,234,203,278,203,265,203,309,234,203,203,247,247,278,278,203,203,340,247,247,278,278,309,216,322,247,216,247,247,247,247,260,216,260,216,216,216,216,229,260,229,260,260,260,198,322,198,304,291,260,260,291,260,304,198,229,260,260,273,211,229,211,229,242,242,273,198,273,167,273,211,242,242,273,273,242,304,286,317,242,242,273,242,211,335,255,211,242,286,255,286,211,317,224,255,255,255,255,286,286,211,317,224,286,330,255,255,237,255,255,255,299,224,224,255,268,224,206,224,224,224,268,237,268,268,268,268,206,268,206,237,237,237,268,237,237,237,281,312,281,206,268,312,237,312,237,237,206,206,250,250,250,281,299,281,175,250,281,219,312,250,281,281,219,312,219,219,325,250,250,250,219,250,250,188,263,219,188,263,263,263,294,201,219,294,232,188,294,232,263,263,294,294,188,263,325,201,307,232,232,263,263,232,294,263,201,307,219,201,263,307,201,232,351,232,214,214,201,245,245,245,276,201,276,307,201,201,338,214,245,307,276,276,276,183,307,245,289,320,289,245,214,276,276,245,276,320,245,258,214,214,258,289,245,214,289,307,214,320,227,289,227,227,258,258,289,289,289,214,258,320,196,302,227,289,227,258,240,227,289,258,227,302,258,227,227,302,258,271,227,196,227,227,333,227,227,240,240,240,271,271,333,302,196,196,271,240,209,240,315,165,302,271,240,240,302,240,284,271,315,240,240,240,271,271,240,240,315,333,253,222,209,209,240,284,253,284,284,302,209,315,222,222,284,253,222,253,253,209,284,253,284,209,253,315,222,302,328,222,284,222,253,235,284,253,253,191,253,297,209,222,191,253,253,266,266,297,297,222,297,222,222,191,266,266,235,266,266,284,328,297,191,204,235,328,266,227,310,341,235,235,266,266,235,235,297,204,279,204,310,279,235,204,235,266,310,266,235,310,204,235,235,204,204,204,235,248,248,248,279,279,297,279,310,173,204,248,341,217,217,248,310,248,248,279,279,354,248,310,279,204,217,323,292,279,248,217,248,279,217,248,279,217,217,248,261,248,217,217,261,292,186,261,292,292,199,310,292,217,230,230,261,292,230,230,261,261,292,323,292,292,230,199,230,323,230,199,305,292,230,292,230,261,261,248,292,292,261,199,199,305,274,217,261,199,230,261,305,199,274,230,349,274,323,305,199,212,168,230,305,243,243,243,274,274,199,274,305,305,199,230,274,336,274,212,243,305,318,274,305,243,274,243,305,243,305,243,212,287,318,287,243,243,212,243,274,274,212,274,274,318,212,336,256,243,212,225,243,256,318,287,256,256,287,331,305,212,287,318,181,225,287,287,256,225,225,256,256,256,287,318,256,287,256,212,225,318,225,243,300,287,331,300,287,256,225,256,238,238,225,287,256,212,331,256,300,331,225,225,194,287,300,300,194,269,225,344,300,225,225,300,225,331,225,194,300,269,238,238,225,269,269,287,331,300,269,300,194,207,269,331,269,225,313,238,300,313,163,300,269,269,251,256,238,238,300,269,344,282,269,313,282,238,238,207,238,269,313,207,269,238,238,313,220,331,251,313,207,207,207,251,282,282,313,251,251,282,251,282,300,220,282,313,189,220,238,251,344,220,220,326,251,313,251,251,251,282,251,282,251,251,326,313,282,220,212,300,375,264,295,282,282,220,251,282,282,282,220,251,251,251,326,233,295,264,207,251,220,189,264,251,264,295,264,264,220,295,295,202,357,220,295,220,220,251,220,264,295,233,233,233,264,264,264,295,326,295,264,295,220,202,233,264,326,264,202,225,370,295,339,233,233,295,264,264,264,251,233,220,233,295,264,220,277,233,308,277,233,264,233,202,233,264,264,308,202,277,233,308,352,202,326,277,233,308,233,264,184,202,233,308,246,246,246,233,277,383,277,295,277,308,277,308,202,233,277,277,339,308,246,215,246,246,308,321,277,308,277,246,277,259,352,246,215,308,277,246,202,290,215,370,290,215,277,246,246,215,246,277,277,215,215,290,277,246,321,228,339,246,259,246,246,215,246,215,259,290,321,259,259,259,215,290,334,197,308,215,215,290,321,197,228,228,290,290,352,228,228,334,259,259,303,228,290,321,290,259,290,228,215,215,228,259,321,228,197,228,303,290,334,228,259,290,259,228,259,259,290,228,290,228,290,259,259,215,334,241,303,197,272,334,259,228,197,228,303,197,303,197,272,272,228,303,347,303,272,321,228,303,197,334,228,228,197,272,303,241,241,241,241,228,272,166,272,272,334,272,303,241,303,197,210,228,272,272,334,272,228,210,316,241,347,316,272,272,303,272,241,272,254,241,303,241,241,303,272,272,197,285,241,365,316,285,241,272,241,210,210,241,272,272,316,210,210,272,272,316,316,223,223,334,241,254,241,210,210,223,241,254,285,316,285,254,254,254,241,285,329,285,192,303,210,223,285,316,316,223,223,285,254,285,347,285,223,223,329,254,316,254,254,285,316,285,254,316,285,254,223,210,254,254,316,254,254,241,360,303,285,329,298,285,254,285,254,223,254,254,241,236,329,298,223,285,254,329,210,329,272,347,342,267,329,254,254,223,192,192,285,298,329,298,192,267,267,223,298,342,298,205,223,360,223,298,298,329,205,236,236,223,267,298,267,236,236,236,236,267,267,267,267,285,285,329,298,267,329,298,267,236,205,267,267,329,298,236,223,228,311,236,342,236,311,267,298,267,267,236,267,236,254,236,311,236,236,298,267,342,223,342,280,236,311,267,280,267,267,236,236,205,280,218,311,311,311,205,205,280,267,236,311,355,311,218,329,236,249,311,236,342,218,205,373,249,280,311,280,249,311,249,249,280,280,249,280,187,311,280,218,280,280,311,174,205,218,236,280,249,342,280,249,249,218,324,249,249,355,311,280,267,311,236,280,311,280,280,262,355,249,324,249,311,280,280,218,205,293,298,218,373,280,293,249,280,280,249,249,249,249,280,218,280,280,218,218,280,280,324,386,324,231,231,342,249,262,249,324,249,249,187,249,218,262,249,324,293,249,262,262,262,218,293,337,293,200,187,311,355,218,293,280,324,187,231,249,187,293,218,355,262,262,231,249,337,262,262,156,262,262,293,280,324,293,262,324,293,231,218,218,262,231,231,324,324,231,231,218,223,368,231,293,337,293,231,262,293,262,262,231,262,368,244,249,231,306,218,231,293,262,262,218,218,337,244,218,355,262,275,262,262,262,231,200,262,213,293,306,200,275,306,200,200,275,443,262,306,350,306,213,275,324,231,231,306,231,337,231,262,231,293,200,275,306,368,306,275,244,244,244,275,275,381,275,275,182,293,337,275,306,275,200,306,275,231,231,169,275,275,337,337,306,306,213,275,319,244,244,350,306,319,275,275,306,275,244,244,275,275,257,244,350,306,244,244,306,275,275,275,182,213,293,244,368,319,213,288,213,244,275,244,244,213,275,244,275,231,275,319,275,213,288,275,275,319,244,319,319,226,288,337,244,257,244,244,244,213,213,275,244,213,257,244,288,319,288,257,257,257,257,213,288,288,332,288,195,306,213,350,319,288,213,319,257,195,226,244,213,288,257,288,350,257,257,226,244,332,275,257,319,301,332,200,288,257,319,288,257,257,319,288,257,213,226,195,257,257,257,319,288,226,213,244,226,306,257,288,332,288,301,288,257,288,257,257,226,226,257,363,288,226,239,288,226,226,226,288,257,257,213,213,332,275,239,257,345,257,270,332,226,257,226,257,195,270,288,270,301,195,270,301,195,270,270,270,257,226,301,345,301,239,208,319,270,226,332,301,301,226,332,301,257,226,288,226,270,301,301,270,270,239,239,239,407,270,270,270,270,270,270,288,301,332,270,301,270,332,301,239,226,226,239,270,270,239,270,332,270,239,301,239,231,314,239,239,345,283,314,270,270,270,301,270,270,239,239,270,239,252,257,239,345,239,226,239,314,270,270,345,226,345,416,239,226,363,345,270,283,270,239,270,252,239,208,270,221,239,270,270,270,314,283,208,208,283,283,270,239,314,195,358,314,221,221,332,239,252,252,314,208,345,208,221,208,252,208,252,283,314,314,283,252,314,239,252,252,239,283,283,389,327,283,190,283,301,345,239,221,283,283,314,314,283,239,221,239,283,252,283,283,345,314,252,283,221,270,327,252,252,314,358,314,327,283,252,314,252,283,252,252,314,283,252,265,252,358,252,327,252,252,314,283,283,283,283,239,221,358,301,221,376,265,283,296,283,252,283,283,252,252,221,221,314,221,283,239,283,327,296,221,221,283,252,283,252,327,389,398,234,270,252,345,340,252,265,252,327,252,252,221,221,190,252,190,327,296,221,327,265,296,296,265,265,265,252,221,296,296,340,296,203,203,203,314,358,221,221,296,296,283,327,190,252,234,252,296,221,265,296,296,358,234,265,234,234,252,265,265,265,265,327,265,265,265,296,296,327,265,296,265,265,327,296,234,265,221,234,203,265,371,265,265,327,296,234,203,221,234,234,371,234,234,296,340,234,309,265,265,234,296,265,265,265,296,265,265,234,252,203,247,340,234,234,327,234,296,265,265,340,203,221,340,278,247,203,309,265,265,278,265,265,221,265,234,234,265,203,278,234,265,309,172,309,309,278,203,278,278,278,265,234,265,309,371,353,309,216,216,327,278,234,247,234,309,203,234,340,203,265,234,265,371,247,278,234,309,371,278,247,309,265,247,247,234,278,278,278,384,278,353,278,247,309,340,278,309,278,278,185,309,247,278,234,234,234,234,278,247,278,278,340,278,309,278,247,216,239,322,247,247,247,353,247,322,322,278,278,247,309,234,278,247,309,247,278,247,309,247,353,247,322,247,234,247,322,278,278,247,278,216,265,353,296,216,247,371,322,353,291,229,247,247,278,278,260,247,247,247,216,309,247,278,234,278,322,322,291,216,291,291,260,278,247,322,322,384,322,229,229,229,340,291,247,260,260,247,322,247,247,216,247,229,247,185,216,291,291,247,322,322,291,260,322,260,260,260,260,229,216,291,260,335,353,291,198,260,309,353,216,291,229,291,278,291,322,260,247,229,216,247,247,291,260,260,291,353,260,322,260,229,229,247,335,278,291,260,322,304,322,335,291,291,291,322,229,291,291,260,260,322,291,229,260,216,216,322,260,260,366,229,260,322,291,260,291,229,198,247,229,366,309,229,291,335,291,291,304,291,260,198,291,260,260,260,229,291,260,260,366,291,247,229,242,304,291,229,229,229,304,260,260,260,335,216,216,335,335,260,242,353,304,260,260,273,260,335,229,260,304,229,229,229,260,211,291,273,304,304,198,260,304,273,198,198,273,273,441,260,260,304,304,198,348,304,304,211,273,322,273,229,242,273,304,304,198,335,229,198,260,242,242,291,198,229,273,304,304,366,304,273,304,242,242,242,242,229,273,273,273,379,273,273,348,180,304,291,335,198,304,304,273,273,335,304,304,273,229,198,229,229,211,273,260,348,273,335,304,304,304,304,379,242,273,379,322,242,242,304,348,286,317,273,304,273,242,304,273,273,242,242,242,255,273,379,255,304,198,348,304,348,242,229,242,317,317,273,273,273,348,229,229,419,286,291,242,211,366,317,348,286,286,273,273,255,273,242,242,361,242,242,273,242,242,273,273,180,273,286,317,286,211,211,211,286,286,273,242,317,317,198,361,317,242,317,224,335,330,242,242,255,286,317,242,304,348,242,211,286,242,242,255,211,255,286,242,317,317,255,286,255,317,348,255,255,255,361,286,286,286,255,392,286,286,193,193,304,211,348,211,224,317,286,286,286,317,317,286,242,242,211,242,211,286,255,211,286,286,348,255,286,286,317,224,255,242,330,273,286,255,317,361,255,317,330,224,286,286,255,317,255,286,423,255,330,317,286,286,255,242,211,361,317,255,330,255,255,255,255,317,286,286,286,361,286,242,242,361,304,255,224,379,330,268,286,299,286,286,255,224,286,255,255,374,255,224,224,255,361,255,286,317,224,286,330,299,299,224,224,224,299,255,286,255,255,330,211,211,330,237,273,237,237,348,343,255,255,268,255,330,255,255,255,224,255,224,224,255,268,193,286,268,299,193,330,330,299,268,299,193,268,268,268,436,255,224,224,299,361,343,299,299,206,206,206,317,268,361,224,237,330,299,299,206,268,330,193,299,255,237,255,286,193,260,268,268,299,299,361,299,237,361,237,255,237,255,237,405,299,268,268,162,312,268,268,268,299,286,299,281,330,268,299,193,268,268,330,299,299,268,268,224,224,268,224,343,268,374,255,268,268,330,299,299,299,299,299,237,255,237,374,317,237,255,299,343,237,299,312,387,268,268,237,299,268,268,268,268,237,237,250,268,206,250,250,255,237,193,343,312,237,237,237,330,312,281,299,268,268,343,224,224,343,414,281,250,237,206,361,312,343,268,281,268,268,343,224,268,237,250,237,268,206,268,281,237,299,237,312,206,206,312,312,312,206,206,206,281,281,281,449,237,268,312,312,312,374,312,312,219,219,219,330,281,237,237,250,250,312,312,237,312,343,343,206,219,268,237,250,374,206,312,281,237,312,312,374,281,250,281,312,268,250,250,250,250,237,281,281,281,343,387,281,343,281,188,299,312,294,343,206,281,312,281,281,281,281,343,312,250,281,237,219,219,237,206,281,250,262,281,281,343,281,281,312,281,312,237,219,268,242,325,250,281,250,281,356,294,263,325,325,281,268,281,219,312,250,250,281,418,250,312,250,281,281,281,312,250,206,356,312,312,325,250,356,250,250,312,281,281,281,281,219,356,237,237,356,356,299,250,219,237,374,263,281,281,294,281,281,250,232,281,281,263,250,219,250,219,281,232,312,219,281,281,237,219,281,281,325,294,219,219,312,294,281,343,281,250,250,325,325,387,369,396,232,268,250,232,343,338,250,250,263,338,250,250,325,312,250,356,219,250,232,219,188,250,201,281,325,294,294,219,325,325,294,294,263,387,325,263,263,263,263,250,219,294,294,294,263,400,294,294,294,201,325,294,312,219,356,219,232,219,294,294,219,294,325,325,263,250,219,232,263,250,219,294,294,263,263,294,294,356,294,232,325,294,232,232,232,250,232,338,281,263,263,263,325,307,263,325,338,263,294,263,294,276,325,263,263,294,232,263,263,325,294,294,232,263,263,219,232,232,325,263,263,232,369,250,263,338,325,294,263,232,263,369,294,232,250,232,369,312,263,232,250,387,338,276,294,307,263,294,276,263,232,294,263,232,263,276,232,232,294,263,263,369,232,294,294,294,294,232,338,294,232,338,232,325,307,294,263,263,263,263,338,338,219,219,338,338,281,245,232,245,356,351,263,263,276,276,263,263,338,219,263,263,307,232,232,263,201,263,276,201,294,276,307,307,280,201,307,276,307,276,201,201,276,276,276,276,444,232,232,263,307,307,369,351,307,307,307,214,214,276,325,276,232,232,245,245,276,307,307,201,232,338,338,201,263,263,245,232,263,369,201,307,276,232,276,307,276,369,276,307,276,369,307,245,245,294,263,413,232,276,276,276,276,382,276,276,276,351,170,294,294,307,276,338,276,307,307,276,276,276,263,276,307,307,245,276,232,214,232,232,232,276,276,263,245,276,276,338,338,307,307,307,307,307,232,294,245,276,382,237,245,245,245,245,351,289,289,307,320,276,276,245,276,214,307,245,276,276,276,245,245,307,245,276,276,382,245,307,263,201,351,276,351,320,245,245,232,338,245,320,276,276,276,276,276,351,232,263,232,422,289,294,214,245,214,369,320,258,351,276,289,382,276,351,245,214,276,276,258,245,245,258,245,245,289,214,245,307,245,276,232,183,320,276,320,320,276,320,214,214,289,289,276,338,276,245,245,320,320,214,382,364,391,320,227,227,201,289,338,333,245,382,245,258,258,320,320,245,307,320,351,214,245,214,276,245,245,258,307,320,320,289,289,320,320,320,320,289,289,320,289,320,258,258,258,276,426,258,245,214,320,289,289,232,395,351,289,289,289,196,289,307,214,289,351,214,289,320,227,289,289,320,289,320,320,258,289,214,214,227,258,245,183,245,289,258,227,258,289,289,351,289,289,320,258,289,245,227,227,276,227,333,276,395,289,258,258,320,364,302,320,333,258,289,320,276,289,258,320,258,289,289,289,426,258,258,320,289,289,227,258,271,258,214,227,258,320,271,333,258,364,258,258,258,320,320,289,289,227,289,364,289,245,245,245,227,364,307,271,227,245,382,333,271,289,289,302,302,289,364,258,245,227,333,258,258,258,377,258,302,289,227,240,258,364,227,289,245,196,227,289,227,333,289,302,214,227,320,227,302,289,470,289,258,258,258,333,227,214,214,333,333,276,240,258,240,214,351,346,258,258,258,271,364,258,333,258,395,258,258,302,227,258,196,227,196,258,271,209,289,271,302,302,302,209,333,333,271,302,271,302,196,271,271,271,271,271,439,258,227,258,227,302,302,364,346,302,302,302,302,209,333,271,320,271,364,227,227,240,333,271,302,302,196,227,271,333,271,302,302,258,240,271,258,240,289,196,302,271,240,271,302,302,364,302,302,240,271,364,240,408,240,258,240,302,408,196,302,302,271,271,333,377,333,271,271,346,196,302,271,302,284,333,196,271,302,302,377,271,271,271,333,302,302,240,271,271,271,209,227,240,333,271,346,271,258,240,346,271,271,333,271,302,302,302,302,302,377,209,240,258,271,240,377,320,258,240,240,302,346,284,284,302,315,240,302,271,284,271,253,302,271,271,240,271,240,333,240,302,240,271,271,377,240,302,302,258,196,346,196,240,346,240,240,227,240,333,240,315,302,271,271,271,271,302,346,227,227,227,346,417,284,289,253,240,253,227,364,315,346,271,271,284,240,271,271,346,253,240,271,240,315,240,302,359,209,209,271,284,222,240,302,307,315,271,178,209,315,240,315,346,271,284,209,284,284,240,284,271,452,271,240,240,240,315,315,271,377,359,315,315,240,315,209,222,284,333,328,240,240,240,253,253,284,315,315,240,302,240,346,346,209,209,271,284,240,240,253,377,302,209,315,284,284,240,315,315,315,284,284,315,253,284,315,253,346,253,253,253,421,359,240,284,284,284,284,346,390,328,284,284,359,284,191,315,284,315,209,346,209,209,271,315,315,284,284,284,271,284,315,315,253,284,284,240,222,209,253,240,222,284,284,253,253,265,284,284,284,359,284,346,315,253,284,315,284,222,253,271,271,245,328,209,284,284,253,253,315,359,297,253,315,328,253,284,284,253,284,222,315,284,284,253,284,284,421,253,328,315,253,284,284,222,284,266,266,253,209,359,315,315,359,328,222,359,253,253,346,253,315,253,284,315,284,284,284,359,284,271,240,240,253,359,253,302,253,253,240,377,328,266,266,284,284,297,235,284,284,359,240,222,284,284,253,266,253,372,253,297,222,284,235,222,315,359,253,328,235,315,222,284,284,297,328,297,297,328,222,222,315,297,297,346,297,284,253,253,253,328,328,222,390,372,399,328,235,271,235,253,235,235,346,341,253,253,253,315,266,359,253,328,253,209,328,253,222,222,222,253,235,253,253,253,266,266,204,284,328,289,297,297,270,328,328,191,297,297,328,266,297,328,191,266,266,266,266,434,266,372,222,266,297,297,297,359,341,297,297,359,297,204,191,328,266,315,266,297,359,222,235,235,328,222,297,297,191,284,222,328,328,266,297,297,253,315,222,266,253,284,297,235,297,266,284,297,297,297,297,359,266,297,328,328,359,235,328,235,235,284,235,297,403,284,266,297,266,266,266,328,310,328,297,328,266,266,222,297,266,297,297,266,328,191,297,204,297,235,266,266,266,328,266,297,297,279,266,266,372,266,222,235,266,222,328,341,266,235,372,235,266,266,266,341,266,297,297,297,297,297,297,372,253,253,253,227,235,372,315,235,235,235,279,235,297,341,279,403,297,310,385,266,372,279,266,248,235,297,297,266,235,266,235,279,235,235,297,235,266,266,372,235,248,297,253,191,235,235,248,235,341,297,310,235,235,235,328,235,310,297,266,297,297,266,235,266,341,341,222,222,222,412,341,279,341,248,266,248,222,359,310,266,341,266,266,279,235,266,341,341,266,204,235,341,235,310,235,266,354,266,235,204,266,279,204,235,297,279,310,310,310,266,204,310,235,279,310,279,279,310,204,279,279,279,279,279,279,447,266,235,235,266,310,310,310,266,372,354,310,310,248,310,217,217,217,279,328,323,235,372,235,248,248,248,235,310,310,310,279,310,310,341,341,204,204,217,266,248,235,235,266,372,204,248,310,235,279,279,266,310,310,372,279,279,310,271,279,310,279,310,248,248,248,310,266,271,354,235,279,279,279,279,341,341,385,279,279,341,354,279,279,310,248,310,204,292,341,374,279,310,310,310,279,279,279,310,279,279,341,310,248,248,279,235,235,217,235,235,235,235,217,279,279,266,248,279,279,279,279,341,279,310,279,310,310,279,310,279,217,217,266,266,279,248,385,328,248,279,248,279,248,310,354,248,248,310,323,323,279,279,310,292,279,217,248,310,279,279,248,279,248,416,248,248,310,248,248,279,279,261,279,261,310,279,310,217,354,310,248,354,323,248,248,354,248,323,341,248,323,248,279,279,279,279,248,279,354,354,235,266,235,354,425,354,297,261,248,248,217,235,372,323,261,416,279,235,292,248,279,279,354,248,230,235,279,279,248,261,248,248,261,248,248,217,279,217,230,248,310,217,248,279,279,310,279,217,323,217,323,323,279,292,217,217,217,310,292,292,292,341,248,279,248,248,248,248,323,323,204,385,367,323,394,323,266,323,248,230,230,292,341,336,230,248,292,248,261,336,248,248,323,323,248,310,248,248,354,354,217,248,279,336,217,248,248,261,385,310,279,204,323,292,292,265,217,323,292,323,292,292,323,323,292,385,323,261,354,199,295,261,261,429,261,230,217,292,323,292,292,292,354,398,292,354,292,292,292,199,323,305,261,310,217,217,354,217,217,292,230,323,217,292,292,217,279,292,292,323,323,261,292,292,248,217,230,248,261,248,230,292,248,292,261,261,230,261,292,292,261,367,292,261,292,323,261,292,261,292,318,230,279,248,230,248,398,323,261,292,292,261,261,261,323,305,305,367,323,274,336,230,292,292,261,292,292,274,323,292,292,292,261,292,261,261,261,261,261,323,261,292,292,230,230,292,323,323,217,217,261,261,323,261,323,336,261,261,367,261,248,261,261,336,323,305,292,292,230,292,292,336,367,292,248,230,248,222,230,367,248,310,261,248,230,274,385,292,336,292,292,292,230,305,261,292,292,274,261,261,243,336,292,261,261,230,261,380,274,230,230,230,292,230,261,261,199,367,230,336,292,323,292,292,336,292,336,336,305,292,305,336,230,230,323,305,305,305,305,261,305,261,261,261,261,336,336,230,230,217,380,336,336,336,279,243,261,261,243,217,354,349,305,261,261,261,261,274,230,261,261,336,336,261,398,261,261,367,305,230,261,390,248,261,199,199,261,274,212,212,292,274,336,305,305,305,278,261,336,336,199,305,305,336,274,305,336,199,199,274,274,274,274,274,442,261,230,230,305,230,305,305,323,186,367,349,305,305,305,230,305,212,212,212,274,323,274,274,367,274,230,230,243,336,274,305,305,305,230,292,305,336,336,336,274,199,305,318,261,243,230,230,261,367,292,199,305,305,274,274,199,274,305,305,305,367,274,274,305,336,274,274,367,305,261,243,243,292,305,243,261,411,230,230,274,274,274,274,274,336,380,336,305,274,336,349,274,305,181,305,274,305,199,287,336,369,199,305,212,305,380,243,274,274,274,336,274,274,305,305,243,274,274,274,230,230,212,243,274,230,274,274,349,274,261,261,212,349,274,274,274,336,336,287,305,274,305,305,274,305,274,380,212,292,261,261,274,243,380,212,323,274,274,243,243,243,305,349,243,287,411,305,318,243,274,305,274,380,287,274,243,305,274,274,274,243,274,274,243,274,243,243,305,305,256,274,274,256,380,243,256,305,336,305,305,349,274,305,305,349,318,243,318,243,243,243,336,243,318,318,318,274,274,305,274,274,274,274,349,212,230,261,230,349,420,349,349,292,256,243,274,230,230,367,274,318,256,411,274,274,367,287,380,274,274,349,243,256,225,274,274,243,243,256,243,274,362,243,243,212,243,274,287,225,243,305,287,310,274,318,230,274,274,349,318,243,318,318,287,274,287,318,212,212,212,287,287,287,274,362,243,287,243,243,243,287,318,318,318,212,380,362,318,389,318,243,225,318,243,225,225,287,336,331,287,243,380,287,349,256,256,256,287,318,318,243,243,305,243,318,349,349,243,287,243,199,287,243,243,243,243,256,380,318,424,194,318,287,287,318,287,318,318,318,318,287,287,380,318,279,287,318,181,318,349,256,256,256,274,424,287,243,424,212,287,318,287,287,287,256,349,393,287,349,287,287,362,287,318,194,318,287,305,318,212,305,349,212,212,287,287,318,318,287,287,287,274,318,287,287,318,318,256,256,287,300,243,243,225,243,256,243,243,181,349,287,287,256,256,225,287,274,287,287,287,349,287,300,349,362,318,256,287,318,287,243,225,225,274,274,248,243,393,274,393,287,287,287,256,256,318,318,362,300,287,256,318,331,256,225,318,318,256,287,287,225,274,318,287,287,287,305,287,287,424,256,256,331,256,318,256,287,287,287,225,256,256,318,256,256,318,256,362,212,318,318,362,331,256,256,362,256,243,349,349,256,331,331,269,287,318,287,287,287,287,287,362,362,243,243,243,243,256,256,362,256,305,269,287,256,225,243,380,287,331,269,269,287,287,300,300,256,287,362,362,256,256,238,243,331,287,256,256,269,256,256,375,269,256,300,225,287,225,238,256,256,362,300,256,287,287,243,318,331,287,287,256,256,331,300,287,300,225,212,225,225,318,225,225,300,287,300,468,300,256,256,256,256,256,331,331,225,287,393,375,331,402,331,238,274,331,256,238,238,238,349,256,344,256,256,256,256,256,269,238,362,256,256,331,256,256,393,256,256,362,300,238,225,256,331,194,225,194,256,256,331,269,207,207,437,207,331,256,300,300,256,207,331,331,331,194,300,300,269,300,269,300,393,269,194,269,269,269,269,269,269,437,256,256,225,300,331,300,300,300,300,362,362,344,300,344,300,356,207,300,207,194,331,269,269,318,269,269,362,269,225,225,287,238,331,269,300,300,300,225,225,300,300,331,331,331,269,269,300,207,313,256,238,225,269,300,238,287,300,375,300,269,269,269,300,269,300,300,300,300,362,300,269,300,331,331,269,362,238,269,406,238,300,238,256,238,256,300,406,225,269,300,300,269,269,287,225,331,375,331,313,269,269,269,344,269,269,300,331,269,300,300,282,269,331,437,269,300,238,300,375,238,269,269,269,269,331,269,269,300,300,300,282,269,269,282,331,225,225,225,269,269,468,269,344,344,331,331,269,375,269,344,269,269,269,344,331,269,300,300,300,269,300,300,300,269,375,238,238,256,256,207,269,375,375,269,318,282,269,269,238,282,238,393,344,300,282,269,406,300,313,238,388,300,282,251,282,269,251,251,300,300,269,269,269,238,269,269,238,331,238,313,300,300,238,251,331,269,269,375,313,251,300,269,256,300,238,238,344,194,238,344,406,300,238,238,225,238,238,238,331,238,313,313,313,269,269,300,269,269,238,300,269,344,238,225,225,406,388,344,415,344,282,287,251,251,225,238,251,225,362,313,357,251,344,269,269,251,362,282,375,269,269,269,344,269,220,238,269,269,238,313,251,238,238,300,357,269,238,238,269,344,282,269,220,238,300,344,305,313,313,313,269,269,207,344,313,238,207,313,313,344,269,313,313,450,282,300,282,238,282,282,282,357,450,269,238,238,238,313,238,313,313,313,313,269,375,357,313,313,313,369,220,313,220,238,220,331,282,331,326,282,220,375,282,238,238,251,326,251,282,313,313,313,313,300,313,238,313,344,344,282,282,207,269,313,282,238,251,238,282,269,251,375,419,207,251,313,282,282,251,274,269,313,313,282,375,313,282,282,375,251,344,282,313,251,282,344,251,251,251,251,251,419,251,274,357,220,282,282,282,282,282,282,251,344,388,326,282,313,282,344,357,282,329,238,313,300,282,313,295,295,282,344,207,207,295,238,220,313,251,282,282,282,282,313,282,282,344,313,313,313,251,207,282,282,525,238,220,238,251,282,313,344,269,220,282,282,269,251,388,263,269,282,282,282,282,357,282,282,344,282,313,251,251,282,313,282,238,220,220,269,269,269,243,282,326,388,220,331,282,282,251,251,282,251,313,357,295,295,313,357,313,326,326,401,282,282,313,251,282,269,220,176,313,313,282,282,251,264,282,282,419,282,282,326,251,313,251,251,282,282,282,264,251,313,264,313,313,282,207,207,251,357,264,313,313,357,326,251,251,357,357,251,251,344,344,264,326,326,326,282,282,313,282,282,282,313,282,357,357,220,269,269,238,238,357,428,357,357,264,300,264,251,251,238,264,238,388,326,326,264,357,282,282,264,375,295,251,282,282,282,357,251,282,233,251,282,282,251,251,264,251,251,251,370,251,251,295,220,282,295,233,233,251,313,357,251,251,282,326,220,313,282,220,220,326,251,326,295,326,295,220,295,326,220,220,220,313,295,251,295,295,282,344,251,295,282,251,251,326,251,326,326,326,220,282,388,370,370,397,326,326,233,269,326,233,251,207,233,295,344,295,339,251,326,251,251,251,313,264,339,357,264,326,326,326,251,313,388,326,251,357,357,295,238,220,326,282,233,295,220,264,251,264,282,264,202,202,432,264,326,295,295,295,326,295,251,326,326,326,220,326,295,295,326,326,264,295,388,326,264,357,264,220,264,264,264,264,432,264,251,370,233,295,295,326,295,295,295,295,357,233,401,295,357,295,357,295,295,202,189,295,326,308,295,313,326,264,220,357,220,220,344,295,233,326,326,220,295,295,295,282,202,282,295,295,326,326,326,264,264,295,295,251,251,313,251,251,264,251,251,233,282,295,370,295,264,264,282,282,295,264,295,295,295,295,370,295,264,326,295,326,326,264,357,295,264,401,321,233,233,282,282,282,256,295,401,282,189,264,295,264,264,264,264,264,326,370,308,326,308,370,326,277,339,264,233,277,295,326,264,295,295,277,264,326,326,251,295,295,264,295,295,264,264,264,264,264,264,326,264,264,295,295,295,264,277,264,295,370,326,264,264,220,233,264,220,326,264,326,326,339,264,233,264,370,282,251,233,264,264,264,339,326,264,295,295,339,295,295,295,264,295,370,370,295,251,233,251,251,220,225,233,370,251,313,233,383,401,233,233,277,233,388,295,339,295,277,401,295,295,308,233,383,264,295,370,277,264,264,233,246,251,295,295,264,264,233,246,264,339,383,326,264,233,233,233,295,233,246,264,264,417,370,308,233,246,339,246,264,326,295,295,295,295,189,233,295,339,370,295,308,233,339,233,308,233,326,233,233,308,295,277,476,264,308,264,264,264,295,264,339,339,339,220,233,220,220,383,339,410,339,277,401,282,246,233,264,246,246,220,357,308,352,264,339,264,264,264,233,277,277,370,277,264,339,264,339,264,220,233,233,264,339,233,308,251,233,264,233,393,264,233,202,233,264,339,277,277,277,215,233,295,339,308,308,308,264,339,295,264,432,308,339,202,233,308,308,339,308,277,308,277,189,339,277,277,277,277,277,277,277,277,445,308,383,326,233,308,264,233,308,308,308,308,264,370,202,352,308,308,308,364,308,308,215,202,202,339,215,277,326,233,321,233,233,370,233,233,476,246,246,339,277,277,308,308,308,383,233,295,308,308,339,339,339,277,202,202,308,308,339,264,326,264,233,264,246,264,370,308,246,202,246,308,277,277,277,202,277,264,308,308,277,308,370,308,277,277,308,339,339,277,370,339,277,308,414,246,295,246,295,308,246,269,246,414,233,202,277,277,321,277,277,277,277,339,339,383,339,277,277,277,430,339,352,277,308,445,308,295,246,295,308,277,290,295,339,372,202,277,308,277,308,308,383,277,277,277,277,277,308,339,277,339,308,308,308,189,246,277,277,277,339,264,233,233,233,277,233,233,339,277,339,352,277,277,277,383,238,277,352,277,277,277,277,352,339,277,290,308,352,308,308,308,383,308,308,277,383,215,264,295,264,264,264,277,246,383,264,238,326,277,277,277,246,277,246,246,308,352,290,246,290,308,259,308,321,321,246,414,308,308,277,383,308,277,215,246,246,308,277,414,277,277,259,277,277,246,414,277,246,246,246,308,246,246,259,277,277,277,383,215,308,246,308,308,277,339,308,308,215,352,277,308,246,352,246,321,246,321,246,352,264,246,246,339,246,246,321,321,321,277,277,308,277,277,277,277,308,277,352,352,352,233,233,264,233,233,352,423,246,352,246,295,290,246,246,246,233,259,233,370,277,383,277,259,414,277,277,215,290,290,246,383,277,277,352,352,246,259,228,228,246,277,277,246,321,259,246,246,246,365,259,277,246,308,277,246,277,308,228,215,228,246,308,215,321,246,277,321,246,308,277,215,352,321,277,215,321,321,321,290,277,290,290,321,458,215,215,308,290,352,290,290,277,290,339,246,277,246,246,246,246,277,290,321,321,321,321,202,383,383,365,321,392,321,321,321,264,321,334,246,391,228,228,290,339,277,334,290,246,246,383,246,246,246,259,259,334,290,246,321,321,321,246,246,308,383,246,321,352,352,352,290,290,321,277,321,334,277,215,246,246,246,215,259,383,321,321,427,259,321,290,290,290,246,321,263,290,321,321,290,321,383,290,321,290,383,321,308,290,282,383,259,259,352,259,197,293,259,259,321,259,427,290,246,365,228,246,290,321,290,290,290,290,290,352,352,396,334,290,352,290,352,290,290,290,215,290,321,308,259,290,308,321,215,197,290,352,215,215,215,290,290,228,321,321,215,290,290,290,277,321,277,290,290,321,321,321,321,259,259,290,290,290,352,246,290,228,246,259,228,246,246,166,290,352,365,290,290,259,277,277,290,259,259,290,290,290,365,365,290,290,259,352,290,321,321,290,352,290,321,321,321,316,277,228,277,277,277,246,246,259,396,277,321,396,290,290,290,259,259]
cache = [0] * 1000000

def collatz_read (r) :
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        yield [b, e]
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval ((i, j)) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    assert i < 1000000
    assert j < 1000000

    #swap if numbers aren't in chronological order
    if i > j:
        working_num = j
        j = i
        i = working_num
    
    v = 1

    #if j/2 > we can start tallying cycle lengths from j/2
    if(j >> 1) > i:
        i = j >> 1


    if (j - i) > 125:
        meta_index_1 = i/125
        meta_index_2 = j/125
  
        while i % 125 != 0:
            working_num = i
            cycle = 1
            while working_num > 1:
                if working_num < 1000000 and cache[working_num] != 0:
                           cycle += cache[working_num] - 1
                           break
                elif working_num % 2 == 0:
                    working_num = working_num >> 1
                    cycle += 1
                else:
                    working_num = working_num + (working_num >> 1) + 1
                    cycle += 2

            cache[i] = cycle
            if cycle > v:
                v = cycle
            i += 1

        meta_index_1 += 1 #increment since we calculated cycle lengths to an increment on 125
        while meta_index_1 < meta_index_2 :
            if meta_cache[meta_index_1] > v:
                v = meta_cache[meta_index_1]
            meta_index_1 += 1
        start = (125 * meta_index_2)
    else:
        start = i

    while start <= j:
        working_num = start
        cycle = 1
        while working_num > 1:
            if working_num < 1000000 and cache[working_num] != 0:
                       cycle += cache[working_num] - 1
                       break
            elif working_num % 2 == 0:
                working_num = working_num >> 1 
                cycle += 1
            else:
                working_num = working_num + (working_num >> 1) + 1
                cycle += 2

              
        cache[start] = cycle
        if cycle > v:
            v = cycle

        start+= 1

    assert v > 0
    return v


# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """

    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)


collatz_solve(sys.stdin, sys.stdout)