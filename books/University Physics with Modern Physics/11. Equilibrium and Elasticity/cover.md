Codes in this chapter shares following functions.

```matlab
% calculate the magnitude of the torque of two vectors
function t = torque(a,b)
    v = cross([a;0],[b;0]);
    t = v(3);
end

% rotate a 2d vector by theta
function y = rotate(x, theta)
  c = cos(theta);
  s = sin(theta);
  y = [c, -s; s, c] * x;
end
```