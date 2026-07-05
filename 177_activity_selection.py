def print_max_activities(s, f):
    n = len(f)
    print("Following activities are selected:")
    
    i = 0
    print(f"Activity {i} (Start: {s[i]}, End: {f[i]})")
    
    for j in range(1, n):
        if s[j] >= f[i]:
            print(f"Activity {j} (Start: {s[j]}, End: {f[j]})")
            i = j

if __name__ == '__main__':
    # Assuming activities are already sorted according to their finish time
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print_max_activities(s, f)
