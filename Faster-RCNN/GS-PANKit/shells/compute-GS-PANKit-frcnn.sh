#!/bin/bash
#OAR -p gpu='YES' and host='nefgpu10.inria.fr' and cluster='dellt630gpu'
#OAR -l /gpunum=1, walltime=10 
#OAR --name GS-PANKitTesting


module load cuda/7.5
module load cudnn/5.1-cuda-7.5
module load anaconda
module load opencv2.4.13

dataset_path=/data/stars/user/aabubakr/pd_datasets/datasets/GS-PANKIT/images
save_path=/data/stars/user/aabubakr/pd_datasets/outputs/GS-PANKit

# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do
    source_folder=$folder
    save_folder=$save_path/${folder#${dataset_path}}
    # Create the folder if one does not exist already
    mkdir -p $save_folder
    python /data/stars/share/py-faster-rcnn/tools/pd_code.py --source $source_folder --save $save_folder --thresh 0.0 
    # Give proper permissions so that we do not have to face any delays due to the permissions issue.
    chmod -R 770 $save_folder 
done


