### BDA Seminar 1 - Part 1 & 2

# Complete the following exercises on computational complexity.**

# 1. Study the following script. This program implements a `linear_search(arr, x)` function 
# that returns element `x`'s index in the list `arr`. If `x` is not found, it returns `-1`.

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 2. Now, let's put your understanding to the test. Can you determine the time complexity 
# of the following script? Take a moment to think about it.

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  result = linear_search(data,40)
  print(result)


# 5. What is the time complexity of the following code?

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(data[-1])

# 6. What is the time complexity of the following code?

def get_it(arr):
    for i in arr:
      return i

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(get_it(data))

# 7. What is the time complexity of the following code?

def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(sum_elements(data))

# 8. Is this a computationally or data-intensive task?

# 9. What is the time complexity of the following code?

def count_lines(filename):
  count=0
  with open(filename, 'r') as file:
    for line in file:
      count+=1
            
  return count

if __name__ == "__main__":
  filename = 'file1.txt'
  try:
      counts = count_lines(filename)
      print("Line counts:", counts)
  except FileNotFoundError:
      print("File not found")


# 12. Compare the following scripts; which one do you prefer and why?

def reverse1(data):
  reverse=[]
  for i in range(len(data) - 1, -1, -1):
    reverse.append(data[i])
  return reverse

def reverse2(data):
    left, right = 0, len(data) - 1
    while left < right:
        # Swap the elements at the left and right indices
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return data

if __name__ == "__main__":
  print(reverse1([1,2,3,4,5]))
  print(reverse2([1,2,3,4,5]))
'''I prefer reverse2 because it is more efficient. 
It performs the reversal in place with a time complexity of O(n) 
and a space complexity of O(1), whereas reverse1 has a space complexity of O(n) 
due to creating a new list.'''

# 12. What is the time complexity of the following code?

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
  data = [64, 34, 25, 12, 22, 11, 90]
  print(bubble_sort(data))

# 13. What is the space complexity of the above script?

# 14. Examine the next code.

def bubble_sort_count1(arr):
  n = len(arr)
  count_n=0
  for i in range(n):
      for j in range(0, n-1):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
          count_n+=1
  return count_n

if __name__ == "__main__":
  data = [10, 9, 88, 7, 62, 5, 43]
  print(bubble_sort_count1(data))

# 15. What is the purpose of this script?

# 16. What is the time complexity of this script?

# 17. Analyse the Provided Code.
def bubble_sort_count2(arr):
  n = len(arr)
  count_n=0
  for i in range(n):
      for j in range(0, n-1):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
              count_n+=1
  return count_n

if __name__ == "__main__":
  data = [10, 9, 88, 7, 62, 5, 43]
  print(bubble_sort_count2(data))
  
# 19. Why does it output 12?


# 20. What is the purpose of the script?

# Examine the code.

def bubble_sort_count3(arr):
  n = len(arr)
  count_n=0
  for i in range(n):
      for j in range(0, n-1-i):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
          count_n+=1
  return count_n

if __name__ == "__main__":
  data = [10, 9, 88, 7, 62, 5, 43]
  print(bubble_sort_count3(data))

# 21. Why does it output 21?


# What is the time complexity of this script?
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2 # // means integer division (5//2)=2 :)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
  data = [10, 19, 28, 32, 45, 55, 66]
  target = 28
  print(binary_search(data, target))

# 23. The following script generates all the possible permutations of a given list. 
# Without running the script, can you define the time complexity of this script?

from itertools import permutations

def all_permutations(elements):
    return list(permutations(elements))

if __name__ == "__main__":
  elements = [1, 2, 3]
  print(all_permutations(elements))
  
# The script outputs:
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 24. What is the length of the output list if the input list has 5 numbers?

# 25. What is the computational complexity of the following script?
# The script uses the `bubble_sort` and the `binary_search` functions.

if __name__ == "__main__":
  data = [10,2,4,6,22,3,55,12]
  print(binary_search(bubble_sort(data), 10))


### BDA Seminar 1 - Part 2

# Complete the following exercises on creating small programs.**

# 1. Examine the following code. The script calculates the time needed to run the `all_permutations` function.

import time
from itertools import permutations

def all_permutations(elements):
    return list(permutations(elements))

if __name__ == "__main__":
  elements=[1,2,3,4,5,6,7,8,9,10,11]  
  # Start the timer
  start = time.time()
  result = all_permutations(elements)
  # End the timer
  end = time.time()
  
  print(f'Total time to run (seconds):',round(end-start,4))

# 2. Let's begin by downloading our initial large file, the Common Password List (`rockyou.txt`). Download the file from [Common Passwords List in Kaggle](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt). 
  
# 3. Examine the following script. The script extracts each line of our file using the `strip` that removes any leading or trailing whitespace.

if __name__ == "__main__":
  with open('rockyou.txt', 'r',encoding='ISO-8859-1') as file:
    for line in file:
      # Strip newline and whitespace from the line
      current_password = line.strip()
      print(current_password)
      break



# ISO 8859-1` is the ISO standard Latin-1 character set and encoding format.

# 4. How many passwords are in the file?

def count_pass(file_path):
  count = 0
  try: 
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            count += 1
    return count
  except FileNotFoundError:
    print ("File not found")
    return None
  

## Use the following main
if __name__ == "__main__":
  print(count_pass('rockyou.txt'))

#  There are 14344391 passwords; make sure your result is correct.

# When working with files, use the `except FileNotFoundError` .

# 5. What is the computational complexity of the above script?

# 6. Create a `search_password` function to search for a password in a given file.

import os

def search_password(file_path, target_password):
  try:
      with open(file_path, 'r', encoding='ISO 8859-1') as file:
         for line in file:
            if line.strip() == target_password:
              return line.strip()
  except FileNotFoundError:
    print('File not found')
    return None

if __name__ == "__main__":
    file_path = input("Enter the path to the password file: ")
    target_password = input("Enter the password to search for: ")
    found = search_password(file_path, target_password)
    if found:
        print("Password found.")
    else:
        print("Password not found.")


# 7. Calculate the time to find:

# * 1234
# * 1233242432
# * mary

# 8. Does your input affect the time complexity?

# | Provide your answer here. |
# | ------------------------- |
# |                           |

# **:mount_fuji: The following tasks are challenging.**

# 9. Create a script to find out if there are any duplicated records in the rockyou.txt file.

# Store your results in a list.
# For this script, you have to use a nested loop.

# :clock1: Try only using the first 25 records. Otherwise, this script might run for hours!
# Then, run it for the whole dataset. Is it ever finished?

def check_duplicates1(file_path):
    try:
        seen = set()
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                password = line.strip()
                if password in seen:
                    return f"Duplicate found: {password}"
                seen.add(password)
        return "No duplicates found"
    except FileNotFoundError:
        print('File not found')
        return None
    
if __name__ == "__main__":
    file_path = "rockyou.txt"
    check_duplicates1(file_path)

# 10. What is the space complexity?

# 11. Create a script to find the duplicated records in the `rockyou.tx`t file.
'''
- Use a set instead of a list to store your data.
- Print a set of the duplicated values at the end.
'''

def check_duplicates2(file_path):
    # Provide your solution here
    pass

if __name__ == "__main__":
    file_path = "rockyou.txt"
    check_duplicates2(file_path)


# 12. What is this script's time and space complexity if you don't use a set? What is when using sets?



