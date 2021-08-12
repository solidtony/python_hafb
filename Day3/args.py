import socket
from pprint import pp

def main():
    #resolver = Resolver()
    #print(resolver('weber.edu'))
    #print(resolver('google.com'))
    #print(resolver('google.com'))
    #print(resolver._cache)

    #if resolver.has_host("google.com"):
    #    resolver.clear()
    #print(resolver("google.com"))
    #print(resolver._cache)
    test_lambda()


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


def sequence_class(immutable):
    return tuple if immutable else list


def test_lambda():
    scientist = ['Marie Curie',
                 'Albert Einstein',
                 'Dimitri Mendeleev',
                 'Charles Darwin',
                 'Isaac Newton']
    pp(sorted(scientist, key=lambda name: name.split()[0]))


if __name__ == '__main__':
    main()