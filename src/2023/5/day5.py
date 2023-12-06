from functools import reduce


class Almanac:
    def __init__(self, data):
        self.data = data
        self.parse_data()

        self.get_location = lambda id: reduce(self.seed_to_location, self.maps, id)
        self.get_seed = lambda id: reduce(
            self.location_to_seed, reversed(self.maps), id
        )

    def get_closest_location(self):
        locations = [self.get_location(int(seed_id)) for seed_id in self.seed_ids]
        return min(locations)

    def get_closest_location_by_seed_pair(self):
        found_seed = False
        location = 0
        while not found_seed:
            seed_id = self.get_seed(location)
            if self.is_valid_seed(seed_id):
                return location
            location += 1

    def is_valid_seed(self, seed_id):
        for start, len in self.seed_pairs:
            if seed_id in range(start, start + len):
                return True
        return False

    def seed_to_location(self, val, map):
        for range_dest, range_start, range_len in map:
            if val in range(range_start, range_start + range_len):
                return range_dest + (val - range_start)
        return val

    def location_to_seed(self, val, map):
        for range_dest, range_start, range_len in map:
            if val in range(range_dest, range_dest + range_len):
                return range_start + (val - range_dest)
        return val

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

        self.maps = [
            self.parse_map(map_1, map_2),
            self.parse_map(map_2, map_3),
            self.parse_map(map_3, map_4),
            self.parse_map(map_4, map_5),
            self.parse_map(map_5, map_6),
            self.parse_map(map_6, map_7),
            self.parse_map(map_7, len(self.data) + 1),
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
