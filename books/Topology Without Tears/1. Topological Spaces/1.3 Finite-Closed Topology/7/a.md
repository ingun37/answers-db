(i) If $`\tau_3`$ is defind by $`\tau_3 = \tau_1 \cup \tau_2`$ then $`\tau_3`$ is not necessarily a topology on $`X`$

> $`X = \{0, 1\}`$  
> $`\tau_1 = \{\emptyset, X, \{0\}\}`$  
> $`\tau_2 = \{\emptyset, X, \{1\}\}`$  

(ii) if $`\tau_4`$ is defined by $`\tau_4 = \tau_1 \cap \tau_2`$, then $`\tau_4`$ is a topology on $`X`$.

> Let $`A`$ and $`B`$ be from $`\tau_4`$.  
> (1) $`A`$ and $`B`$ are in $`\tau_1`$ $`\rightarrow`$ $`A \cap B \in \tau_1`$  
> (2) $`A`$ and $`B`$ are in $`\tau_2`$ $`\rightarrow`$ $`A \cap B \in \tau_2`$  
> (1) and (2) $`\rightarrow`$ $`A \cap B \in \tau_4`$

> Let $`S = \bigcup _{j\in J} S_j `$ where each $`S_j \in \tau_4`$ and $`J`$ is infinite or finite index set.  
> (1) Each $`S_j`$ are in $`\tau_1`$ $`\rightarrow`$ $`S \in \tau_1`$  
> (2) Each $`S_j`$ are in $`\tau_2`$ $`\rightarrow`$ $`S \in \tau_2`$  
> (1) and (2) $`\rightarrow S \in \tau_4`$

(iii) if $`(X, \tau_1)`$ and $`(X, \tau_2)`$ are $`T_1`$-spaces, then $`(X, \tau_4)`$ is also a $`T_1`$-space.

> If a subset $`s`$ is closed in both $`\tau_1`$ and $`\tau_2`$, then $`s`$ is closed in $`\tau_4`$.  
> For every $`x`$ that is $`x \in X`$, $`\{x\}`$ is closed in both $`\tau_1`$ and $`\tau_2`$.  
> $`\rightarrow \{x\}`$ is closed in $`\tau_4 \rightarrow \tau_4`$ is $`T_1`$-space 

(iv) If $`(X, \tau_1)`$ and $`(X,\tau_2)`$ are $`T_0`$-spaces, then $`(X,\tau_4)`$ is not necessarily a $`T_0`$-space.

> $`X = \{0, 1\}`$  
> $`\tau_1 = \{\emptyset, X, \{0\}\}`$  
> $`\tau_2 = \{\emptyset, X, \{1\}\}`$  

(v) If $`\tau_1, \tau_2, ... , \tau_n`$ are topologies on a set $`X`$, then $`\tau = \bigcap ^{n}_{i=1}\tau_i`$ is a topology on $`X`$

> Goes same as (ii)

(vi) If for each $`i \in I`$, for some index set $`I`$, each $`\tau_i`$, is a topology on the set $`X`$, then $`\tau = \bigcap _{i \in I} \tau_i`$ is a topology on $`X`$

> Goes same as (ii)