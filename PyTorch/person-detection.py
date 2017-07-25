import os
import cv2
import numpy as np
import argparse
import sys

sys.path.append('/home/aabubakr/detection-pytorch/')
import faster_rcnn_pytorch

from faster_rcnn_pytorch import *

from faster_rcnn_pytorch.faster_rcnn import network
from faster_rcnn_pytorch.faster_rcnn.faster_rcnn import FasterRCNN
from faster_rcnn_pytorch.faster_rcnn.utils.timer import Timer

model_file = '/home/aabubakr/detection-pytorch/faster_rcnn_pytorch/models/VGGnet_fast_rcnn_iter_70000.h5'

detector = FasterRCNN()
network.load_net(model_file, detector)
detector.cuda()
detector.eval()
print('load model successfully!')


def detection(im_file, results_path, threshold):
    #print(im_file)
    #print(results_path)
    #print(threshold)
    #im_file = 'demo/004545.jpg'
    #im_file = 'data/VOCdevkit2007/VOC2007/JPEGImages/009036.jpg'
    # im_file = '/media/longc/Data/data/2DMOT2015/test/ETH-Crossing/img1/000100.jpg'
    image = cv2.imread(im_file)

    t = Timer()
    t.tic()
    dets, scores, classes = detector.detect(image, threshold)
    runtime = t.toc()
    
    print(dets.shape, scores.shape, classes.shape )

    person_idx = np.where(classes == 'person')
    #people  = np.asarray( [dets[person_idx]] )
    #p_scores = np.asarray([ scores[person_idx]] )
    people  = dets[person_idx]
    p_scores = scores[person_idx]
    if people.shape[0] == 0:
        people = people.reshape(0, 4)
    #people[..., np.newaxis]
    #p_scores[..., np.newaxis]
    #print(people)
    print(people.shape ,np.atleast_2d(people).shape)
    #print(p_scores.T)
    print(p_scores.shape, np.atleast_2d(p_scores).T.shape)
    people_detection = np.hstack((np.atleast_2d(people), np.atleast_2d(p_scores).T)).astype(np.float32)
    #print(people_detection)
    print('total spend: {}s'.format(runtime))
    
    # Save results to csv file

    save_file_path = os.path.join(results_path, 'detection_csv')
    save_detection_path = os.path.join(results_path,'images')
    if not os.path.isdir(save_detection_path):
        os.makedirs(save_detection_path)
    if not os.path.exists(save_file_path):
        os.makedirs(save_file_path)
   
    #os.path.basename(os.path.normpath(im_file))
    img_name = os.path.splitext(os.path.basename(os.path.normpath(im_file)))[0]
    file_name = img_name + '.csv'
    image_savename = img_name + '.jpg'

    out_csv = os.path.join(save_file_path, file_name)
    out_img = os.path.join(save_detection_path, image_savename)
    
    # Save detection results and images with rectangles
    np.savetxt(out_csv, people_detection, fmt=["%d",]*4 + ["%1.3f"], delimiter=",")

    im2show = np.copy(image)
    for i, det in enumerate(people_detection):
        det = tuple(int(x) for x in det)
        #print(det)
	
        cv2.rectangle(im2show, det[0:2], det[2:4], (255, 205, 51), 2)
        cv2.putText(im2show, '%s: %.3f' % (classes[i], scores[i]), (det[0], det[1] + 15), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 255), thickness=1)
    cv2.imwrite(out_img, im2show)
    #cv2.imshow('demo', im2show)
    #cv2.waitKey(0)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--source', help = 'Path to images', required = True )
	parser.add_argument('--save', help = 'Path to output files from detection', required = True)
	parser.add_argument('--thresh', help = 'Threshold value for detection', required = True )
	
	args = vars(parser.parse_args())

	if args['source'] is not None:
		input_path = args['source']
	if args['save'] is not None:
		results_path = args['save']
	if args['thresh'] is not None:
		threshold = float(args['thresh'])


	if not os.path.exists(results_path):
		os.makedirs(results_path)

	im_names = []

	for path, subdirs, files in os.walk(input_path):
		for name in files:
			if name.endswith(".jpg") or name.endswith(".png") or name.endswith(".pgm") or name.endswith(".jpeg"):
				im_names.append(os.path.join(path, name))
		print("Processing for {}".format(path))
		remaining = len(im_names)
		if remaining == 0:
			print("No files here at {}".format(path))
		for im_name in im_names:
			print ("{} images remaining".format(remaining))
			commonpref = os.path.commonprefix([path, results_path])
			rel_pth = os.path.relpath(path, commonpref)
			if not os.path.exists(os.path.join(results_path, rel_pth)):
				os.makedirs(os.path.join(results_path, rel_pth))
			im_base = os.path.basename(os.path.splitext(im_name)[0]) + '.jpg'
			if not os.path.exists(os.path.join(results_path,rel_pth,im_base)):
				detection(im_name, os.path.join(results_path,rel_pth), threshold)
			else:
				print("{} already exists. Moving to next !!".format(im_base))
			remaining = remaining - 1
		im_names = []


	#detection(input_path, results_path, threshold)
