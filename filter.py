# Used to filter and format Shuttle data (from NASA:
# http://archive.ics.uci.edu/ml/datasets/Statlog+%28Shuttle%29)
# which will be fed to C5.0/See5

def simplify(string_list, file):
	attr1 = string_list[0][:-1] # Excludes the last character

	attr2 = int(string_list[1])
	if attr2 == 0:
		attr2 = "0"
	elif attr2 < 0:
		attr2 = "negative"
	else:
		attr2 = "positive"

	attr3 = string_list[2][:-1]
	
	attr4 = int(string_list[3])
	if attr4 == 0:
		attr4 = "0"
	else:
		attr4 = "negative"

	target = string_list[-1]

	file.write('{},{},{},{},{}\n'.format(attr1, attr2, attr3, attr4, target))

	return

# Main
read_from = input('File to read from: ')
write_to = input('File to write to: ')
partition = input('Specify partition? (Y/N): ')

f = open(read_from, 'r')
fo = open(write_to, 'w')

if partition.upper() == "Y":
	# Partition version
	c1_req = int(input('Number of class 1 instances: '))
	c4_req = int(input('Number of class 4 instances: '))
	c1_count = 0
	c4_count = 0

	for line in f: # Python recognises lines in a file object
		splits_list = line.split()

		if splits_list[-1] == "1" and c1_count < c1_req:
			simplify(splits_list, fo)
			c1_count += 1
		elif splits_list[-1] == "4" and c4_count < c4_req:
			simplify(splits_list, fo)
			c4_count += 1
else:
	# Non-partition version
	total_req = int(input('Total number of instances: '))
	total_count = 0

	for line in f:
		splits_list = f.readline().split()

		if (splits_list[-1] == "1" or splits_list[-1] == "4") and total_count < total_req:
			simplify(splits_list, fo)
			total_count += 1

f.close()
fo.close()