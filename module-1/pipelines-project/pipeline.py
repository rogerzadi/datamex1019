import pandas as pd
shark=pd.read_csv("sharks.csv")
import re

def limpiezaDate (shark):
    pattern = '\d+-\w+-\d+'

    def eli(text):
        sep = re.findall(pattern, text)[0].split('-')
        sep.pop(2)
        return '-'.join(sep)

    def det(text):
        r = re.findall(pattern, text)
        return r != []

    colDate1 = []

    for x in colDate:
        if det(x) == True:
            f = eli(x)
            colDate1.append(f)
        else:
            f1 = x
            colDate1.append("-")

    shark_clean["Date"] = colDate1
def limpiezaSpecies ():
    pattern1 = ("\d+|shark|'|,")

    def sup(te):
        r = re.sub(pattern1, '', te)
        return r

    shark_clean["Species "].fillna('UNKNOWN', inplace=True)
    shark_clean["Species "] = shark_clean["Species "].apply(sup)
    shark_clean["Species "] = shark_clean["Species "].str.upper()

    def cleaningS(text):
        if "WHIT" in text:
            s = "WHITE"
        elif "TIGE" in text:
            s = "TIGER"
        elif "GRE" in text:
            s = "GREY"
        elif "BLUE" in text:
            s = "BLUE"
        elif "BULL" in text:
            s = "BULL"
        elif "NURSE" in text:
            s = "NURSE"
        elif "MAKO" in text:
            s = "MAKO"
        elif "HAMMER" in text:
            s = "HAMMERHEAD"
        elif "BLACK" in text:
            s = "BLACKTIP"
        elif "WOBBE" in text:
            s = "WOBBEGONG"
        elif "ZAMB" in text:
            s = "ZAMBESI"
        elif "RAGGE" in text:
            s = "RAGGEDTOOTH"
        elif "BRONZE" in text:
            s = "BRONZE WHALER"
        elif "LEMON" in text:
            s = "LEMON"
        elif "SHOVE" in text:
            s = "SHOVELNOSE"
        else:
            s = "UNKNOWN"
        return s

    shark_clean["Species "] = shark_clean["Species "].apply(cleaningS)
def limpiezaType ():
    shark_clean.Type = shark_clean.Type.str.replace('Boating', 'Boat')
def limpiezaCountry ():
    shark_clean.Country.fillna('UNKNOWN', inplace=True)
    pattern2 = ("\s$|^\s|$\?|\(")

    def sup1(te):
        r = re.sub(pattern2, '', te)
        return r

    shark_clean.Country = shark_clean.Country.apply(sup1)

    pattern3 = ("\s/\s")

    def sup2(te1):
        r = re.sub(pattern3, ' ', te1)
        return r

    shark_clean.Country = shark_clean.Country.apply(sup2)
    shark_clean.Country = shark_clean.Country.str.replace('MAARTIN', 'MARTIN').str.replace('?', '').str.replace(
        'BETWEEN ', '')
    shark_clean.Country = shark_clean.Country.str.replace('COAST OF ', '')
    shark_clean.Country = shark_clean.Country.str.upper().str.replace(" UAE", '')
def limpiezaArea ():
    shark_clean.Area.fillna('UNKNOWN', inplace=True)
    patternA = ('\d+|^\s|\s$|"|\)|,')

    def supA(te):
        r = re.sub(patternA, '', te)
        return r

    shark_clean.Area = shark_clean.Area.apply(supA)

    shark_clean.Area = shark_clean.Area.str.replace('miles ', '').str.replace('PROVINE', 'PROVINCE')
    shark_clean.Area = shark_clean.Area.str.upper()
def limpiezaLocation ():
    shark_clean.Location.fillna('UNKNOWN', inplace=True)
    patternL = ('\s$|^\s|"|\)|,')

    def supL(te):
        r = re.sub(patternL, '', te)
        return r

    shark_clean.Location = shark_clean.Location.apply(supL)
def limpiezaActivity ():
    shark_clean.Activity.fillna('UNKNOWN', inplace=True)

    def cleaning(text):
        if "SWIMMING" in text:
            s = "SWIMMING"
        elif "FISHING" in text:
            s = "FISHING"
        elif "DIVING" in text:
            s = "DIVING"
        elif "SURF" or "SURFING" in text:
            s = "SURFING"
        else:
            s = text
        return s

    shark_clean.Activity = shark_clean.Activity.str.upper()
    shark_clean.Activity = shark_clean.Activity.apply(cleaning)
def limpiezaName ():
    shark_clean.Name.fillna('UNKNOWN', inplace=True)
    patternN = ("\s$|^\s|'|\d+")

    def supN(te):
        r = re.sub(patternN, "", te)
        return r

    shark_clean.Name = shark_clean.Name.apply(supN)

    def cleaningN(text):
        if "UNKNOWN" in text:
            s = "UNKNOWN"
        else:
            s = text
        return s

    shark_clean.Name = shark_clean.Name.apply(cleaningN)
    shark_clean.Name = shark_clean.Name.str.replace('male', "UNKNOWN").str.replace("males", "UNKNOWN").str.replace(
        'Anonymous', "UNKNOWN").str.replace("girl", "UNKNOWN")
    shark_clean.Name = shark_clean.Name.str.replace('boat', "UNKNOWN").str.replace("boy", "UNKNOWN").str.replace(
        'sailor', "UNKNOWN").str.replace("fishermen", "UNKNOWN")
