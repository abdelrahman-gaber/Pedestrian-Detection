function writeObject(fp, obj, sep2d, sep3d)
% function writeObject(fp, obj, sep)
%
% Write an object entry to file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.

% separator
if (obj.data(15))
    fprintf(fp, [sep3d ' ']);
elseif (obj.data(16))
    fprintf(fp, [sep2d ' ']);
else
    error('invalid object specification');
end

% object class
fprintf(fp, '%d\n', obj.data(1)); 

% ids
fprintf(fp, '%d %d\n', obj.data(2), obj.data(3)); 

% confidence
fprintf(fp, '%.4f\n', obj.data(4)); 

if (obj.data(15))
    % 3d position
    fprintf(fp, '%.2f %.2f %.2f\n', obj.data(5), obj.data(6), obj.data(7));
    fprintf(fp, '%.2f %.2f %.2f\n', obj.data(8), obj.data(9), obj.data(10));
elseif (obj.data(16))
    % 2d position
    fprintf(fp, '%d %d ', obj.data(11), obj.data(12));
    fprintf(fp, '%d %d\n', obj.data(13), obj.data(14));
    % one additional line which is ignored here
    fprintf(fp, '0\n');
else
    error('invalid object specification');
end
   