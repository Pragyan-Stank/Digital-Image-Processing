clc
clear all
close all

n=5;   %input
fact=1;  %to store factorial
for ii=1:n     % loop to find factorial of number
    fact=fact*ii;    
end

disp(fact);    % display factorial
