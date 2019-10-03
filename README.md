# Hyperscript Markup Language Python Extension

An extension to the Python language with an
[f-string](https://www.python.org/dev/peps/pep-0498/)-like
template syntax for writing HTMl inspired by [pyxl](https://github.com/dropbox/pyxl):

```python
# coding=html

def html(tag, props, children):
    return (tag, props, children)

size = "30px"
text = "Hello!"

model = html"""
<div height={size} width={size} >
    <p>{text}</p>
</div>
"""
```


# HTML Template Usage

Every file that uses the HTML template syntax must:

1. Have an `html` encoding indicator as its first or second line.
2. Define a callable ``html(tag, props, children)`` in the module.

So your files should all start a bit like this:

```python
# coding=html
def html(tag, props, children): ...
```

If you haven't [permanently installed](#HTML-Template-Syntax-Installation) the
language extension you'll need to import modules with HTML Template Syntax, you'll need
to make sure `idom` has been imported at your application's entry point to register the
language extension before importing your module:

```python
import htm_pyx
import my_project
```

Where ``my_project.py`` would have the following contents:

```python
# coding=html

def html(tag, props, children):
    ...

cool_stuff = html"<div>...</div>"
```


# HTML Template Syntax Installation

If you want to more permanently install the language extension you can run the console command:

```bash
htm-pyx register
```

Which can be undone (if desired) later:

```bash
htm-pyx deregister
```


This is **optional**, because you can always `import htm_pyx` at the root of your application
to enable the extension. After this initial import all the follow with `coding=html`
will be appropriately transpiled.


# Additional Support For HTML Template Syntax

You won't be able to use the HTML template syntax directly in Python's default REPL, but
it will work out of the box with:

1. [Jupyter](https://jupyter.org)
2. [IPython](http://ipython.org/)
