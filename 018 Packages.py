# A package is a directory with __init__.py in it. It can contain one or more
# modules.

# importing the entire shipping module

from ecommerce import shipping
shipping.calc_shipping()

# importing one function in the shipping module

from ecommerce.shipping import calc_shipping
calc_shipping()
