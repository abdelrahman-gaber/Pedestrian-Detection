import numpy as np
import os
import math
import argparse

def ReadAnnotationFiles(filename):
        annotations = []
        f = open(filename)
        lines = f.read().splitlines()

        for l in lines:
                values = l.split(",")
                annotations.append( [int(i) for i in values[0:6]])
		#imagenum.append(values[0])

        return np.asarray(annotations)#, imagenum



if __name__ == "__main__":

        parser = argparse.ArgumentParser()

        parser.add_argument('-annotations', help = 'Full path to annotation file', required = True )
        parser.add_argument('-output', help = 'Full path for output files', required = True )

        args = vars(parser.parse_args())

        if args['annotations'] is not None:
                annotation_path = args['annotations']
        if args['output'] is not None:
                output_file = args['output']

        annot_orig = ReadAnnotationFiles(annotation_path)
	
        for row in annot_orig:
            file_name = "frame_" + str(row[0]).zfill(4) + ".txt"
            out_file = os.path.join(output_file, file_name)

            # annotation = [col_min, row_min, body_width, body_hight ]
            # new annotations = [col_min, row_min, col_max, row_max]
            col_min = row[2]
            row_min = row[3]
            col_max = col_min + row[4]
            row_max = row_min + row[5]
            
            print(out_file)
            print( str(col_min) + " " + str(row_min) + " " + str(col_max) + " " + str(row_max)  )
            
            if os.path.exists(out_file):
                wtype = 'a' # append if already exists
            else:
                wtype = 'w' # make new file
 
            f = open(out_file, wtype)
            f.write(str(col_min) + " " + str(row_min) + " " + str(col_max) + " " + str(row_max) + "\n" )
            f.close()

