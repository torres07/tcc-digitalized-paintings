% GIST Parameters:
clear param
param.imageSize = [512 512]; % set a normalized image size
param.orientationsPerScale = [8 8 8 8]; % number of orientations per scale (from HF to LF)
param.numberBlocks = 4;
param.fc_prefilt = 4;

%Obtain images from folders
fid = fopen('/home/pedrotorres/Documents/UFC/TCC/log.txt','r');
txt = textscan(fid,'%s\n');
fclose(fid);
sdirectory = '/home/pedrotorres/Documents/UFC/TCC/copia';

jpegfiles = {};

for i = 1:length(txt{1})
    filename = txt{1}(i);
    jpegfiles{i} = strjoin([sdirectory,'/',filename], '');
end

% Pre-allocate gist:
Nfeatures = sum(param.orientationsPerScale)*param.numberBlocks^2;
gist = zeros([length(jpegfiles) Nfeatures]); 
% 
% Load first image and compute gist:
filename = jpegfiles(1605);
img = imresize(imread(filename{1}),param.imageSize);
[gist(1, :), param] = LMgist(img, '', param); % first call
% % Loop:
% for i = 2:length(jpegfiles)
%    filename = jpegfiles(i);
%    img = imresize(imread(filename{1}),param.imageSize);
%    gist(i, :) = LMgist(img, '', param); % the next calls will be faster
% end
% csvwrite('/home/pedrotorres/Documents/UFC/TCC/implementacao/GIST/gistdescriptor/csv/gist_features_novo.csv',gist)