

def removeElement(nums):
    cpt = 0
    size = len(nums)
    memo = {}

    for x in nums:
        if x in memo:
            memo[x] += 1
        else:
            memo[x] = 1

    while cpt < size :
        if memo[nums[cpt]] > 1 :
            del nums[cpt]
            size -= 1
            continue
        cpt += 1

    return len(nums)