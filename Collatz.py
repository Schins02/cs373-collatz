#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


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

    global cache

    if i > j:
        i,j = j,i
    
    v = 1

    #if j/2 > i we can start tallying cycle lengths from j/2
    if(j >> 1) > i:
        i = j >> 1

    while i <= j:
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

            i+= 1

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
    


