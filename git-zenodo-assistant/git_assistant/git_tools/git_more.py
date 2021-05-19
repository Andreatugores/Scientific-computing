def git_review():

    # Tools
    import tkinter as tk
    import tkinter.ttk

    # Messages for windows

    message0 = """
    Git is more than a website, Git is a control version software, which is
    a software made for tracking changes in any set of files in a directory. 
    Managing changes of your documents, data, notebooks and coding 
    scripts is essential when you do research.\n
    As you probably have learned by now, just copying your files and 
    renaming them as "myProjectUpdateFinalTrueFinalPrint.ipynb" is not the    
    most efficient way to do so. Git makes it easier by providing an online 
    plataform for Version Control of personal and collaborative projects. 
    """

    message1 = """
    The Git software stores and save files to a directory called repository,
    also shorten as repo. A Git repository allows various operations to create   
    different versions of the files in it.\n
    A Git repository can be local (placed in your computer) or remote 
    (hosted on the Internet, or in a different server).\n
    By installing git to your computer, and creating a GitHub or GitLab
    account you can start your Version Control with git.
    """

    message2 = """
    From Github or Gitlab you can Fork and Clone repositories.\n
    A git fork is an operation of copying a repository to your git account.\n
    A git clone is an operation of copying a repository to your local machine.\n
    Maybe you knew all of this already. In fact, you probably have this program 
    running because you did a git clone to your computer (or Virtual Machine, 
    for that matter).\n
    One more thing before you continue: remember than you can only push to git   
    repositories where you have permissions to do so. If you need to clone a 
    repo that you do not own and need to make changes, fork the repo first and 
    then you can clone it.
    """

    message3 = """
    You can obtain a Git repository by either cloning a Git repository
    or by converting a local directory to a Git repository, using git init.   \n
    It does not matter if the directory is a new local directory, or an
    already existent local directory, the command git init works in 
    both cases.\n
    And you can also git init a git repository, is it safe to do so, 
    it will not overwrite files that are already there.
    """

    message4 = """
    Git push is an operation to publish new local commits on a remote server.\n
    When you want to update your changes (could be a new file in the directory,
    or a change in an already existing file)to your Git account, you need to git
    push.\n
    But before a git push, you have to git add (to add your new or modified
    files to your git repo), git commit (to save these changes) and then you
    can execute your git push command.\n
    There could be more commands that you need to execute before a git push. 
    This is only a basic review, and although the tutorial will include some new 
    steps. You can learn more in the documentation and you should.
    """

    message5 = """
    While Git push allows you to publish local commits on a remote server, the 
    git pull command lets you update the local version with the new commits 
    saved on the remote server. It is the most common way to update a repository   
    and you should use it everytime that you interact with the remote server.\n
    Note that this tutorial does not include how to git pull although it is being 
    considered for future versions. If you need to git pull, we recommend to 
    consult the documentation available in the repository and the program.
    """
    
    # Creating window
    root = tk.Tk()
    root.title("Review of Git")
    root.geometry("250x280")
    root.config(background = "#F5F5F5")
    root.eval('tk::PlaceWindow . center')
    label = tk.Label(root, text ="Select an option and\n review some concepts")
    label.pack(pady = 10)

  
    # Open window functions
    def open_window_0():
      
        window_0 = tk.Toplevel(root)
        window_0.title("Git and Version Control")
        window_0.geometry("510x250")
        window_0.config(background = "#F5F5F5")
        # Texts
        title = tk.Label(window_0, text ="\n\nWhat is Git?", bg= "#F5F5F5").pack()
        text = tk.Label(window_0, text =message0, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()

        return

    def open_window_1():
      
        window_1 = tk.Toplevel(root)
        window_1.title("Git Repository")
        window_1.geometry("500x280")
        window_1.config(background = "#F5F5F5")
        title = tk.Label(window_1, text ="\n\nWhat is a Git repository?", bg= "#F5F5F5").pack()
        text = tk.Label(window_1, text = message1, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()

        return

    def open_window_2():
      
        window_2 = tk.Toplevel(root)
        window_2.title("git fork/git clone")
        window_2.geometry("525x350")
        window_2.config(background = "#F5F5F5")
        title = tk.Label(window_2, text ="\n\nWhat does a git fork/git clone do?", bg= "#F5F5F5").pack()
        text = tk.Label(window_2, text =message2, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()

    def open_window_3():

        window_3 = tk.Toplevel(root)
        window_3.title("git init")
        window_3.geometry("460x260")
        window_3.config(background = "#F5F5F5")
        title = tk.Label(window_3, text ="\n\nWhat does a git init do?", bg= "#F5F5F5").pack()
        text = tk.Label(window_3, text =message3, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()
        return

    def open_window_4():
      
        window_4 = tk.Toplevel(root)
        window_4.title("git add/git commit/git push")
        window_4.geometry("510x320")
        window_4.config(background = "#F5F5F5")
        title = tk.Label(window_4, text ="\n\nGit push and the previous steps", bg= "#F5F5F5").pack()
        text = tk.Label(window_4, text =message4, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()
        return
    
    def open_window_5():
      
        window_5 = tk.Toplevel(root)
        window_5.title("git pull")
        window_5.geometry("530x250")
        window_5.config(background = "#F5F5F5")
        title = tk.Label(window_5, text ="\n\nWhat does a git pull do?", bg= "#F5F5F5").pack()
        text = tk.Label(window_5, text =message5, bg= "#F5F5F5", anchor="e", justify="left", width=100).pack()
        return
  
    # Buttons that open windows and destroy the root window.

    button_0 = tk.Button(root, text ="Git and Version Control",  bg="#B0E0E6", command=open_window_0)
    button_0.pack(side="top")

    button_1 = tk.Button(root, text= "Git Repository", bg="#B0E0E6", command=open_window_1)
    button_1.pack(side="top")

    button_2 = tk.Button(root, text= "git fork/git clone", bg="#B0E0E6", command=open_window_2)
    button_2.pack(side="top")

    button_3 = tk.Button(root, text ="git init",  bg="#B0E0E6", command=open_window_3)
    button_3.pack(side="top")

    button_4 = tk.Button(root, text= "git add/git commit/git push", bg="#B0E0E6", command=open_window_4)
    button_4.pack(side="top")
    
    button_5 = tk.Button(root, text= "git pull", bg="#B0E0E6", command=open_window_5)
    button_5.pack(side="top")

    button_done = tk.Button(root, text = "Done", bg="#FF6347", command=root.destroy)
    button_done.pack(side="bottom")

    # mainloop, runs infinitely, unless root.destroy
    root.mainloop()

    return
