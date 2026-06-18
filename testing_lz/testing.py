from func import func

def test(a, b, c, d, f):
    try:
        res = func(a, b, c, d, f)  
        print(f"a={a}, b={b}, c={c}, d={d}, f={f}\nРезультат: {res}")
        return res
    except ZeroDivisionError: 
        print(f"a={a}, b={b}, c={c}, d={d}, f={f}\nОшибка: деление на ноль")
        return 'деление на ноль'
    except TypeError: 
        print(f"a={a}, b={b}, c={c}, d={d}, f={f}\nОшибка: ошибка типов данных")
        return 'ошибка типов данных'
    except ValueError: 
        print(f"a={a}, b={b}, c={c}, d={d}, f={f}\nОшибка: корень из отрицательного числа")
        return 'корень из отрицательного числа'
    except Exception as exc:
        print(f"a={a}, b={b}, c={c}, d={d}, f={f}\nНеизвестная ошибка: {exc}")
        return f'неизвестная ошибка: {exc}'

if __name__ == '__main__': 
    print('Ручное тестирование')
    #Позитивный тест (целые числа) 
    test(2, 3, 5, 3, 4)  
    #Позитивный тест (дробные числа)
    test(1.5, 2.5, 4.0, 2.0, 0.25)
    #тест подкоренное выражение f равно нулю
    test(1, 1, 3, 1, 0)
    #Тестирование ZeroDivisionError (c - d = 0)
    test(5, 5, 2, 2, 9)  
    #Тестирование ValueError (f = -4, отрицательное под корнем)
    test(4, 2, 5, 1, -4)  
    #Тестирование TypeError (строка вместо числа)
    test('2', 3, 5, 3, 4)  
    #Тестирование TypeError (комплексное число)
    test(2, 3, 5, 3, complex(4, 1))  
    print('Конец тестирования')
