# coding=html


def html(tag, *args):
    return (tag, tuple(a for a in args if a))


expectations = [
    (html"<div/>", html("div"))
]
