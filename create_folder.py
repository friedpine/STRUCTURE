import os, sys

new_Path = os.path.join("./", sys.argv[1])
os.mkdir("./"+sys.argv[1])

file_path = os.path.join("./", sys.argv[1], "_infos")
with open(file_path, 'w') as infile:
	infile.write("Successfully!")

print "Create Successfully."