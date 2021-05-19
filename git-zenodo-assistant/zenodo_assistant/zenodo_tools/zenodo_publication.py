def pub_options():

    # Tools
    import tkinter as tk
    from termcolor import colored, cprint
    
    # Create window
    root = tk.Tk()
    root.title("Publication options")
    root.geometry('250x200')
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')
    
    # Create the list of publication options
    options_list = ["Annotation collection", "Book", "Book section", "Conference paper", 
                    "Data management plan", "Journal article", "Patent", "Preprint", 
                    "Project deliverable", "Project milestone", "Proposal", "Report", 
                    "Software documentation", "Taxonomic treatment", "Technical note", 
                    "Thesis", "Working paper", "Other"]
    
    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside = tk.StringVar(root)
    
    # Set the default value of the variable
    value_inside.set("Select an Option")
    
    # Create the optionmenu
    question_menu = tk.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    
    # Function to store and print the submitted option
    def pick_pub_type():
        done = colored('Done', 'red')
        global pub_type
        pub_type = value_inside.get()
        print(f"You selected: {pub_type}. Click {done} or change your selection.")
        return 

    # Buttons to print and submit the option and close the window
    submit_button = tk.Button(root, text='Submit',  bg="#B0E0E6", command=pick_pub_type)
    submit_button.pack(padx=15, pady=35)

    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)
    button_done.pack()

    # Generate loop
    root.mainloop()
    
    return pub_type
