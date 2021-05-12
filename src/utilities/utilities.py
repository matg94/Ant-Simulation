import time
import math

def get_distance(point_a, point_b):
    dist_x = point_b[0] - point_a[0]
    dist_y = point_b[1] - point_a[1]
    return math.sqrt((dist_x**2) + (dist_y**2))

class Timer:

    def __init__(self, interval):
        self.interval = interval
        self.time_remaining = interval
        self.current_time = time.time()

    def update(self):
        self.time_since_last_update = time.time() - self.current_time
        self.time_remaining -= self.time_since_last_update
        if self.time_remaining <= 0:
            self.time_remaining = self.interval
            return True
        self.current_time = time.time()
        return False

if __name__ == "__main__":
    timer = Timer(1)
    first = timer.update()
    time.sleep(1)
    second = timer.update()
    print("TIMER TEST PASSED: ", (first == False and second == True))
    test_a = (0, 0)
    test_b = (4, 3)
    print("DISTANCE TEST PASSED:", get_distance(test_a, test_b) == 5)
