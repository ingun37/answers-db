<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS_CHTML">
</script>

Let's proove interchange law.

<p>
$\left( \beta '\cdot \alpha '\right) \circ \left( \beta \cdot \alpha \right) =\left( \beta '\circ \beta \right) \cdot \left( \alpha '\circ \alpha \right)$
</p>

Let's say each natural transformation is defined as

<p>
$\alpha :F\rightarrow F_{2}$<br>
$\alpha ':F_{2}\rightarrow F_{3}$<br>
$\beta :G\rightarrow G_{2}$<br>
$\beta ':G_{2}\rightarrow G_{3}$<br>
</p>

![]({{site.baseurl}}/assets/img/nat.JPG)

Let's see what we get with first one.
<p>
$\left( \beta '\cdot \alpha '\right) \circ \left( \beta \cdot \alpha \right)GF$ <br>
</p>
Using horizontal composition
<p>$=\left( \beta'\cdot \alpha '\right) G_{2}F_{2}$</p>
Again, using horizontal composition
<p>$=G_{3}F_{3}$</p>

Now the second one.
<p>
$\left( \beta '\circ \beta \right) \cdot \left( \alpha '\circ \alpha \right)GF$
</p>
Unlike previous one, we cannot directly apply the $(\alpha' \circ \alpha)$ to $GF$. No problem. We can composite horizontally with $id:G\rightarrow G$
<p>
$=\left( \beta '\circ \beta\right) \cdot \left( \left( id\cdot \alpha '\right) \circ \left( id\cdot \alpha \right) \right)GF$<br>
$=\left( \beta'\circ \beta\right)GF_3$
</p>
Same way but this time with $id:F\rightarrow F$
<p>
$=\left( \left( \beta'\cdot id\right) \circ \left( \beta \cdot id\right) \right) GF_{3}$<br>
$=G_3 F_3$
</p>

Proooven BAMMM