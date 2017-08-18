import numpy as np
import cv2
import os
import argparse

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
	
	parser.add_argument('-detection_files', help = 'Full path to detection files', required = True )
	parser.add_argument('-images', help = 'Full path to original images', required = True)
	parser.add_argument('-output', help = 'Full path to output results images', required = True )
	parser.add_argument('-thresh', help = 'Threshold to visualize detections', required = True )

	args = vars(parser.parse_args())

	if args['detection_files'] is not None:
		detection_csv = args['detection_files']
	if args['images'] is not None:
		images_path = args['images']
	if args['output'] is not None:
		output_path = args['output']
	if args['thresh'] is not None:
                Threshold = float(args['thresh'])

	
	for files in os.scandir(detection_csv):
		if files.is_file() and files.name.endswith('.csv'):
			csv_path = os.path.join(detection_csv, files.name )
			im_path = os.path.join(images_path, os.path.splitext(files.name)[0] + ".png" )
			out_path = os.path.join(output_path, os.path.splitext(files.name)[0] + ".jpg" )
			all_bbox = ReadResultsFiles(csv_path)
			print(im_path)

			img = cv2.imread(im_path)

			for b in all_bbox:
				if b[4] >= Threshold:
					x_min = int(b[0])
					y_min = int(b[1])
					x_max = int(b[2])
					y_max = int(b[3])
				
					cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0,255,0), 2)
			
			cv2.imwrite(out_path, img)


