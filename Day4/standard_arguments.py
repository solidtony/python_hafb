
def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


def print_pos_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

def main():
    print_args(arg1=1, kwarg1='hi', arg2=2, kwarg2='yes', kwargs={'me': 'hello', 'you': 'hi', 'them': 'you'})


if __name__ == '__main__':
    main()