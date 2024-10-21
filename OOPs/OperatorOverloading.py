# We can use the same operator for multiple purposes, which is nothing but operator overloading. 

# print(1+2)
# print("1"+"2")
# print("Shubham"+ "Kumar")
# print("Shubham"*3)
# print("5" *3)


# Using + operator for our class object:

# class Book:
#     def __init__(self,pages):
#         self.pages = pages

# b1 = Book(100)
# b2 = Book(200)

# print(b1+b2)



class Book:
    def __init__(self,pages):
        self.pages = pages
        
    # Magic method __add__ to add pages of two books    
    def __add__(self, other):
        return self.pages + other.pages
    
b1 = Book(100)
b2 = Book(200)

print(b1+b2)