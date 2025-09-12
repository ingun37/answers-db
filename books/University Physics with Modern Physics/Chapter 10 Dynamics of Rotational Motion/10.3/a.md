```matlab
r=0.09
F1=[0;-24]
F2=[0;-15.8]
F3=rotd(45) * [15.5;0]

Fs=[F1 F2 F3]
Rs=[[r;0] [-r;0] [r;-r]]
Ls=arrayfun(@(i) (cro2(Fs(:,i), Rs(:,i))), 1:length(Fs))
sum(Ls)
```