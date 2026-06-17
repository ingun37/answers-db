```matlab
clear;
% in kg/m3
rho_Al = 2.7e3;
rho_Fe = 7.8e3;
rho_Cu = 8.9e3;
rho_Ag = 10.5e3;
rho_Pb = 11.3e3;
rho_Hg = 13.6e3;
rho_Au = 19.3e3;
rho_Pt = 21.4e3;


rho_array =  [rho_Al rho_Fe rho_Cu rho_Ag  rho_Pb rho_Hg rho_Au  rho_Pt];
% into g/m3
rho_array = rho_array .* 1e3;
% into g/cm3
rho_array = rho_array .* 1e-6;
mass_array = [26.982 55.845 63.546 107.868 207.2  200.59 196.967 195.078];
plot(rho_array, mass_array)
```

![figure_0.png](./p85_media/figure_0.png)