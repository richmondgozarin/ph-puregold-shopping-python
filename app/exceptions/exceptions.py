class ShoppingException(Exception):
    def __init__(self, code, desc):
        self.code = code
        self.description = desc

    def __str__(self):
        return self.description

class KeyNotFoundException(ShoppingException):
    def __init__(self, key_name=''):
        self.code = 404
        self.description = "shopping service error during key retrieval: key not found ({0}).".format(key_name)


class ServiceUnavailableException(ShoppingException):
    def __init__(self, domain):
        self.code = 503
        self.description = "Error during service call: " + domain + " unavailable."
