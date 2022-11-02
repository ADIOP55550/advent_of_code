#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        aim = 0
        x = 0
        depth = 0

        for line in lines:
            fc = line[0]
            if fc == 'u':
                # up
                aim -= int(line[2:])
            elif fc == 'd':
                # down
                aim += int(line[4:])
            else:
                # forward
                val = int(line[8:])
                x += val
                depth += aim * val
        print(f"{x=} {depth=} {x*depth=}")

if __name__ == '__main__':
    main()
