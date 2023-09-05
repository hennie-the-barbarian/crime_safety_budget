import os

def parse_census_place_id_file(relative_location):
    with open(relative_location, "r") as census_file:
        lines = census_file.readlines()
        return(parse_census_place_id_lines(lines))

def parse_census_place_id_lines(pid_lines):
    pid_dict = {}
    for line in pid_lines:
        line_dict = parse_census_place_id_line(line)
        pid_dict[line_dict['ID']] = line_dict
    return(pid_dict)

def parse_census_place_id_line(pid_string):
    pid_dict = {}
    pid_dict['ID'] = pid_string[0:12]
    pid_dict['Name'] = pid_string[12:76].strip()
    pid_dict['County'] = county = pid_string[76:111].strip()
    pid_dict['FIPS Place Code'] = pid_string[111:116].strip()

    population = pid_string[116:125].strip()
    pid_dict['Population'] = int(population) if population else 0
    pid_dict['Population Year'] = pid_string[125:127]

    enrollment = pid_string[127:134].strip()
    pid_dict['Enrollment'] = int(enrollment) if enrollment else 0
    pid_dict['Enrollment Year'] = pid_string[134:136].strip()
    pid_dict['School Level Code'] = pid_string[138:140].strip()

    pid_dict['Funciton Code for Special Districts'] = pid_string[136:138].strip()
    pid_dict['Fiscal Year Ending'] = pid_string[140:144].strip()
    pid_dict['Survey Year'] = pid_string[144:146].strip()
    return(pid_dict)

def write_pid_sql_table_to_file(filename):
    govt_units_sql_create_table = """CREATE TABLE IF NOT EXISTS govt_units_info (
    pid6_id_code char(6) UNIQUE PRIMARY KEY,
    place_name text,
    fips_place_code char(5),
    population int,
    county_code char(3),
    state_code char(2)
);"""

    with open(filename, 'w') as sql_out:
        sql_out.write(govt_units_sql_create_table)

def write_pid_sql_entry_to_file(entry_data, opened_file):
    govt_units_sql_stub = "    ('{state_code}', {county_code}, '{pid6_id_code}', '{fips_place_code}', '{place_name}', '{population}'),\n"
    opened_file.write(
        govt_units_sql_stub.format(
            state_code=entry_data['state_code'], 
            county_code=entry_data['county_code'],
            pid6_id_code=entry_data['pid6'],
            fips_place_code=entry_data['fips_place_code'],
            place_name=entry_data['place_name'].replace("'", "''"),
            population=entry_data['population']
        )
    )

def pid_line_to_dict(pid_line):
    entry_data = {}
    entry_data['state_code'] = pid_line[:2]
    entry_data['county_code'] = entry_data['state_code'].strip()
    entry_data['pid6'] = pid_line[6:12]
    entry_data['place_name'] = pid_line[12:76].strip()
    entry_data['fips_place_code'] = pid_line[111:116]
    population = pid_line[116:125].strip()
    entry_data['population'] = int(population) if population else 0
    return(entry_data)

def read_pid_files_write_sql(pid_directory, sql_out):
    with open(sql_out, 'w') as govt_units_sql:
        govt_units_sql.write("""INSERT INTO govt_units_info (state_code, county_code, pid6_id_code, fips_place_code, place_name, population)
VALUES
""")
        found_govt_units = {}
        for filename in os.listdir(pid_directory):
            with open(pid_directory + "/" + filename, 'r') as govt_units_txt:
                for govt_unit in govt_units_txt.readlines():
                    entry_data = pid_line_to_dict(govt_unit)
                    if entry_data['pid6'] not in found_govt_units:
                        write_pid_sql_entry_to_file(entry_data, govt_units_sql)
                        found_govt_units[entry_data['pid6']] = entry_data['place_name']