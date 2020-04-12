# GUI Linux Management Console
GUI based version of the Linux Management Console.
-----------------------------------------------------------------------------------------------------------------------

NOTE: To view the program screenshots, access the Screenshots folder
-----------------------------------------------------------------------------------------------------------------------

Author: Gustavo Wydler Azuaga - 04-12-2020
-----------------------------------------------------------------------------------------------------------------------

Setup and running the program:

ADVANTAGE: Requires no installation!

* Clone the repo (from terminal with git clone )

* Access the folder, open the  Linux_users_and_groups.py (preferred with a code editor, or python interpreter) and make sure   to import all the libraries first.

* Once All the libraries are imported, inside the folder run Linux_users_and_groups.py file: python3.x     Linux_users_and_groups.py

OPTIONAL: If you want a Desktop launcher for the program:

    - Copy all the contents of the cloned folder (GUI_Linux_Management_Console) to your /home/$USER path
    - Trust the GUI_LINUX.Desktop file ( sudo chmod +rx GUI_LINUX.Desktop)
    - OPTIONAL: You can use the main_menu.png image for your Launcher.
    - Double click the icon to launch the progam.

-----------------------------------------------------------------------------------------------------------------------

Mandatory to run the program:

  - Python 3.x interpreter
  - Python program libraries installed
  - gnome-terminal 
  
-----------------------------------------------------------------------------------------------------------------------

About How the program works, its functionalities and purpose:

* Interactive python GUI (easygui library), to manage users and groups in client side or server systems.
* The Ubuntu/Debian system is managed entirely through the GUI, through buttons, and interactive dialog windows.
* All the user input is received through the GUI, and passed to the linux system through subprocess calls or os.system calls.
* The gnome-terminal runs all the final commands and displays them in the terminal. 

Viewing options: 

  * Display /etc/passwd file
  * Display SUDOERS list
  * Show USERS list
  * Show GROUPS list
  
Search Users/Groups:

 * USERS|GROUPS in /etc/passwd file
 * Search USER in users List (/etc/passwd file).
 * Search GROUP in groups List.
 * Search a USER´S group.
 * Search for ALL members of a GROUP
 * Search USER´S PRIMARY GROUP
 
Configuration and operation modes:

 * USER modes:
 
    * + ADD USER TO SUDOERS GROUP
    * - REMOVE USER FROM SUDOERS GROUP
    * + NEW USER/S AND FOLDER/S
    * - REMOVE USER, FOLDER AND IT´S PRIMARY GROUP
    * + Add user to a group
    * - Remove user from a group
    
 * GROUP modes:
 
    * + NEW GROUP/S
    * - DELETE GROUP/S
    * --> Change/Rename group's name
    
 * USER GROUP change modes:
 
    * --> CHANGE A USER´S PRIMARY GROUP
    * --> Change user´s username
    * --> Set | Change a user's password
 
 -----------------------------------------------------------------------------------------------------------------------

Purpose: The purpose of this program, focuses on operating a linux system in a more structured and accurate manner, regarding its users and groups. Using the program accordingly, will avoid and prevent you from forgetting or missusing commands and actions, which are many to remember, unless you are an expert linux operating sysadmin in a daily fashion.
-----------------------------------------------------------------------------------------------------------------------

