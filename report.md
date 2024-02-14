# Merge Sort Runtime vs. Insertion Sort Runtime

## Hypothesis

Merge sort has a time complexity of $\theta(nlog(n))$ and a space complexity of 
$\theta(n)$. Insertion sort, on the other hand, has a time complexity of $O(n^2)$
and a space complexity of $\theta(1)$. While merge sort has an asymptotically faster
runtime complexity than insertion sort, merge sort accrues overhead from allocating
sub-arrays and copying into the sub-arrays. Moreover, due to the recursive nature
of merge sort, additional space and time must be spent on maintaining the call stack.
Due to the overhead, I expect insertion sort to be experimentally faster than merge
sort for input sizes of approximately 20 elements or fewer.

## Methodology

View the source code for this project [here](https://github.com/wskaggs/sorting-algorithm-runtime-visualization).

Both insertion sort and merge sort are experimentally tested according to the following
procedure for each input size in the range [1, 100]:

1. Create an array containing each integer in the range [0, input size).
2. Randomly shuffle the array, pass to the sorting algorithm, and measure the time taken
   to sort the array. 
3. Repeat step 2 for a total of ten trials.
4. Calculate and store the average time taken for the ten trials.

Once the analysis is complete, the average time to sort the array is plotted against
the respective input size for each sorting algorithm. See the next section to view my 
experimental results, which are collected using the CPython 3.10.2 interpreter.

## Results

![Algorithm runtime comparison graph](./images/runtime_visualization.png)

The above figure shows the experimental runtimes for both merge sort and insertion sort.
The x-axis represents the size of the array passed to the sorting algorithm and the y-axis
represents the average time taken to sort the array in seconds. Each sorting algorithm
is plotted as a line on the graph; view the legend to determine which line represents
which sorting algorithm.

## Discussion

Overall, I found no surprises or challenges in collecting and analyzing the data. Implementing the
sorting algorithms, experimentally collecting runtime data, and visualizing the collected data
was fairly smooth sailing. Moreover, the results match quite closely to my hypothesis.

## Conclusion

Under the conditions tested, insertion sort is a faster algorithm than merge sort for input sizes
of approximately 30 elements or fewer. For input sizes between 25 and 35 elements, the two algorithms
are almost indistinguishable in performance.
