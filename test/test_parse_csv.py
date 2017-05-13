import datetime
import dobjobs.parse as parser

def test_read_csv():
    assert len(list(parser.read_csv('test/sample.csv'))) == 2

def test_headers():
    assert parser.headers()[0] == 'Job'
    assert parser.headers()[-1] == 'DOBRunDate'
    assert len(parser.headers()) == 82

def test_type_lookup():
    lookup = parser.type_lookup()
    assert isinstance(lookup, dict)
    assert lookup['StreetName'] == 'text'
    assert lookup['LoftBoard'] == 'boolean'
    assert lookup['bbl'] == 'char(10)'

class Test_type_cast_field():
    def test_returns_none(self):
        lookup = parser.type_lookup()
        assert parser.type_cast_field('ApplicantProfessionalTitle', '  ', lookup) is None

    def test_returns_text(self):
        assert parser.type_cast_field('OwnersFirstName', 'bob', parser.type_lookup()) == 'bob'

    def test_returns_integer(self):
        assert parser.type_cast_field('ExistingZoningSqft', '50', parser.type_lookup()) == 50

    def test_returns_money(self):
        assert parser.type_cast_field('InitialCost', '$20.25', parser.type_lookup()) == '20.25'

    def test_returns_boolean(self):
        l = parser.type_lookup()
        assert parser.type_cast_field('VerticalEnlrgmt', 'YES',l) is True
        assert parser.type_cast_field('VerticalEnlrgmt', '', l) is False

    def test_returns_date(self):
        l = parser.type_lookup()
        assert parser.type_cast_field('Paid', '04/25/2013', l) == datetime.date(2013,4,25)

def test_type_cast_row():
    lookup = parser.type_lookup()
    row = {'House': '123', 'LatestActionDate':  '02/03/2017', 'ExistingNoofStories': ' 3 '}
    row_casted = {'House': '123', 'LatestActionDate':  datetime.date(2017,2,3), 'ExistingNoofStories': 3}
    assert parser.type_cast_row(row, lookup) == row_casted


def test_add_bbl():
    data = [{'Borough': 'BROOKLYN', 'Block': '1', 'Lot': '6'}]
    out = list(parser.add_bbl(data))
    assert out == [{'Borough': 'BROOKLYN', 'Block': '1', 'Lot': '6', 'bbl': '3000010006'}]
