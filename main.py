clients = 'tomas,juan,'


def create_client(client_name): #1
    global clients

    clients += client_name
    _add_comma()


def list_clients(): #3
    global clients

    print(clients)


def _add_comma(): #2 
    global clients

    clients += ','


if __name__ == '__main__':
    client_name = 'Cristian'

    list_clients()
    create_client(client_name)

    list_clients()