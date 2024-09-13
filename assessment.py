#Step 1

# Create a file in the directory that has this file. In the print write you your name and save it.
# Then using this function access the file and print as well as return your name.

def printName(file_name):
   file=open(file_name,'w')
   name='Tumi'
   file.write(name)
#printName('test_name.txt')

def multiplication_pattern(height):
    for i in range(1,height+1):
        for x in range(1,height):
            print(x*i)

  

def number_pyramid(height):
    pass

def triangle(height):
    for i in range(1,height+1):
        print(" "*(height-i)+"*"*(i))


if __name__ == "__main__":
    print("my.txt")  # Replace file.txt with your file
   # multiplication_pattern(4)
    number_pyramid(4)
    triangle(5)