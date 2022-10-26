def count_stones(jewels, stones):
    count_collection = 0
    for element in jewels:
        for item in stones:
            if element == item:
                count_collection += 1
    return count_collection
print(count_stones(jewels = "aA", stones = "aAAbbbb"))