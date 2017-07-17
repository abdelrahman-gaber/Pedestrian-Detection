#!/bin/bash


#source activate cntk-py36


python ../inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/inriacode/Test/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/Test/pos/detection_csv   -output ../evaluation-results/inria-test-out.txt

python ../inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/inriacode/Train/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/Train/pos/detection_csv   -output ../evaluation-results/inria-train-out.txt

python ../plot-results-log.py -resfile "../evaluation-results/inria-test-out.txt"

python ../plot-results-log.py -resfile "../evaluation-results/inria-train-out.txt"


