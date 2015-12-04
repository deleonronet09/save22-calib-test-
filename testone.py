i=0
first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']
full_names = []

while i != len(first_names):
  full_names.append(first_names[i]+" "+last_names[i])
  i+=1

print(full_names)