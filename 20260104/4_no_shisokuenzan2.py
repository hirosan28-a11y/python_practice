def add_calc(a,b):1
    return a + b

def sub_calc(a,b):
    return a - b

def mul_calc(a,b):
    return a * b

def div_calc(a,b):
    return a / b
 
calc_list = {add_calc, sub_calc, mul_calc, div_calc}

for calc_func1 in calc_list:
    for calc_func2 in calc_list:
        result1 = calc_func2(4, 4)    
        result2 = calc_func2(result,4)