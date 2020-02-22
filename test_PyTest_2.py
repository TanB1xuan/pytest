class TestClass():
    name = 'TestClass'
    def test_one(self):
        x = 'This'
        assert 'h' in x

    def test_two(self):
        x = 'TestClass'
        assert hasattr(self, 'name')