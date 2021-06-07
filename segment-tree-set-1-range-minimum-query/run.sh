#!/usr/bin/env bash

res=$(java ./main.java <./in.txt)
colordiff -u ./out.txt <(echo "$res")
