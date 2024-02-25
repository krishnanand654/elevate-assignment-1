def run(n):
    try:
        x = 10/n
        return x
    except ZeroDivisionError:
        print(f'Error:{ZeroDivisionError}\n Cannot perform Division by zero')
        return 0
    finally:
        print("this is test1")
        print("this is test2")
        print("this is test3")
    
print(run(10))  

