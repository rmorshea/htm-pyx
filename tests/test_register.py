import htm_pyx  # noqa


def test_html_coding():
    from .html_coding import expectations

    for transpiled, expected in expectations:
        assert transpiled == expected
