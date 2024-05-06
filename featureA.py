import unittest

def map_lists(list1: List[int], list2: List[int]) -> List[float]:
    """
        Maps two lists to its convolution.
        Args: Two Input Lists
        Returns: Result list
    """
    result = []
    total_length = len(list1) + len(list2) - 1
    for i in range(total_length):
        dot_product = list1[i] * list2[i]
        result.append(dot_product + 0.0)
    return result

class test_conv(unittest.TestCase):
    def test_featureC(self):
        self.assertIsInstance(map_lists.action(), ([int], [int]), "Not a convoluted list")

if __name__=="main":
    print('Feature A Merge(main, branch-A) Resolved')
