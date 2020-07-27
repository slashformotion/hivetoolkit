from .. import utils
from beem.blockchain import Blockchain
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

    def run(self, comment_criteria):
        if not isinstance(comment_criteria, CommentCriteria):
            raise TypeError("comment_criteria argument must be an instance of Comment Criteria")
        
        if hasattr(comment_criteria, start) and hasattr(comment_criteria, stop):

            #get starting block id
            start_block_id = self.__blockchain.get_estimated_block_num()
            for comment_json in self.__blockchain.stream(opNames=['comment'], start=start_block_id, stop=stop_block_id):

                #
