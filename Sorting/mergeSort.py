def mergeSort(nums):
    if len(nums) > 1:
        m = len(nums)//2
        left_half = nums[:m]
        right_half = nums[m:]

        mergeSort(left_half)
        mergeSort(right_half)

        # merge the sorted halves
        i = j = k = 0
        while i<len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k]  = right_half[j]
                j +=1
            k += 1
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1

# Driver code to test the function
if __name__ == '__main__':
    my_list = [12, 11, 13, 5, 6, 7]
    print(f"Given array is: {my_list}")
    
    mergeSort(my_list)
    
    print(f"Sorted array is: {my_list}")
