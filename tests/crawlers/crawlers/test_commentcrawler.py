import unittest
import datetime
from beem.comment import Comment
from hivetoolkit.crawlers.criterias import CommentCriteria


class test_CommentCrawler(unittest.TestCase):
    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _getTargetClass(self):
        from hivetoolkit.crawlers.crawlers import CommentCrawler

        return CommentCrawler

    def test__filter_unallowed_authors(self):

        crawler = self._makeOne(blockchain="hive")

        authorperms = [
            "@theophile.roos/little-fountain",
            "@theophile.roos/one-of-my-best-macro-shot",
        ]
        comments = [Comment(authorperm) for authorperm in authorperms]

        criteria = CommentCriteria()
        criteria.set_rule("unallowed_authors", ["theophile.roos"])

        for comment in comments:
            with self.subTest(comment=comment):
                self.assertFalse(crawler._filter(comment, criteria))

        ## return use case
        crawler = self._makeOne(blockchain="hive")

        authorperms = [
            "@slashformotion/learn-flask-n1-basics",
            "@slashformotion/learn-flask-2-clean-architecture",
        ]
        comments = [Comment(authorperm) for authorperm in authorperms]

        criteria = CommentCriteria()
        criteria.set_rule("unallowed_authors", ["theophile.roos"])

        for comment in comments:
            with self.subTest(comment=comment):
                self.assertTrue(crawler._filter(comment, criteria))

    def test__filter_allowed_authors(self):
        # test rule 'allowed_author'

        crawler = self._makeOne(blockchain="hive")

        authorperms = [
            "@theophile.roos/little-fountain",
            "@theophile.roos/one-of-my-best-macro-shot",
        ]
        comments = [Comment(authorperm) for authorperm in authorperms]

        criteria = CommentCriteria()
        criteria.set_rule("allowed_authors", ["slashformotion"])

        for comment in comments:
            with self.subTest(comment=comment):
                self.assertFalse(crawler._filter(comment, criteria))

        ## return use case

        crawler = self._makeOne(blockchain="hive")

        authorperms = [
            "@slashformotion/learn-flask-n1-basics",
            "@slashformotion/learn-flask-2-clean-architecture",
        ]
        comments = [Comment(authorperm) for authorperm in authorperms]

        criteria = CommentCriteria()
        criteria.set_rule("allowed_authors", ["slashformotion"])

        for comment in comments:
            with self.subTest(comment=comment):
                self.assertTrue(crawler._filter(comment, criteria))

    def test__filter_unallowed_tags(self):
        crawler = self._makeOne(blockchain="hive")

        authorperms = [
            "@slashformotion/learn-flask-n1-basics",
            "@oniemaniego/android-mockups-using-html-and-css",
        ]
        comments = [Comment(authorperm) for authorperm in authorperms]

        criteria = CommentCriteria()
        criteria.set_rule("unallowed_tags", ["devtalk"])

        for comment in comments:
            with self.subTest(comment=comment):
                self.assertFalse(crawler._filter(comment, criteria))

        ## return use case

        crawler = self._makeOne(blockchain="hive")

        authorperms = [
            "@theophile.roos/little-fountain",
            "@theophile.roos/one-of-my-best-macro-shot",
        ]
        comments = [Comment(authorperm) for authorperm in authorperms]

        criteria = CommentCriteria()
        criteria.set_rule("unallowed_tags", ["devtalk"])

        for comment in comments:
            with self.subTest(comment=comment):
                self.assertTrue(crawler._filter(comment, criteria))

        def test__filter_allowed_tags(self):
            crawler = self._makeOne(blockchain="hive")

            authorperms = [
                "@slashformotion/learn-flask-n1-basics",
                "@oniemaniego/android-mockups-using-html-and-css",
            ]
            comments = [Comment(authorperm) for authorperm in authorperms]

            criteria = CommentCriteria()
            criteria.set_rule("allowed_tags", ["devtalk"])

            for comment in comments:
                with self.subTest(comment=comment):
                    self.assertTrue(crawler._filter(comment, criteria))

            ## return use case

            crawler = self._makeOne(blockchain="hive")

            authorperms = [
                "@theophile.roos/little-fountain",
                "@theophile.roos/one-of-my-best-macro-shot",
            ]
            comments = [Comment(authorperm) for authorperm in authorperms]

            criteria = CommentCriteria()
            criteria.set_rule("allowed_tags", ["devtalk"])

            for comment in comments:
                with self.subTest(comment=comment):
                    self.assertFalse(crawler._filter(comment, criteria))
