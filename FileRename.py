import os

for filename in os.listdir("."):
	if filename[0].isdigit():
		c = '_'
		n=1
		words = filename.split(c)
		temp_name = c.join(words[:n]), c.join(words[n:])
		os.rename(filename, (temp_name[1][:-4] + '_' + temp_name[0] + '.pdf'))

