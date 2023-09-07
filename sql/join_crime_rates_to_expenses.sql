SELECT pid6_place,
	   fbi_ucr_known_crimes.city,
	   fbi_ucr_known_crimes.state,
	   fbi_ucr_known_crimes.violent_crime::float*100000/fbi_ucr_known_crimes.population::float AS violent_crime_per_100k,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]62' AND local_state_govt_expenses.year = 2019))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2019))::float*
	   100
	    AS police_expense_curr,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]62' AND local_state_govt_expenses.year = 2018))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2018))::float*
	   100
	    AS police_expense_1,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]62' AND local_state_govt_expenses.year = 2017))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2017))::float*
	   100
	    AS police_expense_2,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]((12)|(16)|(18)|(21))' AND local_state_govt_expenses.year = 2019))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2019))::float*
	   100
	    AS edu_expense_curr,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]((12)|(16)|(18)|(21))' AND local_state_govt_expenses.year = 2018))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2018))::float*
	   100
	    AS edu_expense_1,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]((12)|(16)|(18)|(21))' AND local_state_govt_expenses.year = 2017))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2017))::float*
	   100
	    AS edu_expense_2,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]52' AND local_state_govt_expenses.year = 2019))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2019))::float*
	   100
	    AS lib_expense_curr,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]52' AND local_state_govt_expenses.year = 2018))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2018))::float*
	   100
	    AS lib_expense_1,
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M]52' AND local_state_govt_expenses.year = 2017))::float/
	   (SUM(amount) FILTER (WHERE expense_code ~ '[E-M].*' AND local_state_govt_expenses.year = 2017))::float*
	   100
	    AS lib_expense_2
	FROM local_state_govt_expenses
	INNER JOIN govt_units_info
		ON local_state_govt_expenses.pid6_place = govt_units_info.pid6_id_code
	INNER JOIN fips_state_info
		ON local_state_govt_expenses.state_code = fips_state_info.state_code
	INNER JOIN fbi_ucr_known_crimes
		ON REPLACE(govt_units_info.place_name, ' CITY', '') = UPPER(fbi_ucr_known_crimes.city)
	WHERE UPPER(fips_state_info.state_name) = fbi_ucr_known_crimes.state
	GROUP BY pid6_place,
			 fbi_ucr_known_crimes.state,
			 fbi_ucr_known_crimes.city,
			 fbi_ucr_known_crimes.violent_crime,
			 fbi_ucr_known_crimes.population
	LIMIT 5;