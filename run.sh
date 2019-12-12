#!/bin/bash
# This file will run all the previous test and time the output of each test.

for f in *.py; do python3 "$f"; done
