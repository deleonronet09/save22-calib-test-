def add(input1,input2):
  return input1+input2
  
def subtract(input1,input2):
  return input1-input2
  
def multiply(input1,input2):
  return input1*input2
  
def divide(input1,input2):
  return input1/input2
  
def operator(num1,op,num2):
<<<<<<< HEAD
  functions = {'+':add, '-':subtract, '*':multiply, '/':divide}
  func = functions.get(op, None)
  if num1 == None or num2 == None:
    return None
  elif op == "/" and num2 == 0:
    return '{} can not be {} by {}'.format(num1,op,num2)
  else:
    if func:
      return func(num1,num2)
    return None
    
def input1(input=input):
  input1 = input("Enter first number: ")
  if isinstance(input1,int):
    return input1
  elif not isinstance(input1,int):
    if input1.isdigit():
      return int(input1)
  else:
    return None
  
def input2(input=input):
  input2 = input("Enter first number: ")
  if isinstance(input2,int):
    return input2
  elif not isinstance(input2,int):
    if input2.isdigit():
      return int(input2)
  else:
    return None

def inputop(input=input):
  return input("Enter operation: ")
  
def output(num1,op,num2,ans):
  if num1 == None or num2 == None or ans == None:
    return "You must input an integer."
  elif op == "/" and num2 == 0:
    return '{} can not be {} by {}'.format(num1,op,num2)
  else:
    return '{} {} {} = {}'.format(num1,op,num2,ans)
=======
  if op == '+':
    return add(num1,num2)
  elif op == '-':
    return subtract(num1,num2)
  elif op == '*':
    return multiply(num1,num2)
  elif op == '/':
    return divide(num1,num2)
  else:
    return None 
    
def input1():
  return int(raw_input("Enter first number: "))
  
def input2():
  return int(raw_input("Enter second number: "))

def inputop():
  return raw_input("Enter operation: ")
  
def output(num1,op,num2,ans):
  return '{} {} {} = {}'.format(num1,op,num2,ans)
>>>>>>> b423a7cf35c64cce351780af90892118efc61cfc

def main():
  num1 = input1()
  op = inputop()
  num2 = input2()
  ans = operator(num1,op,num2)
<<<<<<< HEAD
  print(output(num1,op,num2,ans))
  
if __name__ == "__main__":
    main()
=======
  print output(num1,op,num2,ans)
  
main()
  
  
>>>>>>> b423a7cf35c64cce351780af90892118efc61cfc
