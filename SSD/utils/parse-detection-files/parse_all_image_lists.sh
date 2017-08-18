#!/bin/bash

dataset_path=/data/stars/user/aabubakr/pd_datasets/datasets/caltech/code3.2.1/data-USA/res/SSD

# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do
    source_folder=$folder
    # Create the folder if one does not exist already
    python parse-image-list-txt.py -DetectionResultsPath $source_folder 
    # Give proper permissions so that we do not have to face any delays due to the permissions issue.
    #chmod -R 770 $save_folder 
done



