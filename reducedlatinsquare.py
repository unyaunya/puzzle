#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
import copy

class Square(object):
    def __init__(self, n):
        self.n = n
        self.rows = []
        self.status = 'unknown'
        for i in range(n):
            row = []
            for j in range(n):
                row.append(range(1,n+1))
            self.rows.append(row)
        self.row = 0
        self.col = 0

    def get(self, row, col):
        return self.rows[row][col]
        
    def next(self):
        self.col = self.col + 1
        if self.col >= self.n:
            self.col = 0
            self.row = self.row + 1
        if self.row >= self.n:
            self.row = -1
            self.col = -1

    def _set(self, row, col, value):
        self.rows[row][col] = value

    def _remove(self, row, col, value):
        v = self.get(row, col)
        if type(v) != list:
            return
        try:
            v.remove(value)
            #self.rows[row][col] = v
        except:
            pass
        if len(v) == 0:
            self.status = 'error'

    def set(self, row, col, value):
        v = self.get(row, col)
        for i in range(self.n):
            if i == col:
                continue
            self._remove(row, i, value)
        for i in range(self.n):
            if i == row:
                continue
            self._remove(i, col, value)
        self._set(row, col, value)

    def print_sq(self):
        for i in range(self.n):
            for j in range(self.n):
                print self.rows[i][j],
            print
    
    def clone(self):
        o = Square(0)
        o.n = self.n
        o.rows = copy.deepcopy(self.rows)
        o.status = self.status
        o.row = self.row
        o.col = self.col
        return o
    
    @staticmethod
    def initial(n):
        sq = Square(n)
        if n == 1:
            sq.set(0,0,1)
        else:
            for i in range(sq.n):
                sq.set(0,i,i+1)
                for i in range(sq.n):
                    sq.set(i,0,i+1)
            sq.row = 1
            sq.col = 1
        return sq


def ReducedLatinSquareGenerator(n):
    queue = [Square.initial(n)]
    while len(queue) > 0:
        e = queue.pop(0)
        if e.row == -1 and e.col == -1:
            if e.status == 'error':
                continue
            e.status = 'ok'
            yield e
        else:
            v = e.get(e.row, e.col)
            if type(v) == int:
                e.next()
                queue.insert(0,e)
                continue
            for i in range(len(v)):
                cp = e.clone()
                cp.set(cp.row, cp.col, v[i])
                if cp.status == 'error':
                    continue
                cp.next()
                queue.insert(i,cp)
        
def main():
    parser = argparse.ArgumentParser(
                description="""ラテン方格標準形作成""")
    parser.add_argument('-n', default=3,
                dest='size',
                type=int,
                help='方格の大きさ')
    args = parser.parse_args()
    if args.size <= 0:
        print "The size of latin-square must be more than zero."
    bar = "-"*args.size*2
    n = 0
    for e in ReducedLatinSquareGenerator(args.size):
        n = n + 1
        print bar
        print "No:%d" % n 
        print bar
        e.print_sq()
    print bar
    print u'The number of reduced latin squares of size %d = %d' % (args.size, n)
    
if __name__ == "__main__":
    main()
