#!/usr/bin/env bash

declare -a answers=(10 35)
declare -i i=0
for line in $(python3 ./main.py <./in.txt); do
    ((line == answers[i])) && status="ok" || status="fail"
    echo "$status: out=$line, expected=${answers[i]}"
    ((i++))
done
