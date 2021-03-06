#!/usr/bin/python3

"""
	How to use this script?
	Prepare a user list file containing firstname<space>lastname
	Run: python3 user_generate.py user_list.txt
	The script now generated a new user format
"""

import sys

# read users from a txt file
users = sys.argv[1]

with open(users, 'r') as file:
	name = file.read()
name = name.split('\n')

all_users = []

# transform user format
for n in name:
	fname = n.split(' ')[0].lower()
	lname = n.split(' ')[1].lower()

	# concatinate first and last name
	all_users.append(fname + lname)

	# add period between 1st and last name
	all_users.append(fname + '.' + lname)

	# first name initial then concatenate last name
	all_users.append(fname[0] + lname)

	# first name initial, period then last name
	all_users.append(fname[0] + '.' + lname)

# write new generated usersto a new file
with open('generated_users.txt', 'w') as file:
	file.writelines("%s\n" % user for user in all_users)
