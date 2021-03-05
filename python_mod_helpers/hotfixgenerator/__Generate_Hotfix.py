"""
This program was heavly based on apocalyptech bl3mods/python_mod_help
Link to current reposatory: https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers
apocalyptech has written most all functions that I am using. All I am doing is making
a interface for people to use.

At the time of coding this there is nothing like a BLCMM or other tools to make the hotfix for you, 
so you have to manually enter all data in order for it to work, and even then my coding my be off in some way.

BL3 is still in its modding infancy so if this program becomes obsolete in the future, well I still found it a great experience
making this and I hope BL3 live as long as BL2 did, as they are tied for some of my favorite games of all times
"""
from bl3hotfixmod import Mod
from bl3data import BL3Data
from _global_lists import NonUsedInfo, List_1, List_2, Mod_Header, Reg_hotfix, Search_Results, FileNames, File_Results_List
################################################################################################################################################################
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
#Global variables
DATA = BL3Data()
################################################################################################################################################################
# I have to put the program like this because in order to make hotfixes in the way 
# the bl3data/bl3hotfixmod work, it has to be executed in a row in order to work
def Create_HotFix_File():
    #this firat part puts the header inside a new file it creats
    if len(Mod_Header) < 6:
        # If you don't give it someting, this is what I will replace it with
        Mod_Header.extend(["Chadd", "Chadd", "Chadd",
                           "Chadd", "Chadd", "Chadd"])
    input1 = Mod_Header[0]
    input2 = Mod_Header[1]
    input3 = Mod_Header[2]
    input4 = Mod_Header[3]
    input5 = Mod_Header[4]
    input6 = Mod_Header[5]
    mod = Mod(input1 + '.bl3hotfix', input2, input3,
              [input4, ], lic=Mod.CC_BY_SA_40, v=input5, cats=input6,)
    i = 0
    if i > len(Reg_hotfix):
        None
    else:
        while i < len(Reg_hotfix):
            input1 = Reg_hotfix[i], input2 = Reg_hotfix[i+1], input3 = Reg_hotfix[i+2], input4 = Reg_hotfix[i+3], input5 = Reg_hotfix[i+4], input6 = Reg_hotfix[i+5],
            if input1 == "patch":
                input1 = mod.PATCH
            elif input1 == "level":
                input1 = mod.LEVEL
            elif input1 == "earlylevel":
                input1 = mod.EARLYLEVEL
            elif input1 == "char":
                input1 = mod.CHAR
            mod.reg_hotfix(input1, input2, input3, input4, input5, input6)
            i += 6
################################################################################################################################################################
#This swill put all your results into a list that you can look at later
# Now it will search for all items related to it regardless of capitalization or puncuation
def Search(input):
    info = DATA.get_refs_from_data(input)
    for details in info:
        if details[0] not in List_1:
            Search_Results.append(details[0])
################################################################################################################################################################
# the user is able to choose a json file and search through the contents
def FileChoice():
    Tk().withdraw()
    file = askopenfilename(filetypes=[("Choose file", ".json")])
    # Removes the files extention, as we dont need it
    raw_path = os.path.splitext(file)[0]
    i = 0
    index = 0
    # What this will do is that the program will search for a game file related to what I have specified,
    # Then it will grab the index of that found search, and then procede to disregard everything before
    # The index, and only grab what is needed to search for things
    if os.path.exists(file) == True:
        while index <= 0:
            Find = "/" + FileNames[i]
            i += 1
            if Find in raw_path:
                index = raw_path.find(Find)
        # this is the data we need to pass in information
        True_Path = raw_path[index::]
        # JSONInfo(True_Path)
        JSONInfo(True_Path, "", "", 1)

#This will be used to choose a selection choice from the file you have chosen
def WindowSel(proper_path, info, check):
    Testwindow = Tk()
    Testwindow.title("JSON File Content Display")
    w = 200
    h = 200
    ws = Testwindow.winfo_screenwidth()
    hs = Testwindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    if check == 1:
        Testwindow.geometry('%dx%d+%d+%d' % (w, h, x/4, y/4))
        Lb1 = Listbox(Testwindow, width=50)
        k = 1
        for i in List_1:
            Lb1.insert(k, i)
            k += 1
        Lb1.pack()
        testing = Button(Testwindow, text="Select One", font=("Times New Roman", 14),
                         command=lambda: JSONInfo(proper_path, Lb1.get(ANCHOR), "", 2))
        testing.pack()
    elif check == 2:
        Testwindow.geometry('%dx%d+%d+%d' % (w, h, x*1.8, y/4))
        Lb2 = Listbox(Testwindow, width=50)
        k = 1
        for i in List_2:
            Lb2.insert(k, i)
            k += 1
        Lb2.pack()
        testing = Button(Testwindow, text="Click And Look At \nClick To Look At Stored information", font=("Times New Roman", 14),
                         command=lambda: JSONInfo(proper_path, info, Lb2.get(ANCHOR), 3))
        testing.pack()

#This is what parses the data that will be used to displayed
def JSONInfo(proper_path, info, Choice, check):
    Parent = DATA.get_data(proper_path)
    i = 0
    if check == 1:
        while i < len(Parent):
            for pool in Parent[i]:
                if pool not in NonUsedInfo:
                    List_1.append(pool)
            i += 1
        WindowSel(proper_path, "", 1)
    elif check == 2:
        Child = Parent[0][info]
        for pool in Child[i]:
            if pool not in NonUsedInfo:
                List_2.append(pool)
            i += 1
        WindowSel(proper_path, info, 2)
    elif check == 3:
        for pool in Parent[0][info]:
            File_Results_List.append(pool[Choice][1])
################################################################################################################################################################
#This was me messing around with how these things work. still learning though
# mod.reg_hotfix(
# mod.LEVEL,
# "Anger_P",
# "/Game/GameData/Regions/RegionManagerData.RegionManagerData",
# "PlayThroughs.PlayThroughs[0].bGameStageTracksPlayerLevelAboveMinimum",
# "True",
# "")

# mod.reg_hotfix(mod.EARLYLEVEL,
# "MatchALL",
# "/Game/GameData/Balance/HealthAndDamage/HealthBalanceScalers/DataTable_DamageAndHealthScalers.DataTable_DamageAndHealthScalers",
# "AI_AdditionalDamagePerLevel,Scaler_4_FE2B037B42E1F6E76E3AEBAFDCC8DB86",
# "0.065",
# "")


#F:\Users\Trevor\Desktop\extracted_new\Game\GameData\Regions\RegionManagerData.json