import dogecoinrpc


connection = dogecoinrpc.connect_to_local()


def get_cost():
    return 0


def generate_address():
    return connection.getnewaddress()


def check_balance(addr):
    return connection.getbalance(addr)
