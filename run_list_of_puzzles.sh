#!/bin/bash
while read p; do
  bash ./run_single_puzzle.sh "$p"
done <${1}