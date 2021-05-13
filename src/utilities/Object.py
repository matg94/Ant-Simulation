import utilities
import math

class Object:

    def __init__(self, start_x, start_y, radius, velocity, is_static):
        self.x = start_x
        self.y = start_y
        self.radius = radius
        self.direction_angle = 0
        self.static = is_static
        if not is_static:
            self.velocity = velocity

    @classmethod
    def create_static_object(cls, start_x, start_y, radius):
        return cls(start_x, start_y, radius, 0, True)

    @classmethod
    def create_dynamic_object(cls, start_x, start_y, radius, velocity):
        return cls(start_x, start_y, radius, velocity, False)

    def check_radius_collision(self, target_object, scan_radius=False):
        distance = utilities.get_distance((self.x, self.y), (target_object.x, target_object.y))
        total_radius = (self.radius if not scan_radius else scan_radius) + target_object.radius
        if distance <= total_radius:
            return True
        return False

    def check_cone_collision(self, target_object, scan_radius, scan_angle):
        if not self.check_radius_collision(target_object, scan_radius):
            return False
        collision_angle = utilities.get_angle((self.x, self.y),(target_object.x, target_object.y))
        min_collision_angle = self.direction_angle - scan_angle / 2.0
        max_collision_angle = self.direction_angle + scan_angle / 2.0
        if collision_angle >= min_collision_angle and collision_angle <= max_collision_angle:
            return True
        return False

    def update_position(self, time_since_last_update):
        if self.static:
            return
        vel_x = self.velocity * math.cos(self.direction_angle)
        vel_y = self.velocity * math.sin(self.direction_angle)
        self.x += vel_x * time_since_last_update
        self.y += vel_y * time_since_last_update
