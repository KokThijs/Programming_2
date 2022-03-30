class DNA():
    valid_nucs = ['A', 'C', 'T', 'G']
    def __init__(self, nucleotides):
        self.check_params(nucleotides)

        self.nucleotides = nucleotides


    def check_params(self, nucleotides):
        if not isinstance(nucleotides, str) == str:
            raise TypeError(f'{nucleotides} is not a string')
        
        if len(nucleotides) % 3 != 0:
            raise ValueError(f'{nucleotides} is not a multiple of three')
        
        for nucleo in nucleotides:
            if not nucleo in self.valid_nucs:
                raise ValueError(f'{nucleo} is not a valid nucleotide')
        self.nucleotides = nucleotides


    def __str__(self):
        return self.nucleotides
    

    def __repr__(self):
        return self.__str__()
    

    def __add__(self, triplet):
        return DNA(self.nucleotides + triplet)
    

    def __iter__(self):
        return self.get_triplet()


    def get_triplet(self):
        for i in range(0, len(self.nucleotides), 3):
            yield self.dna[i:i+3]

    
