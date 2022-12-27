from Hello import hello

def test_hello():
    assert hello('David') == 'Hello, David'
    assert hello() == 'Hello, World'
    
