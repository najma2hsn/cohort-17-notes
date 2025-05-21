def get_min(nums: list[int]) -> int:

    possible_mins = []

    for num in nums:
        for num2 in nums: n^2
            if num < num2:
                possible_mins.append(num) 

    for num in possible_mins:
        larger = False 
        for num2 in nums: n ^ 2
            if num >= possible_mins: 
                larger = True
        if not larger:
            return num 
        
    O(n^2)