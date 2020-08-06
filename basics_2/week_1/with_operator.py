## WITH EXAMPLE

# file handling 
  
# 1) without using with statement 
file = open('file_path', 'w') 
file.write('hello world !') 
file.close() 
  
# 2) without using with statement 
file = open('file_path', 'w') 
try: 
    file.write('hello world') 
finally: 
    file.close() 
 

filter_none
brightness_4
# using with statement 
with open('file_path', 'w') as file: 
    file.write('hello world !') 


#
#  To use with statement in user defined objects you only need to 
#   add the methods __enter__() and __exit__() in the object methods. 
#   Consider the following example for further clarification.
#
#


# a simple file writer object 
  
class MessageWriter(object): 
    def __init__(self, file_name): 
        self.file_name = file_name 
      
    def __enter__(self): 
        self.file = open(self.file_name, 'w') 
        return self.file
  
    def __exit__(self): 
        self.file.close() 
  
# using with statement with MessageWriter 
  
with MessageWriter('my_file.txt') as xfile: 
    xfile.write('hello world') 