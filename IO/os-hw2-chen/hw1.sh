#!/bin/bash

for size in 10 20 30 40 50 60 70 80 90 100 200 300 400 500 600 700 800 900 1000
do
  echo "${size}MB"
  echo -e "${size}\n1\n2\n3\n4\n3\n8\n3\n16\n3\n32\n0" | ./hw1
done
