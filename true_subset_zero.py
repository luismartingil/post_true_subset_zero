#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
true_subset_zero.py

Implementing the true subset puzzle.

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

import unittest

MIN_RANGE = -65000
MAX_RANGE = 65000

class itemNotRange(Exception):
    pass

def subset_zero(array, iterations=None):
    """ Receives a list of integers in the range [-65000, 65000] and 
    returns True if any subset of the list summed is equal to zero. 
    False otherwise.

    Implementation based on a Set.
    Taking advantage of the Integer nature of the problem.    
    """
    # PRE. array is a list of integers
    found, myset = False, set([])
    for elem in array:
        if not (MIN_RANGE < elem < MAX_RANGE):
            raise itemNotRange('Found item out of the range. %s' % elem)
        # >>> Debugging iterations
        if iterations is not None:
            iterations.append((elem, list(myset)))
        # <<< End debug iterations
        # Lets find subsets
        if (elem == 0 or (elem * -1) in myset): 
            found = True
            break
        else:            
            map(lambda x : myset.add(x + elem), myset.copy()) # .copy() overhead!
            myset.add(elem)
    # end for
    return found

# Lets work on some unittests
tests_true = [
    [0],
    [33, -15, 1, 2, 3, 1, -5],
    [1, 2, -3],
    [7, 3, 4, -1, -1, 2, 7, 8],
    [1, 4, 5, 2, -3],
    [1, 4, 5, 2, -7],
    [10, 40, 5, 2, -60, 5],
    [10, 40, 5, 1, -60, 9],
    [5, 2, 1, 10, -13],
    [-15, 5, 5, 5],
    [15, 5, -1, -2, -17, 5, 5, 5, 5, 5, 5, 5, -1, -4],
    ]

tests_false = [
    [],
    [1, 2, -5],
    [1, 1, 5, 11],
    [60, 1, 1, 5, 60],
    [10, -1, -3, 6, 10, 6, 10],
    ]

class Test_Apply(unittest.TestCase):
    pass

def test_Function_subset_zero(t, desired):
    def test(self):
        if desired:
            self.assertTrue(subset_zero(t))
        else:
            self.assertFalse(subset_zero(t))
    return test

def attach(where, desc, fun, l, desired):
    """ Attaches tests. DRY function helper. """
    for a, b in [("test-%s-%.6i" % (desired, l.index(x)), fun(x, desired)) \
                     for x in l]:
        setattr(where, a, b)

def suite():
    test_suite = unittest.TestSuite()
    attach(Test_Apply, 
           "test_Function_subset_zero_true", 
           test_Function_subset_zero, 
           tests_true,
           True)
    attach(Test_Apply, 
           "test_Function_subset_zero_false", 
           test_Function_subset_zero, 
           tests_false,
           False)
    test_suite.addTest(unittest.makeSuite(Test_Apply))
    return test_suite
    
if __name__ == '__main__':

    test = True
    iterations = True

    if test:
        mySuit=suite()
        runner=unittest.TextTestRunner(verbosity=2)
        runner.run(mySuit)
        print 'Should be %i tests' % (len(tests_true) + len(tests_false))
        print '~' * 60

    if iterations:
        # Lets get the iterations
        array, ite = [1, 1, 2, -10, 8], []
        print 'resolving array: %s' % array
        result = subset_zero(array, iterations=ite)
        print 'result: %s' % (result)
        for value, list_status in ite:
            print '%10s %s' % (value, list_status)
