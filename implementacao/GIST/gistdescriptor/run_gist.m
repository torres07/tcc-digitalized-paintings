% GIST Parameters:
clear param
param.imageSize = [256 256]; % set a normalized image size
param.orientationsPerScale = [8 8 8 8]; % number of orientations per scale (from HF to LF)
param.numberBlocks = 4;
param.fc_prefilt = 4;

%Obtain images from folders
sdirectory = 'base-tcc2';
jpegfiles = dir([sdirectory '/*.jpg']);

% Pre-allocate gist:
Nfeatures = sum(param.orientationsPerScale)*param.numberBlocks^2;
gist = zeros([length(jpegfiles) Nfeatures]); 

% Load first image and compute gist:
filename = [sdirectory '/' jpegfiles(1).name];
img = imresize(imread(filename),param.imageSize);
[gist(1, :), param] = LMgist(img, '', param); % first call
% Loop:
for i = 2:length(jpegfiles)
   filename = [sdirectory '/' jpegfiles(i).name];
   img = imresize(imread(filename),param.imageSize);
   gist(i, :) = LMgist(img, '', param); % the next calls will be faster
end
csvwrite('saida.csv',gist)