class Query:

    def __init__(self):
        self._query = {
            'SELECT': [],
            'FROM': [],
        }

    def SELECT(self, *args):
        self._query['SELECT'].extend(args)
        return self

    def FROM(self, *args):
        self._query['FROM'].extend(args)
        return self

    def _line(self, key):
        return ', '.join(self._query[key])

    def _lines(self):
        for key in self._query:
            yield key + '\n'
            yield '\t' + self._line(key) + '\n'

    def __str__(self):
        return ''.join(self._lines())


if __name__ == '__main__':
    q = Query()
    q.SELECT('*')
    q.FROM('d', 'e', 'f')
    print(q)
    # print(', '.join(['1', '2', '3']))
