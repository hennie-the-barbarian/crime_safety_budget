from census_parse.utils import *

test_state_id = '27'
test_state_info = ('Minnesota', 'MN')
def test_fips_state_id_to_state():
    state_info = fips_state_id_to_state(test_state_id)
    assert(state_info==test_state_info)

test_govt_type = '0'
test_govt_type_info = 'State'
def test_fips_type_to_government_type():
    govt_type_info = fips_type_to_government_type(test_govt_type)
    assert(test_govt_type_info==govt_type_info)

test_id = '272053193551'
test_id_info = {
    'FIPS state': ('Minnesota', 'MN'), 
    'Type': 'City',
    'County or county-type entity': '053', 
    'Unit identifier': '193551'
}
def test_parse_id():
    id_info = parse_id(test_id)
    print(id_info)
    assert(id_info==test_id_info)