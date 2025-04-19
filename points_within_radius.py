import math
# algorithm for finding the given points that are within the given radius
def points_within_radius(points, radius):    
    return [v for v in points if math.hypot(v[0], v[1]) <= abs(radius)]

    