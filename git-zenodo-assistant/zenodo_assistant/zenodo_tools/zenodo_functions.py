
# Title function
def type_title():

    from termcolor import cprint, colored
    enter = colored('Enter', 'cyan')

    title = input(str("Type the title of your work: "))
    print(f"\nCheck the title: {title}")
    title_answer = input(str("\nIs the title correct? (y/n): "))

    # Change the title
    while title_answer not in ("y", "yes", "YES"):

        if title_answer in ("n", "no", "NO"):
            title = input(str("\nPlease, type the title of your work again: "))
            print(f"\nCheck the title: {title}")
            title_answer = input(str("\nIs the title correct? (y/n): "))
        else:
            print(f"\nInvalid option. Check the title: {title}")
            title_answer = input(str("\nIs the title correct? (y/n): "))
    
    # Store the title as variable
    if title_answer in ("y", "yes", "YES"):
        input(f"\nThe title has been stored. Press {enter} to continue.\n")
        
    return title

# Description function
def type_description():

    from termcolor import cprint, colored
    enter = colored('Enter', 'cyan')

    description = input(str("Type or paste the description of your work: "))
    print(f"\nCheck the description:\n{description}")
    description_answer = input(str("\nIs the description correct? (y/n): "))
    
    # Change description
    while description_answer not in ("y", "yes", "YES"):

        if description_answer in ("n", "no", "NO"):
            description = input(str("\nPlease, type or paste the description  of your work again: "))
            print(f"\nCheck the description:\n{description}")
            description_answer = input(str("\nIs the description correct? (y/n): "))
        else:
            print(f"\nInvalid option. Check the description:\n{description}")
            description_answer = input(str("\nIs the description correct? (y/n): "))

    # Store description as variable       
    if description_answer in ("y", "yes", "YES"):
        input(f"\nThe description has been stored. Press {enter} to continue.\n")
    
    return description


# Creators function
def creators_dict():

    from termcolor import cprint, colored
    enter = colored('Enter', 'cyan')

    # Create array
    creators = []
    
    # Add creator 
    author_i = input(str("Type the name of the author (format: Ramos, Maria): "))
    affiliation_i = input(str("\nType their affiliation: "))
    creator_i = author_check(author_i, affiliation_i)
    creators.append(creator_i)
    input(f"\nThe author's information has been stored. Press {enter} to continue.\n")
    
    # Add more creators
    creators_answer = input(str("Do you want to add another author? (y/n): "))
    
    while creators_answer not in ("n", "no", "NO"):

        if creators_answer in ("y", "yes", "YES"):
            author_i = input(str("\nType the name of the author (format: Ramos, Maria): "))
            affiliation_i = input(str("\nType their affiliation: "))
            creator_i = author_check(author_i, affiliation_i)
            creators.append(creator_i)
            input(f"\nThe author's information has been stored. Press {enter} to continue.\n")
            creators_answer = input(str("Do you want to add another author? (y/n): "))
        else: 
            creators_answer = input(str("Invalid option. Do you want to add another author? (y/n): "))
    
    # Stop adding authors
    if creators_answer in ("n", "no", "NO"):
        print("\nThe creators data has been stored.\n")
        
    return creators

# Check author's information 
def author_check(author_i, affiliation_i):
    
    print(f"\nCheck the author's information:\n"
          f"Name: {author_i}\n"
          f"Affiliation: {affiliation_i}")
    author_answer = input(str("\nIs the information correct? (y/n): "))

    # Change the author's information   
    while author_answer not in ("y", "yes", "YES"):

        if author_answer in ("n", "no", "NO"):
            author_i = input(str("\nPlease, type the name of the author again (format: Ramos, Maria): "))
            affiliation_i = input(str("\nType their affiliation: "))
            print(f"\nCheck the author's information:\n"
                  f"Name: {author_i}\n"
                  f"Affiliation: {affiliation_i}")
            author_answer = input(str("\nIs the information correct? (y/n): "))
        else:
            print(f"\nInvalid option. Check the author's information:\n"
                  f"Name: {author_i}\n"
                  f"Affiliation: {affiliation_i}")
            author_answer = input(str("\nIs the information correct? (y/n): "))
    
    # Store the author's information as a dictionary to add in the array
    if author_answer in ("y", "yes", "YES"):
        creator_i = {'name': f'{author_i}',
                     'affiliation': f'{affiliation_i}'}

    return creator_i



