file=open("dumm12.txt","w")
file.write("Add new line")
file.writelines(["line number 1\n,
                 "line number 2\n,"])

file.close()