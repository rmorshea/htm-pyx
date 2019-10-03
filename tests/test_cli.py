import os

from htm_pyx.cli import execute, PTH_FILE


def run_execute(arguments):
    for k, v in {"register": False, "deregister": False, "registered": False}.items():
        arguments.setdefault(k, v)
    return list(execute(arguments))


def test_register():
    assert run_execute({"register": True}) == []
    with open(PTH_FILE) as f:
        assert f.read() == "import htm_pyx\n"
    assert run_execute({"registered": True}) == ["True"]

    # test_register should already have run
    assert run_execute({"register": True}) == [f"already registered: '{PTH_FILE}'"]
    with open(PTH_FILE) as f:
        assert f.read() == "import htm_pyx\n"


def test_deregister():
    assert run_execute({"deregister": True}) == []
    assert not os.path.exists(PTH_FILE)
    assert run_execute({"registered": True}) == ["False"]

    # test_register should already have run
    assert run_execute({"deregister": True}) == [f"already deregistered: '{PTH_FILE}'"]
    assert not os.path.exists(PTH_FILE)
