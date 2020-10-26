# hivetoolkit  ***DISCONTINUED !!***
![PyPI](https://img.shields.io/pypi/v/hivetoolkit?label=pypi)
---

Hivetools is a set of python writen tools to work with the Hive (and steem blockchain)

BE CAREFULL, THIS PACKAGE IS IN PRE-ALPHA PHASE. IT MAY NOT WORK.


### Requirements

- beem >= 0.24.5
- Python >= 3.6.x

### Installation

```
pip install hivetoolkit==0.0.2
```

## Starting

Crawl through comments on the Hive Blockchain (right now, you can only do this... but more is comming)
```Python
from hivetoolkit.crawlers.crawlers import CommentCrawler
from hivetoolkit.crawlers.criterias import CommentCriteria
import datetime

print(
    "This a demo of the crawler system embeded into hivetoolkit - by @slashformotion"
)

print("start and end point")
stop = datetime.datetime.now() - datetime.timedelta(days=1)
start = stop - datetime.timedelta(days=1)

print("creating crawler")
crawler = CommentCrawler(blockchain="hive")
crawler.set_timeframe(start, stop)

print("creating criteria")
criteria = CommentCriteria()
criteria.set_rule("unallowed_authors", ["theophile.roos"])

print("crawling through the blockchain")
for index, c in enumerate(crawler.run(criteria=criteria)):
    print("    {}: {}".format(index, c.authorperm))

```
## Testing

To run test, just use this:
```
python -m unittest discover tests -v -f
```
If you find a bug, please fill an issue.

## Contributing

Fork if you want ! 

## Versions

<<<<<<< HEAD
- **0.0.2**: `CommentCrawler` and `CommentCriteria` are working

## RoadMap

- get the documentation working...(kind of a big deal, so this is priority ***n1***)
- Implementation of a specific crawler and criteria for Votes, Proposals, Transferts, CustomJsons, Vestings
- Implementation of integration tests
=======
THIS PACKAGE IS IN PRE-ALPHA PHASE
>>>>>>> 12c706ce19e904a8120cf1c1e719a600a2039b2a

## License

This project is licenced under the  ``GNU General Public License v3.0`` - see [LICENSE](https://github.com/slashformotion/hivetoolkit/blob/master/LICENCE) for more.

