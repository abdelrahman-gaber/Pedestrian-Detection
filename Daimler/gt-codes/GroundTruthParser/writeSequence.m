function writeSequence(fp,seq, sep)
% function writeSequence(fp,seq, sep)
%
% Write a sequence entry to file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.


% sequence separator
fprintf(fp, [sep '\n']);

% sequence id
fprintf(fp, '%s\n', seq.seq_id);

% path to data
fprintf(fp, '%s\n', seq.path_to_seq_data);

% number of images
fprintf(fp, '%d\n', seq.numimages);
