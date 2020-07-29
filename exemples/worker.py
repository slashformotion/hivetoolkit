from context import hivetoolkit
from hivetoolkit.crawlers.crawlers import CommentCrawler
from hivetoolkit.crawlers.criterias import CommentCriteria
import datetime

print("This a demo of the crawler system embeded into hivetoolkit - by @slashformotion")

print("start and end point")
stop = datetime.datetime.now() - datetime.timedelta(days=1)
start = stop - datetime.timedelta(days=1)

print("creating crawler")
crawler = CommentCrawler(blockchain="hive")

print("creating criteria")
criteria = CommentCriteria()
criteria.setUnallowedAuthors(["theophile.roos"])
criteria.setTimeframe(start, stop)

print("crawling through the blockchain")
for index, c in enumerate(crawler.run(criteria=criteria)):
    print("    {}: {}".format(index, c.authorperm))

    if index >= 10:
        break
