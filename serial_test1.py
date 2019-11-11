import test


con = test.open_console()
test.run_command(con)
test.run_command(con, 'sh version')
output = test.read_from_console(con)
print(output)