#!/usr/bin/env python

"""Tests for `pcc` package."""

from pcc import pcc

def help_get_complexity(code: str):
    code = bytes(code, "utf8")
    graphs = pcc.calc_code_complexity(code, 'c')
    if not graphs:
        return 0
    max_item = max(graphs, key=lambda x: x.complexity())
    return max_item.complexity()


def test_empty_func():
    code = '''\
void f() {
    return;
}
'''
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_sequential():
    code = """\
int func(int n) {
    int k = n + 4;
    int s = k + n;
    return s;
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_sequential_unencapsulated():
    code = """\
int k = 2 + 4;
int s = k + n;
"""
    complexity = help_get_complexity(code)
    assert complexity == 0


def test_if_else_dead_path():
    code = """\
int func(int n) {
    if (n > 3){
        return 3;
    }
    else {
        return 0;
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_if_elif_else_dead_path():
    code = """\
int func(int n) {
    if (n > 3){
        return 3;
    }
    else if (n > 4) {
        return 4;
    }
    else if (n > 5) {
        return 5;
    }
    else {
        return 0;
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 4


def test_if_elif_else_nest():
    code = """\
int func(int n) {
    int m = 1;
    if (n > 3){
        return 3;
    }
    else if (n > 4) {
        return 4;
    }
    else if (n > 5) {
        if (m > 6) {
            return 6;
        } else {
            return 7;
        }
    }
    else {
        return 0;
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 6


def test_if_for():
    code = """\
int func(int n) {
    if (n > 3){
        return 3;
    }
    else {
        for(;n<3;n++) {
            return 33;
        }
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_for_loop():
    code = """\
void f(int i){
    int s = 0;
    for(i; i<10; i +=) {
        s += i
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_for_if_loop():
    code = """\
void f(int i){
    int s = 0;
    for(i; i<10; i +=) {
        if(i == 5){
            s += 50;
        } else {
            s += i;
        }
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 3


def test_while_loop():
    code = """\
void f(int i){
    int s = 0;
    while(i<10) {
        s += i;
        i +=1;
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_while_if_loop():
    code = """\
void f(int i){
    int s = 0;
    while(i<10) {
        if(i == 5){
            s += 50;
        } else {
            s += i;
        }
        i +=1;
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 3


def test_recursive():
    code = """\
int func(int n) {
    if (n > 3){
        n = n - 1;
        return func(n);
    }
    else {
        return 0;
    }
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 2


def test_macro():
    # TODO: Support macro
    code = """\
#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
int func(int a, int b) {
    int c = MIN(a,b);
    return c;
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_conditional_operator():
    # TODO: Support conditional_operator
    code = """\
int func(int a, int b) {
    int c = a > b ? a : b;
    return c
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 1


def test_return():
    # TODO: Support return
    code = """\
int func(int a, int b) {
    return a > b ? a : b;
}
"""
    complexity = help_get_complexity(code)
    assert complexity == 1
