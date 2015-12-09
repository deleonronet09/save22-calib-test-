def add(input1,input2):
  return input1+input2
  
def subtract(input1,input2):
  return input1-input2
  
def multiply(input1,input2):
  return input1*input2
  
def divide(input1,input2):
  return input1/input2
  
def operand():
  print '\n'
  print "a. ADDITION (+)"
  print "b. SUBTRACTION (-)"
  print "c. MULTIPLICATION (*)"
  print "d. DIVISION (/)"
  operand = raw_input("Choose operation to be performed: ")
  return operand
  
def main():
  while 1:
    input1 = input("Enter 1st number: ")
    input2 = input("Enter 2nd number: ")

    if operand() == 'a':
      print "The result of {} added by {} is {}".format(input1,input2,add(input1,input2))
    elif operand() == 'b':
      print "The result of {} subtracted by {} is {}".format(input1,input2,subtract(input1,input2))
    elif operand() == 'c':
      print "The result of {} multiplied by {} is {}".format(input1,input2,multiply(input1,input2))
    elif operand() == 'd':
      print "The result of {} divided by {} is {}".format(input1,input2,divide(input1,input2))
    else:
      print "Choose only from the operand choices."
    
main()