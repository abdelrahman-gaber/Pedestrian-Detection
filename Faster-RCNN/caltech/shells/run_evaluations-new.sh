#!/bin/bash


#source activate cntk-py36

python ../caltech-evaluation-new.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/caltech/annot-new-sk30/annotations/anno_test_1xnew -results /data/stars/user/aabubakr/pd_datasets/outputs/caltech/out-skip30/test  -output ../evaluation-results/caltech-new-test-person-only.txt

python ../plot-results.py -resfile "../evaluation-results/caltech-new-test-person-only.txt"

