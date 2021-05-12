import utilities

class Object:

    def __init__(self, start_x, start_y, radius, velocity, is_static):
        self.x = start_x
        self.y = start_y
        self.radius = radius
        if not is_static:
            self.vel_x = 0
            self.vel_y = 0
            self.velocity = velocity

    @classmethod
    def create_static_object(cls, start_x, start_y, radius):
        return cls(start_x, start_y, radius, 0, True)

    @classmethod
    def create_dynamic_object(cls, start_x, start_y, radius, velocity):
        return cls(start_x, start_y, radius, velocity, False)

    def check_radius_collision(self, target_object):
        distance = utilities.get_distance((self.x, self.y), (target_object.x, target_object.y))
        total_radius = self.radius + target_object.radius
        if distance <= total_radius:
            return True
        return False

if __name__ == "__main__":
    obj_a = Object.create_static_object(0, 0, 10)
    obj_b = Object.create_static_object(0, 15, 6)
    print("COLLISION TEST PASSED:", obj_a.check_radius_collision(obj_b))
    obj_b = Object.create_static_object(0, 15, 4)
    print("NO COLLISION TEST PASSED:", not obj_a.check_radius_collision(obj_b))