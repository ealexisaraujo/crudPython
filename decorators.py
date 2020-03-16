PASSWORD = '12345'


def password_require(func):
    def wrapper():
        password = input('Cual es tu contraseña: ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')

    return wrapper


@password_require
def need_password():
    print('La contrasena es correcta')


def upper(func):
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)

        return result.upper()

    return wrapper


@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)


if __name__ == "__main__":
    print(say_my_name('David'))
