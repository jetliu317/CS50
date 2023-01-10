def main():
    n = int(input('What\'s n?'))
    for s in sheep(n):
        print(s)
    # for i in range(n):
    #     print(sheep(i))
        
def sheep(n):
    for i in range(n):
        yield '🐑' * i #(yield is for massive data)
    # return '🐑' * n

if __name__ == '__main__':
    main()