def zenodo_review():

    # Tools
    import tkinter as tk
    import tkinter.ttk

    # Messages for windows

    message0 = """
    Zenodo is a website where you can upload and publish files,
    funded by CERN, OpenAIRE and the EU.\n
    It is built and developed by researchers who want to
    promote Open Science and welcome research from all nations
    and disciplines, to help scientific work to be more
    shareable and citeable.\n
    Currently, all meta data is openly available under CC0 licence, 
    and all open content is openly accessible through open APIs.\n
    """

    message1 = """
    You can upload many types of files to Zenodo: publications, posters,
    presentations, datasets, images, videos, audios, softwares, lessons, 
    all research outputs from all fields of science are welcome, and 
    they are currently accepting up to 50GB per dataset!.\n
    When your files are ready, you can publish them, so they will be 
    permanently available on the Internet: your work will be stored 
    safely and it will be easier to cite, discover, share, considering
    flexible licensing (although Zenodo encourages you to share your 
    research as openly as possible).
    """

    message2 = """
    A DOI (Digital Object Identifier) is a unique string of numbers, letters,
    and symbols used to identify objects (like your scientific publication).\n
    DOIs are standardized and assigned by a registration agency.\n
    Zenodo supports DOI versioning by providing your published work 
    two DOIs, allowing you to:
    -Edit/update the record’s files after they have been published.
    -Cite a specific version of a record.
    -Cite all of versions of a record.\n
    This makes your work easier to identify, search and cite.
    """

    message3 = """
    Metadata is a set of data that contains information about other data.\n
    While uploading a file to Zenodo, and before you publish it in the
    website, you have to provide important data about your file, like its
    title, creators, and type, which represents its metadata.\n
    Not only this is a requirement of Zenodo, but it is very useful: it 
    helps to describe your work, making it easier to find and identify, 
    and it also makes it more accesible, by using a standard format and
    vocabulary.
    """

    # Creating window
    root = tk.Tk()
    root.title("Review of Zenodo")
    root.geometry("260x220")
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')
    label = tk.Label(root, text ="Select an option and\n review some concepts")
    label.pack(pady = 10)

  
    # Open window functions
    def open_window_0():
      
        window_0 = tk.Toplevel(root)
        window_0.title("About Zenodo")
        window_0.geometry("420x300")
        window_0.config(background = "#F5F5F5")
        # Texts
        title = tk.Label(window_0, text ="\n\nWhat is Zenodo?", bg= "#F5F5F5").pack()
        text = tk.Label(window_0, text =message0, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()

        return

    def open_window_1():
      
        window_1 = tk.Toplevel(root)
        window_1.title("Zenodo's repository")
        window_1.geometry("460x300")
        window_1.config(background = "#F5F5F5")
        title = tk.Label(window_1, text ="\n\nUploading and publishing", bg= "#F5F5F5").pack()
        text = tk.Label(window_1, text = message1, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()

        return

    def open_window_2():

        window_2 = tk.Toplevel(root)
        window_2.title("DOI Versioning in Zenodo")
        window_2.geometry("465x300")
        window_2.config(background = "#F5F5F5")
        title = tk.Label(window_2, text ="\n\nWhat is DOI Versioning?", bg= "#F5F5F5").pack()
        text = tk.Label(window_2, text =message2, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()
        return

    def open_window_3():
      
        window_3 = tk.Toplevel(root)
        window_3.title("Zenodo's metadata")
        window_3.geometry("460x250")
        window_3.config(background = "#F5F5F5")
        title = tk.Label(window_3, text ="\n\nWhat is metadata?", bg= "#F5F5F5").pack()
        text = tk.Label(window_3, text =message3, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()
        return
  
    # Buttons that open windows and destroy the root window.

    button_0 = tk.Button(root, text ="What is Zenodo?",  bg="#B0E0E6", command=open_window_0)
    button_0.pack(side="top")

    button_1 = tk.Button(root, text= "Uploading and publishing", bg="#B0E0E6", command=open_window_1)
    button_1.pack(side="top")

    button_2 = tk.Button(root, text= "What is DOI Versioning?", bg="#B0E0E6", command=open_window_2)
    button_2.pack(side="top")

    button_3 = tk.Button(root, text ="What is metadata?",  bg="#B0E0E6", command=open_window_3)
    button_3.pack(side="top")

    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)
    button_done.pack(side="bottom")

    # mainloop, runs infinitely, unless root.destroy
    root.mainloop()

    return
