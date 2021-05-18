import os
import time
from termcolor import colored, cprint

def start_git():
    answer = input(f"\nPress any key to start the {c_Git} Tutorial.\n"
                   "\nPress x to take you back to the main menu.")
    if answer in ("x", "X"):
        print(f"\nGoing back to main menu...\n")
        time.sleep(2)
        return
    else:
        print(f"\nStarting {c_Git} Tutorial...\n")
        time.sleep(2)
        os.system("clear")
        from git_assistant import git_tutorial
        os.system("clear")
        input("Press any key to take you back to the main menu.\n")
        print(f"Going back to main menu...\n")
        time.sleep(2)
        return

# Start zenodo tutorial
def start_zenodo():
    answer = input(f"\nPress any key to start the {c_Zenodo} Assistant.\n"
                   "\nPress x to take you back to the main menu.")
    if answer in ("x", "X"):
        print(f"\nGoing back to main menu...\n")
        time.sleep(2)
    else:
        print(f"\nStarting {c_Zenodo} Assistant...\n")
        time.sleep(2)
        os.system("clear")
        from zenodo_assistant import zenodo_tutorial
        os.system("clear")
        input("Press any key to take you back to the main menu.\n")
        print(f"Going back to main menu...\n")
        time.sleep(2)
        return

# Access Git Documentation
def about_git():
    print(f"\nTo learn more about {c_Git}:\n\n"
          f"Github: https://github.com/ \n"
          f"Gitlab: https://about.gitlab.com/ \n"
          f"Documentation: https://docs.github.com/en \n")
    input("Press any key to take you back to the main menu.\n")
    print(f"Going back to main menu...\n")
    time.sleep(2)
    return

# Access Zenodo Documentation
def about_zenodo():
    print(f"\nTo learn more about {c_Zenodo}:\n\n"
          "Zenodo: https://zenodo.org/ \n"
          "Zenodo REST API: https://developers.zenodo.org/ \n")
    input("Press any key to take you back to the main menu.\n")
    print(f"Going back to main menu...\n")
    time.sleep(2)
    return

c_assistant = colored("Git&Zenodo Assistant", "cyan")
c_atlas = colored("ATLAS Virtual Machine", "cyan")
c_Git = colored("Git", "cyan")
c_Github = colored("GitHub", "cyan")
c_Gitlab = colored("GitLab", "cyan")
c_Zenodo = colored("Zenodo", "cyan")
c_README = colored("README.md", "cyan")
c_test = colored("test_tutorial", "cyan")
c_NOTE = colored("NOTE", "cyan", attrs=["reverse"])


# Welcome message
main_message = f"""
\nWelcome to your {c_assistant}.\n
I will help you to start your journey in Open Science by uploading 
your own files created in the {c_atlas} to your {c_Git} account 
and/or {c_Zenodo} account.\n
If you do not have already an account in {c_Github}, {c_Gitlab} or 
{c_Zenodo}, consult the documentation, where you can find links 
to their respective websites.\n
                          {c_NOTE}\n
**Please, read the {c_README} file before starting the assistant,
you will find helpful information in there** \n
**If you are only testing this program, the {c_test} folder
contains a text file you can use to try the {c_Git} push and the
{c_Zenodo} upload.**
"""
print(main_message)


input("Press any key to start the main menu...\n")
print(f"Starting main menu...\n")
time.sleep(2)

# Main Menu
str_menu = ("Do you wish to:\n"
            f"a) Upload a file to your {c_Git} repository?\n"
            f"b) Upload a file to your {c_Zenodo} account?\n"
            f"c) Consult the {c_Git} Documentation\n"
            f"d) Consult the {c_Zenodo} Documentation\n"
            "e) Exit\n")
print(str_menu)
menu = input(str())

while menu != "e" and menu != "E":
    if menu in ("a", "A"):
        start_git()
        print(str_menu)
        menu = input(str())
    elif menu in ("b", "B"):
        start_zenodo()
        print(str_menu)
        menu = input(str())
    elif menu in ("c", "C"):
        about_git()
        print(str_menu)
        menu = input(str())
    elif menu in ("d", "D"):
        about_zenodo()
        print(str_menu)
        menu = input(str())
    else:
        print("\nSorry, that was not a valid option. "
              "Check again and choose a valid option\n")
        print(str_menu)
        menu = input(str())
if menu in ("e", "E"):
    print("\nOk, see you later. Keep researching!\n")
