function writeImageDatabase(idb,filename)
% function writeImageDatabase(idb,filename)
%
% Write image database to filename.
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
[fid,msg] = fopen(filename, 'w');
if (fid < 0)
    error(['cannot open file: ''' filename '''. Reason: ' msg]);
end


% sequences
for s=1:length(idb.sequences)
    writeSequence(fid, idb.sequences(s), seq_separator);
    imgList = idb.sequences(s).imgList;
    
    % images
    for i=1:length(imgList)       
        writeImage(fid, idb.images(imgList(i)), img_separator);
        objList = idb.images(imgList(i)).objList;
        
        % objects
        for o=1:length(objList)
          writeObject(fid, idb.objects(objList(o)), ...
                      obj_2d_separator, obj_3d_separator);        
        end
    end       
end

fclose(fid);