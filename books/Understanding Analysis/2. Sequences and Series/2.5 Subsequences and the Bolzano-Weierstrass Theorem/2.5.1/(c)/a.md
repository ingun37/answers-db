Arrange the numbers like this

```math
\begin {aligned}
& 1 \\
& 1, \enspace \frac 1 2 \\
& 1, \enspace \frac 1 2, \enspace \frac 1 3 \\
& 1, \enspace \frac 1 2, \enspace \frac 1 3, \enspace \frac 1 4 \\
& \dots
\end {aligned}
```

Now concatenate them.

```math
S = \left( 1, 1, \frac 1 2, 1, \frac 1 2, \frac 1 3, 1, \frac 1 2, \frac 1 3, \frac 1 4, \dots \right)
```

You can formulate any subsequence that is consists of only one specific numbers. For example, the subsequence of 1/3 would be

```math
S'_i = S_{6 + (3 + (3 + i - 1)) * i / 2} = \left(\frac 1 3, \enspace \frac 1 3, \enspace \frac 1 3, \enspace \frac 1 3, \enspace \dots \right)
```