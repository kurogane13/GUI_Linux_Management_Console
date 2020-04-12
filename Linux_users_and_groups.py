import sys
import easygui
from easygui import *
import random
import os
import subprocess
        
loop = 2
while (loop==2):

    def exit_program():
        image = "warning.png"
        msg = "Do you want to Quit the Program?"
        title = "Quit Program?"
        choices = ["Yes", "No"]
        choice = buttonbox(msg, title, choices, image=image)
        if choice == "Yes":
            sys.exit(0)
        else:
            pass


    def main_menu():
        
        image = "Ubuntu_linux_penguin.png"
        msg ="********************************************************************************\n****** WELCOME TO UBUNTU/DEBIAN LINUX USER AND GROUPS MANAGEMENT PROGRAM! ******\n********************************************************************************\n\n     - THIS PROGRAM ALLOWS YOU TO RUN MANY OPERATIONS ON USERS AND GROUPS\n\n     - FOR ALL OPERATIONS YOU WILL BE PROMPTED FOR YOUR SUDO PASSWORD\n--------------------------------------------------------------------------------\n\n     * IMPORTANT NOTE: PLEASE USE THE PROGRAM WITH CAUTION, AND AT YOUR OWN RISK\n\n--------------------------------------------------------------------------------\n\n         --> MAIN MENU SCREEN - PRESS ANY BUTTON FROM THE MENU <--"
        title = "LINUX USERS AND GROUPS MANAGEMENT PROGRAM"
        choices = [ "Viewing Modes", "Searching Modes", "User Modes", "Group Modes", "Change User and Group Modes", "EXIT PROGRAM"]
        choice = buttonbox(msg ,title, image=image, choices=choices)

        if choice == "Viewing Modes":
                def viewing_modes():
                    
                    title = "Viewing modes window"
                    image = 'view_file.png'
                    image2= 'warning2.png'
                    msg = ("You accessed the VIEWING modes screen.")
                    choices = [ "View /etc/passwd file", "SUDOERS list", "USERS list", "GROUPS list", "Back to Main Menu", "EXIT PROGRAM"]
                    choice = buttonbox(msg ,title, image=image, choices=choices)
                    if choice == "View /etc/passwd file":
                        
                        gnome_var = 'gnome-terminal -- bash -c "printf  '
                        gnome_var2 = "'SHOWING /etc/passwd FILE: \n\n'"
                        gnome_var3 = ' && cat /etc/passwd; exec bash"'
                        gnome_var_end = gnome_var+gnome_var2+gnome_var3
                        subprocess.call(gnome_var_end+' %s' , shell=True)
                        viewing_modes()

                    if choice == "SUDOERS list":
                        quote = "'"
                        gnome_var = 'gnome-terminal -- bash -c "printf '
                        gnome_var2 = "'SHOWING SUDOERS LIST: \n\n'"
                        gnome_var3 = ' && grep -Po '
                        gnome_var4 = "'^sudo.+:\K.*$'"
                        gnome_var5 = ' /etc/group; exec bash"'
                        sudolist = gnome_var+gnome_var2+gnome_var3+gnome_var4+gnome_var5
                        subprocess.call(sudolist+' %s' , shell=True)
                        viewing_modes()

                    if choice == "USERS list":
                        
                        gnome_var = 'gnome-terminal -- bash -c "printf  '
                        gnome_var2 = "'SHOWING USERS LIST: \n\n'"
                        gnome_var3 = ' && cut -d: -f1 /etc/passwd; exec bash"'
                        gnome_var_end = gnome_var+gnome_var2+gnome_var3
                        subprocess.call(gnome_var_end+' %s' , shell=True)                        
                        viewing_modes()

                    if choice == "GROUPS list":
                         
                        gnome_var = 'gnome-terminal -- bash -c "printf '
                        gnome_var2 = "'SHOWING GROUPS LIST: \n\n'"
                        gnome_var3 = ' && getent group; exec bash"'
                        gnome_var_end = gnome_var+gnome_var2+gnome_var3
                        subprocess.call(gnome_var_end+' %s' , shell=True)                        
                        viewing_modes()

                    if choice == "Back to Main Menu":
                        main_menu()
                            
                    if choice == "EXIT PROGRAM":
                        image = "warning.png"
                        msg = "Do you want to Quit the Program?"
                        title = "Quit Program?"
                        choices = ["Yes", "No"]
                        choice = buttonbox(msg, title, choices, image=image)
                        if choice == "Yes":
                            sys.exit(0)

                        if choice == "No":
                            viewing_modes()
                            
                        else:
                            viewing_modes()

                    else:
                        viewing_modes()

                viewing_modes()

        if choice == "Searching Modes":
            def searching_modes():
                
                title = "Searching Modes window"
                image = 'search_image.png'
                image2= 'warning2.png'
                msg = ("You accessed the SEARCHING modes screen.")
                choices = [ "USERS|GROUPS in /etc/passwd", "USER", "GROUP", "Search a USER'S GROUP/S", "ALL members of a GROUP", "USER´S PRIMARY GROUP", "Back to Main Menu", "EXIT PROGRAM"]
                choice = buttonbox(msg ,title, image=image, choices=choices)
                if choice == "USERS|GROUPS in /etc/passwd":
                    def search_user_or_group():
                        
                        title = "Search User or Group"
                        find_user_group = enterbox("Enter a user or group to search in /etc/passwd file: ", title)
                        if find_user_group is not None:
                    
                            cat_var = ' '
                            gnome_var = 'gnome-terminal -- bash -c "printf '
                            gnome_var2 = "'SEARCH RESULT IN /etc/passwd: \n\n'"
                            gnome_var3 = ' && cat /etc/passwd | grep -w '+find_user_group
                            gnome_var4 = '; exec bash"'
                            gnome_var_end = gnome_var+gnome_var2+gnome_var3+gnome_var4
                            subprocess.call(gnome_var_end+' %s' , shell=True)   
                            searching_modes()
                            
                        else:
                            
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Searching Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                search_user_or_group()

                            if choice == "<-- Back to Searching Modes":
                                searching_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                search_user_or_group()

                    search_user_or_group()

                if choice == "USER":
                    def find_user_user_list():
                        
                        title = "SEARCH USER in USERS list"
                        find_user_in_users_list= enterbox("Enter a USER to search in the users list: ", title)
                        if find_user_in_users_list is not None:
                            
                            gnome_var = 'gnome-terminal -- bash -c "printf '
                            gnome_var2 = "'SEARCH RESULT FOR USER IN LIST: \n\n'"
                            gnome_var3 = ' && cut -d: -f1 /etc/passwd | grep -w '+find_user_in_users_list
                            gnome_var4 = '; exec bash"'
                            gnome_var_end = gnome_var+gnome_var2+gnome_var3+gnome_var4
                            subprocess.call(gnome_var_end+' %s' , shell=True)
                            searching_modes()

                        else:
                            
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Searching Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                find_user_user_list()
                                
                            if choice == "<-- Back to Searching Modes":
                                searching_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                find_user_user_list()

                    find_user_user_list()

                if choice == "GROUP":
                    def find_group_group_list():
                            
                        title = "Search GROUP in GROUPS list"
                        find_group_in_groups_list= enterbox("Enter a GROUP to find in the groups list: ", title)
                        if find_group_in_groups_list is not None:
                            
                            gnome_var = 'gnome-terminal -- bash -c "printf '
                            gnome_var2 = "'SEARCH RESULT FOR GROUP IN LIST: \n\n'"
                            gnome_var3 = ' && getent group '+find_group_in_groups_list
                            gnome_var4 = '; exec bash"'
                            gnome_var_end = gnome_var+gnome_var2+gnome_var3+gnome_var4
                            subprocess.call(gnome_var_end+' %s' , shell=True)
                            searching_modes()

                        else:
                        
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Searching Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                find_group_group_list()
                                
                            if choice == "<-- Back to Searching Modes":
                                searching_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                find_group_group_list()

                    find_group_group_list()

                if choice == "Search a USER'S GROUP/S":
                    def find_user_belongs_to_groups():

                        title = "Find ALL GROUPS a USER belongs to"
                        find_match_user_groups= enterbox("Enter a USER, to see all the GROUPS it belongs to: ", title)
                        if find_match_user_groups is not None:
                            
                            gnome_var = 'gnome-terminal -- bash -c "printf '
                            gnome_var2 = "'RESULT OF USER BELONGS TO GROUPS: \n\n'"
                            gnome_var3 = ' && groups '+find_match_user_groups
                            gnome_var4 = '; exec bash"'
                            gnome_var_end = gnome_var+gnome_var2+gnome_var3+gnome_var4
                            subprocess.call(gnome_var_end+' %s' , shell=True)
                            searching_modes()

                        else:   
                        
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Searching Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                find_user_belongs_to_groups()
                                
                            if choice == "<-- Back to Searching Modes":
                                searching_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                find_user_belongs_to_groups()

                    find_user_belongs_to_groups()

                if choice == "ALL members of a GROUP":
                    def all_members_of_a_group():
                        
                            title = "Search ALL MEMBERS of a GROUP"
                            find_all_member_of_group = enterbox("Enter a GROUP, to see all its members: ", title)
                            if find_all_member_of_group is not None:
                                
                                gnome_var = 'gnome-terminal -- bash -c "printf '
                                gnome_var2 = "'RESULT OF ALL MEMBERS OF A GROUP: \n\n'"
                                gnome_var3 = ' && grep -w '+find_all_member_of_group
                                gnome_var4 = ' /etc/group'
                                gnome_var5 = '; exec bash"'
                                gnome_var_end = gnome_var+gnome_var2+gnome_var3+gnome_var4+gnome_var5
                                subprocess.call(gnome_var_end+' %s' , shell=True)
                                searching_modes()
                            
                            else:
                                
                                image = "warning.png"
                                msg = "Do you want to Quit the Program?"
                                title = "Quit Program?"
                                choices = ["Yes", "No", "<-- Back to Searching Modes", "<-- Back to Main Menu"]
                                choice = buttonbox(msg, title, choices, image=image)
                                if choice == "Yes":
                                    sys.exit(0)

                                if choice == "No":
                                    all_members_of_a_group()
                                    
                                if choice == "<-- Back to Searching Modes":
                                    searching_modes()

                                if choice == "<-- Back to Main Menu":
                                    main_menu()
                                    
                                else:
                                    all_members_of_a_group()

                    all_members_of_a_group()

                if choice == "USER´S PRIMARY GROUP":
                    def users_primary_group():
                        
                        title = "Search a USER PRIMARY GROUP"
                        find_user_primary_group = enterbox("Enter a USER, to find its PRIMARY GROUP: ", title)
                        if find_user_primary_group is not None:
                            
                            gnome_var = 'gnome-terminal -- bash -c "printf '
                            gnome_var2 = "'RESULT OF USER PRIMARY GROUP: \n\n'"
                            gnome_var3 = ' && id -gn '+find_user_primary_group
                            gnome_var4 = '; exec bash"'
                            gnome_var_end = gnome_var+gnome_var2+gnome_var3+gnome_var4
                            subprocess.call(gnome_var_end+' %s' , shell=True)
                            searching_modes()
                        

                        else:
                        
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Searching Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                users_primary_group()
                                
                            if choice == "<-- Back to Searching Modes":
                                searching_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                users_primary_group()

                    users_primary_group()


                if choice == "Back to Main Menu":
                    main_menu()
                        
                if choice == "EXIT PROGRAM":
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":
                        sys.exit(0)

                    if choice == "No":
                        searching_modes()
                        
                    else:
                        searching_modes()

                else:
                    searching_modes()

            searching_modes()
            
        if choice == "User Modes":
            def user_operations_mode():
         
                title = "USER OPERATIONS SCREEN"
                image = 'user_icon.png'
                image2= 'warning2.png'
                msg = ("           YOU ARE IN USER OPERATIONS MODE SCREEN.\n\n----------------------------------------------------------------\n\n       This menu enables you to run operations on USERS.\n\n****************************************************************\n\n*** IMPORTANT: Please use with caution and at your own risk. ***\n\n****************************************************************")
                choices = [ "+ Add to SUDOERS", "- Remove from SUDOERS", "+ User and folder", "- Remove USER, folder, primary group", "+ Add to group", "- Remove from group", "Back to Main Menu", "EXIT PROGRAM"]
                choice = buttonbox(msg ,title, image=image, choices=choices)
                if choice == "+ Add to SUDOERS":
                    def add_to_sudoers():
    
                        title = "ADD USER TO SUDOERS"
                        global add_sudoer
                        add_sudoer = enterbox("Enter a USER, to add it to the SUDOERS group: ", title)
                        if add_sudoer is not None:

                            def confirm_or_reject():

                                warning = "warning.png"
                                confirm_sudoer = "ADD USER TO SUDOER CONFIRMATION"    
                                msg_sudoer = "NOTE: YOU WILL BE ADDING THE USER ---> "+add_sudoer+" to the SUDOERS group\n\n* YOU ARE REQUESTED TO CONFIRM OR REJECT THIS ACTION"
                                choices = ["CONFIRM NOW", "REJECT OPERATION - Back to prompt", "<-- Back to USER modes", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                                confirm_selection = buttonbox(msg_sudoer, confirm_sudoer, image=warning, choices=choices)
                                if confirm_selection == "CONFIRM NOW":
                                    sudo_var = ' sudo'
                                    add_user_to_sudoers = 'sudo adduser '
                                    user_to_sudoers = open('add_to_sudoers.sh', 'w')
                                    user_to_sudoers.write(str("echo 'Provide SUDO password to add user '"+add_sudoer+' to SUDOERS group.'+'\n'))
                                    user_to_sudoers.write(str("echo '------------------------------------'"+'\n'))
                                    user_to_sudoers.write(str(add_user_to_sudoers+add_sudoer+sudo_var)+'\n')
                                    user_to_sudoers.write(str("echo '------------------------------------'"+'\n'))
                                    user_to_sudoers.write(str("echo 'Press enter to close session...'"+'\n'))
                                    user_to_sudoers.write(str("read enter"))
                                    user_to_sudoers.close()
                                    os.system("gnome-terminal -- bash add_to_sudoers.sh")
                                    os.system("gnome-terminal -- rm add_to_sudoers.sh 2> /dev/null")
                                    user_operations_mode()

                                if confirm_selection == "REJECT OPERATION - Back to prompt":
                                    add_to_sudoers()

                                if confirm_selection == "<-- Back to USER modes":
                                    user_operations_mode()

                                if confirm_selection == "<-- Back to MAIN MENU":
                                    main_menu()

                                if confirm_selection == "EXIT PROGRAM":
                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No":
                                        confirm_or_reject()
                                        
                                    if choice == "<-- Back to USER operations menu":
                                        user_operations_mode()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()
                                        
                                    else:
                                        user_operations_mode()

                            confirm_or_reject()

                        else:
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                add_to_sudoers()
                                
                            if choice == "<-- Back to USER operations menu":
                                user_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                user_operations_mode()   

                    add_to_sudoers()
                   
                if choice == "+ User and folder":
                    
                    def user_and_folder():

                        title = "USER AND FOLDER CREATION"       
                        user_and_folder_creation = enterbox("USER AND FOLDER CREATION MODE ACCESSED.\n\n--> Enter a name, to create a New USER and its FOLDER: ", title)
                        if user_and_folder_creation is not None:

                            def confirm_user_folder():
                                
                                title = "Create USER and Folder"
                                warning = "warning.png"
                                choices = ["Yes, Create USER", "No - Back to Prompt", "<-- Back to USER modes", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                                confirm_user_and_folder = buttonbox("NOTE: You will create the user ---->   "+user_and_folder_creation+'\n\n'+"* IT IS MANDATORY TO SET A PASSWORD FOR THE USER BEFORE CREATING IT.\n\n--> YOU WILL BE PROMPTED FOR A PASSWORD IN THE TERMINAL WINDOW", title, choices=choices, image=warning)
                                if confirm_user_and_folder == "Yes, Create USER":
                                    
                                    passowrd_command = 'sudo passwd '
                                    create_new_user_and_folder = 'sudo useradd -m '
                                    add_to_bin_bash = 'sudo usermod --shell /bin/bash '
                                    create_user_and_folder = open('user_and_folder.sh', 'w')
                                    create_user_and_folder.write(str("echo 'PROVIDE SUDO PASSWORD TO SET A PASSWORD FOR THE CREATED USER: '"+'\n'))
                                    create_user_and_folder.write(str(create_new_user_and_folder+user_and_folder_creation)+'\n')
                                    create_user_and_folder.write(str(add_to_bin_bash+user_and_folder_creation)+'\n')
                                    create_user_and_folder.write(str(passowrd_command+user_and_folder_creation)+'\n')
                                    create_user_and_folder.write(str("echo '------------------------------------'"+'\n'))
                                    create_user_and_folder.write(str("echo 'Press enter to close session...'"+'\n'))
                                    create_user_and_folder.write(str("read enter"))
                                    create_user_and_folder.close()
                                    os.system("gnome-terminal -- bash user_and_folder.sh")
                                    os.system("gnome-terminal -- rm user_and_folder.sh 2> /dev/null")
                                    user_operations_mode()

                                if confirm_user_and_folder == "No - Back to Prompt":
                                    user_and_folder()

                                if confirm_user_and_folder == "<-- Back to USER modes":
                                    user_operations_mode()

                                if confirm_user_and_folder == "<-- Back to MAIN MENU":
                                    main_menu()

                                if confirm_user_and_folder == "EXIT PROGRAM":

                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No":
                                        confirm_user_folder()
                                        
                                    if choice == "<-- Back to USER operations menu":
                                        user_operations_mode()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()
                                        
                                    else:
                                        user_and_folder()

                            confirm_user_folder()

                        else:
                            
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                user_and_folder()
                                
                            if choice == "<-- Back to USER operations menu":
                                user_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                user_operations_mode()

                    user_and_folder()
                  

                if choice == "- Remove USER, folder, primary group":
                    def remove_user_folder_primary_group():
                        
                        image = "warning.png"
                        title = "Remove USER folder and primary group"
                        global remove_user_folder_primary
                        remove_user_folder_primary = enterbox("Enter the name of a user, to remove it, its folder, and primary group: ", title)
                        if remove_user_folder_primary is not None:

                            def confirm_reject_removal():
                                
                                warning = "warning.png"
                                confirm_remove_user_folder = "REMOVE USER AND FOLDER CONFIRMATION"    
                                msg_user_folder = 'WARNING!: YOU WILL BE DELETING THE USER: '+remove_user_folder_primary+' AND ITS FOLDER'+'\n\nTO RUN THIS OPERATION YOU WILL BE REQUESTED YOUR SUDO PASSWORD\n\nDO YOU WISH TO PROCEED TO DELETION?'
                                choices = ["CONFIRM NOW", "REJECT OPERATION - Back to prompt", "<-- Back to USER modes", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                                confirm_selection = buttonbox(msg_user_folder, confirm_remove_user_folder, image=warning, choices=choices)
                                if confirm_selection == "CONFIRM NOW":
                                
                                    remove_user = 'sudo userdel -r '
                                    remove_user_folder = 'sudo rm -r /home/'
                                    remove_user_folder_and_primary = open('remove_user_folder_primary.sh', 'w')
                                    remove_user_folder_and_primary.write(str("echo 'PROVIDE SUDO PASSWORD TO REMOVE THE USER AND ITS FOLDER: '"+'\n'))
                                    remove_user_folder_and_primary.write(str(remove_user+remove_user_folder_primary)+'\n')
                                    remove_user_folder_and_primary.write(str(remove_user_folder+remove_user_folder_primary)+'\n')
                                    remove_user_folder_and_primary.write(str("echo '------------------------------------'"+'\n'))
                                    remove_user_folder_and_primary.write(str("echo 'Press enter to close session...'"+'\n'))
                                    remove_user_folder_and_primary.write(str("read enter"))
                                    remove_user_folder_and_primary.close()
                                    os.system("gnome-terminal -- remove_user_folder_primary.sh")
                                    os.system("gnome-terminal -- rm remove_user_folder_primary.sh 2> /dev/null")
                                    user_operations_mode()
                                    
                                if confirm_selection == "REJECT OPERATION - Back to prompt":
                                    remove_user_folder_primary_group()

                                if confirm_selection == "<-- Back to USER modes":
                                    user_operations_mode()

                                if confirm_selection == "<-- Back to MAIN MENU":
                                    main_menu()

                                if confirm_selection == "EXIT PROGRAM":
                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No":
                                        confirm_reject_removal()
                                        
                                    if choice == "<-- Back to USER operations menu":
                                        user_operations_mode()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()
                                        
                                    else:
                                        remove_user_folder_primary_group()

                            confirm_reject_removal()
                            
                            
                        else:
                            
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                remove_user_folder_primary_group()
                                
                            if choice == "<-- Back to USER operations menu":
                                user_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                remove_user_folder_primary_group()


                    remove_user_folder_primary_group()

                if choice == "- Remove from SUDOERS":
                    def remove_from_sudoers():
                        
                        title = "REMOVE USER FROM SUDOERS"
                        del_sudoer = enterbox("Enter a SUDO USER, to remove it to from the SUDOERS group: ", title)
                        if del_sudoer is not None:
                            
                            warning = "warning.png"
                            confirm_sudoer = "REMOVE USER FROM SUDOER GROUP CONFIRMATION"    
                            msg_sudoer = "NOTE: YOU WILL BE REMOVING THE USER ---> "+del_sudoer+" from the SUDOERS group\n\n* YOU ARE REQUESTED TO CONFIRM OR REJECT THIS ACTION"
                            choices = ["CONFIRM NOW", "REJECT OPERATION - Back to prompt", "<-- Back to USER modes", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                            confirm_selection = buttonbox(msg_sudoer, confirm_sudoer, image=warning, choices=choices)
                            if confirm_selection == "CONFIRM NOW":

                                del_sudo_user = 'sudo deluser '
                                sudo_var = ' sudo'
                                del_from_sudoers = open('del_from_sudoers.sh', 'w')
                                del_from_sudoers.write(str("echo 'Provide SUDO password to remove user '"+del_sudoer+' from the SUDOERS group.'+'\n'))
                                del_from_sudoers.write(str(del_sudo_user+del_sudoer+sudo_var)+'\n')
                                del_from_sudoers.write(str("echo '------------------------------------'"+'\n'))
                                del_from_sudoers.write(str("echo 'Press enter to close session...'"+'\n'))
                                del_from_sudoers.write(str("read enter"))
                                del_from_sudoers.close()
                                os.system("gnome-terminal -- bash del_from_sudoers.sh")
                                os.system("gnome-terminal -- rm del_from_sudoers.sh 2> /dev/null")
                                user_operations_mode()

                            if confirm_selection == "REJECT OPERATION - Back to prompt":
                                add_to_sudoers()

                            if confirm_selection == "<-- Back to USER modes":
                                user_operations_mode()

                            if confirm_selection == "<-- Back to MAIN MENU":
                                main_menu()

                            if confirm_selection == "EXIT PROGRAM":
                                image = "warning.png"
                                msg = "Do you want to Quit the Program?"
                                title = "Quit Program?"
                                choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                                choice = buttonbox(msg, title, choices, image=image)
                                if choice == "Yes":
                                    sys.exit(0)

                                if choice == "No":
                                    confirm_or_reject()
                                    
                                if choice == "<-- Back to USER operations menu":
                                    user_operations_mode()

                                if choice == "<-- Back to Main Menu":
                                    main_menu()
                                    
                                else:
                                    user_operations_mode()
  
                        else:
                            
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                remove_from_sudoers()
                                
                            if choice == "<-- Back to USER operations menu":
                                user_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                remove_from_sudoers()

                    remove_from_sudoers()

                if choice == "+ Add to group":
                    def add_to_group():
                        
                        global add_user_group_var
                        global title_user_groups
                        title_user_groups = "USER ADDITION FORM"
                        global fieldNames
                        msg = "+ ADD USER TO A GROUP\n\nNOTE: PLEASE COMPLETE THE USER AND THE GROUP FIELDS\n\n  * USER to be added\n\n  * GROUP in which you want the user to be added"
                        fieldNames = ["USER TO ADD: ", "GROUP TO ADD USER: "]
                        global fieldValues
                        fieldValues = []
                        fieldValues = multenterbox(msg, title_user_groups, fieldNames)

                        while 1:
                            errmsg = ""
                            if fieldValues == None:
                                image = "warning.png"
                                msg = "Do you want to Quit the Program?"
                                title = "Quit Program?"
                                choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                                choice = buttonbox(msg, title, choices, image=image)
                                if choice == "Yes":
                                    sys.exit(0)

                                if choice == "No":
                                    add_to_group()
                                    
                                if choice == "<-- Back to USER operations menu":
                                    user_operations_mode()

                                if choice == "<-- Back to Main Menu":
                                    main_menu()
                                
                                else:
                                    add_to_group()
                                    
                            for i in range(len(fieldNames)):
                                if fieldValues[i].strip() == "":
                                    warning = "warning.png"
                                    title = "ATENTION"
                                    errmsg = errmsg + ('* ATENTION!, PLEASE COMPLETE THE "%s" FIELD. IT IS NOT COMPLETE AND MUST BE ENTERED.\n\n' % fieldNames[i])
                                
                            if errmsg == "": break # no problems found
                            msgbox(errmsg, title, image=warning)
                            fieldValues = multenterbox(msg, title, fieldNames, fieldValues)
      
                        msg = "ATENTION: Confirmation of USER addition to GROUP is needed"
                        title = "CONFIRM USER ADDITION"
                        image = "warning.png"
                        choices = ["ADD USER TO GROUP NOW", "Re-enter USER and GROUP", "Go back to User Modes", "EXIT PROGRAM"]
                        confirm_group = buttonbox(msg, title, choices, image=image)
                        if confirm_group == "ADD USER TO GROUP NOW":

                                add_user_group_var = 'sudo usermod -a -G  '
                                add_user_to_group = open('add_a_user_to_group.sh', 'w')
                                add_user_to_group.write(str("echo 'YOU ARE REQUIRED TO ENTER YOUR SUDO PASSWORD TO PROCEED ADDING THE USER '"+'\n'))
                                add_user_to_group.write(str(add_user_group_var+fieldValues[1]+" "+fieldValues[0])+'\n')
                                add_user_to_group.write(str("echo '------------------------------------'"+'\n'))
                                add_user_to_group.write(str("echo 'Press enter to close session...'"+'\n'))
                                add_user_to_group.write(str("read enter"))
                                add_user_to_group.close()
                                
                                os.system("gnome-terminal -- bash add_a_user_to_group.sh")
                                os.system("gnome-terminal -- rm add_a_user_to_group.sh 2> /dev/null")
                                user_operations_mode()
                            
                        if confirm_group == "Re-enter USER and GROUP":
                            add_to_group()

                        if confirm_group == "Go back to User Modes":
                            user_operations_mode()

                        if confirm_group == "EXIT PROGRAM":
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                add_to_group()
                                
                            if choice == "<-- Back to USER operations menu":
                                user_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                add_to_group()
                            
                    add_to_group()
                    
                if choice == "- Remove from group":
                    def remove_from_group():
                        global del_user_group_var
                        global title_user_groups
                        title_user_groups = "USER DELETION FORM"
                        global fieldNames
                        msg = "- DELETE A USER FROM A GROUP\n\nNOTE: PLEASE COMPLETE THE USER AND THE GROUP FIELDS\n\n  * USER to be Deleted\n\n  * GROUP from which you want the user to be deleted"
                        fieldNames = ["USER TO DELETE: ", "GROUP FROM WHICH TO DELETE USER: "]
                        global fieldValues
                        fieldValues = []
                        fieldValues = multenterbox(msg, title_user_groups, fieldNames)

                        while 1:
                            errmsg = ""
                            if fieldValues == None:
                                image = "warning.png"
                                msg = "Do you want to Quit the Program?"
                                title = "Quit Program?"
                                choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                                choice = buttonbox(msg, title, choices, image=image)
                                if choice == "Yes":
                                    sys.exit(0)

                                if choice == "No":
                                    remove_from_group()
                                    
                                if choice == "<-- Back to USER operations menu":
                                    user_operations_mode()

                                if choice == "<-- Back to Main Menu":
                                    main_menu()
                                
                                else:
                                    remove_from_group()

                            for i in range(len(fieldNames)):
                                if fieldValues[i].strip() == "":
                                    warning = "warning.png"
                                    title = "ATENTION"
                                    errmsg = errmsg + ('* ATENTION!, PLEASE COMPLETE THE "%s" FIELD. IT IS NOT COMPLETE AND MUST BE ENTERED.\n\n' % fieldNames[i])
                                
                            if errmsg == "": break # no problems found
                            msgbox(errmsg, title, image=warning)
                            fieldValues = multenterbox(msg, title, fieldNames, fieldValues)

                        msg = "ATENTION: Confirmation of USER from GROUP deletion is needed"
                        title = "CONFIRM USER DELETION"
                        image = "warning.png"
                        choices = ["DELETE USER FROM GROUP NOW", "Re-enter USER and GROUP", "Go back to User Modes", "EXIT PROGRAM"]
                        confirm_group = buttonbox(msg, title, choices, image=image)
                        if confirm_group == "DELETE USER FROM GROUP NOW":
                            
                                del_user_group_var = 'sudo deluser '
                                del_user_from_group = open('del_user_from_group.sh', 'w')
                                del_user_from_group.write(str("echo 'YOU ARE REQUIRED TO ENTER SUDO PASSWORD TO REMOVE THE USER FROM THE GROUP'"+'\n'))
                                del_user_from_group.write(str(del_user_group_var+fieldValues[0]+" "+fieldValues[1])+'\n')
                                del_user_from_group.write(str("echo '------------------------------------'"+'\n'))
                                del_user_from_group.write(str("echo 'Press enter to close session...'"+'\n'))
                                del_user_from_group.write(str("read enter"))
                                del_user_from_group.close()
                                
                                os.system("gnome-terminal -- bash del_user_from_group.sh")
                                os.system("gnome-terminal -- rm del_user_from_group.sh 2> /dev/null")
                                user_operations_mode()
                            
                        if confirm_group == "Re-enter USER and GROUP":
                            remove_from_group()

                        if confirm_group == "Go back to User Modes":
                            user_operations_mode()

                        if confirm_group == "EXIT PROGRAM":
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to USER operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                remove_from_group()
                                
                            if choice == "<-- Back to USER operations menu":
                                user_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                remove_from_group()                            

                    remove_from_group()

                if choice == "Back to Main Menu":
                    main_menu()

                if choice == "EXIT PROGRAM":
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":
                        sys.exit(0)

                    if choice == "No":
                        user_operations_mode()
                        
                    else:
                        user_operations_mode()

                else:
                    user_operations_mode()

                           
                    
            user_operations_mode()

        if choice == "Group Modes":
            def group_operations_mode():
                
                title = "GROUP OPERATIONS SCREEN"
                image = 'User_Group.png'
                msg = ("           YOU ARE IN GROUP OPERATIONS MODE SCREEN.\n\n----------------------------------------------------------------\n\n       This menu enables you to run operations on GROUPS.\n\n****************************************************************\n\n*** IMPORTANT: Please use with caution and at your own risk. ***\n\n****************************************************************")
                choices = [ "+ NEW GROUP", "- DELETE GROUP", "Rename a GROUP", "<-- Back to Main Menu", "EXIT PROGRAM"]
                choice = buttonbox(msg ,title, image=image, choices=choices)
                if choice == "+ NEW GROUP":
                    def new_group():
                        
                        title = "NEW GROUP CREATION"       
                        new_group_creation = enterbox("+ NEW GROUP CREATION MODE ACCESSED.\n\n--> Enter a name, to create a New GROUP: ", title)
                        if new_group_creation is not None:

                            new_group_var = 'sudo groupadd '
                            create_new_group = open('new_group.sh', 'w')
                            create_new_group.write(str("echo 'PROVIDE SUDO PASSWORD TO CREATE THE NEW GROUP: '"+'\n'))
                            create_new_group.write(str(new_group_var+new_group_creation)+'\n')
                            create_new_group.write(str("echo '------------------------------------'"+'\n'))
                            create_new_group.write(str("echo 'Press enter to close session...'"+'\n'))
                            create_new_group.write(str("read enter"))
                            create_new_group.close()
                            os.system("gnome-terminal -- bash new_group.sh")
                            os.system("gnome-terminal -- rm new_group.sh 2> /dev/null")
                            group_operations_mode()

                        else:
                        
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to GROUP operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                new_group()
                                
                            if choice == "<-- Back to GROUP operations menu":
                                group_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                group_operations_mode()
                    new_group()


                if choice == "- DELETE GROUP":
                    def delete_group():
                        
                        title = "GROUP DELETION MENU"       
                        group_deletion = enterbox("- GROUP DELETION MODE ACCESSED.\n\n--> Enter the name of a GROUP to delete: ", title)
                        if group_deletion is not None:

                            delete_group_var = 'sudo groupdel '
                            delete_group = open('del_group.sh', 'w')
                            delete_group.write(str("echo 'PROVIDE SUDO PASSWORD TO DELETE THE GROUP: '"+'\n'))
                            delete_group.write(str(delete_group_var+group_deletion)+'\n')
                            delete_group.write(str("echo '------------------------------------'"+'\n'))
                            delete_group.write(str("echo 'Press enter to close session...'"+'\n'))
                            delete_group.write(str("read enter"))
                            delete_group.close()
                            os.system("gnome-terminal -- bash del_group.sh")
                            os.system("gnome-terminal -- rm del_group.sh 2> /dev/null")
                            group_operations_mode()

                        else:
                        
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to GROUP operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                delete_group()
                                
                            if choice == "<-- Back to GROUP operations menu":
                                group_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                group_operations_mode()
                                
                    delete_group()
                    
                
                if choice == "Rename a GROUP":
                    def rename_group():
                        
                        title = "RENAME GROUP MODE"
                        global rename_group_var
                        rename_group_var = enterbox("* RENAMING GROUP MODE ACCESSED.\n\n--> Enter the name of the GROUP you wish to rename: ", title)
                        if rename_group_var is not None:

                            def assign_new_group_name():
                                
                                title = "NEW GROUP NAME"
                                new_group_name = enterbox("* NEW GROUP ASSIGNMENT OPTION.\n\n- NOW YOU NEED TO ASSIGN A NEW NAME FOR THE GROUP\n\n--> Enter the NEW name for the GROUP: "+rename_group_var, title)
                                if new_group_name is not None:
                                    
                                    command_group_var = 'sudo groupmod --new-name '
                                    rename_group = open('del_group.sh', 'w')
                                    rename_group.write(str("echo 'PROVIDE SUDO PASSWORD TO RENAME THE GROUP: '"+'\n'))
                                    rename_group.write(str(command_group_var+new_group_name+" "+rename_group_var)+'\n')
                                    rename_group.write(str("echo '------------------------------------'"+'\n'))
                                    rename_group.write(str("echo 'Press enter to close session...'"+'\n'))
                                    rename_group.write(str("read enter"))
                                    rename_group.close()
                                    os.system("gnome-terminal -- bash del_group.sh")
                                    os.system("gnome-terminal -- rm del_group.sh 2> /dev/null")
                                    group_operations_mode()

                                else:
                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No - Back to prompt", "<-- Back to GROUP operations menu", "<-- Back to Main Menu", "EXIT PROGRAM"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No - Back to prompt":
                                        assign_new_group_name()
                                        
                                    if choice == "<-- Back to GROUP operations menu":
                                        group_operations_mode()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()

                                    if choice == "EXIT PROGRAM":
                                        image = "warning.png"
                                        msg = "Do you want to Quit the Program?"
                                        title = "Quit Program?"
                                        choices = ["Yes", "No - Back to prompt", "<-- Back to GROUP operations menu", "<-- Back to Main Menu"]
                                        choice = buttonbox(msg, title, choices, image=image)
                                        if choice == "Yes":
                                            sys.exit(0)

                                        if choice == "No - Back to prompt":
                                             assign_new_group_name()
                                            
                                        if choice == "<-- Back to GROUP operations menu":
                                            group_operations_mode()

                                        if choice == "<-- Back to Main Menu":
                                            main_menu()
                                        
                                        else:
                                            group_operations_mode()
                                        
                            assign_new_group_name()

                        else:
                        
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No - Back to prompt", "<-- Back to GROUP operations menu", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No - Back to prompt":
                                rename_group()
                                
                            if choice == "<-- Back to GROUP operations menu":
                                group_operations_mode()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                group_operations_mode()
                                
                    rename_group()
                

                if choice == "<-- Back to Main Menu":
                    main_menu()

                if choice == "EXIT PROGRAM":
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":
                        sys.exit(0)

                    if choice == "No":
                        group_operations_mode()
                        
                    else:
                        group_operations_mode()

                else:
                    group_operations_mode()


            group_operations_mode()
            

        if choice == "Change User and Group Modes":
             def change_user_modes():

                title = "Change User and Group Modes"
                image = 'change_user_group_settings.png'
                msg = ("           YOU ARE IN THE CHANGE USER MODES SCREEN.\n\n----------------------------------------------------------------\n\n     This menu enables you to:\n\n        ---> Change a user´s primary group name\n\n        ---> Rename a user\n\n        ---> Set or change a user´s password\n\n****************************************************************\n\n*** IMPORTANT: Please use with caution and at your own risk. ***\n\n****************************************************************")
                choices = [ "CHANGE PRIMARY GROUP NAME", "RENAME A USER", "SET | CHANGE A USER´S PASSWORD", "<-- Back to Main Menu", "EXIT PROGRAM"]
                choice = buttonbox(msg ,title, image=image, choices=choices)
                
                if choice == "CHANGE PRIMARY GROUP NAME":
                    def change_primary_group_name():
                        
                        title = "CHANGE PRIMARY GROUP NAME"
                        global change_primary_name
                        change_primary_name = enterbox("* CHANGE THE NAME OF A PRIMARY GROUP.\n\n- THIS MODE WILL CHANGE THE NAME OF A PRIMARY GROUP\n\n--> Enter the name of the PRIMARY GROUP you wish to change: ", title)
                        if change_primary_name is not None:

                            def defined_group_name():

                                title = "DEFINE NEW GROUP NAME"
                                global new_defined_name
                                new_defined_name = enterbox("* PROVIDE A NEW NAME FOR THE PRIMARY GROUP.\n\n- A NEW NAME IS NEEDED TO REPLACE THE ACTUAL ONE\n\n--> Enter a NEW name for the PRIMARY GROUP: ", title)
                                if new_defined_name is not None:
                                    
                                    def confirm_change_primary():
                                        
                                        image = "warning.png"
                                        msg = "ATENTION: YOU ARE REQUIRED TO CONFIRM YOU WILL CHANGE THE NAME OF THE PRIMARY GROUP\n\n  --> THE PRIMARY GROUP NAME TO CHANGE IS: "+change_primary_name+'\n\n'"  --> NEW NAME TO ASSIGN TO GROUP IS: "+new_defined_name
                                        title = "CONFIRM RENAMING OF PRIMARY GROUP"
                                        image = "warning.png"
                                        choices = ["CONFIRM RENAMING OF GROUP NOW", "<-- Back to prompt", "<-- Back to Change User and Group Modes", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                                        choice = buttonbox(msg, title, choices, image=image)
                                        if choice == "CONFIRM RENAMING OF GROUP NOW":
                                            
                                            change_group_name = 'sudo groupmod --new-name '+new_defined_name+" "+change_primary_name
                                            get_group_from_list = 'getent group '+change_primary_name
                                            get_new_name_group_from_list = 'getent group '+new_defined_name
                                            
                                            new_sudo_user_group = open('change_primary_group_name.sh', 'w')
                                            new_sudo_user_group.write(str(get_group_from_list)+'\n')
                                            new_sudo_user_group.write(str("echo '------------------------------------'"+'\n'))
                                            new_sudo_user_group.write(str("echo 'ENTER SUDO PASSWORD TO RENAME THE GROUP: '"+'\n'))
                                            new_sudo_user_group.write(str(change_group_name)+'\n')
                                            new_sudo_user_group.write(str("echo '------------------------------------'"+'\n'))
                                            new_sudo_user_group.write(str(get_new_name_group_from_list)+'\n')
                                            new_sudo_user_group.write(str("echo '------------------------------------'"+'\n'))
                                            new_sudo_user_group.write(str("echo 'Press enter to close session...'"+'\n'))
                                            new_sudo_user_group.write(str("read enter"))
                                            new_sudo_user_group.close()
                                            os.system("gnome-terminal -- bash change_primary_group_name.sh")
                                            os.system("gnome-terminal -- rm change_primary_group_name.sh 2> /dev/null")
                                            change_user_modes()  

                                        if choice == "<-- Back to prompt":

                                            defined_group_name()

                                        if choice == "<-- Back to Change User and Group Modes":

                                            change_user_modes()
                                            
                                        if choice == "<-- Back to MAIN MENU":

                                            main_menu()

                                        if choice == "EXIT PROGRAM":

                                            image = "warning.png"
                                            msg = "Do you want to Quit the Program?"
                                            title = "Quit Program?"
                                            choices = ["Yes", "No", "<-- back to Change User and Group Modes", "<-- Back to Main Menu"]
                                            choice = buttonbox(msg, title, choices, image=image)
                                            if choice == "Yes":
                                                sys.exit(0)

                                            if choice == "No":
                                                confirm_change_primary()
                                                
                                            if choice == "<-- back to Change User and Group Modes":
                                                change_user_modes()

                                            if choice == "<-- Back to Main Menu":
                                                main_menu()
                                                
                                            else:
                                                confirm_change_primary()
                                            
                                    confirm_change_primary()


                                else:
                                    
                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No", "<-- Back to Group Name prompt",  "<-- Back to Change User and Group Modes", "<-- Back to Main Menu"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No":
                                        defined_group_name()

                                    if choice == "<-- Back to Group Name prompt":
                                        change_primary_group_name()
                                        
                                    if choice == "<-- Back to Change User and Group Modes":
                                        change_user_modes()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()
                                        
                                    else:
                                        change_user_modes()
 
                            defined_group_name()
                            

                        else:
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Change User and Group Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                change_primary_group_name()
                                
                            if choice == "<-- Back to Change User and Group Modes":
                                change_user_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                change_user_modes()


                    change_primary_group_name()
                   
                if choice == "RENAME A USER":
                    def rename_user_mode():
                        
                        title = "RENAME USER"
                        global user_to_rename
                        user_to_rename = enterbox("* RENAME A USER MODE.\n\n- THIS MODE WILL ALLOW YOU TO RENAME A USER\n\n--> Enter the name of the USER you wish to rename: ", title)
                        if user_to_rename is not None:
                            
                            def set_new_user_name():
                                title = "RENAME USER"
                                global new_name_of_user
                                new_name_of_user = enterbox("* ASSIGN A NEW NAME TO THE USER.\n\n --> Enter a NEW name for the USER: "+user_to_rename, title)
                                if new_name_of_user is not None:

                                    def confirm_change_user_name():
                                
                                        image = "warning.png"
                                        msg = "ATENTION: YOU ARE REQUIRED TO CONFIRM YOU WILL BE RENAMING THE USER: "+user_to_rename+'\n\n'"THE NEW NAME TO ASSIGN TO THIS USER IS: "+new_name_of_user
                                        title = "CONFIRM RENAMING OF USER"
                                        image = "warning.png"
                                        choices = ["CONFIRM RENAMING NOW", "<-- Back to New User prompt", "<-- Back to Existing User prompt", "<-- Back to Change User and Group", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                                        choice = buttonbox(msg, title, choices, image=image)
                                        if choice == "CONFIRM RENAMING NOW":
                                        
                                            renaming_of_user_var = 'sudo usermod -l '+new_name_of_user+" -d /home/"+new_name_of_user+' -m '+user_to_rename
                                            
                                            remove_sudo_user_from_sudo_group = open('rename_a_user.sh', 'w')
                                            remove_sudo_user_from_sudo_group.write(str('cat /etc/passwd | grep -w '+user_to_rename)+'\n')
                                            remove_sudo_user_from_sudo_group.write(str("echo '------------------------------------'"+'\n'))
                                            remove_sudo_user_from_sudo_group.write(str("echo 'ENTER SUDO PASSWORD TO CHANGE THE NAME OF THE USER: '"+'\n'))
                                            remove_sudo_user_from_sudo_group.write(str(renaming_of_user_var)+'\n')
                                            remove_sudo_user_from_sudo_group.write(str("echo '------------------------------------'"+'\n'))
                                            remove_sudo_user_from_sudo_group.write(str('cat /etc/passwd | grep -w '+new_name_of_user)+'\n')
                                            remove_sudo_user_from_sudo_group.write(str("echo '------------------------------------'"+'\n'))
                                            remove_sudo_user_from_sudo_group.write(str("echo 'Press enter to close session...'"+'\n'))
                                            remove_sudo_user_from_sudo_group.write(str("read enter"))
                                            remove_sudo_user_from_sudo_group.close()
                                            os.system("gnome-terminal -- bash rename_a_user.sh")
                                            os.system("gnome-terminal -- rm rename_a_user.sh 2> /dev/null")
                                            change_user_modes()
          

                                        if choice == "<-- Back to New User prompt":

                                            set_new_user_name()


                                        if choice == "<-- Back to Existing User prompt":

                                            rename_user_mode()

                                        if choice == "<-- Back to Change User and Group":

                                            confirm_change_user_name()
                                            
                                        if choice == "<-- Back to MAIN MENU":

                                            main_menu()

                                        if choice == "EXIT PROGRAM":

                                            image = "warning.png"
                                            msg = "Do you want to Quit the Program?"
                                            title = "Quit Program?"
                                            choices = ["Yes", "No", "<-- Back to GROUP operations menu", "<-- Back to Main Menu"]
                                            choice = buttonbox(msg, title, choices, image=image)
                                            if choice == "Yes":
                                                sys.exit(0)

                                            if choice == "No":
                                                confirm_change_user_name()
                                                
                                            if choice == "<-- Back to Change User and Group Modes":
                                                change_user_modes()

                                            if choice == "<-- Back to Main Menu":
                                                main_menu()
                                                
                                            else:
                                                change_user_modes()

                                    confirm_change_user_name()



                                else:
                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No", "<-- Back to Existing User prompt", "<-- Back to Change User and Group Modes", "<-- Back to Main Menu"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No":
                                        set_new_user_name()

                                    if choice == "<-- Back to Existing User prompt":
                                        rename_user_mode()
                                        
                                    if choice == "<-- Back to Change User and Group Modes":
                                        change_user_modes()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()
                                        
                                    else:
                                        change_user_modes()
                                    
                                    

                            set_new_user_name()


                        else:
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Change User and Group Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                rename_user_mode()
                                
                            if choice == "<-- Back to Change User and Group Modes":
                                change_user_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                change_user_modes()

                    rename_user_mode()


                if choice == "SET | CHANGE A USER´S PASSWORD":
                
                    def set_or_change_password():
                        title = "SET | CHANGE A USER´S PASSWORD"
                        global change_set_password
                        change_set_password = enterbox("* SET | CHANGE A USER´S PASSWORD MODE.\n\n --> Enter the name of the USER, to set or change it´s password: ", title)
                        if change_set_password is not None:

                            def confirm_change_user_password():
        
                                image = "warning.png"
                                msg = "ATENTION: YOU ARE REQUIRED TO CONFIRM YOU WILL BE CHANGING THE PASSWORD FOR: \n\n"+change_set_password
                                title = "CONFIRM PASSWORD CHANGE"
                                choices = ["CONFIRM CHANGE NOW", "<-- Back to USER prompt", "<-- Back to Change User and Group", "<-- Back to MAIN MENU", "EXIT PROGRAM"]
                                choice = buttonbox(msg, title, choices, image=image)
                                if choice == "CONFIRM CHANGE NOW":
        
                                    change_set_pass_var = 'sudo passwd '+change_set_password
                                    
                                    change_or_set_user_password = open('change_set_user_pass.sh', 'w')
                                    change_or_set_user_password.write(str("echo '------------------------------------'"+'\n'))
                                    change_or_set_user_password.write(str("echo 'ENTER SUDO PASSWORD TO SET OR CHANGE THE PASSWORD OF THE USER: '"+'\n'))
                                    change_or_set_user_password.write(str(change_set_pass_var)+'\n')
                                    change_or_set_user_password.write(str("echo '------------------------------------'"+'\n'))
                                    change_or_set_user_password.write(str("echo 'Press enter to close session...'"+'\n'))
                                    change_or_set_user_password.write(str("read enter"))
                                    change_or_set_user_password.close()
                                    os.system("gnome-terminal -- bash change_set_user_pass.sh")
                                    os.system("gnome-terminal -- rm change_set_user_pass.sh 2> /dev/null")
                                    change_user_modes()


                                if choice == "<-- Back to USER prompt":

                                    set_or_change_password()

                                if choice == "<-- Back to Change User and Group":

                                    change_user_modes()
                                    
                                if choice == "<-- Back to MAIN MENU":

                                    main_menu()

                                if choice == "EXIT PROGRAM":

                                    image = "warning.png"
                                    msg = "Do you want to Quit the Program?"
                                    title = "Quit Program?"
                                    choices = ["Yes", "No", "<-- Back to Change User and Group Modes", "<-- Back to Main Menu"]
                                    choice = buttonbox(msg, title, choices, image=image)
                                    if choice == "Yes":
                                        sys.exit(0)

                                    if choice == "No":
                                        confirm_change_user_password()
                                        
                                    if choice == "<-- Back to Change User and Group Modes":
                                        change_user_modes()

                                    if choice == "<-- Back to Main Menu":
                                        main_menu()
                                        
                                    else:
                                        confirm_change_user_password()

                            confirm_change_user_password()

                        else:
                            image = "warning.png"
                            msg = "Do you want to Quit the Program?"
                            title = "Quit Program?"
                            choices = ["Yes", "No", "<-- Back to Change User and Group Modes", "<-- Back to Main Menu"]
                            choice = buttonbox(msg, title, choices, image=image)
                            if choice == "Yes":
                                sys.exit(0)

                            if choice == "No":
                                set_or_change_password()
                                
                            if choice == "<-- Back to Change User and Group Modes":
                                change_user_modes()

                            if choice == "<-- Back to Main Menu":
                                main_menu()
                                
                            else:
                                set_or_change_password()

                    set_or_change_password()

                if choice == "<-- Back to Main Menu":
                    main_menu()

                if choice == "EXIT PROGRAM":
                    image = "warning.png"
                    msg = "Do you want to Quit the Program?"
                    title = "Quit Program?"
                    choices = ["Yes", "No"]
                    choice = buttonbox(msg, title, choices, image=image)
                    if choice == "Yes":
                        sys.exit(0)

                    if choice == "No":
                        change_user_modes()
                        
                    else:
                        change_user_modes()

             change_user_modes()
   
        if choice == "EXIT PROGRAM":
            exit_program()

        else:
            main_menu()
                
    
    main_menu()
