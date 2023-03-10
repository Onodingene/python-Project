sample_file = './sample_file/wikepedia.txt'

my_file = open(sample_file, 'r')
content = my_file.read()
my_file.close()
print(content)

