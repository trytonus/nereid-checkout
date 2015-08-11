# -*- coding: utf-8 -*-
import unittest
import trytond.tests.test_tryton
from test_checkout import TestCheckoutSignIn, TestCheckoutShippingAddress, \
    TestCheckoutDeliveryMethod, TestCheckoutBillingAddress, TestSale
from test_payment import TestCheckoutPayment
from test_address import TestAddress


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    loader = unittest.TestLoader()
    test_suite.addTests([
        loader.loadTestsFromTestCase(TestAddress),
        loader.loadTestsFromTestCase(TestCheckoutSignIn),
        loader.loadTestsFromTestCase(TestCheckoutShippingAddress),
        loader.loadTestsFromTestCase(TestCheckoutDeliveryMethod),
        loader.loadTestsFromTestCase(TestCheckoutBillingAddress),
        loader.loadTestsFromTestCase(TestCheckoutPayment),
        loader.loadTestsFromTestCase(TestSale)
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
