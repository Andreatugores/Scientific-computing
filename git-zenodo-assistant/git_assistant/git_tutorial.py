# Tools
import os
import time
from termcolor import colored, cprint
from git_assistant.git_tools.git_search import path_input
from git_assistant.git_tools.git_more import git_review

# Hello world

git = colored('Git', 'cyan')
enter = colored('Enter', 'cyan')
init = colored('init', 'cyan')
fork = colored('fork', 'cyan')
clone = colored('clone', 'cyan')
add = colored('add', 'cyan')
allfiles = colored('--all', 'cyan')
log = colored('log', 'cyan')
commit = colored('commit', 'cyan')
push = colored('push', 'cyan')
remote = colored('remote add origin', 'cyan')
select = colored('Select', 'cyan')
submit = colored('Submit', 'cyan')
explore = colored('Explore', 'cyan')
done = colored('Done', 'red')
password = colored('password', 'cyan')
token = colored('token', 'cyan')
gitlab = colored('GitLab', 'cyan')
github = colored('GitHub', 'cyan')
green = colored('Green', 'green')
red = colored('Red', 'red')
copy = colored("COPY", "green", attrs=['reverse'])
paste = colored("PASTE", "green", attrs=['reverse'])

welcome_message = f"""
Hello! Welcome to this {git} tutorial, where you will upload a file to 
your {git} remote repository, and learn some basic commands of git to 
type them in the terminal the next time, without using this program.\n
Here, you will have to paste the URL of your {git} repository, provide the name 
of the file you want to upload, a commit message and finally, your username and
password/token. You will not execute the commands yourself, the programm will do it 
for you.
"""

print(welcome_message)
input(f"When you are ready, press {enter} to start and learn about {git}.")

more_message = f"""
This tutorial is not intented to teach you ALL about git, but to help
you to {git} {add}, {git} {commit} and {git} {push} a file to your git 
repository by teaching some important things along the way.\n
You do not have to understand it all by the end, altough we hope
that if one day you need to {git} {remote}, you will remember
that you saw it here first.\n
Before starting the tutorial, you should already be a little bit 
familiarized with {git}. If you are not, do not worry. We have created
a review of some important concepts, in case you need it.
"""

# Git review
print(more_message)
input(f"Press {enter} to see the review. Click {done} when you finish.")
git_review()

input(f"Excellent! Let's start the tutorial. Press {enter}.")
os.system("clear")

browser_message = f"""
Before executing your {git} commands, you should be located (pwd) in the 
directory that you want to {git} {init}, {git} {push}, etc... This is, you 
should change directories (cd). But you will not need to exit the program! 
Let me help you to do it.
"""

print(browser_message)
input(f"Press {enter} to open the Directory Browser to {select} and {submit} the " 
      "path of the directory that you want.\n")
open_browser = True
while open_browser == True:
    try:
        git_path = path_input()
        break
    except:
        print(f"You did not {submit} any directory. Try again: click {explore}, pick your directory and then {done}.\n")
        try:
            git_path = path_input()
            break
        except:
            print(f"You did not {submit} any directory. Try again: click {explore}, pick your directory and then {done}.\n")
            open_browser = True
        
input(f"The path to your directory has been stored. Press {enter} to continue.\n")
print("Changing directory...\n")
time.sleep(2)
os.chdir(git_path)
input(f"Done! Press {enter} to continue.\n")
os.system("clear")


# Git init

init_message = f"""
If you try to execute {git} commands in a non-git directory, you will
encounter a fatal error: not a git repository.\n
To avoid this error, first you have to {git} {init}. And if, by accident,
your directory was already a {git} repository, there is no problem,
it wil not overwrite anything.
"""
print(init_message)
cprint("command0: git init ", "green")
input(f"\nPress {enter} to execute your command...\n")
time.sleep(2)
os.system("git init")
input(f"\nDone! Press {enter} to continue.\n")

# Remove origin

rm_message = f"""
A {git} remote origin is the name for the remote repository of a {git} 
directory. If you try to execute {git} commands in the wrong remote
repository, you will encounter errors. To make sure this do not
happen while running the tutorial, we are going to remove the previous
origin just in case.
"""

print(rm_message)
cprint("command1: git remote rm origin ", "green")
input(f"\nPress {enter} to execute your command...\n")
time.sleep(2)
os.system("git remote rm origin")
input(f"\nDone! Press {enter} to continue.\n")
os.system("clear")

# Add origin

origin_message = f"""
Now, let's add a new origin. You will need to provide the url of the
{git} repo where you want to {git} {push}.
"""

print(origin_message)
url = input(str(f"Paste the url of your {git} repository: "))
print(f"Please, check the url: {url}\n")
url_answer = input(str("Is that the right url? y/n: "))
while url_answer != "y":
    if url_answer == "n":
        url = input(str(f"\nNo problem! Let's try again\nPaste the url of your {git} repository: "))
        print(f"Please, check the url: {url}\n")
        url_answer = input(str("Is that the right url? y/n: "))
    else:
        print("\nInvalid option. Try again.\n")
        print(f"Please, check the url: {url}\n")
        url_answer = input(str("Is that the right url? y/n: "))
