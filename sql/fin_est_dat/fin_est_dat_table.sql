CREATE TABLE IF NOT EXISTS local_state_govt_expenses (
    expense_code char(3),
    county_code char(3),
    state_code char(2),
    pid6_place char(6),
    amount integer,
    year integer,
    PRIMARY KEY(expense_code, pid6_place, year)
);