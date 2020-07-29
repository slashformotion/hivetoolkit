import datetime


class EmptyListError(Exception):
    """ Raised if a list argument is empty"""


class Criteria:
    def __init__(self):
        pass

    def setTimeframe(self, start, stop):
        if isinstance(start, datetime.datetime):
            self.start = start
        else:
            raise TypeError("start argument must be an instance of datetime.datetime")

        if isinstance(stop, datetime.datetime):
            self.stop = stop
        else:
            raise TypeError("stop argument must be an instance of datetime.datetime")


class CommentCriteria(Criteria):
    def __init__(self, json_config=None):
        super().__init__()
        # TODO: implement json config
        pass

    def setAllowedAuthors(self, allowed_authors):
        """set allowed authors filter

        Args:
            authors (list(str)): allowed authors

        Raises:
            TypeError: allowed_authors argument must be an instance of list
            TypeError: allowed_authors argument must contain only instances of str
            EmptyListError: allowed_authors mustn't be empty
        """
        if not isinstance(allowed_authors, list):
            raise TypeError("allowed_authors argument must be an instance of list")
        for allowed_author in allowed_authors:
            if not isinstance(allowed_author, str):
                raise TypeError(
                    "allowed_authors argument must contain only instances of str"
                )
        if len(allowed_authors) == 0:
            raise EmptyListError("allowed_authors agument mustn't be empty")
        self.allowed_authors = allowed_authors

    def setUnallowedAuthors(self, unallowed_authors):
        """set unallowed authors filter

        Args:
            authors (list(str)): unallowed authors

        Raises:
            TypeError: unallowed_authors argument must be an instance of list
            TypeError: unallowed_authors argument must contain only instances of str
            EmptyListError: unallowed_authors mustn't be empty
        """
        if not isinstance(unallowed_authors, list):
            raise TypeError("unallowed_authors argument must be an instance of list")
        for unallowed_author in unallowed_authors:
            if not isinstance(unallowed_author, str):
                raise TypeError(
                    "unallowed_authors argument must contain only instances of str"
                )
        if len(unallowed_authors) == 0:
            raise EmptyListError("unallowed_authors agument mustn't be empty")
        self.unallowed_authors = unallowed_authors

    def setAllowedTags(self, allowed_tags):
        """set unallowed tags filter

        Args:
            allowed_tags (list(str)): allowed tags

        Raises:
            TypeError: allowed_tags argument must be an instance of list
            TypeError: allowed_tags argument must contain only instances of str
            EmptyListError: allowed_tags mustn't be empty
        """
        if not isinstance(allowed_tags, list):
            raise TypeError("allowed_tags argument must be an instance of list")
        for allowed_tag in allowed_tags:
            if not isinstance(allowed_tag, str):
                raise TypeError(
                    "unallowed_authors argument must contain only instances of str"
                )
        if allowed_tag == []:
            raise EmptyListError("allowed argument mustn't be an empty list")
        self.allowed_tags = allowed_tags
