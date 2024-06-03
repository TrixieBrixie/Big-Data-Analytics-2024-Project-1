# Count the total number of comparisons made during the sorting process
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

# Count the total number of swaps made during the sorting process
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