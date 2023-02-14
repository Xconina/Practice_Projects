# parameters
```python
def greet_with_name(name):
     print(f"Hello {name}")

 greet_with_name("ash")
 # parameter = argument


 def greet_with(name, location):
    
```
# print vs return
```python
return- what if want to pass to other function. it stores the info instead of just printing
in calculator: 

```
# recursion = function calls itself
```python
def calculator():
    num1 = int(input("What is the first number:\n"))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Please pick an operation from above:\n")
        num2 = int(input("What is the next number?\n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation\n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
      

  ### runs program until reaches end point. if function recalled, it finds the calculator() function and calls, restarting
  need to be careful-- if call calculator in calculator function without a condition to be met, will continue forever

```