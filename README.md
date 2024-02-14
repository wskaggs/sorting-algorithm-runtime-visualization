# Sorting Algorithm Runtime Comparison

The runtime complexity of merge sort is $\theta(nlog(n))$; insertion sort,
on the other hand, has a runtime complexity of $O(n^2)$. As such, we know that
merge sort will be faster than insertion sort for large input sizes. However,
it turns out that insertion sort is faster for very small input sizes. The 
objective of this project is to determine the largest input size for which
insertion sort is faster than merge sort using experimental data.
