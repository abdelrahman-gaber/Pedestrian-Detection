function idb=readImageDatabase(filename)
% function idb=readImageDatabase(filename)
%
% Read in an image database file.
%
% INPUT
%    filename - file to read image database from
%
% OUTPUT
%    idb - image database structure
%
% readImageDatabase(filename) reads an image database from filename and
% returns an image database structure idb containing :
%
% idb.sequences : all sequences in the image database
% idb.images    : all images in the image database
% idb.objects   : all objects in the image database
%
% The format of sequence, image and object is as follows:
%
% sequence
% ++++++++
%   seq_id           : sequence ID identifying this sequence
%   path_to_seq_data : path where the images are located
%   numimages        : number of images in this sequence
%
% image
% +++++
%   image_name        : filename of this image
%   width             : image width
%   height            : image height
%   default_obj_class : default class of objects in this image
%                       (can be overridden by object.data(1))
%   numboxes          : number of objects in this image
%   seqindex          : index of sequence this image belongs to
%
% object
% ++++++
% Note: In order to save memory object data is stored in one 
%       large (sparse) vector, instead of individual fields
%
%   data              : 16-dimensional vector of object data
%                       with the following entries
%   data(1)           : object_class
%                       0=pedestrian, 1=bicyclist, 
%                       2=motorcyclist, 10=pedestrian group, 
%                       255=partially hidden object
%   data(2)           : track id, identifying the same physical
%                       objects in multiple images
%   data(3)           : unique id, identifying this particular 
%                       object in this image
%   data(4)           : object confidence
%   data(5:10)        : 3D object position in the world
%                       [x_min, y_min, z_min, x_max, y_max, z_max]
%   data(11:14)       : 2D object position in the image
%                       [x_min, y_min, x_max, y_max]
%   data(15)          : boolean flag whether this object has 
%                       3D position available (see data(5:10))
%   data(16)          : boolean flag whether this object has 
%                       2D bounding box available (see data(11:14))
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.


% separator characters
seq_separator = ':';
img_separator = ';';
obj_2d_separator = '#';
obj_3d_separator = '§';

% open file
[fid,msg] = fopen(filename, 'r');
if (fid < 0)
    error(['cannot open file: ''' filename '''. Reason: ' msg]);
end

% initialize counters
seqCount = 1;
imgCount = 1;
objCount = 1;


while (~feof(fid))
    token = fscanf(fid, '%c',1);
    
    % check for sequence separator

    if (strcmp(token,seq_separator))   
        % eat up rest of line
        fgetl(fid);
        seq = readSequence(fid);
        seq.imgList = zeros(seq.numimages,1);
        idb.sequences(seqCount) = seq;
        seqCount = seqCount+1;  
        seqImgIndex = 1;
    elseif (strcmp(token,img_separator))   
        % eat up rest of line
        fgetl(fid);      
        img = readImage(fid);          
        img.objList = zeros(img.numobjects,1);  
        idb.images(imgCount) = img;       
        idb.sequences(seqCount-1).imgList(seqImgIndex) = imgCount;
        imgObjIndex = 1;
        imgCount = imgCount+1;        
        seqImgIndex = seqImgIndex+1;
    elseif (strcmp(token,obj_3d_separator)) 
        idb.objects(objCount) = read3DObject(fid);  
        idb.images(imgCount-1).objList(imgObjIndex) = objCount;
        objCount = objCount+1;      
        imgObjIndex = imgObjIndex+1;
    elseif (strcmp(token,obj_2d_separator)) 
        idb.objects(objCount) = read2DObject(fid); 
        idb.images(imgCount-1).objList(imgObjIndex) = objCount;
        objCount = objCount+1;
        imgObjIndex = imgObjIndex+1;
    else
        error(['Parse error: Unknown token ''' token '''']);
    end
end

fclose(fid);