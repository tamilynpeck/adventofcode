class GearRatios:
    def __init__(self, data):
        self.data = data

    def get_gear_part_total(self):
        parts_found = []
        for r, row in enumerate(self.data):
            part_number = ""
            symbol_found = False
            for c, char in enumerate(row):
                if char.isdigit():
                    part_number += char
                    symbol_found = (
                        self.search_for_symbol(r, c)
                        if not symbol_found
                        else symbol_found
                    )
                    print(">>", char, symbol_found)
                elif not char.isdigit() and part_number and symbol_found:
                    print(f">> found part: {part_number}")
                    parts_found.append(part_number)
                    part_number = ""
                    symbol_found = False
                elif part_number:
                    print(">> skipped part:", part_number)
                    part_number = ""
                    symbol_found = False
                else:
                    part_number = ""
                    symbol_found = False

            if part_number and symbol_found:
                print(f">> found part: {part_number}")
                parts_found.append(part_number)

        for r, row in enumerate(self.data):
            print(row)

        print(parts_found)
        return sum([int(part) for part in parts_found])

    def get_gear_ratios(self):
        parts_found = []
        for r, row in enumerate(self.data):
            for c, char in enumerate(row):
                if char != "*":
                    continue

                gear_ratio = self.search_for_gears(r, c)
                # print(">>", char, gear_ratio)
                if gear_ratio:
                    print(f">> found gear_ratio: {gear_ratio}")
                    parts_found.append(gear_ratio)

        print(parts_found)
        return sum([part for part in parts_found])

    def search_for_gears(self, r, c):
        gears = []
        up_locations = [
            [-1, -1],  # up left
            [-1, 0],  # up
            [-1, 1],  # up right
        ]

        right_locations = [
            [0, 1],  # right
        ]
        left_locations = [
            [0, -1],  # left
        ]
        down_locations = [
            [1, -1],  # down left
            [1, 0],  # down
            [1, 1],  # down right
        ]

        value = self.search_locations(r, c, up_locations)
        gears.extend(value)
        value = self.search_locations(r, c, right_locations)
        gears.extend(value)
        value = self.search_locations(r, c, left_locations)
        gears.extend(value)
        value = self.search_locations(r, c, down_locations)
        gears.extend(value)

        gears = [gear for gear in gears if gear]

        print("pos. gears", gears)
        if len(gears) == 2:
            return gears[0] * gears[1]

        return

    def search_locations(self, r, c, locations):
        first_found = False
        middle_found = False
        values = []

        for i, (x, y) in enumerate(locations):
            print(i, middle_found)
            if r + x < 0 or c + y < -1:
                continue

            if i == 2 and middle_found:
                continue

            try:
                value = self.data[r + x][c + y]
                if value.isdigit():
                    value = self.get_value_at_location(r + x, c + y)
                    if i == 1 and first_found:
                        pass
                    else:
                        values.append(value)
                    if i == 0:
                        first_found = True
                    if i == 1:
                        middle_found = True
            except IndexError:
                continue

        return values

    def get_value_at_location(self, r, c):
        found_value = ""
        starting_index = c

        for _ in range(0, c):
            i = starting_index - 1
            if i < 0:
                break

            value = self.data[r][i]

            if value.isdigit():
                starting_index = i
            else:
                break

        for i in range(starting_index, len(self.data[r])):
            if i > len(self.data[r]):
                break
            value = self.data[r][i]

            if value.isdigit():
                found_value += value
            else:
                break
        print("found_value", found_value)
        return int(found_value) if found_value.isdigit() else None

    def search_for_symbol(self, r, c):
        locations = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]

        for x, y in locations:
            # print("location change", x, y, ":", r + x, c + y)
            if r + x < 0 or c + y < -1:
                continue
            try:
                value = self.data[r + x][c + y]
                if value != "." and not value.isdigit():
                    print("found symbol", value, "at", r + x, c + y)
                    return True
            except IndexError:
                # print("index error", r + x, c + y)
                continue

        return False
