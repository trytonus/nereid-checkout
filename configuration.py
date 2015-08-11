# -*- coding: utf-8 -*-
from trytond.pool import PoolMeta

__all__ = ['Configuration']
__metaclass__ = PoolMeta


class Configuration:
    """
    Sale Configuration
    """
    __name__ = 'sale.configuration'

    @staticmethod
    def default_payment_authorize_on():
        return 'manual'

    @staticmethod
    def default_payment_capture_on():
        return 'sale_process'
