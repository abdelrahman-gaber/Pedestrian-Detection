#!/bin/bash


source activate cntk-py36

# positive
python ethz-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/BAHNHOF -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT/BAHNHOF/detection_csv -output BAHNHOF-out.txt

python ethz-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/CROSSING -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT/CROSSING/detection_csv -output CROSSING-out.txt

python ethz-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/JELMOLI -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT/JELMOLI/detection_csv -output JELMOLI-out.txt

python ethz-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/LINTHESCHER -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT/LINTHESCHER/detection_csv -output LINTHESCHER-out.txt

python ethz-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/LOEWENPLATZ -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT/LOEWENPLATZ/detection_csv -output LOEWENPLATZ-out.txt

python ethz-evaluation.py -annotations /data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/SUNNY-DAY -results /data/stars/user/aabubakr/pd_datasets/outputs/ETHZ-OUT/SUNNY-DAY/detection_csv -output SUNNY-DAY-out.txt

python plot-results.py -resfile "BAHNHOF-out.txt"
python plot-results.py -resfile "CROSSING-out.txt"
python plot-results.py -resfile "JELMOLI-out.txt"
python plot-results.py -resfile "LINTHESCHER-out.txt"
python plot-results.py -resfile "LOEWENPLATZ-out.txt"
python plot-results.py -resfile "SUNNY-DAY-out.txt"


