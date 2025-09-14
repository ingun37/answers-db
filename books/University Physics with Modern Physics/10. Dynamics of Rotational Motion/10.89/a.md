```matlab
clear;
syms g m h
Ks = [1/2;1;2/5;2/3];
Types = ['SC';'HC';'SS';'HS'];
function I=moment(k)
  syms m r2
  I = k * m * r2;
end
function rk = rotational_kinetic(k)
  syms r2 v2
  I = moment(k);
  w2 = v2 / r2;
  rk = 1/2 * I * w2;
end

function tk = translational_kinetic(k)
  syms m v2
  tk = 1/2 * m * v2;
end

resolve = @(e) (eval(subs(e, [g,m,h], [9.8 0.84,4.5])));

function y = velocity_squared(k)
  syms m h r2 v2 g
  y = solve(m*g*h == translational_kinetic(k) + rotational_kinetic(k),v2);
end

function t = time(v2)
  syms h
  th = deg2rad(35);
  s = h/sin(th);
  t = 2 * s / sqrt(v2);
end

V2s = arrayfun(@(x) (velocity_squared(x)), Ks);
Ts = arrayfun(@(x) (time(x)), V2s);
Tfs = arrayfun(resolve, Ts);

syms v2
eval_rotational_kinetic=@(k) (resolve(subs(rotational_kinetic(k), v2, velocity_squared(k))));
Rks=arrayfun(eval_rotational_kinetic, Ks);

function y=friction(k)
  syms f a r2 m g
  th = deg2rad(35);
  N = m * g * cos(th);
  E1 = m * g * sin(th) - f * N == m * a;
  E2 = r2*f*N == moment(k) * a;
  solution=solve([E1, E2], [f, a], Real=true);
  y = eval(solution.f);
end

Fs = arrayfun(@(x) (friction(x)), Ks);

table(Types,Ks,V2s, Tfs, Rks, Fs)
```

```
ans = 
    Types      Ks          V2s         Tfs       Rks        Fs   
    _____    _______    __________    ______    ______    _______

     SC          0.5    (4*g*h)/3     2.0463    12.348     0.2334
     HC            1    g*h           2.3628    18.522     0.3501
     SS          0.4    (10*g*h)/7    1.9769    10.584    0.20006
     HS      0.66667    (6*g*h)/5      2.157    14.818    0.28008
```