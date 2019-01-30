import pandas as pd
class simp():
    def __init__(self):
       pass
    def read_in(self,file):
        sheet = pd.read_excel(file)
        sheet.set_index('Cct',inplace = True)
        sheet.columns = [c.replace(' ', '_').replace('-','_').replace('/','_') for c in sheet.columns]
        sheet['A_end_PoP_CLS'] = sheet['A_end_PoP_CLS'].str.split(' / ')
        sheet['Z_end_PoP_CLS'] = sheet['Z_end_PoP_CLS'].str.split(' / ')
        sheet['Item_Subcategory_(Cable_Route)'] = sheet['Item_Subcategory_(Cable_Route)'].str.translate(str.maketrans('+','/'))
        sheet['Item_Subcategory_(Cable_Route)'] = sheet['Item_Subcategory_(Cable_Route)'].str.split('/')

        self.sheetcopy = sheet.copy()
        return self.sheetcopy
        
    def simplifier(self,user):
        for item in user:
            self.sheetcopy = self.sheetcopy.loc[self.sheetcopy[item[0]].isin([item[1]])]
        return self.sheetcopy
    
    def POP_exception_A_end(self,info):
        for location in self.sheetcopy.index.values:
            if info not in self.sheetcopy.loc[location]['A_end_PoP_CLS']:
                self.sheetcopy.drop([location],inplace=True)
        return self.sheetcopy
    
    def POP_exception_Z_end(self,info):
        for location in self.sheetcopy.index.values:
            if info not in self.sheetcopy.loc[location]['Z_end_PoP_CLS']:
                self.sheetcopy.drop([location],inplace=True)
        return self.sheetcopy
    
    def cable_exception(self,info):
        for location in self.sheetcopy.index.values:
            if info not in self.sheetcopy.loc[location]['Item_Subcategory_(Cable_Route)']:
                self.sheetcopy.drop([location],inplace = True)
        return self.sheetcopy

    def list_out(self,info):
        print(self.sheetcopy[info])
        
    def find_Cct(self,cct):
        print(self.sheetcopy.loc[cct])
    
    def show(self):
        return self.sheetcopy
# a = simp("C:/Users/jeffr/Desktop/PCCWExcel/pccwsheet.xlsx")
# print(a.show())