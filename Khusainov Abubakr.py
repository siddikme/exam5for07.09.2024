# ## RULES:
# > No interner, no help to each other!
# > Send the exam to github
# > You have 2 hours only

# ### 1 Question
# Дар бораи рекурсия нависед. 

# Итак рекурсия это функция используюшаяся в питоне! Она предназначена для выполнение определенных действий несколько раз последовательно. Tоесть цикличеки.
# Иными словами это функция которая вызывает себя последовательно несколько раз
# Я так же знаю что раньше вместо цыклов for и while употреблялась рекурсия так те циклы не сушествовали тогда!
# если цикл крутится определеный заданный раз.ТО рекурсия крутится в 2 раза больше.С начала рекурсия занимает места.затем определяет заданные действие 
# solved:


# ### 2 Question
# Closure(Замыкания) - ро бо мисолҳо фаҳмонед.

# Замыкания в Питоне — это концепция, которая позволяет функции запоминать значения переменных из окружающего области видимости даже после того, - 
# как этот контекст больше не существует. 
# Проще говоря, замыкание — это функция, которая "замыкает" переменные из своей внешней функции.
#  
# Например:
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function

# closure = outer_function(10)
# print(closure(5))  

# Здесь outer_function возвращает inner_function, которая использует значение переменной x из outer_function.
# Даже после завершения outer_function, значение x остается доступным внутри inner_function.
# solved:

# ### 3 Question
# Контейнерҳоро ба хотир оварда онҳоро нависед. 

# Список  (List)
# Хранят изменяемую последовательность элементов. Позволяют хранить элементы любого типа, поддерживают индексацию и изменяются.
# Кортежи (Tuple)
# Хранят неизменяемую последовательность элементов. Элементы могут быть любого типа, и они поддерживают индексацию.
# Множества (Set)
# Хранят неупорядоченные уникальные элементы. Не поддерживают индексацию и могут изменяться.
# Словари (Dictionary)
# Хранят пары "ключ-значение". Ключи должны быть уникальными и неизменяемыми, а значения могут быть любыми. Поддерживают быстрый доступ к значениям по ключу.
# solved:



# ### 4 Question
# Дар бораи list, dict comprehension ва args,kwargs нависед.

# List comprehension — это удобный способ создания списков на основе существующих объектов (списков, кортежей и т. д.) 
# с помощью одной строки кода. Это более компактный и читаемый вариант цикла for, который часто используют для данных.
# короче 'comprehension' занимают мало места и позваляет нам не писать один и тот же алгоритм который занимает больше строк 

# В Python *args и **kwargs позволяют передавать переменное количество аргументов в функции:

# *args: Позволяет функции принимать любое количество позиционных аргументов. Аргументы собираются в кортеж.
# Это полезно, когда не знаешь заранее, сколько аргументов передадут функции.

# **kwargs: Позволяет функции принимать любое количество именованных аргументов. 
# Аргументы собираются в словарь. Это полезно, когда не знаешь заранее, какие именованные аргументы будут переданы.
# solved:




# ### 5 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.

# datetime.today()
# Возвращает текущую дату без времени.

# datetime.strptime()
# Преобразует строку в объект даты по заданному формату.Тоесть мы подстраиваем строку под себя и как хотим видеть время 

# datetime.timedelta(days=1)
# Используется для расчёта разницы между датами.

# Модуль random используется для генерации случайных чисел и элементов.

# random.randint(a, b)
# Возвращает случайное целое число в диапазоне от a до b включительно.

# random.choice(sequence)
# Возвращает случайный элемент из списка или последовательности.

# random.shuffle(list) — перемешивает элементы списка случайным образом.

# random.sample(kon, k) — возвращает список из k уникальных элементов, выбранных случайным образом из kon.
# solved:


# ### 1 Task
# Write a Python program that converts currency from one denomination to another.
# Создайте программу, которая конвертирует валюту одного номинала в другой.
# # input
#     Enter the amount in TJS: 1
# # output
#     Rub -> 8.33
#     USD -> 0.094
#     EUR -> 0.084
#     UZ_SUM -> 1000

# amount_tjs = float(input("Enter the amount in TJS: "))

# rates = {
#     "Rub": 8.33,
#     "USD": 0.094,
#     "EUR": 0.084,
#     "UZ_SUM": 1000
# }

# for currency, rate in rates.items():
#     print(f"{currency} -> {amount_tjs * rate:.3f}")
# solved:


# ### 2 Task
# Write a Python program to convert a list of multiple integers into a single integer.
# Напишите программу на Python для преобразования списка из нескольких целых чисел в одно целое число.
# # input
#     Sample list: [11, 33, 50]
# # output
#     Expected Output: 113350


# def genarate(int_list):
#     result = ''
#     for i in int_list:
#         result += str(i)
#     return int(result)


# user_input = input("Enter a list: ")
# int_list = list(map(int, user_input.split()))


# output = genarate(int_list)
# print(output)
# solved:






# ### 3 Task
# Create a closure that concatenates a given string with another string.
# Создайте замыкание, которое объединяет заданную строку с другой строкой.

# # input
#     Tajikistan
# # otput
#     Salom Tajikistan

