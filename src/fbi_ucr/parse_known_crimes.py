import csv

def known_crimes_write_sql_table(sql_file):
    known_crimes_sql_table = """CREATE TABLE IF NOT EXISTS fbi_ucr_known_crimes (
    state text,
    city text,
    population int,
    violent_crime int,
    murder int,
    rape int,
    robbery int,
    aggravated_assault int,
    property_crime int,
    burglary int,
    larceny_theft int,
    motor_vehicle_theft int,
    arson int,
    year int
);"""
    with open(sql_file, "w") as sql_out:
        sql_out.write(known_crimes_sql_table)

def read_known_crimes_csv_write_sql(known_crimes_file, sql_file):
    known_crimes_sql_header = "INSERT INTO fbi_ucr_known_crimes " + \
        "(state, city, population, violent_crime, murder, rape, robbery, aggravated_assault, " + \
        "property_crime, burglary, larceny_theft, motor_vehicle_theft, arson, year)\n" + \
        "VALUES\n"

    known_crime_sql_template = "    ({state}, {city}, {population}, {violent_crime},  " + \
        "{murder}, {rape}, {robbery}, {aggravated_assault}, {property_crime}, {burglary}, " + \
        "{larceny_theft}, {motor_vehicle_theft}, {arson}, {year}),\n"
    with open(sql_file, "w") as sql_file_out:
        sql_file_out.write(known_crimes_sql_header)
        with open(known_crimes_file) as known_crimes:
            known_crimes_csv = csv.DictReader(known_crimes)
            for city_data in known_crimes_csv:
                city_data['city'] = "'{}'".format(city_data['city'].replace("'", "''"))
                city_data['state'] = "'{}'".format(city_data['state'])
                sql_file_out.write(known_crime_sql_template.format(**city_data, year=2019))
