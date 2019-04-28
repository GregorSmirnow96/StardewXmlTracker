import os
import time
import wmi

stardew_executable = 'explorer \"steam://rungameid/413150\"'



#install dependencies
os.system("pip install wmi")
os.system("pip install pypiwin32")



# execute command to pull from git



# var = launch process
os.system(stardew_executable)
time.sleep(5)



# while process is running do nothing
c = wmi.WMI ()
grame_is_running = True
while (grame_is_running):
    for process in c.Win32_Process ():
        grame_is_running = "Valley" in process.Name
print("App closed")


# execute git push