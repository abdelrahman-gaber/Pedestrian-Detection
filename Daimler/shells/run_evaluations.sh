#!/bin/bash


#source activate cntk-py36

python ../daimler-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/Daimler/DaimlerBenchmark/annotations-test-parsed -results /data/stars/user/aabubakr/pd_datasets/outputs/Daimler/TestData/detection_csv -output ../evaluation-results/daimler-test-evaluation-out.txt


python ../plot-results.py -resfile "../evaluation-results/daimler-test-evaluation-out.txt"

