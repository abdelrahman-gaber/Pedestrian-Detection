#!/bin/bash


python ../caltech-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/caltech/annot-images/annotations/test -results /data/stars/user/aabubakr/pd_datasets/outputs/caltech/out-skip30-pytorch/test  -output ../evaluation-results/caltech-test-reasonable-pytorch.txt

python ../plot-results.py -resfile "../evaluation-results/caltech-test-reasonable-pytorch.txt"

