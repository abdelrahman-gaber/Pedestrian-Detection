#!/bin/bash


source activate cntk-py36

# positive
#python tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-MotionPairs/positive/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-MotionPairs/positive/detection_csv  -output TUD-MotionPairs-pos-out.txt

python tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-MotionPairs/negative/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-MotionPairs/negative/detection_csv  -output TUD-MotionPairs-neg-out.txt

python tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-MotionPairs/additional-negative-bootstrap/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-MotionPairs/additional-negative-bootstrap/detection_csv  -output TUD-MotionPairs-additional-out.txt

python tud-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/TUD-Brussels/TUD-Brussels/annotations -results /data/stars/user/aabubakr/pd_datasets/outputs/TUD-Brussels/TUD-Brussels/detection_csv  -output TUD-Brussels-out.txt


python plot-results.py -resfile "TUD-MotionPairs-pos-out.txt"
python plot-results.py -resfile "TUD-MotionPairs-neg-out.txt"
python plot-results.py -resfile "TUD-MotionPairs-additional-out.txt"
python plot-results.py -resfile "TUD-Brussels-out.txt"

