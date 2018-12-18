# Automation learning
# This scrip creates 10 folders and the 
# additional 10 subfolders in each foler using 'while' loops.

import os

i = 1
j = 1
k = 1


print(os.getcwd())

while (i <= 10):
	os.mkdir('a'+ str(i))
	i = i + 1

i = 1

while (j <= 10):
	os.chdir('a' + str(i))
	while (k <= 10):
		os.mkdir('b' + str(k))
		k = k + 1
	os.chdir('..')
	j = j + 1
	i = i + 1
	k = 1

