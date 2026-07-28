
def max_sum(nums_list:list, k:int) -> int:

    if k <= 0:
        return 0
    
    dict_nums = {}
    curr_sum = 0
    max_sum = 0

    for i in range(k):
        ind = nums_list[i]
        curr_sum = curr_sum + ind
        if ind in dict_nums:
            dict_nums[ind] += 1
        else:
            dict_nums[ind] = 1

    if len(dict_nums) == k:
        max_sum = curr_sum


    for i in range(len(nums_list)-k):

        tail_val = nums_list[i]
        head_val = nums_list[k+i]
        curr_sum = curr_sum - tail_val + head_val

        dict_nums[tail_val] -= 1
        if dict_nums[tail_val] == 0:
            del dict_nums[tail_val]
        
        if head_val in dict_nums:
            dict_nums[head_val] += 1
        else:
            dict_nums[head_val] = 1

        if len(dict_nums) == k: 
            max_sum = max(curr_sum, max_sum)
        else:
            continue
    
    return max_sum



if __name__ == "__main__":
    nums = [3, 2, 2, 3, 4, 6, 7, 7, -1]
    k = 4
    result = max_sum(nums,k)
    print(result)