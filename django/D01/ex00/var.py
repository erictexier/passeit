#!/usr/local/bin/python3

def my_var():
    ll = [42,"42","quarante-deux",42.0,True,[42],{'42':42} ,((42,)),set()]
    for a in ll:
        print(a," est de type ", type(a))

if __name__ == '__main__':
    my_var()
