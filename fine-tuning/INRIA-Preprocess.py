import numpy as np
import os
import math
import argparse

data_path = '/data/stars/user/aabubakr/pd_datasets/datasets/INRIA/INRIAPerson/Train' # 2 subfolders [pos and neg]
annot_path = '/data/stars/user/aabubakr/pd_datasets/datasets/INRIA/inriacode/Train/annotations' # all pos and neg together

def ReadAnnotationFiles(filename):
	annotations = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		values = l.split(" ")
		annotations.append( [float(i) for i in values[0:4]])
	
	return np.asarray(annotations)


if __name__ == "__main__":
	im_names = []
	annotations = []

	for folder in next(os.walk(data_path))[1]: # return folder pos and neg
		im_path = os.path.join(data_path, folder)
		for image in os.scandir(im_path):
			if image.is_file() and image.name.endswith('.jpg'):
				im_names.append(os.path.join(im_path, image))
				#print(im_names)
				annfile = os.path.join(annot_path, os.path.splitext(image.name)[0] +".png.txt")
				if not os.path.exists(annfile):
					annotations.append([])
				else:
					annot = ReadAnnotationFiles(annfile)
					print(annot)
					annot.flatten()
					print(annot)
					annotations.append(annot)
	print(len(im_names), len(im_names[0]))
	print(len(annotations), len(annotations[0]))

	data_final = np.vstack((im_names, annotations)) 

	np.savetxt("INRIA_training_annot.csv" , data_final, delimiter= ",")



