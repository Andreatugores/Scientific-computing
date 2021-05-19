def path_input():

    # Tools
    import tkinter as tk
    from tkinter import filedialog
    from termcolor import colored, cprint

    # Function to select directory and store path
    def select_dir():
        done = colored('Done', 'red')
        global path
        path = tk.filedialog.askdirectory()
        print(f"Selected directory: {path}\n"
              f"\nClick {done} or change your selection.\n")
        return

    # Creating window
    root = tk.Tk()
    root.title("File browser")
    root.geometry("250x60")
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')

    # Buttons that execute the function and destroy the loop
    button_explore = tk.Button(root, text="Explore", bg="#B0E0E6", command=select_dir)
    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)

    button_explore.pack(side="top")
    button_done.pack(side="top")

    root.mainloop()

    return path
