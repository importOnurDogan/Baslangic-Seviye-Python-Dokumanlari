# Baska dosyalarfdan verinin alinip kullanilmasi.
"""
with open('dosya1.rtf', 'r') as dosya:
    dosya.read()"""

"""dosya=("dosya1.rtf","r")
print(dosya.read())"""

"""with open('dosya1.rtf',"r") as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()"""

counter_dict = {}
with open('dosya1.rtf',"r") as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
