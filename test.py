from shwarmap import Swharmap

collection = [
    {
        'type': 'TV',
        'price': '999.99',
        'reviews': {
            'kevin': 'good',
            'george': 'terrible'
        }
    },
    {
        'type': 'TV',
        'price': '899.99',
        'reviews': {
            'kevin': 'good',
            'george': 'not terrible',
            'david': 'meh'
        }
    },
    {
        'type': 'Computer',
        'price': '1199.99',
        'reviews': {
            'kevin': 'Dreadful',
            'george': 'terrible'
        }
    },
]

foo = Swharmap(collection, flatten=False)

# foo.print_map()
