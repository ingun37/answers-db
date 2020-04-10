Let $`l`$ be the limit of the identity functor.  
To be an initial object, there must be only one morphism from $`l`$ to any other object.  
If there's 2 morphisms $`m`$ and $`n`$ from $`l`$ to some other object $`o`$, and if the 2 morphisms are same, then it must imply that $`l`$ is a initial object. Let's proove it.

Just like a cone can't have two lines for one base vertex, $`l`$, as an apex of a cone, can't have both $`m`$ and $`n`$. We have to assign one morphism, to say $`n`$, to some other apex $`a`$.

$`m:l\rightarrow o`$
$`n:a\rightarrow o`$

Being a limit point, there must be a unique factorizing morphism $`f`$ from $`a`$ to $`l`$ which makes $`n = m \cdot f`$.

$`\exists ! f:a \rightarrow l \enspace s.t \enspace n = m \cdot f`$

But $`l`$ and $`a`$ is same point that means $`f`$ must be $`id`$ morphism which means $`n = m \cdot id`$ again which means $`n = m`$

$`l=a`$
$`\rightarrow f = id`$
$`\rightarrow n = m \cdot id`$
$`\rightarrow n=m`$
