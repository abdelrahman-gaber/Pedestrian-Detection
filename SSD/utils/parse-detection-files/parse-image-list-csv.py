import numpy as np
import os
import math
import argparse
import glob

# This code parse the output from SSD algorithm , and add the persom detections to csv files. 
# NOTE: If you will re-run the code be sure to delete the old files of detections. 

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
	
	parser.add_argument('-DetectionResultsPath', help = 'Path detection results list', required = True )
	
	args = vars(parser.parse_args())

	if args['DetectionResultsPath'] is not None:
		detection_path = args['DetectionResultsPath']	


	file_name = os.path.join(detection_path, "detections-preprocessed.txt")
	
	if os.path.exists(file_name):
		image_pths, results = ReadDetectionFile(file_name)

		#save_file_path = os.path.join(detection_path, 'detection_csv')
		save_file_path = detection_path + "/detection_csv"
		if not os.path.isdir(save_file_path):
			os.makedirs(save_file_path)
	
		for idx, im_pth in enumerate(image_pths):
			im_name = os.path.basename(im_pth)
			out_csv = os.path.join(save_file_path, os.path.splitext(im_name)[0] + ".csv" )

			f = open(out_csv, 'ab')
			if results[idx, 0] == 15:
				det_person =np.atleast_2d( np.asarray([ abs(results[idx,2]), abs(results[idx,3]), abs(results[idx,4])  , abs(results[idx,5]) , results[idx, 1] ]) ) # [detection prob]
				#print(det_person)
				#f = open(out_csv, 'ab')
				np.savetxt(f, det_person, fmt=["%d",]*4 + ["%1.3f"], delimiter=",")
			f.close
				
	else:
		print("nothing to do here")

