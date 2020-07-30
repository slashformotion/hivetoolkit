from beem.comment import Comment, ContentDoesNotExistsException, construct_authorperm

from ..criterias import CommentCriteria
from .basecrawler import Crawler


class CommentCrawler(Crawler):
    def __init__(self, blockchain="hive"):
        super().__init__(name="Comment crawler", blockchain=blockchain)

    def run(self, criteria):
        if not isinstance(criteria, CommentCriteria):
            raise TypeError("criteria argument must be an instance of CommentCriteria")

        if hasattr(criteria, "start") and hasattr(criteria, "stop"):

            # get starting block id
            start_block_id = self._blockchain.get_estimated_block_num(
                criteria.start, accurate=True
            )
            stop_block_id = self._blockchain.get_estimated_block_num(
                criteria.stop, accurate=True
            )

            # looping trough generator
            for comment_json in self._blockchain.stream(
                opNames=["comment"], start=start_block_id, stop=stop_block_id
            ):

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

                if self.filter(comment, criteria):
                    # filters passed
                    yield comment

        else:
            print("Timeframe was not set in criteria, direct streaming used")

    def filter(self, comment, criteria):
        comment_json = comment.json()

        # allowed authors filter
        if hasattr(criteria, "allowed_authors"):
            if not comment.author in criteria.allowed_authors:
                return False

        # unallowed authors filter
        if hasattr(criteria, "unallowed_authors"):
            if comment.author in criteria.unallowed_authors:
                return False

        # allowed tags filter
        if hasattr(criteria, "allowed_tags"):
            # get tags
            tags = json.loads(comment_json.get("json_metadata")).get("tags", [])
            if utils.intersection(criteria.allowed_tags, tags) == []:
                return False

        return True