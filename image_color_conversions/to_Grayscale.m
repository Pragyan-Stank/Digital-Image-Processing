function gray = toGrayscale(I)
    [rows, cols, ~] = size(I);
    gray = zeros(rows, cols);

    for i = 1:rows
        for j = 1:cols
            R = double(I(i,j,1));
            G = double(I(i,j,2));
            B = double(I(i,j,3));
            gray(i,j) = 0.3 * R + 0.59 * G + 0.11 * B;
        end
    end

    gray = uint8(gray); % Convert to displayable image
end
