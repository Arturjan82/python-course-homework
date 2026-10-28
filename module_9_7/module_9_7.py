# coding= utf-8
def is_prime(func):
    def wrapper(*args):
        result_func = func(*args)
        if result_func >= 1:
            delitel = 1
            for i in range(1, int(result_func/2)+1):
                if result_func % i == 0:
                    delitel += 1
            if delitel == 2:
                print('Простое')
            else:
                print('Составное')
        else:
            print('Составное')
        return result_func
    return wrapper
    

@is_prime
def sum_three(a,b,c):
    return a+b+c


result = sum_three(1,3,0)
print(result)