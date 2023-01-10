def main():
    n = int(input('What\'s n?'))
    for s in sheep(n):
        print(s)
    # for i in range(n):
    #     print(sheep(i))
        
def sheep(n):
    flock = []
    for i in range(n):
        flock.append('🐑'* i)
    return flock
    # return '🐑' * n

if __name__ == '__main__':
    main()