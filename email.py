import random
import string

list_of_domain = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
length_of_email = 15

letters = string.ascii_lowercase

all_email = []
for cap in list_of_domain:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length_of_email))
        email = random_string + '@' + cap
        my_file = open('./out_generate-random_email_with_List_of_domain.txt', 'w')
        my_file.write(email)
        all_email.append(email)

my_file = open('./output_email.txt', 'w')
my_file.write(str('\n'.join(all_email)))
print("DONE!")
my_file.close()




