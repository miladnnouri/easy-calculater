#### add
def add (x,y):
    return x + y
#### subtract
def subtract (x , y):
    return x - y
#### multiply\
def multiply (x , y):
    return x * y
#### divide 
def divide (x , y):
    if  y ==0:
        return("Error! ")
    else:
        return x / y
    

def calculater():
    print("Select Opaaration ")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    
    while True:
        Choice = input("Enter Choices (1/2/3/4): ")

        if Choice in ['1','2','3','4']:
            num1=float(input("Enter The First Number :"))
            num2=float(input("Enter The Secend Number :"))

            if Choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
                
            if Choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")

            if Choice == '3':
                print(f"{num1} * {num2} = {multiply(num1,num2)}")

            if Choice == '4':
                print(f"{num1} / {num2} = {divide(num1,num2)}")

            next_calculation = input("Do You Want to Perform another calculation ? (Yes/No):")
            if next_calculation.lower()  != 'yes' :
                 break

    print("Exiting calculater.goodbye !")
calculater()             
                
 


