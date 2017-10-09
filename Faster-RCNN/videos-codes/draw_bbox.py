import numpy as np
import cv2
import os
import argparse
import scandir
from scandir import scandir

def ReadResultsFiles(filename):
	results = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		value = l.split(",")
		results.append([float(i) for i in value])

	# Remember that last elemnt is probability
	return np.asarray(results)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-detection_files', help = 'Path to annotation files', required = True )
	parser.add_argument('-images', help = 'Path to original images', required = True)
	parser.add_argument('-output', help = 'Full path to output results file', required = True )
	
	args = vars(parser.parse_args())

	if args['detection_files'] is not None:
		detection_csv = args['detection_files']
	if args['images'] is not None:
		images_path = args['images']
	if args['output'] is not None:
		output_path = args['output']
	
	#images_path = "/data/stars/user/aabubakr/pd_datasets/datasets/videos/images/vid08"
	#detection_csv= "/data/stars/user/aabubakr/pd_datasets/outputs/videos-ujjwal/vid08/thresh01/detection_csv"
	#output_path = "/data/stars/user/aabubakr/pd_datasets/outputs/videos-ujjwal/vid08/thresh01/thresh_05"
	
	for files in scandir(detection_csv):
		if files.is_file() and files.name.endswith('.csv'):
			#im_path = os.path.join(images_path, image_name + ".jpg" )
			csv_path = os.path.join(detection_csv, files.name )
			im_path = os.path.join(images_path, os.path.splitext(files.name)[0] + ".jpg" )
			out_path = os.path.join(output_path, os.path.splitext(files.name)[0] + ".jpg" )
			all_bbox = ReadResultsFiles(csv_path)
			print(im_path)

			img = cv2.imread(im_path)

			for b in all_bbox:
				if b[4] >= 0.5:
					x_min = int(b[0])
					y_min = int(b[1])
					x_max = int(b[2])
					y_max = int(b[3])
				
					cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0,0,255), 2)
			
			cv2.imwrite(out_path, img)
					


# https://stackoverflow.com/questions/23720875/how-to-draw-a-rectangle-around-a-region-of-interest-in-python
