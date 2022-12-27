from test import get_fraction

def main():
    test_fraction()
    
def test_fraction():
    assert get_fraction('4/4') == 'FULL'
    assert get_fraction('1/2') == '50%'
    assert get_fraction('3/4') == '75%'
    assert get_fraction('2/4') == '50%'
    assert get_fraction('0/4') == 'EMPTY'
        
if __name__ == '__main__':
    main()