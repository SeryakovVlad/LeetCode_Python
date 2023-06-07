class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates[2:]:
            delta_x1 = x1 - x0
            delta_y1 = y1 - y0
            delta_x2 = x - x0
            delta_y2 = y - y0
            if delta_x1 * delta_y2 != delta_x2 * delta_y1:
                return False
            x1, y1 = x, y
        return True