import numpy as np
import os
import math
import argparse
import glob
import scandir
from scandir import scandir

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-ImagesPath', help = 'Path to all images to put in list', required = True )
	#parser.add_argument('-Output', help = 'Full path to output results file', required = True )
	
	args = vars(parser.parse_args())

	if args['ImagesPath'] is not None:
		images_path = args['ImagesPath']
	#if args['Output'] is not None:
	#	output_file = args['Output']
	
	num_images = len(glob.glob1(images_path, "*.png")) + len(glob.glob1(images_path, "*.jpg")) + len(glob.glob1(images_path, "*.jpeg")) + len(glob.glob1(images_path, "*.pgm")) 
	if num_images > 1 :
		print("path: " + images_path + " contains " + str(num_images) )
	
		#file_name = os.path.join(images_path, os.path.basename(images_path) + ".txt")
		file_name = os.path.join(images_path, "images_list.txt")
		f = open(file_name, "w")

		for files in scandir(images_path):
			if files.is_file() and (files.name.endswith('.jpg') or files.name.endswith('.png') or files.name.endswith('.jpeg') or files.name.endswith('.pgm')) :
				images_full_path = os.path.join(images_path, files.name) 
			
				f.write(str(images_full_path) + "\n" )


