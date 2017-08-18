import numpy as np
import os
import math
import argparse
import glob
import re

# This code parse the output from SSD algorithm , and add the person detections to text file in the same format required for caltech evaluation code.  

def ReadDetectionFile(filename):
	results = []
	images = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		values = l.split(" ")
		images.append(values[0])
		results.append( [float(i) for i in values[1:]])
	
	return np.asarray(images), np.asarray(results) 


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-DetectionResultsPath', help = 'Path to detection results list from SSD', required = True )
	
	args = vars(parser.parse_args())

	if args['DetectionResultsPath'] is not None:
		detection_path = args['DetectionResultsPath']	


	file_name = os.path.join(detection_path, "detections-preprocessed.txt")
	out_file = os.path.join(os.path.split(detection_path)[0], os.path.basename(detection_path) + ".txt")
	f = open(out_file, 'ab')

	if os.path.exists(file_name):
		image_pths, results = ReadDetectionFile(file_name)

		#save_file_path = os.path.join(detection_path, 'detection_csv')
		#if not os.path.isdir(save_file_path):
		#	os.makedirs(save_file_path)
	
		for idx, im_pth in enumerate(image_pths):
			im_name_ = os.path.basename(im_pth)
			im_name = os.path.splitext(im_name_)[0]
			im_number = int(re.findall('\d+', im_name)[-1]) + 1 # Matlab numbering system start from 1
			#out_csv = os.path.join(save_file_path, os.path.splitext(im_name)[0] + ".csv" )
		
			if results[idx, 0] == 15:
				det_person =np.atleast_2d( np.asarray([im_number , results[idx,2], results[idx,3], results[idx,4]-results[idx,2], results[idx,5]-results[idx,3], results[idx, 1] ]) ) # [detection prob]
				#print(det_person)
				#f = open(out_file, 'w')
				np.savetxt(f, det_person, fmt=["%d",]*5 + ["%1.3f"], delimiter=",")
				f.close
				
	else:
		print("nothing to do here")

