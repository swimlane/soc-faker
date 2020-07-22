class Elastic(object):

    """The main entrypoint for all things Elastic
    """

    def hits(self, count=10):
        """Returns a provided count of generated / fake Elasticsearch query hits.  Default is 10.

        Args:
            count (int, optional): The number of Elasticsearch query hits returned in a list. Defaults to 10.

        Returns:
            list: A list of Elasticsearch query hits
        """
        from .elastichits import ElasticHits
        return ElasticHits().get(count=count)

    @property
    def document(self):
        """A generated Elastic Common Schema documents that could be sent to Elasticsearch

        Returns:
            ElasticECS: Returns the base class for Elastic Common Schema
        """
        from .elasticecs import ElasticECS
        return ElasticECS(windows_events=True)
