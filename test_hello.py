from hello import hello

def test_hello():
    assert hello("david") == "hello, david"
    assert hello() == "hello, world"

def test_argument():
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"