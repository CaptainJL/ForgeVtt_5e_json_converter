import unittest
import jsonpath




def load_value_direct(json_data, key):
    if key in pdf_to_json_mapping:
        json_string = jsonpath.jsonpath(json_data, '$.system.abilities.str')[0]




def pdf_decode_value(json_data, key):
    if key in pdf_to_json_mapping:        
        if pdf_to_json_mapping[key] is not None:
            print(key, pdf_to_json_mapping[key])
            output = jsonpath.jsonpath(json_data, pdf_to_json_mapping[key])[0]
            return output


pdf_to_json_mapping = {
    "ClassLevel": None,
    "Background": None,
    "PlayerName": None,
    "CharacterName": None,
    "Race": None,
    "Alignment": None,
    "XP": None,
    "Inspiration": None,
    "(STR)": "$.system.abilities.str.value",
    "ProfBonus": None,
    "AC": None,
    "Initiative": None,
    "Speed": None,
    "PersonalityTraits": None,
    "STRmod": None,
    "ST Strength": None,
    "DEX": None,
    "Ideals": None,
    "DEXmod": None,
    "Bonds": None,
    "CON": None,
    "HDTotal": None,
    "CheckBox12": None,
    "CheckBox13": None,
    "CheckBox14": None,
    "CONmod": None,
    "CheckBox15": None,
    "CheckBox16": None,
    "CheckBox17": None,
    "HD": None,
    "Flaws": None,
    "INT": None,
    "ST Dexterity": None,
    "ST Constitution": None,
    "ST Intelligence": None,
    "ST Wisdom": None,
    "ST Charisma": None,
    "Acrobatics": None,
    "Animal": None,
    "Athletics": None,
    "Deception": None,
    "History": None,
    "WpnName": None,
    "Wpn1AtkBonus": None,
    "Wpn1Damage": None,
    "Insight": None,
    "Intimidation": None,
    "WpnName2": None,
    "Wpn2AtkBonus": None,
    "WpnName3": None,
    "Wpn3AtkBonus": None,
    "CheckBox11": None,
    "CheckBox18": None,
    "CheckBox19": None,
    "CheckBox20": None,
    "CheckBox21": None,
    "CheckBox22": None,
    "INTmod": None,
    "Wpn2Damage": None,
    "Investigation": None,
    "WIS": None,
    "Arcana": None,
    "Perception": None,
    "WISmod": None,
    "CHA": None,
    "Nature": None,
    "Performance": None,
    "Medicine": None,
    "Religion": None,
    "Stealth": None,
    "CheckBox23": None,
    "CheckBox24": None,
    "CheckBox25": None,
    "CheckBox26": None,
    "CheckBox27": None,
    "CheckBox28": None,
    "CheckBox29": None,
    "CheckBox30": None,
    "CheckBox31": None,
    "CheckBox32": None,
    "CheckBox33": None,
    "CheckBox34": None,
    "CheckBox35": None,
    "CheckBox36": None,
    "CheckBox37": None,
    "CheckBox38": None,
    "CheckBox39": None,
    "CheckBox40": None,
    "Persuasion": None,
    "HPMax": None,
    "HPCurrent": None,
    "HPTemp": None,
    "Wpn3Damage": None,
    "SleightofHand": None,
    "CHamod": None,
    "Survival": None,
    "AttacksSpellcasting": None,
    "Passive": None,
    "CP": None,
    "ProficienciesLang": None,
    "SP": None,
    "EP": None,
    "GP": None,
    "PP": None,
    "Equipment": None,
    "FeaturesAndTraits": None
}



















