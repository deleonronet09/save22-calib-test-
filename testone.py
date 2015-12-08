first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']

full_names = ['{} {}'.format(fname,last_names[i]) for i,fname in enumerate(first_names)]

print(full_names)