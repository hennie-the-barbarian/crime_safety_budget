from census_parse.fin_est_dat_file import *

from pathlib import Path

THIS_DIR = Path(__file__).parent

test_lines = [
    '01000022608519T      2287652020R',
    '010000226085A44        10672020R'
]
test_dict_line_0 = {
    'ID': '010000226085',
    'Item Code': '19T',
    'Amount': 228765,
    'Year of data': '2020',
    'Imputation type/item data flag': 'R'
}
test_dict_all_lines = {
    '010000226085': {
        'ID': '010000226085', 
        'Item Code': 'A44', 
        'Amount': 1067, 
        'Year of data': 
        '2020', 
        'Imputation type/item data flag': 'R'
    }
}

def test_parse_fin_est_dat_lines():
    fin_est_dat_dict = parse_fin_est_dat_lines(test_lines)
    print(fin_est_dat_dict)
    assert(fin_est_dat_dict==test_dict_all_lines)

def test_parse_fin_est_dat_line():
    fin_est_dat_dict = parse_fin_est_dat_line(test_lines[0])
    assert(fin_est_dat_dict==test_dict_line_0)