#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    data = []
    data_raw = ""

    with open("input.txt", "r") as f:
        data_raw = f.readall()
        f.seek(0)
        data = f.readlines()
    
    ########
    result = ""



    print(result)


if __name__ == "__main__":
    main()
