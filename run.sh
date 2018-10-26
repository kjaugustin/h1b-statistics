#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
# The command below runs the code. The first argument is the python3 file to execute. The second argument is the input file in the csv format. This input file needs to be placed in the ./input folder. The third and forth arguments are the output files and their expected order and the folder to place them. 
#
python3 ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt

