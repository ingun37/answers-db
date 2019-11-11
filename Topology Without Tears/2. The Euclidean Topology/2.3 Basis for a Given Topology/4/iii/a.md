<p>
Understanding of convergeance is a prerequisite.
<br>
By definition, if two topologies are really same, a sequence must converge to same point in both topology.
<br>
Let's define $ f_{n}\left( x\right) $ and see if it converge to same point in both $ \tau _{1}$ and $ \tau _{2}$
$$ f_{n}\left( x\right) :=e^{-\dfrac {n^{2}x^{2}}{2}} $$
It is a function of gaussian form
<br>
Being a gaussian form, definite integral from $ -\infty $ to $ \infty $ would be
$$ \int ^{\infty }_{-\infty }f_{n}=\dfrac {\sqrt {2\times \pi }}{n} $$
Since the function is always positive, trivially definite integral from 0 to 1 would be smaller than $ -\infty $ to $ \infty $ isn't it?
<br>
Being always positive also trivially deduce following statements
$$ f_{n}=\left| f_{n}\right| =\left| f_{n}-0\right| $$
Now lets prove that $ f_{n} $ converge to 0 in $ \tau_{1} $
<br>
Given any $ \varepsilon $, there exist integer $ n_{0}$ which holds
$$ \int ^{1}_{0}f_{n_{0}} <\int ^{\infty }_{-\infty }f_{n_{0}}=\dfrac {\sqrt {2\times \pi }}{n_{0}} <\varepsilon $$
deduce
$$ \forall n\geq n_{0},d\left( 0,f_{n}\right) =\int ^{1}_{0}\left| f_{n}-0\right| =\int ^{1}_{0}f_{n} <\int ^{\infty }_{-\infty }f_{n}=\dfrac {\sqrt {2\times \pi }}{n}\leq \dfrac {\sqrt {2\times \pi }}{n_{0}} <\varepsilon $$
Now lets prove that $ f_{n} $ does not converge to 0 in $ \tau_{2} $
<br>
It's easy since gaussian function always has supermum of 1 so in $ \tau_{2} $ following holds no matter what $ f_{n}$
$$ d\left( 0,f_{n}\right) =\sup _{x\in \left[ 0,1\right] }\left| f_{n}-0\right| =1$$
So $ \tau_{1} $ and $ \tau_{2}$ is not same
<br>
following image summarizes
</p>

![]({{site.baseurl}}/assets/img/img.jpg)