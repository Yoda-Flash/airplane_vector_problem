class Solver:
    def __init__(self):
        pass

    def getDetails(self):
        self.engine_speed = float(input("What is the engine speed?"))
        self.engine_angle_type = input("Is it in bearing? If yes, type bearing. If no, type direction angle.")
        self.engine_angle = float(input("What is the engine's angle?"))
        self.wind_speed = float(input("What is the wind speed?"))
        self.wind_angle_type = input("Is it in bearing? If yes, type bearing. If no, type direction angle.")
        self.wind_angle = float(input("What is the wind's angle?"))

    def bearingToAngle(self):
        if self.engine_angle_type == "bearing":
            self.engine_angle -= 90
            if self.engine_angle > 360:
                self.engine_angle -= 360
            elif self.engine_angle < 0:
                self.engine_angle += 360
        print(f"Engine angle: {self.engine_angle}")
        if self.wind_angle_type == "bearing":
            self.wind_angle -= 90
            if self.wind_angle > 360:
                self.wind_angle -= 360
            elif self.wind_angle < 0:
                self.wind_angle += 360
        print(f"Wind angle: {self.wind_angle}")

    def get_component_form(self):
        from math import cos, sin, radians
        self.component_form = [self.engine_speed*cos(radians(self.engine_angle)) + self.wind_speed*cos(radians(self.wind_angle)), self.engine_speed*sin(radians(self.engine_angle)) + self.wind_speed*sin(radians(self.wind_angle))]
        self.x = self.component_form[0]
        self.y = self.component_form[1]
        print(f"X: {self.x}")
        print(f"Y: {self.y}")

    def calculate_ground_speed(self):
        from math import pow, sqrt
        ground_speed = sqrt(pow(self.x, 2) + pow(self.y, 2))
        print(f"Ground speed: {ground_speed}")

    def calculate_direction_angle(self):
        from math import atan, degrees
        self.tan_result = degrees(atan(self.y/self.x))
        if self.x > 0 and self.y > 0:
            self.direction_angle = self.tan_result
        elif self.x < 0 and self.y > 0:
            self.direction_angle = 180 - self.tan_result
        elif self.x < 0 and self.y < 0:
            self.direction_angle = 180 + self.tan_result
        elif self.x > 0 and self.y < 0:
            self.direction_angle = 360 - self.tan_result
        print(f"Direction angle: {self.direction_angle}")


def main():
    solver = Solver()
    solver.getDetails()
    solver.bearingToAngle()
    solver.get_component_form()
    solver.calculate_ground_speed()
    solver.calculate_direction_angle()

if __name__ == "__main__":
    main()