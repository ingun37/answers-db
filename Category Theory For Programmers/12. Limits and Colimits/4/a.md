In the context of given example from the book, it's same to equalizer. (Of course it's mostly not in outside of the context. Check out [wikipedia](https://en.wikipedia.org/wiki/Coequalizer))

I'll use the same example the book used explaining equalizer.

equalizer                  | coequalizer
---                        | ---
![]({{site.baseurl}}/assets/img/equalizer.jpg) | ![]({{site.baseurl}}/assets/img/equalizer-co.jpg)
$$ACx=BCx$$<br>$$\rightarrow \left( A-B\right) Cx=0$$<br>$$\rightarrow \left( \left( 1\enspace 2\right) -\left( -1\enspace 1\right) \right) C=0$$<br>$$\rightarrow \left( 2\enspace 1\right) C=0$$<br>$$\rightarrow C=\begin{pmatrix}1 \\ -2\end{pmatrix}$$<br> | $$CA\begin{pmatrix}x \\y\end{pmatrix}=CB\begin{pmatrix}x \\ y\end{pmatrix} $$<br>$$\rightarrow CA-CB=0$$<br>$$\rightarrow C\left( A-B\right) =0$$<br>$$\rightarrow C\left( 2\enspace 1\right) =0$$<br>$$\rightarrow C=\begin{pmatrix}1 \\-2\end{pmatrix}$$
