import hashlib
import pprint


class Swharmap:

    def __init__(self, collection, flatten=False):
        self.items = {}
        self.map = {}

        if not flatten:
            for item in collection:
                item_id = self.generate_id()
                self.items[item_id] = item
                self.recursively_build_map(item_id, self.items[item_id], self.map)
        else:
            # TODO: Flatten map builder
            pass

    def recursively_build_map(self, item_id, item, item_map):
        """
        Builds the item map recursively
        :param item: Input Object
        :param item_id: Input Object ID
        :param item_map: Recursive Tree
        """
        for key, value in item.items():
            if key not in item_map:
                item_map[key] = {}
            if isinstance(value, dict):
                self.recursively_build_map(item_id, value, item_map[key])
            else:
                item_map[key][value] = self.items[item_id]

    # TODO: Flatten builder method
    def recursively_build_map_flat(self, item_id, item, item_map):
        pass

    def generate_id(self):
        length = sum(len(t) for t in self.items.items())
        return hashlib.md5(str(length).encode()).hexdigest()

    def print_map(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.map)
