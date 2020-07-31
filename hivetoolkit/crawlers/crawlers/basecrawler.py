from ...utils import blockchains
from beem.blockchain import Blockchain
import datetime

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

    def _stream(self, opNames=[]):
        if hasattr(self, "start") and hasattr(self, "stop"):

            # get starting block id
            start_block_id = self._blockchain.get_estimated_block_num(
                self.start, accurate=True
            )
            stop_block_id = self._blockchain.get_estimated_block_num(
                self.stop, accurate=True
            )

            # looping trough generator
            for op_json in self._blockchain.stream(
                opNames=opNames, start=start_block_id, stop=stop_block_id
            ):
                yield op_json

        else:
            print("Timeframe was not set in criteria, direct streaming used")
            # looping trough generator
            for op_json in self._blockchain.stream(opNames=opNames):
                yield op_json
    
    def set_timeframe(self, start, stop):
        if isinstance(start, datetime.datetime):
            self.start = start
        else:
            raise TypeError("start argument must be an instance of datetime.datetime")

        if isinstance(stop, datetime.datetime):
            self.stop = stop
        else:
            raise TypeError("stop argument must be an instance of datetime.datetime")

        if start >= stop:
            raise RuntimeError("stop({}) < start({})".format(stop, start))
