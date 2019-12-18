class Elastic(object):

    def hits(self, count=10):
        from .elastichits import ElasticHits
        return ElasticHits().get(count=count)