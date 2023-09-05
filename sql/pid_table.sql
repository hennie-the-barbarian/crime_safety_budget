CREATE TABLE IF NOT EXISTS govt_units_info (
    pid6_id_code char(6) UNIQUE PRIMARY KEY,
    place_name text,
    fips_place_code char(5),
    population int,
    county_code char(3),
    state_code char(2)
);