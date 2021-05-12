import unittest
from Object import Object
from utilities import Timer, get_distance
import time

class UtilitiesTests(unittest.TestCase):

    def test_collision(self):
        obj_a = Object.create_static_object(0, 0, 10)
        obj_b = Object.create_static_object(0, 15, 6)
        self.assertTrue(obj_a.check_radius_collision(obj_b))
   
    def test_no_collision(self):
        obj_a = Object.create_static_object(0, 0, 10)
        obj_b = Object.create_static_object(0, 15, 4)
        self.assertFalse(obj_a.check_radius_collision(obj_b))

    def test_distance(self):
        point_a = (0,0)
        point_b = (4,3)
        distance = get_distance(point_a, point_b)
        self.assertEqual(distance, 5, "Distance should be 5")

    def test_timer(self):
        timer = Timer(0.05)
        self.assertFalse(timer.update())
        time.sleep(0.05)
        self.assertTrue(timer.update())

if __name__ == "__main__":
    unittest.main()