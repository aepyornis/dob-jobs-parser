import dobjobs.bbl as bbl

def test_boro_to_code():
    assert bbl.boro_to_code('MANHATTAN') == '1'
    assert bbl.boro_to_code('BRONX') == '2'
    assert bbl.boro_to_code('   BROOKLYN   ') == '3'
    assert bbl.boro_to_code('NOWHERE') == '0'

def test_bbl():
    assert bbl.bbl('QUEENS', '870', '12') == '4008700012'
