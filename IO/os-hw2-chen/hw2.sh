#!/bin/bash

for size in 10 20 30 40 50 60 70 80 90 100 200 300 400 500 600 700 800 900 1000
do
  echo "${size}MB"
  echo -e "${size}\n3\n4\n4\n4\n8\n4\n16\n4\n32\n5\n0" | ./hw2
done
