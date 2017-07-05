function obj = read2DObject(fid)
% function obj = read2DObject(fid)
%
% Read in a 2D object entry from file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.

obj.data = sparse(17,1);
obj.data(1) = uint8(fscanf(fid,'%d\n',1));
obj.data(2) = uint32(fscanf(fid,'%d',1));
obj.data(3) = uint32(fscanf(fid,'%d\n',1));
obj.data(4) = single(str2double(fgetl(fid)));
%obj.data(5:10) = 0; % only relevant for 3D
obj.data(11)  = uint16(fscanf(fid,'%d',1));
obj.data(12)  = uint16(fscanf(fid,'%d',1));
obj.data(13)  = uint16(fscanf(fid,'%d',1));
obj.data(14)  = uint16(fscanf(fid,'%d\n',1));
% eat up one additional line (ignored here)
ignore        = fscanf(fid,'%g\n',1);
%obj.data(15) = 0;
obj.data(16) = 1;


% obj.object_class = uint8(fscanf(fid,'%d\n',1));
% obj.obj_id = uint32(fscanf(fid,'%d',1));
% obj.unique_id = uint32(fscanf(fid,'%d\n',1));
% obj.confidence = single(str2double(fgetl(fid)));
% obj.position = sparse(10,1);
% obj.position(1:6,1) = 0; % only relevant for 3D
% obj.position(7,1)  = uint16(fscanf(fid,'%d',1));
% obj.position(8,1)  = uint16(fscanf(fid,'%d',1));
% obj.position(9,1)  = uint16(fscanf(fid,'%d',1));
% obj.position(10,1) = uint16(fscanf(fid,'%d\n',1));
% % eat up one additional line (ignored here)
% ignore        = fscanf(fid,'%g\n',1);
% obj.imgIndex = imgCount;
% obj.has3DPos = 0;
% obj.has2DBox = 1;
% 
% 
% 
% 
