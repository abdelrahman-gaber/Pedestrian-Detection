#!/bin/bash

#module load anaconda
#module load gcc/5.3.0 
#module load opencv2/gcc5
module load cuda/8.0 
module load cudnn/5.1-cuda-8.0
#module load caffe_priv/ssd

dataset_path=/data/stars/user/aabubakr/pd_datasets/datasets/caltech/annot-images/images/test
save_path=/data/stars/user/aabubakr/pd_datasets/outputs/SSD-OUT/caltech/SSD-ft-cal-fc2-40000

# The following finds all the leaf folders in the dataset path and stores them in an array
data_folders=( $(find $dataset_path -type d -mindepth 1 -links 2) )

# Now we iterate through all the image folders
for folder in "${data_folders[@]}"
do
    source_folder=$folder
    save_folder=$save_path/${folder#${dataset_path}}
    # Create the folder if one does not exist already
    mkdir -p $save_folder
    /home/aabubakr/ssd-new/build/examples/ssd/ssd_detect /home/aabubakr/ssd-new/models/VGGNet/VOC0712Plus/deploy.prototxt /home/aabubakr/ssd-new/models/VGGNet/VOC0712Plus/VGG_VOC0712Plus_SSD_512x512_ft_iter_40000_cal_fc2.caffemodel $source_folder/images_list.txt --confidence_threshold 0.0 --out_file $save_folder/detections-preprocessed.txt
  
    python ../utils/parse-detection-files/image-list-seperate-CalEval.py -DetectionResultsPath $save_folder

    # Give proper permissions so that we do not have to face any delays due to the permissions issue.
    chmod -R 770 $save_folder 
done

   cp -a $save_path /home/aabubakr/codes/pedestrian-detection-evaluation/CalEval-3.2.1/data-USA/res/



