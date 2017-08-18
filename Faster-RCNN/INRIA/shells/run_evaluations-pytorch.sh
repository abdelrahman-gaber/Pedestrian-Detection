#!/bin/bash


python ../inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/INRIA/inriacode/Test/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/frcnn-pytorch-new/Test/pos/detection_csv   -output ../evaluation-results/inria-test-pos-pytorch.txt

python ../plot-results.py -resfile "../evaluation-results/inria-test-pos-pytorch.txt"


python ../inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/INRIA/inriacode/Train/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/frcnn-pytorch-new/Train/pos/detection_csv   -output ../evaluation-results/inria-train-pos-pytorch.txt

#python ../plot-results.py -resfile "../evaluation-results/inria-test-out2.txt"

python ../plot-results.py -resfile "../evaluation-results/inria-train-pos-pytorch.txt"


