function writeImage(fp, img, sep)
% function writeImage(fp, img, sep)
%
% Write an image entry to file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.


% separator
fprintf(fp, [sep '\n']);

% name
fprintf(fp, '%s\n', img.image_name);

% dimensions
fprintf(fp, '%d %d\n', img.width, img.height);

% default class + number of objects
fprintf(fp, '%d %d\n', img.default_obj_class, img.numobjects); 

