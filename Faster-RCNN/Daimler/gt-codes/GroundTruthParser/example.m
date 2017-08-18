% Read and display 2D and 3D Ground Truth files.

clear all;
close all;

% read 2D database
gt2D_fname = '../GroundTruth/GroundTruth2D.db';
disp(['reading ' gt2D_fname ' ...']);
gt2D = readImageDatabase(gt2D_fname);
printImageDatabase(gt2D);
clear gt2D;

% read 3D database
% gt3D_fname = '../GroundTruth/GroundTruth3D.db';
% disp(['reading ' gt3D_fname ' ...']);
% gt3D = readImageDatabase(gt3D_fname);
% printImageDatabase(gt3D);
% clear gt3D;

