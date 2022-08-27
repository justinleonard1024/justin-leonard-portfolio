"""
	Directory Clone
	DirectoryClone.py
	Created by Justin Leonard

	Copies an entire directory and all files in the subdirectories to a seperate folder.
	The resulting folder will contain empty versions of the source files besides basic file info.
	The only files that will be untouched will be files that have the files extensions to ignore.

	If the program mode is normal, all files will be copied normally
	If the program mode is blank, all files will be copied with blank versions of the originals
	If the program mode is ignore, all files that don't have the ignored extensions will be blank copied and the rest normal copied
	If the program mode is used, all files that only have the extensions will be normal copied
"""

# import
import os, sys, time, shutil
from stat import *
from time import localtime, strftime

# definitions
MODE_NORMAL = 0
MODE_BLANK = 1
MODE_IGNORE = 2
MODE_USED = 3

# program mode
# MODE_NORMAL -> This is a pure copy. All files will be copied and not modified
# MODE_BLANK -> All files (even the ignored extensions) are copied into blank files
# MODE_IGNORE -> Only the files that have extensions that are not ignored will be copied
# MODE_USED -> Only the files that have extensions will be normal copied
PROGRAM_MODE = MODE_NORMAL

# variables
sourceDir = r"<Source Directory>"
targetDir = r"<Target Directory>"
programMode = ""
stringCreated = ""
stringModified = ""
stringAccessed = ""
countMain = 0
unprocessedFiles = []
fileExtensionsIgnore = []
fileExtensionsUsed = [".txt"]

# check dirs
if not os.path.isdir(sourceDir):
    print "Error: Source directory doesn't exist"
    sys.exit()
    
if not os.path.isdir(targetDir):
    print "Error: Target directory doesn't exist"
    sys.exit()
    
if (sourceDir == targetDir):
    print "Error: Source directory and target directory are the same"
    sys.exit()

# initial display
if (PROGRAM_MODE == MODE_NORMAL):
    programMode = "Normal"
elif (PROGRAM_MODE == MODE_BLANK):
    programMode = "Blank"
elif (PROGRAM_MODE == MODE_IGNORE):
    programMode = "Ignore"
elif (PROGRAM_MODE == MODE_USED):
    programMode = "Used"

print "********************************\r\n\r\nDirectory Clone\r\nCreated by Justin Leonard\r\n\r\nProgram Mode: %s"%(programMode)
if (PROGRAM_MODE == MODE_IGNORE):
    print "Ignored Extensions:\r\n"
    for ext in fileExtensionsIgnore:
        print "%s"%ext.replace(".","")
if (PROGRAM_MODE == MODE_USED):
    print "Used Extensions:\r\n"
    for ext in fileExtensionsUsed:
        print "%s"%ext.replace(".","")
print "\r\n\r\n\r\nFile List:\r\n"

# program mode normal
if (PROGRAM_MODE == MODE_NORMAL):
    for path, subdirs, files in os.walk(sourceDir):
        for filename in files:
         # source and target files
         originalFile = os.path.join(path, filename)
         newFile = os.path.join(path.replace(sourceDir,targetDir), filename)

         # copy files
         if os.path.isfile(originalFile):
             # file is in new directory
             if not os.path.isdir(path.replace(sourceDir,targetDir)):
                 os.makedirs(path.replace(sourceDir,targetDir))

             # copy original file
             shutil.copy(originalFile, newFile)
         else:
            unprocessedFiles.append(originalFile)
            
         # display progress
         countMain += 1
         print "Processed (%d) \"%s\""%(countMain,os.path.join(path, filename).replace(sourceDir + "\\",""))

# program mode blank
elif (PROGRAM_MODE == MODE_BLANK):
    for path, subdirs, files in os.walk(sourceDir):
        for filename in files:
         # source and target files
         originalFile = os.path.join(path, filename)
         newFile = os.path.join(path.replace(sourceDir,targetDir), filename)

         # file info setup
         if(os.path.getctime(originalFile) > 0):
             stringCreated = strftime("%a, %b %d %Y %I:%M:%S %p", localtime(os.path.getctime(originalFile)))
         else:
             stringCreated = "None"
             
         if(os.path.getmtime(originalFile) > 0):
             stringModified = strftime("%a, %b %d %Y %I:%M:%S %p", localtime(os.path.getmtime(originalFile)))
         else:
             stringModified = "None"
             
         if(os.path.getatime(originalFile) > 0):
             stringAccessed = strftime("%a, %b %d %Y %I:%M:%S %p", localtime(os.path.getatime(originalFile)))
         else:
             stringAccessed = "None"

         # file info
         strFileStats = "Name: " + filename + "\r\n" + \
                        "Full Path: " + originalFile + "\r\n\r\n" + \
                        "Size: " + str(os.path.getsize(originalFile)) + " Bytes\r\n" + \
                        "Created: " + stringCreated + "\r\n" + \
                        "Modified: " + stringModified + "\r\n" + \
                        "Accessed: " + stringAccessed + "\r\n"

         # copy files
         if os.path.isfile(originalFile):
             # file is in new directory
             if not os.path.isdir(path.replace(sourceDir,targetDir)):
                 os.makedirs(path.replace(sourceDir,targetDir))

             # create new blank file
             curFile = open(newFile, "w+")
             curFile.write(strFileStats)
             curFile.close()
         else:
            unprocessedFiles.append(originalFile)
            
         # display progress
         countMain += 1
         print "Processed (%d) \"%s\""%(countMain,os.path.join(path, filename).replace(sourceDir + "\\",""))

