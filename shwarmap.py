import hashlib


class Swharmap:

    def __init__(self, collection, flatten=False):
        self.items = {}

        if not flatten:
            for item in collection:
                new_item = self.items[self.generate_id()] = item
                self.map = self.recursively_build_map(item, new_item, {})
        else:
            # TODO: Flatten map builder
            pass

    def recursively_build_map(self, item_hash, new_item, item_map):
        """
        Builds the item map recursively
        :param item_hash: Input object
        :param new_item: Reference to item in new collection
        :param item_map: Recursive tree
        :return:
        """

        for key, value in item_hash:
            new_map = {}

            # If it's a nested dict
            if isinstance(value, dict):
                item_map[key] = self.__init__(value)
            # If it's a leaf node
            else:
                item_map[key][value] = new_item

            return new_map

    def generate_id(self):
        length = sum(len(t) for t in self.items.items())
        return hashlib.md5(length).digest()
