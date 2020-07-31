from beem.comment import Comment, ContentDoesNotExistsException, construct_authorperm
import datetime
from ..criterias import CommentCriteria
from .basecrawler import Crawler
import json
from ... import utils


class CommentCrawler(Crawler):
    def __init__(self, blockchain="hive"):
        super().__init__(name="Comment crawler", blockchain=blockchain)


    def run(self, criteria):
        if not isinstance(criteria, CommentCriteria):
            raise TypeError("criteria argument must be an instance of CommentCriteria")

        for comment_json in self._stream(opNames=["comment"]):
            # create authorperm
            authorperm = construct_authorperm(
                comment_json.get("author"), comment_json.get("permlink")
            )

            # try to create Comment object
            try:
                comment = Comment(authorperm)
            except ContentDoesNotExistsException as e:
                # authorperm doen't exists
                continue

            ## FILTERING ##

            if self._filter(comment, criteria):
                # filters passed
                yield comment

    

    def _filter(self, comment, criteria):
        comment_json = comment.json()
        rules = criteria.rules

        # allowed authors filter
        if "allowed_authors" in criteria.rules_names:
            if not comment.author in criteria.rules.get("allowed_authors"):
                return False

        # unallowed authors filter
        if "unallowed_authors" in criteria.rules_names:
            if comment.author in criteria.rules.get("unallowed_authors"):
                return False

        # get tags
        tags = json.loads(comment_json.get("json_metadata")).get("tags", [])
        # allowed tags filter
        if "allowed_tags" in criteria.rules_names:
            allowed_tags = criteria.rules.get("allowed_tags")
            if utils.intersection(allowed_tags, tags) == []:
                return False

        # unallowed tags filter
        if "unallowed_tags" in criteria.rules_names:
            unallowed_tags = criteria.rules.get("unallowed_tags")
            if utils.intersection(unallowed_tags, tags) == []:
                return False

        return True
