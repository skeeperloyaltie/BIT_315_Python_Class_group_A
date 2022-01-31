# Logical operators

# program sample


citizenship = "KENYAN"


def check():
    user_citizenship = str(input("Enter your citizenship: "))
    age = int(input("Enter your age: "))
    if user_citizenship == citizenship and age >= 18:
        print("Kenyan Citizen and age to vote")
    elif user_citizenship == citizenship and age <= 17:
        print("Check your age. You still a kiddo")
    elif user_citizenship != citizenship and age >= 18:
        print("You not kenyan. You cannot be here. ")
    elif user_citizenship != citizenship and age <= 17:
        print("Get out of here")
    else:
        print("We dont know you")
        
if __name__ == '__main__':
    def main():
        print(check())  
    main()
                
        