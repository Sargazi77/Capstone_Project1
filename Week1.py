from datetime import date
def main():
    name = input('What is your name?')
    name = name.upper() #converts the name to all uppercase
    
    month = input('What is your birthday month?(type it in full format)')
    new_month = month.title() # converts the month to first charector upper case to make the program not so user can enter all lower case 
    classes = input('what classes are you taking this semester? (seprate them by using ",") ')
    splited = classes.split(',')
    classes_list = []
    for i in splited:
        classes_list.append(i)
    calculate = calculateMonth(name, new_month) # calls the calculateMonth function
    print('You are taking these classes:')
    for j in classes_list :
        print(j)
   

def calculateMonth(name, new_month):
    now = date.today()
    text_month = now.strftime('%B') # %B gives the month of the full today date format
    #  converts the month to lower case to make the program not to be case sensetive
    print('Welcome '+ name)
    print('There are ' + str(len(name)) + ' letters in your name') # len() counts the number of letter and since python cannot put int and strings together we have to use str() function to convert the int to string
    print('new month is '+ new_month)
    print('new text month is '+ text_month)
    if new_month == text_month:
        print('Happy Birthday month!')
    else:
        print("Your birthday is in "+ new_month)    
    return text_month       

main()
    