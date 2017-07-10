import numpy as np
import os
import math
import argparse

# loop for different thresholds
# loop for all images, then:
# read annotations and detection results
# Evaluate the detection for each image 
def MainEvaluation(AnnotationFilesPath, ResultsFilesPath, Thresh):
	igt= ReadAnnotationFiles(AnnotationFilesPath)
	NumGTWindows = np.shape(igt)[0]
	# Remember: last element of res is the probability
	res = ReadResultsFiles(ResultsFilesPath)
	TP = 0.0
	FP = 0.0
	indexes = []
	for row in res:
		bb = np.asarray([row[0], row[1], row[2], row[3]])
		prob = row[4]
		det, idx = OverlapArea(bb, igt)
		#indexes.append(idx)
		if (prob >= Thresh):
			if det > 0.5:
				TP += 1
				indexes.append(idx)
			else:
				#if (prob > Thresh):
				FP += 1
				#indexes.append(idx)
	#FN = NumGTWindows - (TP + FP)
	gt_unmatched = np.delete(igt, indexes, axis = 0)
	FN = np.shape(gt_unmatched)[0]
	return TP, FP, FN


def ReadAnnotationFiles(filename):
	annotations = []
	labels = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines[1:]:
		values = l.split(" ")
		class_label =  values[0]
		if class_label == 'person': # only person not people
			annotations.append( [float(i) for i in values[1:12]])
		#labels.append(values[0])
	return np.asarray(annotations) 


def ReadResultsFiles(filename):
	results = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		value = l.split(",")
		results.append([float(i) for i in value])

        # Remember that last elemnt is probability
	return np.asarray(results)


# input gt(all gt for the given image) and detected bounding boxes
# output: area of overlap as stated in the paper (PASCAL measure)
def OverlapArea(bb, bbgt):
	ovmax = - 9999.9 # initialize by big -ve number
	imax = 0

	for i in range(bbgt.shape[0]):
		# determine the (x, y)-coordinates of the intersection rectangle
		xA = max(bb[0], bbgt[i,0])
		yA = max(bb[1], bbgt[i,1])
		xB = min(bb[2], bbgt[i,2])
		yB = min(bb[3], bbgt[i,3])

		# compute the area of intersection rectangle
		interArea = (xB - xA + 1) * (yB - yA + 1)
 
		# compute the area of both the prediction and ground-truth
		# rectangles
		boxAArea = (bb[2] -bb[0] + 1) * (bb[3] - bb[1] + 1)
		boxBArea = (bbgt[i, 2] - bbgt[i, 0] + 1) * (bbgt[i, 3] - bbgt[i, 1] + 1)
 
		# compute the intersection over union by taking the intersection
		# area and dividing it by the sum of prediction + ground-truth
		# areas - the interesection area
		#print(boxAArea)
		#print(interArea)
		iou = interArea / (boxAArea + boxBArea - interArea)
		if iou > ovmax:
			ovmax = iou
			imax = i
 
	# return the intersection over union value
	return ovmax, imax


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-annotations', help = 'Path to annotation files', required = True )
	parser.add_argument('-results', help = 'Path to output files from algorithm', required = True)
	parser.add_argument('-output', help = 'Full path to output results file', required = True )
	
	args = vars(parser.parse_args())

	if args['annotations'] is not None:
		annotation_path = args['annotations']
	if args['results'] is not None:
		detection_results = args['results']
	if args['output'] is not None:
		output_file = args['output']
	
	f = open(output_file, "w")
	step = 0.01
	ThreshRange = np.arange(0.0, 1.0 + step, step)
	for Threshold in ThreshRange:
		TPtot = 0.0
		FPtot = 0.0
		NumofImages = 0.0
		FNtot = 0.0
		for folder in next(os.walk(detection_results))[1]: # return folder
			res_path = os.path.join(detection_results, folder)
			for folder2 in next(os.walk(res_path) )[1]:
				res_path2 = os.path.join(res_path, folder2, 'detection_csv')
				for files in os.scandir(res_path2):
					if files.is_file() and files.name.endswith('.csv'):
						resfile = os.path.join(res_path2, files.name)
						#print(resfile)
						annfile = os.path.join(annotation_path, folder, folder2 ,os.path.splitext(files.name)[0] +".txt")
						#print(annfile)
						if os.path.isfile(annfile):
							TP, FP, FN = MainEvaluation(annfile, resfile, Threshold)
							NumofImages += 1
							TPtot += TP
							FPtot += FP
							FNtot += FN
		FFPI = FPtot/NumofImages
		MR = FNtot/(FNtot+TPtot)
		print("Threshold= " + str(Threshold) + "  TP= " + str(TPtot) + "  FP= "+ str(FPtot) + "  FPPI= " + str(FPtot/NumofImages) + "  FN= " + str(FNtot) + "  Miss Rate= " + str(FNtot/(FNtot+TPtot)) )
		#with open(output_file, "w") as f:
		f.write(str(Threshold) + " " + str(FFPI) + " " + str(MR) + "\n")
