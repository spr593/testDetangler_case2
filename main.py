import unittest

if __name__=="__main__":
    #obj = featureA(7,9)
    suite = unittest.TestLoader().loadTestsFromTestCase(testFeature)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Tests passed")
    else:
        print("Tests failed")

