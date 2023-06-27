from abc import ABC

AND = 'AND'
OR = 'OR'


class BaseQueryExpression(ABC):
    seperator = ', '

    def __init__(self) -> None:
        self._params: list[str] = []

    def add(self, *args) -> None:
        [self._params.append(arg) for arg in args if arg not in self._params]

    def __str__(self) -> str:
        ''' Return line of part of query expression '''
        return f'{self.seperator}'.join(self._params)

    def __bool__(self) -> bool:
        """ For exclude from lines if it does not participate in the query """
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
        self._select = SELECT()
        self._where = WHERE()
        self._from = FROM()

        self.query_parts = (
            self._select,
            self._where,
            self._from,
        )

    def SELECT(self, *args):
        self._select.add(*args)
        return self

    def FROM(self, *args):
        self._from.add(*args)
        return self

    def WHERE(self, **kwargs):
        self._where.add(**kwargs)
        return self

    def _lines(self):
        for query_part in self.query_parts:
            if query_part:
                yield ' ' + query_part.__class__.__name__ + ' '
                yield str(query_part)
        yield ';'

    def oneline(self):
        return str(self).replace('\n', ' ').replace('\t', ' ').strip()

    def __str__(self):
        return ''.join(self._lines()).strip()
