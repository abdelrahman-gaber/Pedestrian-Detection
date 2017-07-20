import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import argparse
from matplotlib import ticker

def PlotResults(filename):
	thresh = []
	FPPI = []
	MR = []

	f = open(filename)
	lines = f.read().splitlines()

	for l in lines[1:-2]: #lines[1:-2]:
		values = l.split(" ")
		thresh.append(float(values[0]))
		FPPI.append(float(values[1]))
		MR.append(float(values[2]) )
		#annotations.append( [float(i) for i in values[0:2]])
		
		FPPI_log = np.log10(FPPI)
		#MR_log = np.log10(MR)

	return thresh, FPPI, MR, FPPI_log#, MR_log
	#return np.asarray(annotations)


if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument('-resfile', help = 'Results file from evaluation', required= True)

	args = vars(parser.parse_args())

	if args['resfile'] is not None:
		rfile = args['resfile']

	Thresh, FPPI, MR, FPPI_log = PlotResults(rfile) 
	MR = np.asarray(MR)
	#print(FPPI_log)
	#print(MR_log)
	#print(MR_log.shape)
	arg_fppi = np.argwhere(np.logical_and(FPPI_log > -2, FPPI_log < 0) )
	#print(arg_fppi)
	MR_mean = average(MR[arg_fppi])
	print("MR mean")
	print(MR_mean) 
	fig = plt.figure()

	ax = fig.add_subplot(111)

	ax.plot(FPPI, MR)

	ax.set_yscale('log')
	ax.set_xscale('log')
	#ax.ticklabel_format(style = 'sci', useOffset=False)
	ax.set_yticks([.05, .10, .20, .30, .40, .50, .64 , .80, 1])
	ax.yaxis.set_major_formatter(ticker.ScalarFormatter() )
	ax.ticklabel_format(axis='y', style='plain', useOffset=False)

	#ax.plot(FPPI, MR)
	#plt.plot(FPPI[1:-2], MR[1:-2])
	plt.xlabel('False Positive Per Image (FPPI)')
	plt.ylabel('Miss Rate')
		
	#plt.grid(True)
	plt.show()
