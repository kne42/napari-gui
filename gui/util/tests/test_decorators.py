from ..decorators import classgetter


def test_classgetter():
    class Foo(object):
        bar = {}

        @classgetter
        def baz(cls):
            return list(cls.bar.keys())


    assert Foo.baz == []
    assert Foo().baz == []

    Foo.bar['SPAM'] = 42

    assert Foo.baz == ['SPAM']
    assert Foo().baz == ['SPAM']
