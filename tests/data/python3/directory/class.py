import copy
import json
import requests
import time


def get_url(env):
    pass


class Myclass(object):
    def __init__(self, name):
        self.name = name

    def classfun1(self, a, b, c):
        env_list = ["1", "2"]
        try:
            for env in env_list:
                base_url = get_url(env)
                if base_url == 'eeee':
                    print(33333)
                elif base_url == 'rrrrrrrrrrr':
                    print(3456)
                elif base_url == 'dddddddd':
                    print(678776)
                else:
                    print(11111)
        except Exception as e:
            print(str(e))


def myfun():
    env_list = ["1", "2"]
    try:
        for env in env_list:
            base_url = get_url(env)
            if base_url == 'eeee':
                print(33333)
            elif base_url == 'rrrrrrrrrrr':
                print(3456)
            elif base_url == 'dddddddd':
                print(678776)
            else:
                print(11111)
    except Exception as e:
        print(str(e))


a = 3


def myfun2(e, a):
    env = 123
    base_url = get_url(env)

    # while (base_url is not None):
    env += 1
    base_url = get_url(env)
    while base_url is not None:
        if base_url == 'eeee':
            print(33333)
        elif base_url == 'rrrrrrrrrrr':
            print(3456)
        elif base_url == 'dddddddd':
            print(678776)
        elif base_url == 'aaaaaaaaa':
            print(678987656789)
        else:
            print(66666)
