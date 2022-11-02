#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def main():
    with open("input.txt") as f:
        lines = f.readlines()

        prev = deque()
        curr = deque()
        totalInc = 0
        firstCurr = True
        c = None

        for line in lines:
            c = int(line)
            if len(prev) < 3:
                prev.append(c)
                continue

            if firstCurr:
                firstCurr = False
                curr = prev.copy()
                curr.popleft()
                curr.append(c)
            
            if sum(prev) < sum(curr):
                totalInc += 1

            prev.popleft()
            prev.append(curr[2])
            curr.popleft()
            curr.append(c)


        print(totalInc)

if __name__ == '__main__':
    main()
