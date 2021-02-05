#!/usr/bin/env bash

res=$(python3 ./main.py <./in.txt)
colordiff -u ./out.txt <(echo "$res")
