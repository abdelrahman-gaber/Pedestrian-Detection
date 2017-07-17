#!/bin/bash


python ../ethz-evaluation-all.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT -output ../evaluation-results/all-out.txt


python ../plot-results.py -resfile "../evaluation-results/all-out.txt"



