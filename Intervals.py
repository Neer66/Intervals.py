
#  File: Intervals.py

#  Description: Take a list of intervals stored as tuples and return the intervals merging overlapping
#               intervals from lowest to highest number. Afterwards, the code arranges the merged intervals
#               by size from smallest interval size to largest

#  Student Name: Neer Jain

#  Student UT EID: nj6229

#  Partner Name: none

#  Course Name: CS 313E

#  Unique Number: 52235

#  Date Created: 02/01/2021

#  Date Last Modified: 02/05/2021

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
    tuples_list.sort()
    # change tuple pairs into two separate lists to alter them
    list_of_tuples = []
    for i in range(len(tuples_list)):
        list_of_tuples.append(list(tuples_list[i]))
    intervals = []
    intervals.append(list_of_tuples[0])
    #start merging the intervals
    i=0
    for n1,n2 in list_of_tuples[1:]:
        #Condition 1: Interval i+1 is a subset of interval i so we delete interval i+1
        if intervals[i][1] > n2:
            del(list_of_tuples[i + 1])
        # Condition 2: Interval i+1 overlaps with interval i so we combine them
        elif intervals[i][1] >= n1:
            intervals[i][1] = n2
            del(list_of_tuples[i+1])
        # Condition 3: There is no overlap between the two intervals so we add it to our output
        else:
            i += 1
            intervals.append(list_of_tuples[i])
    #change list pairs back to to tuples
    final_intervals = []
    for i in range(len(intervals)):
        temp = tuple(intervals[i])
        final_intervals.append(temp)
    return final_intervals

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size(tuples_list):
    #convert tuple_list into a list of lists
    list_of_pairs = []
    for i in range(len(tuples_list)):
        list_of_pairs.append(list(tuples_list[i]))

    #create a list of differences from each pair from smallest to largest
    list_differences = []
    for i in range(len(list_of_pairs)):
        difference = list_of_pairs[i][1]-list_of_pairs[i][0]
        list_differences.append(difference)
    list_differences.sort()

    #check to see if a pair matches each difference from list_differences starting from the smallest number
    #if a pair matches, insert that pair into a seperate list
    sorted_list = []
    i=0
    #iterate through the list with the interval differences stored
    while i < len(list_differences):
        difference = list_differences[i]
        k=0
        # iterate through the list of pairs to see when it equals the difference taken from list_differences
        while (k<len(list_of_pairs)):
            difference = list_of_pairs[k][1] - list_of_pairs[k][0]
            if difference == list_differences[i]:
                temp = list_of_pairs[k]
                del(list_of_pairs[k])
                sorted_list.append(temp)
                k-=1
            k+=1
        i+=1

    #change the list of lists to a list of tuples
    final_pairs = []
    for i in range(len(sorted_list)):
        temp = tuple(sorted_list[i])
        final_pairs.append(temp)
    return final_pairs

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2),(2,3),(0,5)]) == [(0,5)]
  assert sort_by_interval_size([(0,5), (1,10), (3,5), (4,6)]) == [(3, 5), (4, 6), (0, 5), (1, 10)]
  return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples

    tuple_list = []
    num = int(sys.stdin.readline())
    for i in range (num):
        b = sys.stdin.readline()
        n1, n2 = (int(s) for s in b.split())
        temp_tuple = (n1,n2)
        tuple_list.append(temp_tuple)
    # merge the list of tuples
    new_list = merge_tuples(tuple_list)
    print(new_list)
    #sort the list of tuples according to the size of the interval
    new_list = sort_by_interval_size(new_list)
    print(new_list)
    #run your test cases
    #print(test_cases())


  # open file intervals.out and write the output list of tuples
  # from the two functions
if __name__ == "__main__":
    main()

