function img = readImage(fid)
% function img = readImage(fid)
%
% Read in a image entry from file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.

img.image_name = fgetl(fid);
img.width = uint16(fscanf(fid,'%d',1));
img.height = uint16(fscanf(fid,'%d',1));
img.default_obj_class = uint8(fscanf(fid,'%d',1));
img.numobjects = uint16(fscanf(fid,'%d\n',1));



