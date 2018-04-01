fid = fopen('C:\Users\peelo\Documents\tmp\novo_teste\log.txt','r');
txt = textscan(fid,'%s\n');
fclose(fid);
sdirectory = 'C:\Users\peelo\Documents\tmp\novo_teste\movimentos-artisticos';

jpegfiles = {};

for i = 1:length(txt{1})
    filename = txt{1}(i);
    jpegfiles{i} = strjoin([sdirectory,'\' ,filename], '');
end

for i = 1:length(jpegfiles)
    filename = jpegfiles(i);
    img = imread(filename{1});
    I = imread(filename{1});
    [rows, columns, numberOfColorChannels] = size(I);
    if numberOfColorChannels > 1
    % It's a true color RGB image.  We need to convert to gray scale.
        I = rgb2gray(I);
    end
    lbp_(i, :) = extractLBPFeatures(I);
end

csvwrite('lbp_features.csv',lbp_);