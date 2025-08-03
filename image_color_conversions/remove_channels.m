function removeChannel(I, channel)
    modified = I;

    if channel == 'R'
        modified(:,:,1) = 0;
        name = 'Red Removed';
    elseif channel == 'G'
        modified(:,:,2) = 0;
        name = 'Green Removed';
    elseif channel == 'B'
        modified(:,:,3) = 0;
        name = 'Blue Removed';
    else
        error('Invalid channel. Use R, G, or B.');
    end

    figure;
    imshow(modified);
    title(name);
end
