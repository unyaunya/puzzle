#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def factoradic(n):
    """指定された自然数nを、階乗進法で表した配列を返す
        ex) n = 85 ==> 85=3*4!+2*3!+0*2!+1*1! なので
                       [3,2,0,1]を返す
    """
    rslt = []
    (r, m) = divmod(n, 2)
    rslt.append(m)
    n = n - m
    k = 2
    fact_k = k
    #import pdb; pdb.set_trace();
    while n != 0:
        r = n / fact_k
        a = r % (k+1)
        rslt.append(a)
        #print n, k, fact_k, r, a, rslt
        n = n - a * fact_k
        k = k + 1
        fact_k = k * fact_k
    rslt.reverse()
    return rslt
    
def k_factoradic(k, n):
    """k桁の階乗進を表す配列を作成する"""
    rslt = factoradic(n)
    l = len(rslt)
    if l < k:
        l = ([0]*(k-l))
        l.extend(rslt)
        return l
    else:
        return rslt[-k:]

def permute(sqquence, factor):
    """sequenceを入替えた順列を作成する、factorは階乗進で表した並べ方を示す"""
    k = len(sqquence)
    f = k_factoradic(k-1, factor)
    #print sqquence, f
    rslt = []
    for i in range(k-1):
        rslt.append(sqquence[f[i]])
        sqquence.pop(f[i])
        #print sqquence, rslt
    rslt.append(sqquence[0])
    #rslt.reverse()
    return rslt

def latin_square(k, row_factor=None, col_factor=None):
    """ラテン方陣を作成する"""
    sq = []
    row = range(1, k+1)
    if row_factor is not None:
        row = permute(row, row_factor)
    for i in range(k):
        sq.append(row)
        tmp = row[1:]
        tmp.append(row[0])
        row = tmp
    if col_factor is not None:
        sq = permute(sq, col_factor)
    return sq

def print_sq(sq):
    k = len(sq)
    for i in range(k):
        for j in range(k):
            print sq[i][j],
        print
            
def main():
    (k, row_factor, col_factor) = (5, None, None)
    argc = len(sys.argv)
    if argc >= 2:
        k = int(sys.argv[1])
    if argc >= 3:
        row_factor = int(sys.argv[2])
    if argc >= 4:
        col_factor = int(sys.argv[3])
    print_sq(latin_square(k, row_factor, col_factor))
    
if __name__ == "__main__":
    main()
