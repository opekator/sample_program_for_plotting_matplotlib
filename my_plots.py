import numpy as np
import matplotlib.pyplot as plt


def sub_func_1(x, n):
    x = abs(x)
    while x > (1/2) * (pow(4, -n + 1)):
        x -= (pow(4, -n + 1))
        x = abs(x)
    return ((pow(4, n - 1)*x)/(pow(4, n - 1)))
    
def func_1(x):
    n = 1
    y = 0
    while n <= 3:
        y += sub_func_1(x, n)
        n += 1
    return y

def func_2(x):
    if x == 0:  return 0
    else:  return pow(x, 2) * np.sin(1 / x)

def func_pr_2(x):
    if x == 0:  return 0
    else:  return 2 * x * np.sin(1 / x) - np.cos(1 / x)

def func_3(x):
    if x < 0: return -1
    elif x > 0: return 1
    else:  return 0

def func_4(x):
    if x == 0: return 0
    else: return pow(x, 4) * (2 + np.sin(1 / x))

def func_pr_4(x):
    if x == 0: return 0
    else: return pow(x, 2) * (4 * x * (2 + np.sin(1 / x)) - np.cos(1 / x))

def func_5(x):
    if x == 0:  return 0
    else: return x + 2 * pow(x, 2) * np.sin(1/x)

def func_pr_5(x):
    if x == 0: return 1
    else: return 1 + 4 * x * np.sin(1/x) - 2 * np.cos(1/x)

def func_6(x):
    if x == 0: return 0
    else: return pow(x, 2) * np.sin(1/pow(x, 2))

def func_pr_6(x):
    if x == 0: return 0
    else: return 2 * x * np.sin(1/pow(x, 2)) - (2/x) * np.cos(1/pow(x, 2))

def func_7(x):
    if x == 0: return 0
    else:
        return pow(x, 4) * pow(np.e,-(1/4)*pow(x,2) ) * np.sin(8/pow(x, 3))

def func_pr_7(x):
    if x == 0: return 0
    else:
        return pow(np.e, -(pow(x, 2)/4))*((4*pow(x, 3)-(pow(x, 5)/2))*np.sin(8/pow(x, 3))-24*np.cos(8/pow(x, 3)))

def draw():

    fig, ax = plt.subplots()
    
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    
    #ax.setylim(-2000, 2000)
    
    num_func = input("Номер функции: ")
    func = None
    
    if num_func == "1":
        if "1" == input("Частичная сумма(0) или отдельная функция(1)?: "):
            n = int(input("n = "))
            
            range_plot = float(input("Длина промежутка с центром 0: "))
    
            x = np.linspace(-range_plot, range_plot, 200001)
    
            y = list(map(sub_func_1, x, [n]*len(x)))
    
            plt.grid() 
            plt.plot(x, y)
            plt.show()
            return
        else:
            func = func_1
            
    elif num_func == "2":
        if "1" == input("Производная?(0/1): "):
            func = func_pr_2
        else: func = func_2
    elif num_func == "3":
        
        x_minus = np.linspace(-2, 0, 100)
        x_plus = np.linspace(0, 2, 100)
        
        y_minus = [-1]*len(x_minus)
        y_plus = [1]*len(x_plus)
        
        plt.grid()
        plt.plot(x_minus, y_minus, c='b')
        plt.plot(x_plus, y_plus, c='b')
        plt.scatter(0,0, s = 50)
        
        plt.show()
        return
        
    elif num_func == "4":
        if "1" == input("Производная?(0/1): "):
            func = func_pr_4
        else: func = func_4
    elif num_func == "5":
        if "1" == input("Производная?(0/1): "):
            func = func_pr_5
        else: func = func_5
    elif num_func == "6":
        if "1" == input("Производная?(0/1): "):
            func = func_pr_6
        else: func = func_6
    elif num_func == "7":
        if "1" == input("Производная?(0/1): "):
            func = func_pr_7
        else: func = func_7
    else:
        print("Такой функции нет")
        return
    
    range_plot = float(input("Длина промежутка с центром 0: "))
    
    x = np.linspace(-range_plot, range_plot, 200001)
    
    y = list(map(func, x))
    
    plt.grid() 
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    while True:
        draw()