SELECT * FROM local_state_govt_expenses
	FULL JOIN govt_units_info
	ON local_state_govt_expenses.pid6_place = govt_units_info.pid6_id_code
	FULL JOIN fips_state_info
	ON local_state_govt_expenses.state_code = fips_state_info.state_code
	FULL JOIN fbi_ucr_known_crimes
	ON REPLACE(govt_units_info.place_name, ' CITY', '') = UPPER(fbi_ucr_known_crimes.city)
	AND UPPER(fips_state_info.state_name) = fbi_ucr_known_crimes.state
	WHERE pid6_place = '193551'
	AND expense_code LIKE '%62'
	AND local_state_govt_expenses.year <= 2019;