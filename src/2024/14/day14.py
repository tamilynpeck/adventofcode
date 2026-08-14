class Day14:
    def __init__(self, data):
        self.data = [x.split(" ") for x in data]
        self.data = [
            (
                (int(x[0].split(",")[0].split("=")[1]), int(x[0].split(",")[1])),
                (int(x[1].split(",")[0].split("=")[1]), int(x[1].split(",")[1])),
            )
            for x in self.data
        ]
        self.robots = [Robot(x[0], x[1]) for x in self.data]
        # print(self.robots)

    def print_robots(self, max_x, max_y):
        grid = [["." for _ in range(0, max_x)] for _ in range(0, max_y)]

        for robot in self.robots:
            grid[robot.position[1]][robot.position[0]] = "#"

        for i, row in enumerate(grid):
            print(i, "".join(row))

    def solve_part_one(self, max_x=101, max_y=103):
        seconds = 100
        mid_x = max_x // 2
        mid_y = max_y // 2

        for _ in range(0, seconds):
            for robot in self.robots:
                robot.teleport(max_x, max_y)

        quadrant_1 = [
            x for x in self.robots if x.position[0] < mid_x and x.position[1] < mid_y
        ]
        quadrant_2 = [
            x for x in self.robots if x.position[0] > mid_x and x.position[1] < mid_y
        ]
        quadrant_3 = [
            x for x in self.robots if x.position[0] < mid_x and x.position[1] > mid_y
        ]
        quadrant_4 = [
            x for x in self.robots if x.position[0] > mid_x and x.position[1] > mid_y
        ]

        return len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4)

    def solve_part_two(self, max_x=101, max_y=103):
        seconds = 18176
        # 7774

        for i in range(1, seconds):
            for robot in self.robots:
                robot.teleport(max_x, max_y)
                if self.check_for_christmas_tree(max_x, max_y):
                    self.print_robots(max_x, max_y)
                    return i

        print("No christmas tree found")
        self.print_robots(max_x, max_y)

    def check_for_christmas_tree(self, max_x, max_y):
        grid = [["." for _ in range(0, max_x)] for _ in range(0, max_y)]
        for robot in self.robots:
            grid[robot.position[1]][robot.position[0]] = "#"

        value_check = "###############################"
        found_count = 0
        for i, row in enumerate(grid):
            # if i < 30 or i > 90:
            #     continue
            temp = "".join(row)
            if value_check in temp:
                found_count += 1
            if found_count == 2:
                return True


class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def teleport(self, max_x, max_y):
        x = self.position[0] + self.velocity[0]
        y = self.position[1] + self.velocity[1]

        if x >= max_x:
            x = x - max_x
        elif x < 0:
            x = max_x + x

        if y >= max_y:
            y = y - max_y
        elif y < 0:
            y = max_y + y

        self.position = (x, y)
        return self.position

    def __repr__(self):
        return f"Robot({self.position}, {self.velocity})"
