#!/bin/bash
python3 kenken2smt.py <${1} >puz.smt
./mathsat -stats <puz.smt >model.smt
python3 smt2kenken.py <model.smt >result.txt