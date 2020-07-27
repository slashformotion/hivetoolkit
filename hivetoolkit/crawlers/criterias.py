import datetime


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

    def 
    
    