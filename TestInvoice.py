import pytest
from Invoice import Invoice

@pytest.fixture()
def products():

    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5, 'tax': 2, 'fee': 3},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10, 'tax': 2, 'fee': 5}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_CanCalculateTax(invoice, products):
    invoice.salesTax(products)
    assert invoice.salesTax(products) == 1.39


def test_CanCalculateTaxPrice(invoice, products):
    invoice.taxPrice(products)
    assert invoice.taxPrice(products) == 70.77


def test_CanCalculateFeePrice(invoice, products):
    invoice.deliveryPrice(products)
    assert invoice.deliveryPrice(products) == 78.77
