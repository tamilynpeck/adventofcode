class Day2:
    def __init__(self, data):
        # dimensions (length l, width w, and height h)
        self.data = [(int(l), int(w), int(h)) for l, w, h in (line.split("x") for line in data)]

    def solve_part_one(self):
        return sum(self.square_feet(l, w, h) for l, w, h in self.data)

    def solve_part_two(self):
        return sum(self.ribbon(l, w, h) for l, w, h in self.data)

    # 2*l*w + 2*w*h + 2*h*l
    # plus the area of the smallest side.
    def square_feet(self, l, w, h):
        return (2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, w * h, h * l)

    # smallest perimeter of any one face
    # 2*l + 2*w + 2*h - 2*max(l, w, h)
    # plus l*w*h for the bow
    def ribbon(self, l, w, h):
        return (2 * l + 2 * w + 2 * h - 2 * max(l, w, h)) + (l * w * h)
