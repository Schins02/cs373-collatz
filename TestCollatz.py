

#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz2 import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read(self) :
        r = StringIO.StringIO("250 250\n")
        t = collatz_read(r)
        (i, j) = t.next()
        self.assertTrue(i == 250)
        self.assertTrue(j == 250)

    def test_read_boundaries(self):
        r = StringIO.StringIO("1 999999\n")
        t = collatz_read(r)
        (i, j) = t.next()
        self.assertTrue(i == 1)
        self.assertTrue(j == 999999)


    def test_read3(self) :
        r = StringIO.StringIO("15 1\n")
        t = collatz_read(r)
        (i, j) = t.next()
        self.assertTrue(i == 15)
        self.assertTrue(j == 1)

    # ----
    # eval
    # ----

    def test_eval_1(self) : 
        v = collatz_eval(1 , 1)
        self.assertTrue(v == 1)


    def test_eval_2(self) :
        v = collatz_eval(19902, 63591)
        self.assert_(v == 340)

    def test_eval_3 (self) :
        v = collatz_eval(30, 8)
        self.assert_(v == 112)

    def test_eval_4 (self) :
        v = collatz_eval(1, 2)
        self.assert_(v == 2)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2, 2, 2)
        self.assert_(w.getvalue() == "2 2 2\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 7, 11, 7)
        self.assert_(w.getvalue() == "7 11 7\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2, 3, 999999)
        self.assert_(w.getvalue() == "2 3 999999\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 8, 0, 8)
        self.assert_(w.getvalue() == "8 0 8\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("84442 75795\n17 93\n85 4\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "84442 75795 351\n17 93 116\n85 4 116\n")

    def test_solve (self) :
        r = StringIO.StringIO("1 240\n122 9\n1 67 \n82 79 \n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 240 128\n122 9 21\n1 67 113\n82 79 111\n")

    def test_solve (self) :
        r = StringIO.StringIO("39 33\n19 226\n2 5\n900 1000\n7938 11909\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "39 33 35\n19 226 125\n2 5 8\n900 1000 174\n7938 11909 268\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
