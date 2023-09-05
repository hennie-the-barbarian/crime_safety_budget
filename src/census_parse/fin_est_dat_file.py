import os

def parse_fin_est_dat_file(relative_location):
    with open(relative_location, "r") as fin_est_dat:
        lines = census_file.readlines()
        return(parse_fin_est_dat_lines(lines))

def parse_fin_est_dat_lines(fin_est_dat_lines):
    fin_est_dat_dict = {}
    for line in fin_est_dat_lines:
        line_dict = parse_fin_est_dat_line(line)
        fin_est_dat_dict[line_dict['ID']] = line_dict
    return(fin_est_dat_dict)

def parse_fin_est_dat_line(line):
    fin_est_dat_dict = {}
    fin_est_dat_dict['ID'] = line[0:12]
    fin_est_dat_dict['Item Code'] = line[12:15]
    fin_est_dat_dict['Amount'] = int(line[15:27].strip())
    fin_est_dat_dict['Year of data'] = line[27:31]
    fin_est_dat_dict['Imputation type/item data flag'] = line[31:32]
    return(fin_est_dat_dict)

local_state_govt_expenses_sql_header = """INSERT INTO local_state_govt_expenses (state_code, county_code, pid6_place, expense_code, amount, year)
VALUES
"""

def write_fin_est_dat_sql_table_to_file(filename):
    local_state_govt_expenses_sql_table = """CREATE TABLE IF NOT EXISTS local_state_govt_expenses (
    expense_code char(3),
    county_code char(3),
    state_code char(2),
    pid6_place char(6),
    amount integer,
    year integer,
    PRIMARY KEY(expense_code, pid6_place, year)
);"""

    with open(filename, 'w') as sql_out:
        sql_out.write(local_state_govt_expenses_sql_table)

def write_fin_est_dat_sql_entry_to_file(entry_data, opened_file):
    if entry_data != {}:
        fin_est_dat_sql_stub = "    ('{state_code}', {county_code}, '{pid6_place}', " + \
            "'{expense_code}', '{amount}', {year})"
        opened_file.write(
            fin_est_dat_sql_stub.format(
                state_code = entry_data['state_code'],
                county_code = entry_data['county_code'],
                pid6_place = entry_data['pid6_place'],
                expense_code = entry_data['expense_code'],
                amount = entry_data['amount'],
                year = entry_data['year']
            )
        )

def fin_est_dat_line_to_dict(line):
    entry_data = {}
    ## Pre-2017 has a different format that I'm not wanting to fuck with right now.
    if line[2] != "0":
        entry_data['state_code'] = line[:2].strip()
        entry_data['county_code'] = "'{}'".format(line[3:6].strip()) if entry_data['state_code'] != '09' else 'Null'
        entry_data['pid6_place'] = line[6:12]
        entry_data['expense_code'] = line[12:15]
        entry_data['amount'] = int(line[15:27])
        entry_data['year'] = int(line[27:31])
    return(entry_data)

def read_fin_est_dat_files_write_sql(fin_est_dat_directory, sql_out_dir):
    for filename in os.listdir(fin_est_dat_directory):
        file_to_open = "{}/{}.sql".format(sql_out_dir, filename)
        with open(file_to_open, 'w') as fin_est_dat_sql:
            fin_est_dat_sql.write("""INSERT INTO local_state_govt_expenses (state_code, county_code, pid6_place, expense_code, amount, year)
VALUES
""")
            with open(fin_est_dat_directory + "/" + filename, 'r') as fin_est_dat_txt:
                expense_lines = fin_est_dat_txt.readlines()
                first_line = expense_lines[0]
                entry_data = fin_est_dat_line_to_dict(first_line)
                write_fin_est_dat_sql_entry_to_file(entry_data, fin_est_dat_sql)
                for expense in expense_lines[1:]:
                    entry_data = fin_est_dat_line_to_dict(expense)
                    if entry_data != {}:
                        fin_est_dat_sql.write(',\n')
                    write_fin_est_dat_sql_entry_to_file(entry_data, fin_est_dat_sql)