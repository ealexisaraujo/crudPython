import sys

clients = [
    {
        'name': 'Juan',
        'company': 'Maxidespensa',
        'email': 'Juan@maxi.com',
        'position': 'Sofware Engineer'
    },
    {
        'name': 'Pedro',
        'company': 'Google',
        'email': 'Pedro@google.com',
        'position': 'UX Designer'
    },
]


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)

    else:
        print('Client already is in the client\'s list')


def list_client():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']

        ))


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client not in client\'s list')


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('Welcome to platzi ventas')
    print('*'*50)
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

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
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_client()
    elif command == 'L':
        list_client()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the new client name? ')
        update_client(client_name, updated_name)
        list_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('{} is in the clients list' .format(client_name))
        else:
            print('{} is NOT in the clients list'.format(client_name))

    else:
        print('Invalid command')
