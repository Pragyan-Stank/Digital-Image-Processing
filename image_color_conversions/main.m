clc
clear all
close all

I = imread('auto.jpg'); % Load image

% Show original image
figure;
imshow(I);
title('Original Image');

% Convert to Grayscale
grayImage = toGrayscale(I);
figure;
imshow(grayImage);
title('Grayscale Image');

% Convert to Black and White
bwImage = toBlackWhite(grayImage, 128); % 128 is the threshold
figure;
imshow(bwImage);
title('Black and White Image');

% Remove one color channel at a time
removeChannel(I, 'R'); % Remove Red
removeChannel(I, 'G'); % Remove Green
removeChannel(I, 'B'); % Remove Blue
