# Start of script
"""
This script defines the positions for the software communities government.
"""
bannedPositionList = ["Dictator", "Führer", "Killer"]
starterPositionList = ["Employee", "Volunteer", "Apprentice", "Contributer"]
middlePositionList = ["Project manager", "Group leader", "Professional contributer"]
highPositionList = ["CEO", "Founder", "Owner", "Leader", "Manager", "Chairman"]
print("Position viewer")
loopI = str("forever")
try: # The main script that forever asks for an ID for a position group
  while (loopI == "forever"):
    print("Banned positions - X | Starter positions - S | Middle positions - M | Top positions - T")
    searchX = str(input("Type a code for the position: "))
    searchX = searchX.upper()
    if (searchX = "X"):
      print(bannedPositionList)
    elif (searchX = "S"):
      print(starterPositionList)
    elif (searchX = "M"):
      print(middlePositionList)
    elif (searchX = "T"):
      print(highPositionList)
    else:
      print("Invalid code entered. Please try again")
      print("You entered: " + str(searchX))
except: # The alternate script that shouldn't ever be reached, activates when the forever loop ends
  while not (loopI == "forever"):
    print("A fatal error has occurred. The program will now close")
    print("You can research the error online: 0x0A - forever loop reached an end")
    noMoreExit = input("Press [ENTER] key to quit")
    print("The program should be closed. If it still isn't, click the close button, or use a process manager to end the task")
print("---")
"""
Script info
File type: Python script
File version: 1 (Thursday, July 23rd 2020 at 12:50 pm)
Line count (including blank lines and compiler line): 42

"""
# End of script
