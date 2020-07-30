from .basecriteria import BaseCriteria
from ...utils import arguments


class CommentCriteria(BaseCriteria):
    def __init__(self, json_config=None):
        super().__init__()
        # TODO: implement json config
        pass

    # def _reset(self):
    #     del self.allowed_authors
    #     del self.allowed_tags
    #     del self.unallowed_authors
    #     def self.unallowed_tags

    def setAllowedAuthors(self, allowed_authors):
        """set allowed author filter

        Args:
            allowed_authors (list[str]): allowed authors list

        Raises:
            TypeError: wrong type for one of the arguments
        """
        name_arg = "allowed_authors"
        try:
            arguments.checkList(allowed_authors, name_arg=name_arg)
        except TypeError as e:
            raise TypeError(e) from e
        else:
            self.allowed_authors = allowed_authors

    def setUnallowedAuthors(self, unallowed_authors):
        """set unallowed authors filter

        Args:
            unallowed_authors (list[str]: unallowed authors list

        Raises:
            TypeError: wrong type for one of the arguments
        """
        name_arg = "unallowed_authors"
        try:
            arguments.checkList(unallowed_authors, name_arg=name_arg)
        except TypeError as e:
            raise TypeError(e) from e
        else:
            self.unallowed_authors = unallowed_authors

    def setAllowedTags(self, allowed_tags):
        """set allowed tags filter

        Args:
            allowed_tags (list[str]): allowed tags list

        Raises:
            TypeError: wrong type for one of the arguments
        """
        name_arg = "allowed_tags"
        try:
            arguments.checkList(allowed_tags, name_arg=name_arg)
        except TypeError as e:
            raise TypeError(e) from e
        else:
            
            self.allowed_tags = allowed_tags

    def setUnallowedTags(self, unallowed_tags):
        """set unallowed tag filter

        Args:
            unallowed_tags (list[str]): unallowed tags list

        Raises:
            TypeError: wrong type for one of the arguments
        """
        name_arg = "unallowed_tags"
        try:
            arguments.checkList(unallowed_tags, name_arg=name_arg)
        except TypeError as e:
            raise TypeError(e) from e
        else:
            self.unallowed_tags = unallowed_tags
