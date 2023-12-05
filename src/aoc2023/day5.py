class Almanac:
    def __init__(self, data):
        self.data = data
        self.parse_data()

    def go_through_maps(self, seed_id):
        new_id = seed_id
        for map in self.maps:
            print(new_id)
            new_id = self.get_value_from_map(map, new_id)
        return new_id

    def reverse_go_through_maps(self, location_id):
        new_id = location_id
        for map in reversed(self.maps):
            new_id = self.get_value_from_map_backwards(map, new_id)

        return new_id

    def get_closest_location(self):
        locations = [self.go_through_maps(int(seed_id)) for seed_id in self.seed_ids]
        print(locations)
        return min(locations)

    def get_closest_location_by_seed_pair(self):
        return self.get_location_backwards()

    def is_valid_seed(self, seed_id):
        for start, len in self.seed_pairs:
            if seed_id in range(start, start + len):
                return True
        return False

    def get_location_backwards(self):
        found_seed = False
        location = 0
        while not found_seed:
            seed_id = self.reverse_go_through_maps(location)
            if self.is_valid_seed(seed_id):
                return location
            location += 1

    def get_value_from_map(self, map, x=0):
        for range_dest, range_start, range_len in map:
            if x in range(range_start, range_start + range_len):
                return range_dest + (x - range_start)
        return x

    def get_value_from_map_backwards(self, map, x=0):
        for range_dest, range_start, range_len in map:
            if x in range(range_dest, range_dest + range_len):
                return range_start + (x - range_dest)
        return x

    def parse_data(self):
        seeds = self.data[0].replace("seeds:", "").strip().split(" ")
        self.seed_ids = [int(x) for x in seeds]
        self.seed_pairs = self.get_pairs(seeds)

        map_1 = self.data.index("seed-to-soil map:")
        map_2 = self.data.index("soil-to-fertilizer map:")
        map_3 = self.data.index("fertilizer-to-water map:")
        map_4 = self.data.index("water-to-light map:")
        map_5 = self.data.index("light-to-temperature map:")
        map_6 = self.data.index("temperature-to-humidity map:")
        map_7 = self.data.index("humidity-to-location map:")

        self.seed_to_soil_map = self.parse_map(map_1, map_2)
        self.soil_to_fertilizer_map = self.parse_map(map_2, map_3)
        self.fertilizer_to_water_map = self.parse_map(map_3, map_4)
        self.water_to_light_map = self.parse_map(map_4, map_5)
        self.light_to_temperature_map = self.parse_map(map_5, map_6)
        self.temperature_to_humidity_map = self.parse_map(map_6, map_7)
        self.humidity_to_location_map = self.parse_map(map_7, len(self.data) + 1)

        self.maps = [
            self.seed_to_soil_map,
            self.soil_to_fertilizer_map,
            self.fertilizer_to_water_map,
            self.water_to_light_map,
            self.light_to_temperature_map,
            self.temperature_to_humidity_map,
            self.humidity_to_location_map,
        ]

    def parse_map(self, start_i, end_i):
        return [
            [int(value) for value in line.strip().split(" ")]
            for line in self.data[start_i + 1 : end_i - 1]
        ]

    def get_pairs(self, seeds):
        seeds = [int(x) for x in seeds]
        seed_pairs = []
        it = iter(seeds)
        for x in it:
            seed_pairs.append((x, next(it)))

        return seed_pairs


class Seed:
    def __init__(self, seed_id):
        self.seed_id = int(seed_id)
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temperature = None
        self.humidity = None
        self.location = None

    def __repr__(self):
        return f"Seed({self.seed_id})"
