% raed and parse daimler ground truth 

clear all;

AnnotPath = '/data/stars/user/aabubakr/pd_datasets/datasets/Daimler/DaimlerBenchmark/annotations-test-parsed';
if ~exist(AnnotPath, 'dir')
    mkdir(AnnotPath);
end

% read 2D database
gt2D_fname = '../GroundTruth/GroundTruth2D.db';
disp(['reading ' gt2D_fname ' ...']);
gt2D = readImageDatabase(gt2D_fname);

for i = 1 : size(gt2D.images, 2)
    image_name = gt2D.images(i).image_name;
    % each image has number of objects (refer to objects struct)
    %fprintf( 'image: %s \n' , image_name );
    ImageName = strcat(AnnotPath, '/' , image_name, '.txt');
    %display(ImageName)
    
    %fileID = fopen(ImageName,'w');
    
    for j = 1 : size(gt2D.images(i).objList, 1)
        ObjNum = gt2D.images(i).objList(j);
        AnnotSparse = gt2D.objects(ObjNum).data(11:14);
        Annot = full(AnnotSparse); % from sparse to full matrix
        
        fprintf('%d %d %d %d \n', Annot(1), Annot(2), Annot(3), Annot(4));
        %fprintf(fileID, '%d %d %d %d \n', Annot(1), Annot(2), Annot(3), Annot(4));
    end
    
    %fclose(fileID);
end