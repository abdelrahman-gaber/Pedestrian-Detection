import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import argparse

def PlotResults(filename):
	thresh = []
	FPPI = []
	MR = []

	f = open(filename)
	lines = f.read().splitlines()

	for l in lines:
		values = l.split(" ")
		thresh.append(float(values[0]))
		FPPI.append(float(values[1]))
		MR.append(float(values[2]) )
		#annotations.append( [float(i) for i in values[0:2]])

	return thresh, FPPI, MR
	#return np.asarray(annotations)


if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument('-resfile', help = 'Results file from evaluation', required= True)

	args = vars(parser.parse_args())

	if args['resfile'] is not None:
		rfile = args['resfile']

	Thresh, FPPI, MR = PlotResults(rfile) 

	plt.plot(FPPI, MR)
        #plt.plot(FPPI[1:-2], MR[1:-2])
	plt.xlabel('False Positive Per Image (FPPI)')
	plt.ylabel('Miss Rate')
        #plt.xscale('log')
	plt.xscale('log')
	#plt.yscale('log')
	plt.show()
