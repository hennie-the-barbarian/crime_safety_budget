from census_parse.pid_file import *
from census_parse.fin_est_dat_file import *
from census_parse.state_county_file import *
from fbi_ucr.parse_known_crimes import *

'''
read_pid_files_write_sql('data/census_fips_codes/fin_pid', 'sql/pid_entries.sql')
write_pid_sql_table_to_file('sql/pid_table.sql')

write_fin_est_dat_sql_table_to_file('sql/fin_est_dat/fin_est_dat_table.sql')
read_fin_est_dat_files_write_sql('data/census_fips_codes/fin_est_dat', 'sql/fin_est_dat')

read_geocodes_write_state_county_sql('data/census_fips_codes/2019-geocodes-raw.csv', 'sql')
'''

known_crimes_write_sql_table('sql/fbi_ucr/known_crimes_table.sql')
read_known_crimes_csv_write_sql('data/fbi_ucr/fbi_ucr_known_crimes_2019.csv', 'sql/fbi_ucr/known_crimes.sql')