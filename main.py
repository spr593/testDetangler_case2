from feature import featureA
from feature import testFeatureA
import unittest

if __name__=="__main__":
    objA = featureA(7,9)
    suite = unittest.TestLoader().loadTestsFromTestCase(testFeatureA)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("Tests passed")
    else:
        print("Tests Failed")


