from translate import Translator

def Language(Language1, Language2):

    if Language1 == "England".lower() and Language2 == "persian".lower() :
        user = input("Please Your Text (England): ")
        options = Translator(from_lang="en", to_lang="persian")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "persian".lower() and Language2 == "England".lower():
        user = input("Please Your Text (persian): ")
        options = Translator(from_lang="persian", to_lang="en")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "persian".lower() and Language2 == "French".lower():
        user = input("Please Your Text (persian): ")
        options = Translator(from_lang="persian", to_lang="French")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "French".lower() and Language2 == "persian".lower():
        user = input("Please Your Text (French): ")
        options = Translator(from_lang="French", to_lang="persian")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "England".lower() and Language2 == "French".lower():
        user = input("Please Your Text (England):")
        options = Translator(from_lang="en", to_lang="French")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "French".lower() and Language2 == "England".lower():
        user = input("Please Your Text (French): ")
        options = Translator(from_lang="French", to_lang="en")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "German".lower() and Language2 == "England".lower():
        user = input("Please Your Text (German):")
        options = Translator(from_lang="German", to_lang="en")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "England".lower() and Language2 == "German".lower():
        user = input("Please Your Text (England):")
        options = Translator(from_lang="en", to_lang="German")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "German".lower() and Language2 == "persian".lower():
        user = input("Please Your Text (German):")
        options = Translator(from_lang="German", to_lang="persian")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "persian".lower() and Language2 == "German".lower():
        user = input("Please Your Text (persian):")
        options = Translator(from_lang="persian", to_lang="German")
        translate = options.translate(user)
        print(translate)
    elif Language1 == "German".lower() and Language2 == "French".lower():
        user = input("Please Your Text (German):")
        options = Translator(from_lang="German",to_lang="French")
        translate = options.translate(user)
        print(translate) 
    elif Language1 == "French".lower() and Language2 == "German".lower():
        user = input("Please Your Text (French):")
        options = Translator(from_lang="French", to_lang="German")
        translate = options.translate(user)
        print(translate)
    else:
        print("Erorr")

    

Ln1 = input("from language : ")
Ln2 = input("to language : ")
Language(Ln1, Ln2)