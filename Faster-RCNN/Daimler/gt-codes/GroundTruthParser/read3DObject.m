function obj = read3DObject(fid)
% function obj = read3DObject(fid)
%
% Read in a 3D object entry from file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.


obj.data = sparse(17,1);
obj.data(1) = uint8(fscanf(fid,'%d\n',1));
obj.data(2) = uint32(fscanf(fid,'%d',1));
obj.data(3) = uint32(fscanf(fid,'%d\n',1));
obj.data(4) = single(str2double(fgetl(fid)));
obj.data(5) = single(fscanf(fid,'%g',1));
obj.data(6) = single(fscanf(fid,'%g',1));
obj.data(7) = single(fscanf(fid,'%g\n',1));
obj.data(8) = single(fscanf(fid,'%g',1));
obj.data(9) = single(fscanf(fid,'%g',1));
obj.data(10)= single(fscanf(fid,'%g\n',1));
%obj.data(11:14) = 0; % only relevant for 2D
obj.data(15) = 1;
%obj.data(16) = 0;



% obj.object_class = uint8(fscanf(fid,'%d\n',1));
% obj.obj_id = uint32(fscanf(fid,'%d',1));
% obj.unique_id = uint32(fscanf(fid,'%d\n',1));
% obj.confidence = single(str2double(fgetl(fid)));
% obj.position = sparse(10,1);
% obj.position(1,1)    = single(fscanf(fid,'%g',1));
% obj.position(2,1)    = single(fscanf(fid,'%g',1));
% obj.position(3,1)    = single(fscanf(fid,'%g\n',1));
% obj.position(4,1)    = single(fscanf(fid,'%g',1));
% obj.position(5,1)    = single(fscanf(fid,'%g',1));
% obj.position(6,1)    = single(fscanf(fid,'%g\n',1));
% obj.position(7:10,1) = 0; % only relevant for 2D
% obj.imgIndex  = imgCount;
% obj.has3DPos = 1;
% obj.has2DBox = 0;





