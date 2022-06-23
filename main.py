class FlatIterator:
    def __init__(self, my_list):
        self.my_list = sum(my_list, [])

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.my_list):
            raise StopIteration
        return self.my_list[self.cursor]


def flat_generator(my_list):
    for lists in my_list:
        for item in lists:
            yield item


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('Итератор')
    for item in FlatIterator(nested_list):
        print(item)
    print('\n----------\n')
    print('Комперхеншн')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('\n----------\n')
    print('Генератор')
    for item in flat_generator(nested_list):
        print(item)
