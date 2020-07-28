from .. import utils
from beem.blockchain import Blockchain
from beem.comment import Comment
from .criterias import CommentCriteria

class Crawler:

    def __init__(self, name, blockchain):
        self.__name = name
        if blockchain == 'hive':
            self.__blockchain = Blockchain(blockchain_instance=utils.HIVE_INSTANCE)
            pass
        elif blockchain == 'steem':
            self.__blockchain = Blockchain(blockchain_instance=utils.STEEM_INSTANCE)
        else:
            raise NotImplementedError


class CommentCrawler(Crawler):

    def __init__(self, blockchain='hive'):
        super().__init__(name='Comment crawler')

    def run(self, criteria):
        if not isinstance(criteria, CommentCriteria):
            raise TypeError("criteria argument must be an instance of CommentCriteria")
        
        if hasattr(criteria, start) and hasattr(criteria, stop):

            #get starting block id
            start_block_id = self.__blockchain.get_estimated_block_num(criteria.start, accurate=True)
            start_block_id = self.__blockchain.get_estimated_block_num(criteria.stop, accurate=True)

            #looping trough generator
            for comment_json in self.__blockchain.stream(opNames=['comment'], start=start_block_id, stop=stop_block_id):
                
                # create authorperm
                authorperm = '@{}/{}'.format(
                    comment.get('author'),
                    comment.get('permlink')
                )
                
                # create Comment object
                comment = Comment(authorperm)

                ## FILTERING ##

                # allowed authors filter
                if hasattr(criteria, allowed_authors):
                    if not comment.author in criteria.allowed_authors:
                        continue

                # unallowed authors filter
                if hasattr(criteria, unallowed_authors):
                    if comment.author in criteria.unallowed_authors:
                        continue
        else:
            print('Timeframe was not set in criteria')
    
