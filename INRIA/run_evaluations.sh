#!/bin/bash


source activate cntk-py36


python inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/inriacode/Test/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/Test/pos/detection_csv   -output inria-test-out.txt

python inria-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/inriacode/Train/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/INRIA/Train/pos/detection_csv   -output inria-train-out.txt

python plot-results.py -resfile "inria-test-out.txt"

python plot-results.py -resfile "inria-train-out.txt"


