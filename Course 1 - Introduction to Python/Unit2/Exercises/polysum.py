import math
def polysum(n,s):
    def areaOfPolygon(n,s):
        area = (0.25 * n * s ** 2)/math.tan(math.pi/n)
        return area
    def perimeterOfPolygon(n,s):
        perimeter = n * s
        return perimeter
    sum = areaOfPolygo(n,s) + (perimeterOfPolygon(n,s) ** 2)
    return round(sum,4)
