import dogecoinrpc


connection = dogecoinrpc.connect_to_local()


def get_address():
    return connection.getnewaddress()


def check_balance(addr):
    return connection.getbalance(addr)
