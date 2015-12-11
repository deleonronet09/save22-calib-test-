def add(input1,input2):
  return input1+input2
  
def subtract(input1,input2):
  return input1-input2
  
def multiply(input1,input2):
  return input1*input2
  
def divide(input1,input2):
  return input1/input2
  
def operator(num1,op,num2):
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

def main():
  num1 = input1()
  op = inputop()
  num2 = input2()
  ans = operator(num1,op,num2)
  print output(num1,op,num2,ans)
  
main()
  
  