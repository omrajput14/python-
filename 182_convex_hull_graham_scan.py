from functools import cmp_to_key

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p0 = Point(0, 0)

def next_to_top(S):
    p = S.pop()
    res = S[-1]
    S.append(p)
    return res

def dist_sq(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def orientation(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) - 
           (q.x - p.x) * (r.y - q.y))
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclock wise

def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        if dist_sq(p0, p2) >= dist_sq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1

def convex_hull(points, n):
    ymin = points[0].y
    min_idx = 0
    for i in range(1, n):
        y = points[i].y
        if y < ymin or (ymin == y and points[i].x < points[min_idx].x):
            ymin = points[i].y
            min_idx = i

    points[0], points[min_idx] = points[min_idx], points[0]
    global p0
    p0 = points[0]
    
    sorted_points = [points[0]] + sorted(points[1:], key=cmp_to_key(compare))
    
    m = 1
    for i in range(1, n):
        while i < n - 1 and orientation(p0, sorted_points[i], sorted_points[i + 1]) == 0:
            i += 1
        sorted_points[m] = sorted_points[i]
        m += 1
        
    if m < 3:
        return
        
    S = []
    S.append(sorted_points[0])
    S.append(sorted_points[1])
    S.append(sorted_points[2])
    
    for i in range(3, m):
        while len(S) > 1 and orientation(next_to_top(S), S[-1], sorted_points[i]) != 2:
            S.pop()
        S.append(sorted_points[i])
        
    while S:
        p = S.pop()
        print(f"({p.x}, {p.y})")

if __name__ == '__main__':
    points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
              Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
    print("Convex Hull Points:")
    convex_hull(points, len(points))
