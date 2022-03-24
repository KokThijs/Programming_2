from bin.dna import DNA

dna = DNA('ACTGACTGACTFG')

def test_actg():
    assert 'ACTG' in dna.nucleotides