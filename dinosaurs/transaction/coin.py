import dogecoinrpc


connection = dogecoinrpc.connect_to_local()


def generate_address():
    return connection.getnewaddress()


def check_balance(addr):
    return connection.getbalance(addr)
