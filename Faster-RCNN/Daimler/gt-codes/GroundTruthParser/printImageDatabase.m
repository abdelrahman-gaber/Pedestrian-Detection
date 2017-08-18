function printImageDatabase(idb)
% function printImageDatabase(idb)
%
% Print image database to console.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.

% sequences
for s=1:length(idb.sequences)
    disp(['Sequence ''' idb.sequences(s).seq_id '''']);
    disp(['  Path     : '''  idb.sequences(s).path_to_seq_data '''']);
    disp(['  # images : ' num2str(idb.sequences(s).numimages)]);
    
    imgList = idb.sequences(s).imgList;
    
    % images
    for i=1:length(imgList)       
        img = idb.images(imgList(i));
        disp(['  Image ''' img.image_name '''']);
        disp(['    Dimensions : ' num2str(img.width) ... 
              'x' num2str(img.height)]);
        disp(['    # objects  : ' num2str(img.numobjects)]);
        
        objList = img.objList;
        
        % objects
        for o=1:length(objList)
            obj = idb.objects(objList(o));
            disp(['      Object # ' num2str(obj.data(3))]);
            disp(['        Class        : ' num2str(obj.data(1))]);
            disp(['        Track ID     : ' num2str(obj.data(2))]);
            disp(['        Confidence   : ' num2str(obj.data(4))]);
            if (obj.data(15))
                % has 3D position
                 disp(['        3D Position  : ' num2str(obj.data(5:10)')]);
            end
            if (obj.data(16))
                % has 2D box
                 disp(['        2D Position  : ' num2str(obj.data(11:14)')]);
            end
        end
    end       
end