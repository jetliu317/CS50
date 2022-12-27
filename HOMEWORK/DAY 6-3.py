from test import is_valid

def main():
    test_plate()
    
def test_plate():
    assert is_valid('a0123') == False
    assert is_valid('aa123') == True
    assert is_valid('j') == False
    assert is_valid('.,889') == False
    assert is_valid('ah8123jnjk') == False
    assert is_valid('0123') == False
    assert is_valid('') == False

if __name__ == '__main__':
    main()