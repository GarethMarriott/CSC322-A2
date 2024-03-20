#!/bin/bash
for entry in "${1}"/*
do
  if [[ $entry != *"solution"* ]]; then
    echo "$entry" >> puzzle_list.txt
  fi
done