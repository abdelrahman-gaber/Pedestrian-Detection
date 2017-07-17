import numpy as np
import cv2
import os
import argparse

def ReadFiles(filename):
	results = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		value = l.split(" ")
		results.append([int(i) for i in value])

	# Remember that last elemnt is probability
	return np.asarray(results)


if __name__ == "__main__":
	annot_path = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/JELMOLI"
	imgs_path = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/JELMOLI"
	out_path = "/data/stars/user/aabubakr/pd_datasets/datasets/ETHZ/annotations-all/JELMOLI-vis"

	for files in os.scandir(imgs_path):
		if files.is_file() and files.name.endswith('.png'):
			img_p = os.path.join(imgs_path, files.name )
			annot = os.path.join(annot_path, files.name + ".txt")
			ann = ReadFiles(annot)
			output = os.path.join(out_path, os.path.splitext(files.name)[0] + ".png" )
			
			img = cv2.imread(img_p)
			
			for b in ann:
				x_min = int(b[0])
				y_min = int(b[1])
				x_max = int(b[2])
				y_max = int(b[3])

				cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0,255,0), 2)

			cv2.imwrite(output, img)

			





