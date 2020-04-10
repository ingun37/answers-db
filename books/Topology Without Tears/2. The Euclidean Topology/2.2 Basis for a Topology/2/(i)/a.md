The basic idea is using triangle inequality just like exercise #1-(I).

Let $`r_n`$ $`c_n`$ be $`D_n`$'s radius and center.  
Let's define $`r`$ as

$`r=\min \left( r_{1}-\left| c_{1}-c\right| ,r_{2}-\left| c_{2}-c\right| \right)`$

But for simplicity and without lose of generality, let's just say

$`r=r_{1}-\left| c_{1}-c\right|`$

Let $`p`$ be any point in the small disc $`D_{\langle a,b \rangle}`$.  
Checkout the visual representation so far.

![](assets/IMG_CE178B00DC15-1.jpeg)

First let's proove that $`p`$ is inside of $`D_1`$.  
Triangle inequality of $`c1, p, c`$ says

$`\left| c_{1}-p\right|  <\left| c-p\right| +\left| c_{1}-c\right|`$

$`\left| c-p\right|`$ is smaller than $`r`$ so we can just substitute it and get the definition of $`D_1`$. Hence $`p`$ is inside of $`D_1`$.

$`\left| c_{1}-p\right|  <\left( r_{1}-\left| c_{1}-c\right| \right) +\left| c_{1}-c\right| =r_{1}`$

Now let's proove that $`p`$ is inside of $`D_2`$.  
Triangle inequality of $`c2, p, c`$ says  

$`\left| c_{2}-p\right|  <\left| c-p\right| +\left| c_{2}-c\right|`$

Now we substitute the $`\left| c-p\right|`$ just like what we just did to $`D_1`$

$`\left| c_{2}-p\right|  <\left( r_{1}-\left| c_{1}-c\right| \right) +\left| c_{2}-c\right|`$

But we already have this in our bag.

$`r_{1}-\left| c_{1}-c\right|  <r_{2}-\left| c_{2}-c\right|`$

We can just substitute and the relation won't change.

$`\left| c_{2}-p\right|  <\left( r_{2}-\left| c_{2}-c\right| \right) +\left| c_{2}-c\right| =r_{2}`$

We've got the $`D_2`$ definition. Hence $`p`$ is in $`D_2`$. Hence $`p \in D_1 \cap D_2`$