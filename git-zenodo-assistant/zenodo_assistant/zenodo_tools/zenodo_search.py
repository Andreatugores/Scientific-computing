def filename_input():

    # Tools
    import os
    import tkinter as tk
    from tkinter import filedialog
    from termcolor import colored, cprint

    # Function to open File Browser
    def upload_file():
        done = colored('Done', 'red')
        global path
        global filename
        path = filedialog.askopenfilename()
        filename = os.path.basename(path)
        print(f"You selected: \n"
              f"File: {filename}\n"
              f"Path: {path}\n"
              f"\nClick {done} or change your selection.\n")
        return

    # Create window
    root = tk.Tk()
    root.title("File browser")
    root.geometry("250x60")
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')

    # Buttons to open the File Browser and end loop
    button_explore = tk.Button(root, text="Explore", bg="#B0E0E6", command=upload_file)
    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)

    button_explore.pack(side="top")
    button_done.pack(side="top")

    # Generate loop
    root.mainloop()

    return path, filename
