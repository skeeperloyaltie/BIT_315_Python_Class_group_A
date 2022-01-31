# Logical operators

# program sample


citizenship = "KENYAN"


class logical:
    
    def check_and():
        user_citizenship = str(input("Enter your citizenship: ").upper())
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
        
    def check_or():
        pass
if __name__ == '__main__':
    def main():
        print(logical.check_and())  
    main()
                    
        