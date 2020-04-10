Let's proove interchange law.


$`\left( \beta '\cdot \alpha '\right) \circ \left( \beta \cdot \alpha \right) =\left( \beta '\circ \beta \right) \cdot \left( \alpha '\circ \alpha \right)`$


Let's say each natural transformation is defined as


$`\alpha :F\rightarrow F_{2}`$
$`\alpha ':F_{2}\rightarrow F_{3}`$
$`\beta :G\rightarrow G_{2}`$
$`\beta ':G_{2}\rightarrow G_{3}`$


![](assets/img/nat.JPG)

Let's see what we get with first one.

$`\left( \beta '\cdot \alpha '\right) \circ \left( \beta \cdot \alpha \right)GF`$ 

Using horizontal composition
$`=\left( \beta'\cdot \alpha '\right) G_{2}F_{2}`$
Again, using horizontal composition
$`=G_{3}F_{3}`$

Now the second one.

$`\left( \beta '\circ \beta \right) \cdot \left( \alpha '\circ \alpha \right)GF`$

Unlike previous one, we cannot directly apply the $`(\alpha' \circ \alpha)`$ to $`GF`$. No problem. We can composite horizontally with $`id:G\rightarrow G`$

$`=\left( \beta '\circ \beta\right) \cdot \left( \left( id\cdot \alpha '\right) \circ \left( id\cdot \alpha \right) \right)GF`$
$`=\left( \beta'\circ \beta\right)GF_3`$

Same way but this time with $`id:F\rightarrow F`$

$`=\left( \left( \beta'\cdot id\right) \circ \left( \beta \cdot id\right) \right) GF_{3}`$
$`=G_3 F_3`$


Proooven BAMMM