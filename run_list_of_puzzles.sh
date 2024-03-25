#!/bin/bash
# $var = 0
while read p; do
  bash ./run_single_puzzle.sh "$p"
  ((var++))
  echo $var
  # if [[ $var == 100 ]]
  # then
  #   break 1
  # fi
done <${1}
python3 process_stats.py tmp/stats.txt ${2}