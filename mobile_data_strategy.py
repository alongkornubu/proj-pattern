class DataPackage:

    def __init__(self, package, package_strategy):
        self.package = package
        self.package_strategy = package_strategy

    def price_of_package(self):
        price = self.package_strategy(self)
        return price

    def __repr__(self):
        statement = "price of package: {}"
        return statement.format(self.price_of_package())


def true_package(order):
    package = order.package
    if package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "1day":
        return "22 baht"
    elif package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "7day":
        return "120 baht"
    elif package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "30day":
        return "300 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "1day":
        return "40 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "7day":
        return "220 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "1day":
        return "60 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "7day":
        return "420 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "30day":
        return "520 baht"

    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "1day":
        return "21 baht"
    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "7day":
        return "120 baht"
    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "30day":
        return "310 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "1day":
        return "40 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "7day":
        return "220 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "1day":
        return "60 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "7day":
        return "420 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "30day":
        return "520 baht"

def dtac_package(order):
    package = order.package
    if package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "1day":
        return "25 baht"
    elif package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "7day":
        return "120 baht"
    elif package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "1day":
        return "40 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "7day":
        return "220 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "1day":
        return "60 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "7day":
        return "420 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "30day":
        return "520 baht"

    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "1day":
        return "20 baht"
    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "7day":
        return "120 baht"
    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "30day":
        return "200 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "1day":
        return "40 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "7day":
        return "220 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "1day":
        return "60 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "7day":
        return "420 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "30day":
        return "520 baht"


def ais_package(order):
    package = order.package
    if package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "1day":
        return "20 baht"
    elif package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "7day":
        return "120 baht"
    elif package["type"] == "unlimited" and package["speed"] == "10Mbps" and package["period"] == "30day":
        return "200 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "1day":
        return "40 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "7day":
        return "220 baht"
    elif package["type"] == "unlimited" and package["speed"] == "20Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "1day":
        return "60 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "7day":
        return "420 baht"
    elif package["type"] == "unlimited" and package["speed"] == "30Mbps" and package["period"] == "30day":
        return "520 baht"

    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "1day":
        return "20 baht"
    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "7day":
        return "120 baht"
    elif package["type"] == "limited" and package["speed"] == "10Mbps" and package["period"] == "30day":
        return "200 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "1day":
        return "40 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "7day":
        return "220 baht"
    elif package["type"] == "limited" and package["speed"] == "20Mbps" and package["period"] == "30day":
        return "320 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "1day":
        return "60 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "7day":
        return "420 baht"
    elif package["type"] == "limited" and package["speed"] == "30Mbps" and package["period"] == "30day":
        return "520 baht"