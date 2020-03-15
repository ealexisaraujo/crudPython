import sys

clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_client():
    global clients
    print(clients)


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client not in client\'s list')


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('[C]reat client')
    print('[U]pdate client')
    print('[D]elete client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_client()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the new client name? ')
        update_client(client_name, updated_name)
        list_client()
    else:
        print('Invalid command')
