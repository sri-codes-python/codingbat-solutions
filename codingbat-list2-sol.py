#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0

def count_evens(nums):
  even_cnt=0
  if sum(nums)==0 or sum(nums)==1:
    return 0
  for num in nums:
    if num%2==0:
      even_cnt+=1
  return even_cnt

#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
  array_sum=0
  i=0
  if len(nums)==0:
    return array_sum
  
  while i <= len(nums)-1:
    if nums[i]==13:
      i=i+2
    else:
      array_sum+=nums[i]
      i+=1
  
  return array_sum



#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

#big_diff([10, 3, 5, 6]) → 7
#big_diff([7, 2, 10, 9]) → 8
#big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
  #edge cases
  if len(nums)==1:
    return 0
  if len(nums)==2:
    return abs(nums[0]-nums[1])
  min_val=min(nums[0],nums[1])
  max_val=max(nums[0],nums[1])
  ## actual solution
  for i in range(2,len(nums)):
    min_val=min(min_val,nums[i])
    max_val=max(max_val,nums[i])
  return abs(max_val-min_val)



#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

#sum67([1, 2, 2]) → 5
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5
#sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
  state=0
  sum=0
  for num in nums:
    if state == 0:
      if num == 6:
        state=1
      else:
        sum+=num
    else:
      if num == 7:
        state=0
  return sum

