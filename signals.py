# This file is part of Tryton & Nereid. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from flask.signals import _signals

#: Address update signal
#:  - This signal is triggered when a the address is updated.
cart_address_updated = _signals.signal('address-updated')
