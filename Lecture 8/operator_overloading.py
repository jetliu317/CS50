class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleions = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f'{self.galleions} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'

    def __add__(self, other):
        galleons = self.galleions + other.galleions
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        
potter = Vault(100, 50, 25)
print(f'potter: {potter}')

weasley = Vault(25, 50, 100)
print(f'weasley: {weasley}')

# galleons = potter.galleions + weasley.galleions
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts

total = potter + weasley
print(f'total: {total}')
