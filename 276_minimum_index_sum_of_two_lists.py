# 276. Minimum Index Sum of Two Lists
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

def find_restaurant(list1, list2):
    map1 = {res: i for i, res in enumerate(list1)}
    min_sum = float('inf')
    res = []
    
    for i, r in enumerate(list2):
        if r in map1:
            curr_sum = i + map1[r]
            if curr_sum < min_sum:
                min_sum = curr_sum
                res = [r]
            elif curr_sum == min_sum:
                res.append(r)
                
    return res

if __name__ == "__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    print(find_restaurant(list1, list2))  # ["Shogun"]
