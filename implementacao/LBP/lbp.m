sdirectory = 'C:\Users\peelo\Documents\tmp\movimentos-base';
jpegfiles = dir([sdirectory '/*.jpg']);

for i = 1:length(jpegfiles)
    filename = [sdirectory '/' jpegfiles(i).name];
    I = imread(filename);
    
    [rows, columns, numberOfColorChannels] = size(I);
    if numberOfColorChannels > 1
    % It's a true color RGB image.  We need to convert to gray scale.
        I = rgb2gray(I);
    end
    lbp_(i, :) = extractLBPFeatures(I);
end

csvwrite('lbp_features.csv',lbp_);