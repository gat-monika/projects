import json
import pickle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class SalesPrice():
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type):
        self.Item_Weight=Item_Weight
        self.Item_Fat_Content=Item_Fat_Content
        self.Item_Visibility=Item_Visibility
        self.Item_Type=Item_Type
        self.Item_MRP=Item_MRP
        self.Outlet_Identifier=Outlet_Identifier
        self.Outlet_Establishment_Year=Outlet_Establishment_Year
        self.Outlet_Size=Outlet_Size
        self.Outlet_Location_Type=Outlet_Location_Type
        self.Outlet_Type=Outlet_Type

        
    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)
        
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data=json.load(f)

    def get_predicted_sales(self):

        self.load_models()

        
        test_array=np.zeros(len(self.json_data['columns']))

        test_array[0]=self.Item_Weight
        test_array[1]=self.json_data["Item_Fat_Content"][self.Item_Fat_Content]
        test_array[2]=self.Item_Visibility
        test_array[3]=self.json_data["Item_Type"][self.Item_Type]
        test_array[4]=self.Item_MRP
        test_array[5]=self.json_data["Outlet_Identifier"][self.Outlet_Identifier]
        test_array[6]=self.Outlet_Establishment_Year
        test_array[7]=self.json_data["Outlet_Size"][self.Outlet_Size]
        test_array[8]=self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        test_array[9]=self.json_data["Outlet_Type"][self.Outlet_Type]
        

        charges = round(self.model.predict([test_array])[0],2)
        return f"{charges}"



if __name__=="__main__":
    Item_Weight=9.3
    Item_Fat_Content="Low Fat"
    Item_Visibility=0.016760
    Item_Type="Canned"
    Item_MRP=249.809
    Outlet_Identifier="OUT019"
    Outlet_Establishment_Year=2019
    Outlet_Size="Medium"
    Outlet_Location_Type="Tier 3"
    Outlet_Type="Supermarket Type1"

    med_ins = SalesPrice(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
    charges = med_ins.get_predicted_sales()
    
    print(f"predicted Item Outlet Sales:{charges} ")
