#!/bin/bash

#dataset_path=/home/aabubakr/data/Caltech/images-train
#annot_path=/home/aabubakr/data/Caltech/annotations-train
#res_file=/home/aabubakr/ssd-new/data/Caltech/train.txt

dataset_path=/home/aabubakr/data/INRIAPerson/images-train
annot_path=/home/aabubakr/data/INRIAPerson/annotations-train
res_file=/home/aabubakr/ssd-new/data/INRIA/train.txt

# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do
    source_folder=$folder
    echo $folder
    annot_folder=$annot_path${folder#${dataset_path}}
    # Create the folder if one does not exist already
    #mkdir -p $save_folder
    echo $annot_folder
    python generate_lists.py -ImagesPath $source_folder -AnnotPath $annot_folder -Output $res_file
done
