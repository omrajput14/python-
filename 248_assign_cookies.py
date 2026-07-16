# 248. Assign Cookies (Greedy)
# Assume you are an awesome parent and want to give your children some cookies.
# Each child has a greed factor, and each cookie has a size.
# A child is content if cookie size >= greed factor.
# Maximize the number of content children.

def find_content_children(g, s):
    """
    Greedy approach: Sort both arrays and assign smallest sufficient cookie.
    g: list of greed factors
    s: list of cookie sizes
    Returns the maximum number of content children.
    """
    g.sort()
    s.sort()
    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1

    return child


# Example usage
if __name__ == "__main__":
    greed = [1, 2, 3]
    sizes = [1, 1]
    print(f"Greed factors: {greed}")
    print(f"Cookie sizes: {sizes}")
    print(f"Content children: {find_content_children(greed, sizes)}")
    # Output: 1

    greed2 = [1, 2]
    sizes2 = [1, 2, 3]
    print(f"\nGreed factors: {greed2}")
    print(f"Cookie sizes: {sizes2}")
    print(f"Content children: {find_content_children(greed2, sizes2)}")
    # Output: 2
