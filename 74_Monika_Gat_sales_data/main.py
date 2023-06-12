from flask import Flask,jsonify,render_template,request

from project_app.utils import SalesPrice

app=Flask(__name__)

@app.route("/")
def hello_flask():
    print("welcome to the Sales price Prediction")
    return render_template("index.html")

@app.route("/predict_charges",methods=["POST","GET"])
def get_insurance_charges():
    
    if request.method=="GET":
        print("we are in the GET method")

        Item_Weight = float(request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_Type = request.args.get("Item_Type")
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Establishment_Year = int(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Outlet_Type = request.args.get("Outlet_Type")

  
 

        
        med_ins = SalesPrice(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Item_MRP,Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
        charges = med_ins.get_predicted_sales()

        return render_template("index.html",prdiction=charges)
        
    


print("__name__-->",__name__)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5005,debug=False)