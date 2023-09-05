county_sql_header = """CREATE TABLE IF NOT EXISTS fips_county_info (
    county_code char(3),
    county_name text,
    state_code char(2),
    FOREIGN KEY(state_code) REFERENCES fips_state_info(state_code),
    PRIMARY KEY(state_code, county_code)
);

INSERT INTO fips_county_info (state_code, county_code, county_name)
VALUES
"""

state_sql_header = """CREATE TABLE IF NOT EXISTS fips_state_info (
    state_code char(2) UNIQUE PRIMARY KEY,
    state_name text
);

INSERT INTO fips_state_info (state_code, state_name)
VALUES
"""

def read_geocodes_write_state_county_sql(geocodes_file, output_dir):
    ## Generate .sql code for state + county level information
    with open(geocodes_file, 'r') as raw_geocodes:
        states_sql = open(output_dir + '/2019-fips-states.sql', 'w')
        states_sql.write(state_sql_header)
        counties_sql = open(output_dir + '/2019-fips-counties.sql', 'w')
        counties_sql.write(county_sql_header)
        for line in raw_geocodes.readlines():
            line_data = line.split(',')
            ### If line is for a state
            if line_data[0] == '040':
                states_sql.write("    ('{}', '{}'),\n".format(
                    line_data[1],
                    line_data[6].strip()
                ))
                counties_sql.write("    ('{}', '{}', '{}'),\n".format(
                    line_data[1],
                    line_data[2],
                    line_data[6].strip().replace("'", "''")
                ))
            ### If line is for a county
            if line_data[0] == '050':
                counties_sql.write("    ('{}', '{}', '{}'),\n".format(
                    line_data[1],
                    line_data[2],
                    line_data[6].strip().replace("'", "''")
                ))