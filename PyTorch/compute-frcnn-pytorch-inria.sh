#!/bin/sh

module load cuda/8.0 cudnn/5.1-cuda-8.0 
source activate pytorch


dataset_path=/data/stars/user/aabubakr/pd_datasets/datasets/INRIA/INRIAPerson/Test
save_path=/data/stars/user/aabubakr/pd_datasets/outputs/INRIA/frcnn-pytorch

# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do
    source_folder=$folder
    save_folder=$save_path/${folder#${dataset_path}}
    # Create the folder if one does not exist already
    mkdir -p $save_folder
    python /home/aabubakr/detection-pytorch/faster_rcnn_pytorch/person-detection.py --source $source_folder --save $save_folder --thresh 0.7 
    # Give proper permissions so that we do not have to face any delays due to the permissions issue.
    chmod -R 770 $save_folder 
done

