import unittest

from logics.NaiveBayesClassifier import naive_search


class Tests(unittest.TestCase):

    def test_naive_search(self):
        self.assertEqual(naive_search(
            "Dashing through the snow on a one horse open sleigh o'er the fields we go, laughing all the way bells on bob tail ring, making spirits bright what fun it is to laugh and sing a sleighing song tonight",
            "the"), [(16, 19), (57, 60), (88, 91)])
        self.assertEqual(naive_search("AAAAAAA", "AAAA"), [(0, 4), (1, 5), (2, 6), (3, 7)])