# def create_greeting(greeting):
#     def concatenate_with_name(name):
#         return f"{greeting} {name}"
#     return concatenate_with_name
# name = str(input("-> "))
# greeting = create_greeting("Salom")
# result = greeting(name)
# print(result)
# solved:



# ### 4 Task
# Write a recursive function to find the minimum element in a list.
# Напишите рекурсивную функцию для поиска минимального элемента в списке.

# # input
#     2 3 54 2 4 0 5 3 2 54
# # output
#     0

# def minimal_rec(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         min_of_rest = minimal_rec(lst[1:])
#         return lst[0] if lst[0] < min_of_rest else min_of_rest

# user_input = input("Enter numbers as a list: ")
# numbers = list(map(int, user_input.split()))
# result = minimal_rec(numbers)
# print(result)
# solved:





# ### 5 Task
# Given a natural number n, compute the sum 1^2+2^2+...+n^2.
# Create a function that takes single natural number n. You need to withdraw the calculated amount. Don’t forget to return the result. Solve this problem using the recursion function.

# Дано натуральное число n, вычислите сумму 1^2+2^2+...+n^2.
# Создайте функцию, которая принимает одно натуральное число n. Вам нужно вывести вычисленную сумму. Не забудьте вернуть результат. Решите эту задачу с помощью функции рекурсии.

# # input
#     n = 2
# # output
#     Expected Output: 5

# def funci(n):
#     if n == 1:
#         return 1
#     else:
#         return n**2 + funci(n - 1)

# n = int(input())
# print(funci(n))
# solved:


# ### 6 Task
# Given a natural number N, find the sum of the numbers 1+1/1!+1/2!+1/3!+...+1/N!. The number of actions should be proportional to N.
# По данному натуральному числу N найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. Количество действий должно быть пропорционально N.
# # input
#     1
# # output
#     2

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# def sum(N):
#     total_sum = 1  
#     for i in range(1, N + 1):
#         total_sum += 1 // factorial(i)
#     return total_sum

# n = int(input())
# print(sum(n))
# solved:



# ### 7 Task
# Write a Python program to replace each character of a word of length five and more with a hash character (#).
# Напишите программу на Python, заменяющую каждый символ слова длиной пять и более символом решетки (#).
# # input
#     Count the lowercase letters in the said list of words:
# # output
#     ##### the ######### ####### in the said list of ######

# def replace_long_words(sentence):
#     words = sentence.split()
#     result = []
#     for word in words:
#         if len(word) >= 5:
#             result.append('#' * len(word))
#         else:
#             result.append(word)
#     return ' '.join(result)

# sentence = input()
# print(replace_long_words(sentence))
# solved:



# ### 8 Task
# Given a natural number N, find the sum of numbers 1+1/1!+1/2!+1/3!+...+1/N!. The number of actions must be proportional to N.
# Create a function that takes a single number N. It is necessary to display the result of the calculation as a real number with an accuracy of 5 decimal places. Don’t forget to return the result.

# Дано натуральное число N, найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. Количество действий должно быть пропорционально N.
# Создайте функцию, которая принимает одно число N. Необходимо вывести результат вычисления в виде действительного числа с точностью до 5 знаков после запятой. Не забудьте вернуть результат.

# # input
#     N = 1
# # output
#     res = 2
   

                                #                                     ^
                                #                                     !
                                #                                     !
                                #Подобная задача уже было решено выше ! Нам было сказана не решать данную задачу!








# ### 9 Task
# Write a Python program for binary search of an ordered list.
# Напишите программу на Python для двоичного поиска в упорядоченном списке.
# # Example
#     Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
#     Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False


# def ordered_binary_search(lst, target):
#     low, high = 0, len(lst) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if lst[mid] == target:
#             return True
#         elif lst[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False

# lst = list(map(int, input("Enter ur elmemnts / then внизу искаемый элемент: ").split()))
# target = int(input("Enter the number to search for: "))

# print(ordered_binary_search(lst, target))
# solved:


# ### 10 Task
# Given a string containing only English letters (upper and lower case). Add opening and closing brackets as follows: "example" -> "e(x(a(m)p)l)e" (Opening brackets are added before the middle, closing brackets are added after the middle. If the string length is even, there should be 2 symbols in the brackets located in the middle. ("card -> c(ar)d", but not "c(a()r)d"). Solve this problem using the recursion function.

# Дана строка, содержащая только английские буквы (большие и маленькие). Добавить открывающиеся и закрывающиеся скобки по следующему образцу: "example" -> "e(x(a(m)p)l)e" (До середины добавлены открывающиеся скобки, после середины – закрывающиеся. В случае, когда длина строки четна в скобках, расположенных в середине, должно быть 2 символа. ("card -> c(ar)d", но не "c(a()r)d"). Решите эту задачу с помощью функции рекурсии.

# # input                           # input
#     hello                           khayriddin
# # output                          # output
#     h(e(l)l)o                       k(h(a(y(ri)d)d)i)n

# def funci(s):
#     if len(s) <= 1:
#         return s
#     mid = len(s) // 2
#     if len(s) % 2 == 0:
#         return s[:mid] + "(" + funci(s[mid:mid+2]) + ")" + funci(s[mid+2:])
#     else:
#         return s[:mid] + "(" + funci(s[mid+1:]) + ")" + s[mid]

# print(funci("hello")) 
# print(funci("khayriddin")) 
# solved:









