# hivetoolkit
![PyPI](https://img.shields.io/pypi/v/hivetoolkit?label=pypi)
---

Hivetools is a set of python writen tools to work with the Hive (and steem blockchain)

BE CAREFULL, THIS PACKAGE IS IN PRE-ALPHA PHASE. IT MAY NOT WORK.

### Requirements

- beem => 0.24.5
- Python >= 3.6.x

### Installation

```
pip install hivetoolkit
```

## Starting

Crawl through comments on the Hive Blockchain
```Python
from hivetoolkit.crawlers.crawlers import CommentCrawler
from hivetoolkit.crawlers.criterias import CommentCriteria
import datetime

print('This a demo of the crawler system embeded into hivetoolkit - by @slashformotion')

print('start and end point')
stop = datetime.datetime.now() - datetime.timedelta(days=1)
start = stop - datetime.timedelta(days=1)

print('creating crawler')
crawler = CommentCrawler(blockchain='hive')

print('creating criteria')
criteria = CommentCriteria()
criteria.setUnallowedAuthors(['slashformotion'])
criteria.setTimeframe(start, stop)

print('crawling through the blockchain')
for c in crawler.run(criteria=criteria):
    # c is a beem.comment.Comment
    print(c.authorperm)
```
## Contributing


## Versions

THIS PACKAGE IS IN PRE-ALPHA PHASE

## License

This project is licenced under the  ``GNU General Public License v3.0`` - see [LICENSE](LICENSE) for more.

