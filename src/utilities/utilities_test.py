import unittest
from Object import Object
from utilities import Timer, get_distance, get_angle
import time
import math


class UtilitiesTests(unittest.TestCase):

    def test_collision(self):
        obj_a = Object(0, 0, 10, 0)
        obj_b = Object(0, 15, 6, 0)
        self.assertTrue(obj_a.check_radius_collision(obj_b))

    def test_no_collision(self):
        obj_a = Object(0, 0, 10, 0)
        obj_b = Object(0, 15, 4, 0)
        self.assertFalse(obj_a.check_radius_collision(obj_b))

    def test_distance(self):
        point_a = (0, 0)
        point_b = (4, 3)
        distance = get_distance(point_a, point_b)
        self.assertEqual(distance, 5, "Distance should be 5")

    def test_cone_collision_angle_edge(self):
        obj_a = Object(0, 0, 1, 0)
        obj_b = Object(2, 2, 1, 0)
        collision = obj_a.check_cone_collision(obj_b, 2, math.pi / 2)
        self.assertTrue(collision)

    def test_cone_collision_angle_edge_with_direction(self):
        obj_a = Object(0, 0, 1, 0)
        obj_a.direction_angle = (3/4) * math.pi
        obj_b = Object(-2, 2, 1, 0)
        collision = obj_a.check_cone_collision(obj_b, 2, math.pi / 12)
        self.assertTrue(collision)

    def test_angle_positive(self):
        point_a = (0, 0)
        point_b = (1, 1)
        angle = get_angle(point_a, point_b)
        self.assertEqual(angle, math.pi / 4)

    def test_angle_negative(self):
        point_a = (0, 0)
        point_b = (-1, 1)
        angle = get_angle(point_a, point_b)
        self.assertEqual(angle, (3/4)*math.pi)

    def test_position_change(self):
        obj_a = Object(0, 0, 1, 1)
        obj_a.update_position(1)
        self.assertEqual(obj_a.x, 1, "x position should be 1")
        self.assertEqual(obj_a.y, 0, "y position should be 0")

    def test_handle_edge_collision(self):
        obj = Object(8, 5, 1, 1)
        obj.handle_edge_collision(0, 11, 0, 10)
        self.assertEqual(obj.x, 8, "x position should be 8")

        obj.update_position(2)
        obj.handle_edge_collision(0, 11, 0, 10)
        self.assertEqual(obj.x, 9, "x position should be 9")

    def test_angle_change_from_edge_collision(self):
        obj = Object(9, 4, 1, 1)
        obj.handle_edge_collision(0, 8, 0, 8)
        error = "New angle should equal Pi"
        new_angle = round(obj.direction_angle, 2)
        self.assertEqual(new_angle, round(math.pi, 2), error)
        # Check y - collision
        obj_b = Object(4, 9, 1, 1)
        obj_b.direction_angle = (5/4 * math.pi)
        obj_b.handle_edge_collision(0, 8, 0, 8)
        objb_angle = round(obj_b.direction_angle, 2)
        expected_angle = round((3/4)*math.pi, 2)
        error = "New angle should equal (3pi/4)"
        self.assertEqual(objb_angle, expected_angle, error)

    def test_timer(self):
        timer = Timer(0.05)
        self.assertFalse(timer.update())
        time.sleep(0.05)
        self.assertTrue(timer.update())


if __name__ == "__main__":
    unittest.main()