def limpiezaSex ():
    shark_clean["Sex "].fillna('UNKNOWN', inplace=True)
    shark_clean["Sex "] = shark_clean["Sex "].str.replace('M ', "M").str.replace("lli", "UNKNOWN").str.replace(".","UNKNOWN")

def limpiezaInjury():
    shark_clean.Injury.fillna('UNKNOWN', inplace=True)
    shark_clean.Injury = shark_clean.Injury.str.upper()

    def cleaningI(text):
        if "BITTEN" in text:
            s = "BITTEN"
        elif "FATAL" in text:
            s = "FATAL"
        elif "LACERA" in text:
            s = "LACERATIONS"
        elif "INJUR" in text:
            s = "INJURY"
        elif "SEVERED" in text:
            s = "SEVERED"
        elif "SURVIVED" in text:
            s = "SURVIVED"
        elif "FOOT" or "LEG" in text:
            s = "DAMANGED LIMD"
        else:
            s = text
        return s

    shark_clean.Injury = shark_clean.Injury.str.replace('NO DETAILS', "UNKNOWN")
    shark_clean.Injury = shark_clean.Injury.apply(cleaningI)
def limpiezaAge():
    shark_clean.Age.fillna('0', inplace=True)
    patternA = ("\s$|^\s|'|\D")
    patternB = ("^\d{2}")

    def supAg(te):
        r = re.sub(patternA, "", te)
        return r

    shark_clean.Age = shark_clean.Age.apply(supAg)
def limpiezaFatal():
    shark_clean["Fatal (Y/N)"].fillna('UNKNOWN', inplace=True)

    patternF = ("\s$|^\s")

    def supFF(te):
        r = re.sub(patternF, "", te)
        return r

    def cleaningF(text):
        if "#VALUE!" in text:
            s = "UNKNOWN"
        else:
            s = text
        return s

    shark_clean["Fatal (Y/N)"] = shark_clean["Fatal (Y/N)"].str.replace('F', "UNKNOWN").str.replace('n', "N")
    shark_clean["Fatal (Y/N)"] = shark_clean["Fatal (Y/N)"].apply(supFF)
    shark_clean["Fatal (Y/N)"] = shark_clean["Fatal (Y/N)"].apply(cleaningF)
def limpiezaTime():
    shark_clean.Time.fillna('UNKNOWN', inplace=True)
    shark_clean.Time = shark_clean.Time.str.upper()

    def cleaningT(text):
        if "11" in text:
            s = "MORNING"
        elif "10" in text:
            s = "MORNING"
        elif "12" in text:
            s = "MORNING"
        elif "09" in text:
            s = "MORNING"
        elif "08" in text:
            s = "MORNING"
        elif "07" in text:
            s = "MORNING"
        elif "06" in text:
            s = "MORNING"
        elif "13" in text:
            s = "AFTERNOON"
        elif "14" in text:
            s = "AFTERNOON"
        elif "15" in text:
            s = "AFTERNOON"
        elif "16" in text:
            s = "AFTERNOON"
        elif "17" in text:
            s = "AFTERNOON"
        elif "18" in text:
            s = "EVENING"
        elif "19" in text:
            s = "EVENING"
        elif "20" in text:
            s = "EVENING"
        elif "21" in text:
            s = "EVENING"
        elif "22" in text:
            s = "EVENING"
        elif "NIGHT" in text:
            s = "EVENING"

        elif "MORN" in text:
            s = "MORNING"
        elif "AFTER" in text:
            s = "AFTERNOON"
        else:
            s = "UNKNOWN"
        return s

    shark_clean.Time = shark_clean.Time.apply(cleaningT)
def limpiezaInv():
    shark_clean["Investigator or Source"].fillna('UNKNOWN', inplace=True)
    shark_clean["Investigator or Source"] = shark_clean["Investigator or Source"].str.upper()
    shark_clean["Investigator or Source"] = shark_clean["Investigator or Source"].str.replace('\d+/\d+/\d+', "")

    def cleaningINV(text):
        if "GSAF" in text:
            s = "GSAF"
        elif "FSAF" in text:
            s = "FSAF"
        elif "TIME" in text:
            s = "TIME"
        elif "TIME" in text:
            s = "TIME"
        elif "NBC" in text:
            s = "NBC"
        else:
            s = text
        return s

    shark_clean["Investigator or Source"] = shark_clean["Investigator or Source"].apply(cleaningINV)
def limpiezatotal (Shark):
    limpiezaDate()
    limpiezaSpecies()
    limpiezaType()
    limpiezaCountry()
    limpiezaArea()
    limpiezaLocation()
    limpiezaActivity()
    limpiezaName()
    limpiezaSex()
    limpiezaInjury()
    limpiezaAge()
    limpiezaFatal()
    limpiezaTime()
    limpiezaInv()
    return Shark


