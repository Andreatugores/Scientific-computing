def date_input():

    # Tools
    import tkinter as tk
    from tkcalendar import Calendar, DateEntry
    from termcolor import colored, cprint

    # Function to open calendar and get date
    def select_date():
        done = colored('Done', 'red')
        global pub_date_input
        pub_date_input = cal.selection_get()
        print(f"You selected: {pub_date_input}. Click {done} or change your selection.")
        return

    # Create window
    root= tk.Tk()
    root.title("Calendar")
    root.geometry("250x250")
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')

    # Generate Calendar
    cal= Calendar(root, selectmode="day",year= 2021, month=5, day=10, cursor="hand1")
    cal.pack(fill="both", expand=True)
    
    # Create Buttons
    button_date= tk.Button(root, text= "Select the Date", bg="#B0E0E6", command=select_date)
    button_date.pack(side="top")

    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)
    button_done.pack(side="bottom")

    # Generate loop
    selected_date = None
    root.mainloop()
    
    return pub_date_input
