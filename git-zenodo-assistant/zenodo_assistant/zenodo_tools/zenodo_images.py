def image_options():

    # Tools
    import tkinter as tk
    from termcolor import colored, cprint
    
    # Create window
    root = tk.Tk()
    root.title("Image options")
    root.geometry('250x200')
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')
    
    # List of image options
    options_list = ["Figure", "Plot", "Drawing", "Diagram", "Photo", "Other"]
    
    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside = tk.StringVar(root)
    
    # Set the default value of the variable
    value_inside.set("Select an Option")
    
    # Create the optionmenu
    question_menu = tk.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    
    # Function to get and print the submitted option
    def pick_image_type():
        done = colored('Done', 'red')
        global image_type
        image_type = value_inside.get()
        print(f"You selected: {image_type}. Click {done} or change your selection.")
        return 

    # Create buttons to sumbit the option (print and store) and close the window
    submit_button = tk.Button(root, text='Submit',  bg="#B0E0E6", command=pick_image_type)
    submit_button.pack(padx=15, pady=35)

    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)
    button_done.pack()

    # Generate loop
    root.mainloop()
    
    return image_type
