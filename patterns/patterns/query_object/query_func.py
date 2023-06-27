class QueryBase:

    def _line(self, key):
        """ Generate line of query """
        return ', '.join(self._query[key])

    def _lines(self):
        """ Unite all prepared lines in entire query """
        for key in self._query:
            yield key + '\n'
            yield '\t' + self._line(key) + '\n'

    def __str__(self):
        return ''.join(self._lines())

    def oneline(self) -> str:
        return str(self).replace('\t', '').replace('\n', ' ').strip()


class Query(QueryBase):
    """    Generate queries for SQL    """

    def __init__(self):
        self._query = {
            'SELECT': [],
            'FROM': [],
        }

    def _add_unique(self, uniq, *args):
        # bad practice: have side effect
        [uniq.append(arg) for arg in args if arg not in uniq]

    def SELECT(self, *args):
        args = args if args else ('*',)  # default value

        select = self._query['SELECT']
        self._add_unique(select, *args)

        return self

    def FROM(self, *args):

        from_ = self._query['FROM']
        self._add_unique(from_, *args)

        return self
