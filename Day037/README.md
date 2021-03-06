# Maximum_every_subarray_k_window_sliding
![Stars](https://img.shields.io/github/stars/KERBOUTE/100Dayscodechallenge?style=social)
![Forks](https://img.shields.io/github/forks/KERBOUTE/100Dayscodechallenge?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/KERBOUTE/100Dayscodechallenge)
![Language](https://img.shields.io/github/languages/top/KERBOUTE/100Dayscodechallenge)

Hello, the problem of the day 037, is a problem recently posed by Apple:

program to print maximum of all possible subarrays of k window size
##### Input: 
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
##### Output: 
3 3 4 5 5 5 6
All ccontigious subarrays of size k are
```
# {1, 2, 3} => 3
# {2, 3, 1} => 3
# {3, 1, 4} => 4
# {1, 4, 5} => 5
# {4, 5, 2} => 5
# {5, 2, 3} => 5
# {2, 3, 6} => 6
```
##### Input: 
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4
##### Output: 
10 10 10 15 15 90 90

Naive solution would take 0(N^2) => using two loops, one for outer loop and one inner loop for total array and k size block traversal respectively.


We can also try window sliding techniuqe and simulate it using two pointers both pointing at start and end of k-sized window.
Then, we move one pointer one by one k times and update the max, till it becomes equal to second pointer, there we got max for that subarray
now, we have find the maximum of subarrays of that particular k sized window, then we go for increment second pointer, and then first pointer by 1 from last saved first pointer checkpoint.
In this way, we go through all the subsarrays , this method is actually same as first one, just the way of understanding is different and that's why coding is slightly different but overall asymtodic bounds are same => 0(N * K) which is not better but in space it's 0(1).

using deque DS from collections to build linear time solution as following the logic below basically, idea is to keep a track of all useful elements for a window which keeps sliding across the array one by one, the useful element is one whichis greater than all right elements in the current window. so, basically for every window we need maximum in 0(1) so that we can compare it with incoming new element and then either keep it or remove it, and simulatenously also sliding the window, so the best option is to use Deque so that we will be able to slide the window by popping the elements from left side which is not in current window, and also keep track of maximum at the front by comparing it with each incoming element and also one important thing is that, we need to keep minimum as it at the right side, as [3...2..0...-1], so if cur_max is 3, then we also need to have 2 because maybe in next window, we can have 2 as maximum, threby it will maintain all elements (indices) of elements in decreasing order.

#### time : 
0(N), space : 0(K)
```
# |1, 2, 3|, 1, 4, 5, 2, 3, 6 => deque : [3]
#         ^
# 1 |2 3 1| 4 5 2 3 6 => deque : [3, 1]
#        ^                       
# 1 2 |3 1 4| 5 2 3 6 => deque : [4]
#          ^                     
# 1 2 3 |1 4 5| 2 3 6 => deque : [5]
#            ^
# 1 2 3 1 |4 5 2| 3 6 => deque : [5, 2]
#              ^
# 1 2 3 1 4 |5 2 3| 6 => deque : [5, 3]
#                ^ 
# 1 2 3 1 4 5 |2 3 6| => deque : [6]
             
```   
           
The deque is empty now , final output as seen from above simulation : 3, 3, 4, 5, 5, 5, 6

We can also apply heap based sliding window approach, where max-heap can be used to obtain max from k sized heap in 0(1), but the problem is in getting random access  when we move out of theh window, we will not be directly able to delete the non useful elements (whcih are not part of curr window) as we need their indices to delete  from heap, and so we find the index in the heap, and replace it with the next obtained element in the current wndow.

Max-heaify to restore heap, and get the max from root, and then increment pointers i and j poitning for window control.

Asymtodically, this will also take 0(N * K) so, deque based in 0(N) is probably good enough for this problem.

There are more methods like using self-BST for solving this problem in 0(N * log(K))

## Contact
Created by me [Amine KERBOUTE](https://github.com/KERBOUTE)

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="aminekerboute@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/amine-kerboute/" target="_blank">LinkedIn</a>, or 
<a href="https://twitter.com/KerbouteA" target="_blank">Twitter</a>. 
My other projects can be found [here](https://github.com/KERBOUTE?tab=repositories).