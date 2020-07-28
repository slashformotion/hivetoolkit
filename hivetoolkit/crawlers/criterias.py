import datetime

class EmptyList(Exception):
    """ Raised if a list argument is empty"""

class Criteria:
    
    def setTimeFrame(self, start, stop):
        if isinstance(start, datetime.datetime):
            self.start = start
        else:
            raise TypeError('start argument must be an instance of datetime.datetime')

        if isinstance(stop, datetime.datetime):
            self.stop = stop
        else:
            raise TypeError('stop argument must be an instance of datetime.datetime')
        

class CommentCriteria:
    def __init__(self, json_config=None):
        # TODO: implement json config
        pass

    def setAllowedAuthors(self, allowed_authors):
        """set allowed authors filter

        Args:
            authors (list(str)): allowed authors

        Raises:
            TypeError: allowed_authors argument must be an instance of list
            TypeError: allowed_authors argument must contain only instances of str
            EmptyList: allowed_authors mustn't be empty
        """
        if not isinstance(allowed_authors, list):
            raise TypeError('allowed_authors argument must be an instance of list')
        for author in allowed_authors:
            if not isinstance(allowed_authors, str):
                raise TypeError('allowed_authors argument must contain only instances of str')
        if len(allowed_authors)==0:
            raise EmptyList("allowed_authors agument mustn't be empty")
        self.allowed_authors = allowed_authors
    
    def setUnallowedAuthors(self, unallowed_authors):
        """set unallowed authors filter

        Args:
            authors (list(str)): unallowed authors

        Raises:
            TypeError: unallowed_authors argument must be an instance of list
            TypeError: unallowed_authors argument must contain only instances of str
            EmptyList: unallowed_authors mustn't be empty
        """
        if not isinstance(unallowed_authors, list):
            raise TypeError('unallowed_authors argument must be an instance of list')
        for author in unallowed_authors:
            if not isinstance(unallowed_authors, str):
                raise TypeError('unallowed_authors argument must contain only instances of str')
        if len(unallowed_authors)==0:
            raise EmptyList("unallowed_authors agument mustn't be empty")
        self.unallowed_authors = unallowed_authors

