import random
def array_defination(Array):
    for i in range(len(Array)):
        Array[i] = random.randint(0,99)

def arrays_comparison(Array_1, Array_2):
    count = 0
    massiv_c = ["Пусто"] * max(len(Array_1), len(Array_2))

    #Проверка на совпадения в массивах и на запрет использования одного элемента 2 раза
    for x in range(len(Array_1)):
        for y in range(len(Array_2)):
            if Array_1[x] == Array_2[y]:
                massiv_c[count] = Array_2[y] 
                count +=1
                Array_2[y] = "Использованный элемент"
                break

    if massiv_c[0] != "Пусто":
        print("Совпавшие элементы:")
        for element_c in massiv_c:
            if element_c != "Пусто":
                print(element_c)
    else:
        print("Совпавших элементов нет")

try:
    print("Введите коливество элементов для массива A:")
    kolvo_elementov_a = int(input())
    print("Введите коливество элементов для массива B:")
    kolvo_elementov_b = int(input())

    massiv_a = ["Пусто"] * kolvo_elementov_a
    massiv_b = ["Пусто"] * kolvo_elementov_b
    

    
    array_defination(massiv_a) #Использование функции для определения двух массивов, чтобы не писать алгоритм 2 раза
    array_defination(massiv_b)


    print("Массив А:")
    print(massiv_a)

    print("Массив B:")
    print(massiv_b)

    arrays_comparison(massiv_a,massiv_b)

except ValueError:
    print("Введите целое число в качестве значения коливества элементов массива")
    quit()