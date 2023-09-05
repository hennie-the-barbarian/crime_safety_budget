in_file = open("census_fin_est_dat_test_data.txt", "r")
out_file = open("sampled_census_fin_est_dat.txt", "w")

lines = in_file.readlines()
out_lines = lines[::40000]
print(len(out_lines))
out_file.write("".join(out_lines))