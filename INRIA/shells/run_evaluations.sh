#!/bin/bash


python ../inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/INRIA/inriacode/Test/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/Test/pos/detection_csv   -output ../evaluation-results/inria-test-out2.txt

python ../plot-results.py -resfile "../evaluation-results/inria-test-out2.txt"


python ../inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/INRIA/inriacode/Train/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/Train/pos/detection_csv   -output ../evaluation-results/inria-train-out2.txt

#python ../plot-results.py -resfile "../evaluation-results/inria-test-out2.txt"

python ../plot-results.py -resfile "../evaluation-results/inria-train-out2.txt"


