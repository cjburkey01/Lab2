import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {
        'Pen': {
            'qnt': 10,
            'unit_price': 3.75,
            'discount': 5.0,
        },
        'Notebook': {
            'qnt': 5,
            'unit_price': 7.5,
            'discount': 10.0,
        },
    }

    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalTax(invoice, products):
    assert round(invoice.totalTax(invoice.totalImpurePrice(products), 0.07), 2) == 5.25


def test_CanCalculateTotalPurePrice(invoice, products):
    assert invoice.totalPurePrice(products, 0.0) == 69.38


def test_CanCalculateTaxedPurePrice(invoice, products):
    assert round(invoice.totalPurePrice(products, 0.09), 2) == 75.62
