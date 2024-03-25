#!/bin/bash
# USAGE ex.  bash puzzle_scraper.sh puzzles/a/easiest
for entry in "${1}"/*
do
  if [[ $entry != *"solution"* ]]; then
    echo "$entry" >> tmp/puzzle_list.txt
  fi
done