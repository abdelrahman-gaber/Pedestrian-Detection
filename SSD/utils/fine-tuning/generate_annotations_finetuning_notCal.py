import numpy as np
import os
import math
import argparse
import glob
import re

# This code prepares the annotations for fine-tuning SSD with different pedestrian datasets.
# The output detection annotation: label_id xmin ymin xmax ymax -->>  
# Refer to: https://github.com/weiliu89/caffe/issues/59
# This code conside only to class labels, 15 as person and 0 as background.

def ReadAnnotFile(filename):
	results = []
	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		values = l.split(" ")
		#labels.append(values[0])
		results.append( [float(i) for i in values])
	
	return np.asarray(results) 


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-AnnotPath', help = 'Path to original annotations', required = True )
	parser.add_argument('-OutPath', help = 'Path to output annotations', required = True )

	args = vars(parser.parse_args())

	if args['AnnotPath'] is not None:
		in_path = args['AnnotPath']	
	if args['OutPath'] is not None:
		out_path = args['OutPath']


	for files in os.scandir(in_path):
		if files.is_file() and (files.name.endswith('.txt') ) :
			in_file_full_path = os.path.join(in_path, files.name) 
			out_file_full_path = os.path.join(out_path, files.name)

			results = ReadAnnotFile(in_file_full_path)
			
			f = open(out_file_full_path, 'ab')
			for rs in results:
				if ( rs[2] > rs[0] and rs[3] > rs[1] ):
					det_person = np.atleast_2d( np.asarray([15 , max(0, rs[0]), max(0, rs[1]), max(0, rs[2]) , max(0, rs[3]) ]) ) # [CLASS, DETS]		
					np.savetxt(f, det_person, fmt=["%d",]*1+["%f",]*4 , delimiter=" " )
			f.close()


