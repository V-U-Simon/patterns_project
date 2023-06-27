from abc import ABC

AND = 'AND'
OR = 'OR'


class BaseQueryExpression(ABC):
    seperator = ', '

    def __init__(self) -> None:
        self._params: list[str] = []

    def add(self, *args) -> None:
        self._params.extend(args)

    def __str__(self) -> str:
        ''' Return line of part of query expression '''
        return f'{self.seperator}'.join(*self._params)

    def __bool__(self) -> bool:
        return bool(self._params)


class SELECT(BaseQueryExpression):
    ...


class FROM(BaseQueryExpression):
    ...


class WHERE(BaseQueryExpression):

    def __init__(self, separator=AND, **kwargs) -> None:
        self.separator = separator
        self._params = kwargs

    def add(self, **kwargs) -> None:
        self._params.update(kwargs)

    def __str__(self) -> str:
        kw_pairs = [f'{key}={value}' for key, value in self._params.items()]
        return f' {self.separator} '.join(kw_pairs)


class Query:

    def __init__(self):
        self._part_of_query = {
            'SELECT': SELECT(),
            'WHERE': WHERE(),
            'FROM': FROM(),
        }

    def SELECT(self, *args):
        self._part_of_query['SELECT'].add(args)
        return self

    def FROM(self, *args):
        self._part_of_query['FROM'].add(args)
        return self

    def WHERE(self, **kwargs):
        self._part_of_query['WHERE'].add(**kwargs)
        return self

    def _lines(self):
        for name, experssion in self._part_of_query.items():
            if experssion:
                yield name + '\n'
                yield '\t' + str(experssion) + '\n'
        yield ';'

    def __str__(self):
        return ''.join(self._lines())


if __name__ == '__main__':

    q = Query()
    q.SELECT('a', 'b')
    q.FROM('d', 'e', 'f')
    q.WHERE(id=1, name='mike')
    print(q)
