records = {'Bruce Dickinson':48,'Ronnie James Dio':51,'SU-METAL':12,'Rob Halford':30,'James Hetfield':37,'Roy Khan':18,'Corey Taylor':24,'Ozzy Osbourne':60,'M. Shadows':29,'Michael Kiske':43}

def funcAge(x):
  return x[1]
  
def funcName(x):
  return x[0]
  
def lambdaAge(x):
  return sorted(records.items(), key=lambda val:val[1])
  
def lambdaName(x):
  return sorted(records.items(), key=lambda val:val[0])
  
choice = input('Input from 1 to 4: ')

if choice == 1:
  for item in sorted(records.items(), key=funcAge):
    print item
elif choice == 2:
  for item in sorted(records.items(), key=funcName):
    print item
elif choice == 3:
  for item in lambdaAge(records):
    print item
elif choice == 4:
  for item in lambdaName(records):
    print item