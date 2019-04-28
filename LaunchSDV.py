import os
import time
import wmi

stardew_executable = 'explorer \"steam://rungameid/413150\"'
save_folder = "SharedFile"



#install dependencies
os.system("pip install wmi")
os.system("pip install pypiwin32")



# execute commands to move git file to save files
os.system("git fetch https://github.com/GregorSmirnow96/StardewXmlTracker/")
time.sleep(5)
os.system("xcopy " + save_folder + " %appdata%\\StardewValley\\Saves\\" + save_folder + " /Y /s")
time.sleep(2)



# var = launch process
os.system(stardew_executable)
time.sleep(30)



# while process is running do nothing
c = wmi.WMI ()
game_is_running = True
while (game_is_running):
    for process in c.Win32_Process ():
        game_is_running = "Valley" in process.Name
print("App closed")



# copy updated xml to local branch
os.system("xcopy %appdata%\\StardewValley\\Saves\\" + save_folder + " " + save_folder + " /Y /s")
time.sleep(2)


# execute git push
os.system("git add .")
os.system("git commit -m \'Updating xml.\'")
os.system("git push --set-upstream origin master")



