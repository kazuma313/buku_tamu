import re

regex_pattern = re.compile(r'\b08\d{10}\b')
teks = "082343023442"
nomor_hp = regex_pattern.search(teks)

print(nomor_hp.group(0))