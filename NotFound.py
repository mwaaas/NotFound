
class NotFound(object):
    def get(self, k, d=None):
        return d


not_found = NotFound()