import pandas as pd

#def readExcel(label,header):
# df = pd.read_excel("Datasheet1.xlsx",sheet_name="DevopsUniv")
# print(df.head())
#
# val = df.loc[df['Label'] == "Microsoft","URL"].values[0]
# print(val)

def readExcel(label,header):
    df = pd.read_excel("Datasheet1.xlsx", sheet_name="DevopsUniv")
    print(df.head())

    val = df.loc[df['Label'] == label, header].values[0]
    return val

print(readExcel("Amazon","Username"))

'''
advantages of using pandas

Faster Performance
Easier Manipulation
'''
