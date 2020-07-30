from ...utils import blockchains
from beem.blockchain import Blockchain


class Crawler:
    def __init__(self, name, blockchain):
        self.__name = name
        if blockchain == "hive":
            self._blockchain = Blockchain(blockchain_instance=blockchains.HIVE_INSTANCE)
            pass
        elif blockchain == "steem":
            self._blockchain = Blockchain(
                blockchain_instance=blockchains.STEEM_INSTANCE
            )
        else:
            raise NotImplementedError
