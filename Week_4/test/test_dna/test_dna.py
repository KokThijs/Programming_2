from bin.dna import DNA
import pytest
initial = 'ACTGACTGACTFG'
dna = DNA(initial)

def test_dna():
    obj = DNA()
    assert type(obj) == DNA


def test_create_with_nucleotides():
    obj = DNA('ACTG')
    assert type(obj) == DNA


def test_invalid_nucleotide():
    with pytest.raises(ValueError) as p_err:
        obj = DNA('QCTG')


def test_invalid_nucleotide_type():
    with pytest.raises(TypeError) as p_err:
        obj = DNA(3.14)


def test_not_a_multiple_of_three():
    with pytest.raises() as p_err:
        obj = DNA('TG')


def test_dna_string_representation():
    obj = DNA('ACTGACTGACGT')
    assert str(obj) == 'ACTGACTGACGT'


def test_add_triplet_to_object():
    obj = DNA('ACTGACTGACGT')
    assert str(obj) + 'CTG' == 'ACTGACTGACGTCTG'


def test_iteration():
    obj = DNA('ACTGACTGACGT')
    codons = [obj.dna[i:i+3] for i in range(0, len(obj.dna), 3)]
    for i, codon in enumerate(obj):
        assert codon == codons[i]


def test_immutability():
    obj = DNA('ACTGACTGACGT')
    obj_id = id(obj)
    n_obj = obj + 'ACTGTG'
    assert obj_id != id(n_obj)
    assert str(obj) == 'ACTGACTGACGT'