from test import shorten

def main():
    test_shorten()
    
def test_shorten():
    assert shorten('sweet') == 'swt'
    

if __name__ == '__main__':
    main()
    

