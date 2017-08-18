#!/bin/bash


#source activate cntk-py36

python ../synthia-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/SYNTHIA/Annotations-bbox/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/SYNTHIA/RGB/detection_csv  -output ../evaluation-results/synthia-out.txt

python ../plot-results.py -resfile "../evaluation-results/synthia-out.txt"

