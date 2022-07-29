import json
# import pandas as pd

def dictToJson(dict, fileName):
  with open("JsonFiles/{}.json".format(fileName), "w") as outfile:
    json.dump(dict, outfile)

# def jsonToExcel(jsonFile, excelFile):
#   pd.read_json(jsonFile).to_excel('{}.xlsx'.format(excelFile))

# def dictToExcel(dict, fileName):
#   dataFrame = pd.DataFrame(dict).T 
#   dataFrame.to_excel("{}.xls".format(fileName))