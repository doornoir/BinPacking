# BinPacking

Bin Packing 
In the bin packing problem, items of different weights (or sizes) must be packed into a finite 
number of bins, each with capacity C, so that the number of bins used is minimized. The 
decision version of the problem (can the items be packed into at most k bins?) is NP
complete. There is no known polynomial-time algorithm for the optimization version. 
In this homework you will implement and compare four greedy approximation algorithms. 
You will evaluate both the quality of the solutions (number of bins used) and the running 
time of each algorithm. 
  • First Fit: Place each item into the first open bin in which it fits. If no bin has sufficient 
  remaining capacity, open a new bin. 
  • First Fit Decreasing: Sort the items in decreasing order, then apply First Fit. 
  • Best Fit: Place each item into the bin that leaves the least remaining space after 
  insertion. If no bin fits, open a new bin. 
  • Best Fit Decreasing: Sort the items in decreasing order, then apply Best Fit. 
  Part 1: Psuedocode  (10 pts) 
Give pseudocode and the asymptotic running time for each of the four approximation 
algorithms. 

Part 2: Implementation (25 pts) 
Implement the four approximation algorithms in Python or C++. Name your program 
"binpack.py" or "binpack.cpp". The program shall read the input from bin.txt and, for each 
test case, output the number of bins used by each algorithm together with its running time. 
Public testing files (bin.txt, BinPackingSolution.txt, and HW4.sh) are provided. Before 
submitting, verify that your program executes correctly using HW4.sh. Passing the public 
tests does not guarantee full credit; additional hidden test cases will be used during grading. 
Input Format 
The first line contains the number of test cases. Each test case consists of: 
  • Bin capacity C 
  • Number of items n 
  • n item weights 
You may assume every item weight is less than or equal to the bin capacity. 
 
Example bin.txt 
 
      3 
      10 
      6 
      5 10 2 5 4 4 
       
      10 
      20 
      4 4 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 6 6 
       
      10 
      4 
      3 8 2 7 
 
Sample Output 
      Test Case 1 
      First Fit: 4, Time: ... 
      First Fit Decreasing: 3, Time: ... 
      Best Fit: 4, Time: ... 
      Best Fit Decreasing: 3, Time: ... 
       
      Test Case 2 
      First Fit: 15, Time: ... 
      First Fit Decreasing: 10, Time: ... 
      Best Fit: 15, Time: ... 
      Best Fit Decreasing: 10, Time: ... 
       
      Test Case 3 
      First Fit: 3, Time: ... 
      First Fit Decreasing: 2, Time: ... 
      Best Fit: 2, Time: ... 
      Best Fit Decreasing: 2, Time: ... 
 
Note: The running times will vary depending on your computer and programming 
language. The number of bins should match the sample output.  
 
 
Part 3: Experimental Analysis (15 pts) 
After verifying your implementation using the provided test files, experimentally compare 
the four algorithms. 
Generate at least 10 random bin packing instances with an increasing number of items. 
For all test cases: 
  • Use the same bin capacity for every test case (for example, C = 100). 
  • Generate random item weights between 1 and C (inclusive), so every item fits into 
  an empty bin. 
  • Increase only the number of items (for example, n = 100, 200, 300, ..., 1000). 
  Briefly describe how the random inputs were generated. Do not submit the code used to 
  generate the random inputs. 
  Solution Quality  
  • Record the number of bins used by each approximation algorithm. 
  • Create a graph showing the number of bins used as a function of the number of items. 
  • Based on your results, determine which algorithm generally produced the best packing 
  and explain why. 
  Running Time  
  • Measure the running time of each algorithm. 
  • Create a graph showing running time as a function of the number of items. 
  • Determine which algorithm was the fastest and discuss any significant differences. 
  Testing on Flip 
Place HW4.sh, bin.txt, BinPackingSolution.txt, and your source code in the same directory. 
Run: 
sh HW4.sh 
Submission: 
Submit the following two files in Canvas: 
  1. HW4.pdf - Answers to Problems 1 and 3 
  2. HW4.zip 
    • binpack.py or binpack.cpp 
    • bin.txt 
    • BinPackingSolution.txt 
    • HW4.sh 
