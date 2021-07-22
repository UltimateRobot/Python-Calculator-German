# Import needed Libs

from pathlib import Path
from datetime import datetime
import time
import sys
import os

# Ckeck for needed folders and get it ready

currentpath_w_cfgfld = (sys.argv[0].replace("main.py", "") + ("config"))
currentpath_w_logfld = (sys.argv[0].replace("main.py", "") + ("logs"))

cfgfld = Path(currentpath_w_cfgfld)
if cfgfld.is_dir():
    pass
else:
    print("No config folder found, creating one...")
    os.mkdir(currentpath_w_cfgfld)

logfld = Path(currentpath_w_logfld)
if logfld.is_dir():
    pass
else:
    print("No logs folder found, creating one...")
    os.mkdir(currentpath_w_logfld)

# Getting ready needed Vars

date_time = datetime.now().strftime('[%d.%m.%Y - %H:%M:%S] ')

# Check for Username file

username = Path(currentpath_w_cfgfld + "/username.cfg")
usrnmfile = currentpath_w_cfgfld + "/username.cfg"

if username.is_file():
    username = open(usrnmfile, 'r')
    usrnm = username.readline()
    username.close()

else:
    username = open(usrnmfile, 'w')
    usrnminp = str(input("Gebe bitte deinen Benutzernamen ein: "))
    username.write(str(usrnminp))
    username.close()
    username = open(usrnmfile, 'r')
    usrnm = username.readline()
    username.close()

# Startscreen, welcome Message

print("Willkommen zum Taschenrechner,",usrnm)
print("--------------------------------------------")
print("\n")

# Prepare File for result log

resultfile = Path(currentpath_w_logfld + "/result.log")

if resultfile.is_file():
    resultlog = open(resultfile, 'a')
    resultlog.write("\n")
    resultlog.write(str(date_time))

else:
    print("No logfile found creating one...")
    resultlog = open(resultfile, 'w')
    resultlog.close()
    resultlog = open(resultfile, 'a')
    resultlog.write("\n")
    resultlog.write(str(date_time))

# Inputs to variables if input is not int exit

try:
    n1 = int(input("Gebe die erste Zahl ein: "))
    print("\n")
    r = str(input("Gebe eine der folgenden Rechenoperationen ein (+ - * / ^): "))
    print("\n")
    n2 = int(input("Gebe nun die zweite Zahl ein: "))
    print("\n")
except:
    print("Invalide Zahl(n), der Taschenrechner wird beendet...")
    resultlog.write("Invalid input, end. (Zahlen)")
    time.sleep(5)
    sys.exit()

# Calc and Output

print("Das ergebnis ist:")

# +
if (r == "+"):
    print(n1 + n2)
    result = n1 + n2
    resultlog.write(str(result))

# -
elif (r == "-"):
    print(n1 - n2)
    result = n1 - n2
    resultlog.write(str(result))

# *
elif(r == "*"):
    print(n1 * n2)
    result = n1 * n2
    resultlog.write(str(result))

# ^
elif(r == "^"):
    print(n1 ** n2)
    result = n1 ** n2
    resultlog.write(str(result))

# /
elif(r == "/"):
    print(n1 / n2)
    result = n1 / n2
    resultlog.write(str(result))

# invalid
else:
    resultlog.write("Invalid input, end. (Rechenoperation)")
    print("Invalide Rechenoperation, Taschenrechner setzt ohne Ergebnis fort...")

# Close File, because not needed

resultlog.close()

# Check if user wants to see logfile and prepares for Y and N

print("\n")
logyn = str(input("Möchtest du die bisherigen Ergebnisse sehen? (Y/N): "))
print("\n")

# Y y
if (logyn == "Y"):
    resultlog = open(resultfile, 'r')
    print("Bisherige ergebnisse:")
    print(resultlog.read())
elif (logyn == "y"):
    resultlog = open(resultfile, 'r')
    print("Bisherige ergebnisse:")
    print(resultlog.read())

# N n
elif(logyn == "N"):
    print("exiting...")
elif(logyn == "n"):
    print("exiting...")

# invalid
else:
    print("Invalide Eingabe, Taschenrechner wird ohne anzeigen der Log-Datei beendet...")

print("\n")

time.sleep(5)