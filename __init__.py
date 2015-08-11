# -*- coding: utf-8 -*-
from trytond.pool import Pool

from sale import Sale, SaleLine
from payment import Website, NereidPaymentMethod
from checkout import Cart, Checkout, Party, Address
from configuration import Configuration


def register():
    Pool.register(
        Cart,
        Sale,
        Configuration,
        Party,
        Website,
        Checkout,
        NereidPaymentMethod,
        Address,
        SaleLine,
        type_="model", module="nereid_checkout"
    )
