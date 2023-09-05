in_file = open("census_pid_test_data.txt", "r")
out_file = open("sampled_census_pid.txt", "w")

lines = in_file.readlines()
out_lines = lines[::1700]
out_file.write("".join(out_lines))