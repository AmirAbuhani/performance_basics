Author: Amir Abu Hani

Note: see the attached results_file.pdf file for the results. This results are showing by plots.

The first problem that I'm measured its complexity time is the fibonacci sequence up to X elements:
for the 2 variants, I'm selected the following inputs: 5, 10, 15, 20, 25, 30, 35, 40
The first variant for this problem was  recursive_fibonacci_sequence. The complexity time for this variant is O(2^n),
because for each fibonacci number, the function branching into two recursive calls. 
The results are that for these inputs, the measured time can be more than 60 seconds for the fibonacci number 40.
The second variant for this problem was iterative_fibonacci. The complexity time for this variant is 0(n), because 
the time taken by the function grows linearly with the input number(overall, we have for loop that iterate until the fib
number).
The results are that for these inputs, the measured time can be about 0.000015 seconds for the 40 fib number.
So, we can conclude that the second variant is more efficient for the fib problem than the second one.

The second problem that I'm measured its complexity time is the searching number in list:
For the 2 variants, I'm selected for list different sizes(10, 100, 1000, 10000).
The first variant for this problem was searching_inlist_first_variant. It's time complexity O(n), because we iterate 
over the list size(which is n) and search about the item.
The results are for example list that conclude 10000 items, the measured time can be about 0.000175 seconds.
The second variant was searching_inlist_second_variant. The time complexity is 0(n*log(n)), because at first we sort
the list in ascending sorting(by the built-in sorted function) which takes 0(n*log(n)(it can be any type pf sorting),
and then when the list is sorted, we do binary searching about the goal item. this binary search is O(log(n)).
so, T(n) = O(nlog(n)) + O(log(n)) = O(nlog(n))
The results are for example list that conclude 10000 items, the measured time is about 0.0030.
So, if we compared the 2 variants, we saw that first variant is more efficient than the second one.

The third problem that I'm measured its complexity time is the count word occurrences in a text.
For the 2 variants, I'm selected 4 text files that include 10, 100, 1000, 10000 words respectively.
The first variant for this problem was the count_word_first_variant. The time complexity is 0(n*m). the n is the 
number of the words in the file, and the m is the length of specific word that we do check. so, foe eche word in the
file, we do check if the given word is the same word for the comparison word.
The results are that for example 10000 words, the measured time is about 0.00035 seconds.
The second variant for this problem is the count_word_second_variant. The time complexity is O(n), because it iterates
over each word in the file and updates the frequency of each word in the frequency_word_dict dictionary by using the
.get() method and retrieve the current frequency and incrementing it by 1.
The results for this variant for example text with 10000 words about is 0.00043 seconds.
So, we can conclude that the 2 variants are had the same time approximately.