# program mode ignore
elif (PROGRAM_MODE == MODE_IGNORE):
    for path, subdirs, files in os.walk(sourceDir):
        for filename in files:
         # source and target files
         originalFile = os.path.join(path, filename)
         newFile = os.path.join(path.replace(sourceDir,targetDir), filename)

         # file info setup
         if(os.path.getctime(originalFile) > 0):
             stringCreated = strftime("%a, %b %d %Y %I:%M:%S %p", localtime(os.path.getctime(originalFile)))
         else:
             stringCreated = "None"
             
         if(os.path.getmtime(originalFile) > 0):
             stringModified = strftime("%a, %b %d %Y %I:%M:%S %p", localtime(os.path.getmtime(originalFile)))
         else:
             stringModified = "None"
             
         if(os.path.getatime(originalFile) > 0):
             stringAccessed = strftime("%a, %b %d %Y %I:%M:%S %p", localtime(os.path.getatime(originalFile)))
         else:
             stringAccessed = "None"

         # file info
         strFileStats = "Name: " + filename + "\r\n" + \
                        "Full Path: " + originalFile + "\r\n\r\n" + \
                        "Size: " + str(os.path.getsize(originalFile)) + " Bytes\r\n" + \
                        "Created: " + stringCreated + "\r\n" + \
                        "Modified: " + stringModified + "\r\n" + \
                        "Accessed: " + stringAccessed + "\r\n"

         # copy files
         if os.path.isfile(originalFile):
             # file is in new directory
             if not os.path.isdir(path.replace(sourceDir,targetDir)):
                 os.makedirs(path.replace(sourceDir,targetDir))

             # check current file extension
             ignoreThisFile = False
             for ext in fileExtensionsIgnore:
                 if (os.path.splitext(filename)[1] == ext):
                     ignoreThisFile = True

             # the current file does not have an ignored extension (wipe file contents and replace with file info)
             if not ignoreThisFile:    
                 curFile = open(newFile, "w+")
                 curFile.write(strFileStats)
                 curFile.close()

             # the current file has an ignored extension (keep file contents the same)   
             else:
                shutil.copy(originalFile, newFile)
         else:
            unprocessedFiles.append(originalFile)
            
         # display progress
         countMain += 1
         print "Processed (%d) \"%s\""%(countMain,os.path.join(path, filename).replace(sourceDir + "\\",""))

# program mode used
elif (PROGRAM_MODE == MODE_USED):
    for path, subdirs, files in os.walk(sourceDir):
        for filename in files:
         # source and target files
         originalFile = os.path.join(path, filename)
         newFile = os.path.join(path.replace(sourceDir,targetDir), filename)

         # copy files
         if os.path.isfile(originalFile):
             # file is in new directory
             if not os.path.isdir(path.replace(sourceDir,targetDir)):
                 os.makedirs(path.replace(sourceDir,targetDir))

             # check current file extension
             useThisFile = False
             for ext in fileExtensionsUsed:
                 if (os.path.splitext(filename)[1] == ext):
                     useThisFile = True

             # the current file has the used extension (copy file)
             if useThisFile:
                shutil.copy(originalFile, newFile)
         else:
            unprocessedFiles.append(originalFile)
            
         # display progress
         countMain += 1
         print "Processed (%d) \"%s\""%(countMain,os.path.join(path, filename).replace(sourceDir + "\\",""))

# no program mode
else:
    print "\r\nNo program mode selected\r\n"

# final display
print "\r\nUnprocessed Files: %d\r\n"%len(unprocessedFiles)
if (len(unprocessedFiles) > 0):
    for unproc in unprocessedFiles:
        print "%s"%unproc
else:
    print "None"
print "\r\nAll %d files have been successfully processed.\r\n\r\n********************************"%(countMain)
