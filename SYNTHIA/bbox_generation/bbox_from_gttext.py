# this code reads the GT text files of SYNTHIA and generate bounding boxes around pedestrian class. 
# the output is in the form [col_min, row_min, col_max, row_max]
import numpy as np
import os
import math
import argparse
import cv2

def ReadGTTXTFile(filename):
	gt_seg = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		values = l.split(" ")
		gt_seg.append( [int(i) for i in values ])
	# NOTE: the output is array (720, 960) >> rows first then columns, not like image format	
	return np.asarray(gt_seg) 


def generate_bbox(seg_array):
	# seg_array is the original segmentation array read from the GTTXT files and converted to int
	person_label = np.argwhere(seg_array == 10) # pedestrian label == 10
	if not len(person_label): # if list is empty
		return -1
	
	row_min = np.argmin(person_label, axis = 0) [0]
	min_idx = person_label[row_min]
	
	# take sub array of original array, and find min and max borders of the person
	seg_array_sub = seg_array[ min_idx[0]  : -1  , min_idx[1] - 100 : min_idx[1] + 100 ]
		
	person_label2 = np.argwhere(seg_array_sub == 10)
	if not len(person_label2):
		return -1
	
	arg_min = np.argmin(person_label2, axis = 0)
	
	#min_row_sub = person_label2[arg_min[0]] # we already know it is in 0 location
	min_col_sub = person_label2[arg_min[1]]
	#print(min_row_sub, min_col_sub)
	
	arg_max = np.argmax(person_label2, axis = 0)
	max_row_sub = person_label2[arg_max[0]]
	max_col_sub = person_label2[arg_max[1]]
	#print(max_row_sub, max_col_sub)
	
	# annotation = [col_min, row_min, col_max, row_max ]
	margin = 5 # margin of n pixels in all sides of the rectangle
	annotation = [ min_col_sub[1]+min_idx[1]-100 - margin , min_idx[0]-margin , max_col_sub[1]+min_idx[1]-100+margin , max_row_sub[0]+min_idx[0]+margin ]

	return annotation

def Generate_bbox_rg(seg_array):
	#print("Region Growing algorithm")
	# seg_array is the original segmentation array read from the GTTXT files and converted to int
	# person_label_idx = np.argwhere(seg_array == 10) # pedestrian label == 10
	annotations = []
	row_max_size, col_max_size = seg_array.shape

	while(True):
		person_label_idx = np.argwhere(seg_array == 10) # pedestrian label == 10
		if not len(person_label_idx): # if list is empty
			break
			#return -1
	
		list_person = []
		list_final = []
		min_row = np.argmin(person_label_idx, axis = 0) [0]
		seed_idx = person_label_idx[min_row] # minimum index
		#print(seed_idx)
 
		list_person.append([seed_idx[0], seed_idx[1]])
		
		while list_person: # while the list is not empty
			current = list_person[0]
			#print(current)
			#current[1] = list_person_col[0]
			list_final.append(current)
			#list_final_col.append(current[1])
			seg_array[current[0]][current[1]] = -1
			
			del list_person[0]
			#del list_person_col[0]
			
			if not (current[0]-1 >= 0 and current[1]-1 >= 0 and current[0]+1 < row_max_size and current[1]+1 < col_max_size ):
				continue
			# check neighbors of current pixels
			if seg_array[current[0]-1][current[1]-1] == 10 and not ( [current[0]-1, current[1]-1] in list_person):
				list_person.append([current[0]-1, current[1]-1 ])
				#list_person_col.append(current[1]-1)
				list_final.append([current[0]-1, current[1]-1])
				#list_final_col.append(current[1]-1)	

			if seg_array[current[0]-1][current[1]] == 10 and not ([current[0]-1, current[1]] in list_person):
				list_person.append([current[0]-1, current[1]])
				list_final.append([current[0]-1, current[1]])
				#list_final_col.append(current[1])

			if seg_array[current[0]-1][current[1]+1] == 10 and not ([current[0]-1, current[1]+1] in list_person):
				list_person.append([current[0]-1, current[1]+1])
				#list_person_col.append(current[1]+1)
				list_final.append([current[0]-1, current[1]+1])
				#list_final_col.append(current[1]+1)

			if seg_array[current[0]][current[1]-1] == 10 and not ([current[0], current[1]-1] in list_person):
				list_person.append([current[0], current[1]-1])
				#list_person_col.append(current[1]-1)
				list_final.append([current[0], current[1]-1 ])
				#list_final_col.append(current[1]-1)

			if seg_array[current[0]][current[1]+1] == 10 and not ([current[0] , current[1]+1] in list_person):
				list_person.append([current[0], current[1]+1])
				#list_person.append(current[1]+1)
				list_final.append([current[0], current[1]+1])
				#list_final_col.append(current[1]+1)
			#print(current[0]+1 , current[1]-1) 
			#print(list_person)
			if seg_array[current[0]+1][current[1]-1] == 10 and not ([current[0]+1, current[1]-1] in list_person):
				list_person.append([current[0]+1, current[1]-1])
				#list_person_col.append(current[1]-1)
				list_final.append([current[0]+1, current[1]-1])
				#list_final_col.append(current[1]-1)

			if seg_array[current[0]+1][current[1]] == 10 and not ([current[0]+1, current[1]] in list_person):
				list_person.append([current[0]+1, current[1]])
				#list_person_col.append(current[1])
				list_final.append([current[0]+1, current[1]])
				#list_final_col.append(current[1])

			if seg_array[current[0]+1][current[1]+1] == 10 and not ([current[0]+1, current[1]+1] in list_person):
				list_person.append([current[0]+1, current[1]+1])
				#list_person_col.append(current[1]+1)
				list_final.append([current[0]+1, current[1]+1])
				#list_final_col.append(current[1]+1)


		# check list_final_* to find min-max row and col
		min_row = np.min(list_final, axis = 0)[0]
		min_col = np.min(list_final, axis = 0)[1]
		max_row = np.max(list_final, axis = 0)[0]
		max_col = np.max(list_final, axis = 0)[1]
		
		if (max_col - min_col > 15) and (max_row - min_row > 30):
			margin = 1	
			annotations.append([min_col-margin, min_row-margin, max_col+margin,  max_row+margin])
		#print(annotations)

	return annotations	

