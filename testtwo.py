full_names = ['Nobita Nobi', 'Shizuka Minamoto', 'Takeshi Goda', 'Suneo Honekawa']
first_names = []
last_names = []

for names in full_names:
  fname,lname = names.split()
  first_names.append(fname)
  last_names.append(lname)
 
print(first_names) 
print(last_names)