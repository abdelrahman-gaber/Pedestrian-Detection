#!/bin/bash


#source activate cntk-py36

python ../caltech-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/caltech/annot-images/annotations/test -results /data/stars/user/aabubakr/pd_datasets/outputs/caltech/out-skip30/test  -output ../evaluation-results/caltech-test-out-person-only.txt

python ../plot-results.py -resfile "../evaluation-results/caltech-test-out-person-only.txt"