if url_answer == "y":
    print(f"Excellent!\n. To {add} the origin we will use the next command.\n")

cprint(f"command2: git remote add origin {url}", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system(f"git remote add origin {url}")
input(f"\nDone! Press {enter} to continue.\n")

# Check the new origin
print("\nAnd you can check the new origin by doing: \n")
cprint("command3: git remote -v ", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system("git remote -v")
input(f"\nDone! Press {enter} to continue.\n")
os.system("clear")

# Git status
status_message = f"""
{git} status shows the current state of your {git} working directory 
and staging area. {green} shows file in {git} repository, committed 
with latest changes. {red} shows file in {git} repository, but with
latest changes that have not been committed. If you do not {add} the 
red files before committing, these files will not be included in 
your {commit}.
"""

print(status_message)
cprint("command4: git status", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system("git status")
input(f"\nDone! Press {enter} to continue.\n")

# Git add 
add_message =f"""
To {git} {add}, you have to pick a file in {red} from the 
status list above and copy the name. Then, paste the name 
of your file and do not forget the extension (example.ipynb),
or type {allfiles} to {add} all the files in the directory.
"""
print(add_message)
file = input(str(f"Please paste the name of your file or type {allfiles}: "))
print(f"\nPlease, check the name of your file: {file}\n")
file_answer = input(str("Is that the right name and extension? y/n: "))
while file_answer != "y":
    if file_answer == "n":
        file = input(str(f"\nNo problem! Let's try again.\n"
                         f"Paste the name of the file (example.ipynb) or type {allfiles}: "))
        print(f"Please, check the name of your file: {file}\n")
        file_answer = input(str("Is that the right name and extension? y/n: "))
    else:
        print("\nInvalid option. Try again.\n")
        print(f"Please, check the name of your file: {file}\n")
        file_answer = input(str("Is that the right name and extension? y/n: "))

if file_answer == "y":
    print("Excellent!\nBy adding a new file, you choose which changes you want to save\n")
cprint(f"command5: git add {file}", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system(f"git add {file}")
input(f"\nDone! Press {enter} to continue.\n")
os.system("clear")

# Git commit
print(f"\nNow, you have to {commit}, to save these changes. To identify the {commit}, you can write a {commit} message")
comment = input(f"Type a {commit} message. Make it short and simple: ")
cprint(f"command6: git commit -m {comment}", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system('git commit -m " '+str(comment)+'"')
input(f"\nDone! Press {enter} to continue.\n")

# Git log
print(f"\nAnd you can see the record of commits that you have done using {git} {log}.")
cprint("command6: git log", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system("git log")
input(f"\nDone! Press {enter} to continue.\n")
os.system("clear")

# Git push
git_token = colored('https://github.com/settings/tokens', 'cyan')

push_message = f"""
Finally, {push} to your repository by executing the next command. Note that
you will need to enter your {git} username and password/token. Do not worry if 
you do not see your password in the console when you type it! 
It is to protect your data.\n
To access your {gitlab} account, you need your {password}.\n
To access your {github} account, you need a {token}.\n
You can generate a token by logging in to your {git} account 
and going into this page:
{git_token}
Select only the repo scopes.\n
Remember to {copy} the token so you can {paste} it here
when you are asked for your password.
Press {enter} when you are ready.
"""

input(push_message)
cprint(f"command6: git push {url}", "green")
input(f"\nPress {enter} to execute the command...\n")
time.sleep(2)
os.system(f"git push {url}")
input(f"\nDone! Press {enter} to continue.\n")

# Check the git push
print(f"Go to:\n{url}\nto see if the {push} was successful.\n"
      f"Check out the master branch if you do not see the file in the main branch.")
push_answer = input(str("Has your file been pushed correctly? y/n: "))

while push_answer =="n":
    push_error = input(str("\nYou probably had an Authentication Error.\n Do you want to:\n"
                          f"a) try to {push} again?\n"
                           "b) Exit and try the tutorial later?\n"))
    if push_error == "a":
        cprint(f"command6: git push {url}", "green")
        input(f"\nPress {enter} to execute the command...\n")
        time.sleep(2)
        os.system(f"git push {url}")
        input(f"\nDone! Press {enter} to continue.\n")
        print(f"Go to:\n{url}\nto see if the {push} was successful.")
        push_answer = input(str("Has your file been pushed correctly? y/n: "))
    elif push_error == "b":
        push_answer = "y"
        
# End of tutorial
if push_answer == "y":
    print("\nAlright! You have reached the end of this tutorial.\n")
input("\nPress {enter} to continue.\n")
