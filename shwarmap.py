import hashlib


class Swharmap:

    def __init__(self, collection, flatten=False):
        self.collection = {}
        self.map = {}

        if not flatten:
            for item in collection:
                new_item = collection[self.generate_id()] = item

                for key, value in collection:
                    if not isinstance(value, dict):
                        self.map[key] = self.__init__(value)
                    else:
                        self.map[key][value] = new_item
        else:
            pass

    def generate_id(self):
        length = sum(len(t) for t in self.collection.items())
        return hashlib.md5(length).digest()
