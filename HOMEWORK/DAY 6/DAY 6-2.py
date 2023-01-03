
from test import value

def main():
    test_greet()
    
def test_greet():
    assert value('hello') == "$0"
    assert value('sunshine') == "$100"
    assert value('hey') == "$20"
    assert value('love') == "$100"
    
if __name__ == '__main__':
    main()
    
    