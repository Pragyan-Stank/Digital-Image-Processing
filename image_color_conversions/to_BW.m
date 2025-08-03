function bw = toBlackWhite(gray, threshold)
    [rows, cols] = size(gray);
    bw = zeros(rows, cols, 'uint8');

    for i = 1:rows
        for j = 1:cols
            if gray(i,j) > threshold
                bw(i,j) = 255;
            else
                bw(i,j) = 0;
            end
        end
    end
end
