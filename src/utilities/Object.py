import utilities
import math


class Object:

    def __init__(self, start_x, start_y, radius, velocity):
        self.x = start_x
        self.y = start_y
        self.radius = radius
        self.direction_angle = 0
        self.velocity = velocity

    def check_radius_collision(self, target_object, scan_radius=False):
        target_loc = (target_object.x, target_object.y)
        distance = utilities.get_distance((self.x, self.y), target_loc)
        radius = self.radius if not scan_radius else scan_radius
        total_radius = radius + target_object.radius
        if distance <= total_radius:
            return True
        return False

    def check_cone_collision(self, target_object, scan_radius, scan_angle):
        if not self.check_radius_collision(target_object, scan_radius):
            return False
        target_coord = (target_object.x, target_object.y)
        collision_angle = utilities.get_angle((self.x, self.y), target_coord)
        min_collision_angle = self.direction_angle - scan_angle / 2.0
        max_collision_angle = self.direction_angle + scan_angle / 2.0
        above_min = collision_angle >= min_collision_angle
        below_max = collision_angle <= max_collision_angle
        if above_min and below_max:
            return True
        return False

    def inverse_velocity_edge_collision(self, hit_x_limit):
        vel_x = math.cos(self.direction_angle) * self.velocity
        vel_y = math.sin(self.direction_angle) * self.velocity
        if hit_x_limit:
            vel_x = -1 * vel_x
        else:
            vel_y = -1 * vel_y
        new_angle = utilities.get_angle((0, 0), (vel_x, vel_y))
        self.direction_angle = new_angle

    def handle_edge_collision(self, min_x, max_x, min_y, max_y):
        if self.x - self.radius <= min_x:
            self.x = min_x + self.radius + 1
            self.inverse_velocity_edge_collision(True)
        elif self.x + self.radius >= max_x:
            self.x = max_x - self.radius - 1
            self.inverse_velocity_edge_collision(True)
        if self.y - self.radius <= min_y:
            self.y = min_y + self.radius + 1
            self.inverse_velocity_edge_collision(False)
        elif self.y + self.radius >= max_y:
            self.y = max_y - self.radius + 1
            self.inverse_velocity_edge_collision(False)

    def update_position(self, time_since_last_update):
        vel_x = self.velocity * math.cos(self.direction_angle)
        vel_y = self.velocity * math.sin(self.direction_angle)
        self.x += vel_x * time_since_last_update
        self.y += vel_y * time_since_last_update
