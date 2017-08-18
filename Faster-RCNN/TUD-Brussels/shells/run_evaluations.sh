#!/bin/bash


#source activate cntk-py36

# positive
python ../tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-MotionPairs/positive/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-MotionPairs/positive/detection_csv  -output ../evaluation-results/TUD-MotionPairs-pos-out.txt

python ../tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-MotionPairs/negative/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-MotionPairs/negative/detection_csv  -output ../evaluation-results/TUD-MotionPairs-neg-out.txt

python ../tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-MotionPairs/additional-negative-bootstrap/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-MotionPairs/additional-negative-bootstrap/detection_csv  -output ../evaluation-results/TUD-MotionPairs-additional-out.txt

python ../tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-Brussels/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-Brussels/detection_csv  -output ../evaluation-results/TUD-Brussels-out.txt


python ../plot-results.py -resfile "../evaluation-results/TUD-MotionPairs-pos-out.txt"
python ../plot-results.py -resfile "../evaluation-results/TUD-MotionPairs-neg-out.txt"
python ../plot-results.py -resfile "../evaluation-results/TUD-MotionPairs-additional-out.txt"
python ../plot-results.py -resfile "../evaluation-results/TUD-Brussels-out.txt"

