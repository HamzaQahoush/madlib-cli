import re



def read_template(root):
    """
    read a file from a root 
    give an exception if it not found 

    """
    try:
      with open (root , "r") as file:
        content=file.read().strip()
        return content

    except FileNotFoundError:
        raise FileNotFoundError('The file not found')    
      
    except Exception as a :
        return (f"Error {a}")

   


def parse_template (text):
    
    """
    • here after we read a file we need to analysis it content.
    • origin_value finds all text inside { } from file and store them in array.
    •  the for loop replace all values above in the text with empty string {} in the text file.
    then we have an text and array.
    """
    index=0
    origin_value=re.findall(r"\{(.*?)\}", text)  

    for i in origin_value:
        text= text.replace(origin_value[index], "",1)
        index+=1
    return text, tuple(origin_value)






def merge(text,origin_value):
    # print(text.format(*origin_value)) 
    updatedText= text.format(*origin_value)
    print(updatedText)

    with open('assets/make_me_a_video_game_output.txt','w') as output:
        output.write(updatedText)

    return updatedText    
  

    # just merging data using .format we used * to destruct tha array and publish it on {}
   

    

   
def result( text,origin_value):
    input_user=[]

    for i in origin_value:
        input_user.append(input(f"enter an { i} "))  #take the variable in bracket as question to user depends on the origin values .
   
    return merge(text,input_user)   



if __name__ == "__main__":

 print("""
 Welcome to Madlib Game 😉
You will enjoy playing with us 😎
""")
 reading_template=read_template('assets/make_me_a_video_game_template.txt')
 parse_template (reading_template)
 text,origin_value=parse_template (reading_template)
 result( text, origin_value)  


 







