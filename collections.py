class SecretDict(collections.UserDict):

    def _password_is_valid(self, password):
        pass

    def _get_item(self, key):
        pass

    def __getitem__(self, key):
         password, key = key.split(':')
         
         if self._password_is_valid(password):
              return self._get_item(key)
         
         return None

my_secret_dict = SecretDict(...)
my_secret_dict['some_password:some_key'] # si el password es válido, regresa el valor


Coffee = collections.NamedTuple('Coffee', ('size', 'bean', 'price'))
def get_coffee(coffee_type):
    if coffee_type == 'houseblend':
        return Coffee('large', 'premium', 10)