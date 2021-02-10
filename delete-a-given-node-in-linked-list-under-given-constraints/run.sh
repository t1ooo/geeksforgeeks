#!/usr/bin/env bash

res=$(python3 ./main.py <./in.txt)
colordiff -wu ./out.txt <(echo "$res")
