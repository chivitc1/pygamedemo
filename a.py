class Spam(object):

    def __init__(self, key, value):
        self.list_ = [value]
        self.dict_ = {key : value}

        self.list_.append(value)
        self.dict_[key] = value

        print(f'List: {self.list_}')
        print(f'Dict: {self.dict_}')

Spam('Key 1', 'Value 1')
Spam('Key 2', 'Value 2')
