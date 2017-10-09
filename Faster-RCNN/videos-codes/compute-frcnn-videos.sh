#!/bin/sh

module load cuda/7.5
module load cudnn/5.1-cuda-7.5
module load anaconda
module load opencv2.4.13

dataset_path=/home/aabubakr/data/Misc/images-orig
save_path=/home/aabubakr/data/Misc/Faster-RCNN


#dataset_path=/data/stars/user/aabubakr/pd_datasets/datasets/videos/images
#save_path=/data/stars/user/aabubakr/pd_datasets/outputs/videos


# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do

    save_folder=$save_path/${folder#${dataset_path}}/"thresh01"
    # Create the folder if one does not exist already
    mkdir -p $save_folder
    python /data/stars/share/py-faster-rcnn/tools/pd_code_saveimages.py --source $data_folders --save $save_folder --thresh 0.1
    # Give proper permissions so that we do not have to face any delays due to the permissions issue.
    chmod -R 770 $save_folder
done




