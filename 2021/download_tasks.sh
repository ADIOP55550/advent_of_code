#!/bin/bash

year=2021

base_url="https://adventofcode.com/$year/day/"
session_cookie="$(cat ../.session_cookie)"

for i in {1..25}; do
  cd day$(printf %02i $i);
  # wget "$base_url$i";
  echo "DAY $i";
  echo "Getting task...";
  curl "$base_url$i" -o "task.html" -H "Cookie: session=$session_cookie";
  echo "Getting input...";
  curl "$base_url$i/input" -o "input.txt" -H "Cookie: session=$session_cookie";
  echo "Transforming task...";
  pandoc -f html -t markdown "task.html" -o "task.md";
  cd ..;
done;