if __name__ == "__main__":
	#file_name = "/data/stars/user/aabubakr/pd_datasets/datasets/SYNTHIA/GTTXT/ap_000_01-11-2015_19-20-57_000001_1_Rand_6.txt"
	#img_name = "/data/stars/user/aabubakr/pd_datasets/datasets/SYNTHIA/GT/ap_000_01-11-2015_19-20-57_000001_1_Rand_6.png"
	#file_name = "/data/stars/user/aabubakr/pd_datasets/datasets/SYNTHIA/GTTXT/ap_000_02-11-2015_18-02-19_000141_2_Rand_7.txt"
	#img_name = "/data/stars/user/aabubakr/pd_datasets/datasets/SYNTHIA/GT/ap_000_02-11-2015_18-02-19_000141_2_Rand_7.png"	
		
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-GTTXT', help = 'Path to ground truth text files', required = True )
	parser.add_argument('-output', help = 'Full path to output results file', required = True )
	parser.add_argument('-images', help = 'Path to original RGB images', required = False, default = None)

	args = vars(parser.parse_args())

	if args['GTTXT'] is not None:
		gt_txt_path = args['GTTXT']
	if args['output'] is not None:
		output_path = args['output']
	if args['images'] is not None:
                images_path = args['images']

	for files in os.scandir(gt_txt_path):
		if files.is_file() and files.name.endswith('.txt'):
			file_name = os.path.join(gt_txt_path, files.name)
			seg_array = ReadGTTXTFile(file_name)
			annotation = Generate_bbox_rg(seg_array)
			print(file_name)
			#print(annotation)
			img_name = os.path.join(images_path, os.path.splitext(files.name)[0] + ".png")
			im_path = os.path.join(output_path , 'visualization-images', os.path.splitext(files.name)[0] + ".png" )
			out_path = os.path.join(output_path , 'annotations',os.path.splitext(files.name)[0] + ".txt" )
			
			f = open(out_path, 'w')
			if annotation:
				for annot in annotation: 
					f.write(str(annot[0]) + " " + str(annot[1]) + " " + str(annot[2]) + " " + str(annot[3]) + "\n")
			f.close()
			
			if args['images'] is not None:
				img = cv2.imread(img_name)
				for annot in annotation:
					cv2.rectangle(img, (annot[0], annot[1]) , (annot[2], annot[3]), (0, 255, 0) , 2)
				cv2.imwrite(im_path, img)


