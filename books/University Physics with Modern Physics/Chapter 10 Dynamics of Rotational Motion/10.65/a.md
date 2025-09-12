```matlab
function h = height(k)
    syms v g
    h = v^2 * (1 + k) / (2*g); 
end
height(2/5)
height(2/3)
disp("thin walled sphere goes higher")
```