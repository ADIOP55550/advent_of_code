#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("input.txt") as f:
        lines = f.readlines()

        prev = None
        totalInc = 0

        for line in lines:
            curr = int(line)
            if prev == None:
                prev = curr
                continue

            if prev < curr:
                totalInc += 1

            prev = curr

        print(totalInc)

if __name__ == '__main__':
    main()
