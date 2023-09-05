from enum import Enum

## add code to load the county fips csv outside of function

def fips_county_to_county(fips_county):
    pass

def fips_type_to_government_type(fips_type):
    government_type_dict = {
        '0': 'State',
        '1': 'County',
        '2': 'City',
        '3': 'Township',
        '4': 'Special District',
        '5': 'Independent School District or Educational Service Agency',
    }
    return(government_type_dict[fips_type])

def fips_state_id_to_state(state_id):
    state_id_dict = {
        '00': ('United States', 'US'),
        '01': ('Alabama', 'AL'),
        '02': ('Alaska', 'AK'),
        '04': ('Arizona', 'AZ'),
        '05': ('Arkansas', 'AR'),
        '06': ('California', 'CA'),
        '08': ('Colorado', 'CO'),
        '09': ('Connecticut', 'CT'),
        '10': ('Delaware', 'DE'),
        '11': ('District of Columbia', 'DC'),
        '12': ('Florida', 'FL'),
        '13': ('Georgia', 'GA'),
        '15': ('Hawaii', 'HI'),
        '16': ('Idaho', 'ID'),
        '17': ('Illinois', 'IL'),
        '18': ('Indiana', 'IN'),
        '19': ('Iowa', 'IA'),
        '20': ('Kansas', 'KS'),
        '21': ('Kentucky', 'KY'),
        '22': ('Louisiana', 'LA'),
        '23': ('Maine', 'ME'),
        '24': ('Maryland', 'MD'),
        '25': ('Massachusetts', 'MA'),
        '26': ('Michigan', 'MI'),
        '27': ('Minnesota', 'MN'),
        '28': ('Mississippi', 'MS'),
        '29': ('Missouri', 'MO'),
        '30': ('Montana', 'MT'),
        '31': ('Nebraska', 'NE'),
        '32': ('Nevada', 'NV'),
        '33': ('New Hampshire', 'NH'),
        '34': ('New Jersey', 'NJ'),
        '35': ('New Mexico', 'NM'),
        '36': ('New York', 'NY'),
        '37': ('North Carolina', 'NC'),
        '38': ('North Dakota', 'ND'),
        '39': ('Ohio', 'OH'),
        '40': ('Oklahoma', 'OK'),
        '41': ('Oregon', 'OR'),
        '42': ('Pennsylvania', 'PA'),
        '44': ('Rhode Island', 'RI'),
        '45': ('South Carolina', 'SC'),
        '46': ('South Dakota', 'SD'),
        '47': ('Tennessee', 'TN'),
        '48': ('Texas', 'TX'),
        '49': ('Utah', 'UT'),
        '50': ('Vermont', 'VT'),
        '51': ('Virginia', 'VA'),
        '53': ('Washington', 'WA'),
        '54': ('West Virginia', 'WV'),
        '55': ('Wisconsin', 'WI'),
        '56': ('Wyoming', 'WY')
    }
    return state_id_dict[state_id]

def parse_id(id):
    id_info = {}
    id_info['FIPS state'] = fips_state_id_to_state(id[:2])
    id_info['Type'] = fips_type_to_government_type(id[2:3])
    id_info['County or county-type entity'] = id[3:6]
    id_info['Unit identifier'] = id[6:12]
    return id_info