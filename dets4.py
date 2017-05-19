import os, platform, time
import threading
import subprocess, sys, color
from unpyc3 import decompile
import quicklib as quicklib
from lib.colorama import init
THREADING_ENABLED = True
THREADS = 2
THRS = []
TH_FILES = []
DEBUG=False

SIMS4_FOLDER = "nf"
TEMPDIR = "C:\\Temp"
ZIPPROGRAM_base = "7z\\"
ZIPPROGRAM = "7z\\7za.exe"
if(quicklib.Is64Windows):
    ZIPPROGRAM = "lib\\7z\\x64\\7za.exe"
    if(platform.architecture()[0] == '32bit'):
        print(color.cyan_bg("We Suggest you from using 64 bit python for faster results!"))
CurrentFolder = None
if os.path.isdir(TEMPDIR):
    os.mkdir(TEMPDIR)
    #print("DEV")
def extract_sims_archive(name):
    if DEBUG:
        print(ZIPPROGRAM + " x \"" + SIMS4_FOLDER + "\\Data\\Simulation\\Gameplay\\" + name + ".zip\" -o" + "\"" + TEMPDIR + "\\" + name + "\"")
    subprocess.call(ZIPPROGRAM + " x \"" + SIMS4_FOLDER + "\\Data\\Simulation\\Gameplay\\" + name + ".zip\" -o" + "\"" + TEMPDIR + "\\" + name + "\"")
    #
    #print("DEV")
def execute():
    global SIMS4_FOLDER
    global TEMPDIR
    global THREADING_ENABLED
    global THREADS
    global DEBUG
    if len([s for s in sys.argv if "debug" in s]) >= 1:
        DEBUG = True;
    init()
    print(color.green("Welcome to FastDec for The Sims 4"))
    print(color.green_bg("Made By GabrielTK with ") +color.red_bg("<3")+color.green_bg(" in SP"))
    print(color.green("Please, answer the questions below to set-up settings (in future, a config file will be accepted): "))
    print(color.magenta_bg("Please, Where is your \"The Sims 4\" game folder located??"))
    if os.path.isdir("C:\\Program Files\\Origin Games\\The Sims 4\\"):
        SIMS4_FOLDER = "C:\\Program Files\\Origin Games\\The Sims 4\\"
        print(color.cyan_bg("Found at "+SIMS4_FOLDER))
    elif os.path.isdir("C:\\Program Files (x86)\\Origin Games\\The Sims 4\\"):
        SIMS4_FOLDER = "C:\\Program Files (x86)\\Origin Games\\The Sims 4\\"
        print(color.cyan_bg("Found at "+SIMS4_FOLDER))
    elif os.path.isdir("C:\\Program Files\\Eletronic Arts\\The Sims 4\\"):
        SIMS4_FOLDER = "C:\\Program Files\\Eletronic Arts\\The Sims 4\\"
        print(color.cyan_bg("Found at "+SIMS4_FOLDER))
    elif os.path.isdir("C:\\Program Files (x86)\\Eletronic Arts\\The Sims 4\\"):
        SIMS4_FOLDER = "C:\\Program Files (x86)\\Eletronic Arts\\The Sims 4\\"
        print(color.cyan_bg("Found at "+SIMS4_FOLDER))
    if SIMS4_FOLDER != "nf":
        print(color.cyan_bg("Leave it blank to use found value"))
    s4i = input("> ")
    if s4i == "" and SIMS4_FOLDER == "nf":
        print(color.yellow_bg("Please type something... Don't leave me alone"))
        return;
    elif not os.path.isdir(SIMS4_FOLDER):
        print(color.yellow_bg("This does not exist or isn't a folder!"))
        return;
    elif not SIMS4_FOLDER:
        SIMS4_FOLDER = s4i
    print(color.magenta_bg("Please, Where is desired output folder?")+" "+color.red_bg("IT MUST NOT EXIST, AS THE DECOMPILER WILL CREATE IT"))
    TEMPDIR = input("> ")
    print(color.magenta_bg("Do you want us to use ")+color.cyan_bg("SUPER COW SPEED")+color.magenta_bg(" (multi-threading) - 0 = NO; 1= YES"))
    THREADING_ENABLED = bool(input("> "))
    if THREADING_ENABLED:
        print(color.magenta_bg("How many threads do you want us to use? (How many files to process at the same time, basically). "))
        THREADS = int(input("> "))
    print(color.green_bg("Press enter to Start!"))
    #DO:
    extract_sims_archive("base")
    extract_sims_archive("core")
    extract_sims_archive("simulation")
    rundecompile()
    print(color.green_bg("Done! The Files were already processed! Thanks for Using FastDec for TS4! Made By GabrielTK with ") +color.red_bg("<3")+color.green_bg(" in SP"))

def outputwhatever():
    print(ZIPPROGRAM + " x \"" + SIMS4_FOLDER + "\\Data\\Simulation\\Gameplay\\" + "base" + ".zip\" -o" + TEMPDIR)
def decompRoutine(arr):
    for root, dirs, files in arr:
        for name in files:
            if ".pyo" in name:
                dodecompile(name, root)

def rundecompile():
    if THREADING_ENABLED == False:
           decompRoutine(list(os.walk(TEMPDIR)))
    else:
        global TH_FILES
        global THRS
        print(color.green_bg("[Threading] Computing Files..."))
        files = list(os.walk(TEMPDIR))
        TH_FILES = split_list(files)
        for filelist in TH_FILES:
            THRS.append(threading.Thread(target=decompRoutine, args=([filelist])))
        print(color.green_bg("[Threading] Starting..."))

        for thread in THRS:
            thread.start()
        localtf = 99
        while localtf != 0:
            localtf = 0
            for thread in THRS:
                localtf = localtf + int(thread.isAlive)
            #print (localtf)
            #time.sleep(5)

def dodecompile(name, currentfolder):
    try:
        fullpath = currentfolder + "\\" + name
        print("Decompiling " + fullpath)
        decompiledstring = str(decompile(str(fullpath)))
        newfilename = name.replace(".pyo", ".py")
        newpath = currentfolder + "\\" + newfilename
        file = open(newpath, "w")
        file.write(decompiledstring)
        file.close()
        os.remove(os.path.join(currentfolder, name))
    except Exception as exc:
        if DEBUG:
            print(color.magenta_bg("Excepted: "+str(exc)))
        pass
def split_list(arr):




    return [arr[i::THREADS] for i in range(THREADS)]
if __name__ == '__main__':
    execute()
