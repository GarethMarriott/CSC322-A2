#!/bin/bash
rm -r tmp/puzzle_list.txt
rm -r tmp/stats.txt
bash puzzle_scraper.sh ${1}
bash run_list_of_puzzles.sh tmp/puzzle_list.txt ${2}