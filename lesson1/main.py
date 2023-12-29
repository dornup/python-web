# # Декораторы
# def twice(func):
#     def wrapper():
#         func()
#         func()
#     return wrapper

# @twice
# def greet():
#     print('hello')

# print(greet())

# def uppercase(func):
#     def wrapper():
#         original = func()
#         modified = original.upper()
#         return modified
#     return wrapper

# @uppercase
# def greet():
#     return 'hello'
    
# print(greet())


