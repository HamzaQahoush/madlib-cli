import re

print("""
Welcome to Madlib Game 😉
You will enjoy playing with us 😎
""")


def read_template(root):
    """
    read a file from a root 
    give an exception if it not found 

    """
    try:
      with open (root , "r") as file:
        content=file.read().strip()
        return content

    except Exception as a :
        print (f"Error {a}")

   


def parse_template (text):
    
    """
    • here after we read a file we need to analysis it content.
    • origin_value finds all text inside { } from file and store them in array.
    •  the for loop replace all values above in the text with empty string {} in the text file.
    then we have an text and array.
    """
    counter=0
    origin_value=re.findall(r"\{(.*?)\}", text)  

    for i in origin_value:
        text= text.replace(origin_value[counter], "",1)
        counter+=1
    return text, origin_value 



parse_template (read_template('../assets/In_video_game.txt'))
reading_template=read_template('../assets/In_video_game.txt')

text,origin_value=parse_template (reading_template)


def merge(text,origin_value):
    print(text.format(*origin_value))   # specified value(s) and insert them inside the string's placeholder..
    return  text.format(*origin_value)
    
    
merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
   
def result( text,origin_value):
    input_user=[]

    for i in origin_value:
        input_user.append(input(f"enter an { i} "))  #take the variable in bracket as question to user depends on th
    print (text.format(*input_user)) 
    return text.format(*input_user)   

result( text, origin_value)  

# print(parse_template (read_template('../assets/In_video_game.txt')))     






