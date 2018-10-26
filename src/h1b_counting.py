#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# h1b_counting.py : Report statistics on approved cases of H1B visa
# Author: Augustine Joseph
# Code skeleton from Insight Data Science Team
#
#################################################################################################################
#                                                                                                               #
#                                                                                                               #
#                           Statistics on CERTIFIED H1B visa applications                                       #
#                           Metrics calculated:                                                                 #
#                               1. Top 10 Occupations                                                           #
#                               2. Top 10 States                                                                #
#                                                                                                               #
#                                                                                                               #
#################################################################################################################
#                                                                                                               #
#                            How to run this code                                                               #
# python3 ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt#
#                                                                                                               #
#################################################################################################################

import sys
import csv
from collections import Counter





def top_jobs(data, fld, out1):

    jobs = Counter(k[fld] for k in data if k.get(fld))
    total = sum(jobs.values())
    most_jobs = jobs.most_common(10)
    #sort based on count first and then alphabetical order of top occupations
    most_jobs.sort(key=lambda pair: (-pair[1], pair[0]))

    with open(out1, 'w') as report_jobs:
        report_jobs.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

        for job, count in most_jobs:

            report_jobs.write('%s;%d;%.1f' % (job, count, count * 100 / total) + '%\n')


def top_states(data, fld, out2):

    states = Counter(k[fld] for k in data if k.get(fld))
    total = sum(states.values())

    most_states = states.most_common(10)
    #sort based on count first and then alphabetical order of top states
    most_states.sort(key=lambda pair: (-pair[1], pair[0]))


    with open(out2, 'w') as report_states:
        report_states.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

        for state, count in most_states:

            report_states.write('%s;%d;%.1f' % (state, count, count * 100 / total) + '%\n')


def main():

# Capture input and output files through command line arguments

    input_file = sys.argv[1]
    output1_file = sys.argv[2]
    output2_file = sys.argv[3]


    with open(input_file, encoding='utf-8') as inp:


        reader = csv.DictReader(inp, delimiter=';')

        data = [r for r in reader]

    # Care for difference in field names apprearing in 2014, 215 data.
    dict1 = data[0]
    if any('CASE_STATUS' in d for d in dict1):

        data[:] = [d for d in data if d.get('CASE_STATUS') == 'CERTIFIED']
        #field1 = 'CASE_STATUS'
        field2 = 'WORKSITE_STATE'
        field3 = 'SOC_NAME'
    else:
        data[:] = [d for d in data if d.get('STATUS') == 'CERTIFIED']
        #field1 = 'STATUS'
        field2 = 'LCA_CASE_WORKLOC1_STATE'
        field3 = 'LCA_CASE_SOC_NAME'



    top_jobs(data, field3, output1_file)
    top_states(data, field2, output2_file)


if __name__ == '__main__':
    main()
