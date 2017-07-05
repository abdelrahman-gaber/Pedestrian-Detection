#!/bin/bash


#source activate cntk-py36

python ../gs-pankit-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/GS-PANKIT/annotations/GT_GS_06 -results   -output GS06-out.txt

python ../gs-pankit-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/GS-PANKIT/annotations/GT_GS_54 -results   -output GS54-out.txt


python plot-results.py -resfile "GS06-out.txt"
python plot-results.py -resfile "GS54-out.txt"

