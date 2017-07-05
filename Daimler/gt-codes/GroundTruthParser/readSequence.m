function sequence = readSequence(fid)
% function sequence = readSequence(fid)
%
% Read in a sequence entry from file identifier.
%
% This software is provided as is without warranty of any kind. 
% Please report bugs and suggestions to
% uni-heidelberg.enzweiler@daimler.com.

sequence.seq_id = fgetl(fid);
sequence.path_to_seq_data = fgetl(fid);
sequence.numimages = uint16(str2num(fgetl(fid)));


