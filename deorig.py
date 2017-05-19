"""
Sims 4 Python File Decompiler Automation Script
Requires unpyc3

Type "import de" then "de.domagic()" in the Python console (with this file in your Python directory) and it will do its magic!
Don't forget to set the folder names (they're in all caps because I like the Caps Lock key)!!111!

by Miguel Leiva-Gomez
"""




import os
import subprocess
from unpyc3 import decompile

SIMS4_FOLDER = "C:\\Program Files (x86)\\Electronic Arts\\The Sims 4"
TEMPDIR = "C:\\Temp"
ZIPPROGRAM = "C:\\Program Files\\7-Zip\\7z.exe"

CurrentFolder = None

def extract_sims_archive(name):
	#subprocess.call(ZIPPROGRAM + " x \"" + SIMS4_FOLDER + "\\Data\\Simulation\\Gameplay\\" + name + ".zip\" -o" + "\"" + TEMPDIR + "\\" + name + "\"")
        print("DEV")
def domagic():
	#extract_sims_archive("base")
	#extract_sims_archive("core")
	#extract_sims_archive("simulation")
	rundecompile()
	
def outputwhatever():
	print(ZIPPROGRAM + " x \"" + SIMS4_FOLDER + "\\Data\\Simulation\\Gameplay\\" + "base" + ".zip\" -o" + TEMPDIR)
	
def rundecompile():
	for root, dirs, files in os.walk(TEMPDIR):
		for name in files:
			if ".pyo" in name:
				dodecompile(name, root)

def dodecompile(name, currentfolder):
	try:
		fullpath = currentfolder + "\\" + name
		print("Decompiling " + fullpath)
		decompiledstring = str(decompile(fullpath))
		newfilename = name.replace(".pyo", ".py")
		newpath = currentfolder + "\\" + newfilename
		file = open(newpath, "w")
		file.write(decompiledstring)
		file.close()
		os.remove(os.path.join(currentfolder, name))
	except Exception as exc:
                print("Excepted: "+str(exc))
                pass 
