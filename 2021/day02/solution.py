#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        x = 0
        y = 0

        for line in lines:
            fc = line[0]
            if fc == 'u':
                y -= int(line[2:])
            elif fc == 'd':
                y += int(line[4:])
            else:
                x += int(line[8:])
        print(f"{x=} {y=} {x*y=}")

if __name__ == '__main__':
    main()
