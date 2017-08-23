import numpy as np
import os
import math
import argparse
import glob

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-ImagesPath', help = 'Path to all images to put in list', required = True )
	parser.add_argument('-AnnotPath', help = 'Path to all annotations to put in list', required = True )
	parser.add_argument('-Output', help = 'Full path to output results file', required = True )
	
	args = vars(parser.parse_args())

	if args['ImagesPath'] is not None:
		images_path = args['ImagesPath']
	if args['AnnotPath'] is not None:
		annot_path = args['AnnotPath']
	if args['Output'] is not None:
		output_file = args['Output']

	
	f = open(output_file, "a")

	images_path_ = images_path[images_path.find("images-train") : ]
	annot_path_ = annot_path[annot_path.find("annotations-train") : ]

	for files in os.scandir(annot_path):
		if files.is_file() and (files.name.endswith('.txt')):
			#if files.is_file() and (files.name.endswith('.jpg') or files.name.endswith('.png') or files.name.endswith('.jpeg') or files.name.endswith('.pgm')) :
			annot_full_path = os.path.join(annot_path_, files.name)
			images_full_path = os.path.join(images_path_, os.path.splitext(files.name)[0]) #+ ".png" )
			#if (os.path.isfile(annot_full_path)):
			f.write(str(images_full_path) + " " + str(annot_full_path) + "\n" )

