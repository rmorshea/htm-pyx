import pytest

from htm_pyx import transpile


def html(tag, *args):
    return (tag, tuple(a for a in args if a))


@pytest.mark.parametrize(
    "code, model, local",
    [
        ("<div/>", html("div"), {}),
        ("<div myAttr=3 />", html("div", {"myAttr": "3"}), {}),
        ("<div myAttr={1 + 2} />", html("div", {"myAttr": 3}), {}),
        ("<div myAttr={a} />", html("div", {"myAttr": 3}), {"a": 3}),
        ("<div>inner HTML</div>", html("div", ["inner HTML"]), {}),
        ("<div>{'inner' + ' ' + 'HTML'}</div>", html("div", ["inner HTML"]), {}),
        ("<div>{inner}</div>", html("div", ["inner HTML"]), {"inner": "inner HTML"}),
        ("<div><img/></div>", html("div", [html("img")]), {}),
        ("<div>{ html'<div/>' }</div>", html("div", [html("div")]), {}),
        (
            "<div>{'a'} b {'c'} d</div>",  # left boundary case
            html("div", ["a", " b ", "c", " d"]),
            {"some": "some"},
        ),
        (
            "<div>a {'b'} c {'d'}</div>",  # right boundary case
            html("div", ["a ", "b", " c ", "d"]),
            {"some": "some"},
        ),
    ],
)
def test_transpile_html_templates(code, model, local):
    to_transpile = "html" + repr(code)  # add template prefix indicator
    assert eval(transpile(to_transpile), globals(), local) == model


@pytest.mark.parametrize(
    "code",
    [
        "'html'",
        "'''html'''",
        '"html"',
        '"""html"""',
        "'html' + x 'html'",
        """ 'html' + x + "html" """,
        """ 'html"' """,
        """ "html'" """,
    ],
)
def test_what_not_to_transpile(code):
    assert transpile(code) == code
