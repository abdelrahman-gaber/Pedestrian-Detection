#!/bin/bash

#dataset_path=/data/stars/user/aabubakr/pd_datasets/outputs/SSD-OUT/caltech/CalEval
#dataset_path=/data/stars/user/aabubakr/pd_datasets/outputs/SSD-OUT/caltech/test-ft
dataset_path=/data/stars/user/aabubakr/pd_datasets/outputs/SSD-OUT/INRIA/ft_cal

# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do
    source_folder=$folder
    # Create the folder if one does not exist already
    python ../utils/parse-detection-files/image-list-seperate-CalEval.py -DetectionResultsPath $source_folder 
    # Give proper permissions so that we do not have to face any delays due to the permissions issue.
    #chmod -R 770 $save_folder 
done



