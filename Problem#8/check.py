"""
Name: Logan Roman
Lab time: 2:00 Thurs
"""

def in_order(nums):
    # Type your code here.
    catch_sort = True
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            catch_sort = False
    return catch_sort

    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
