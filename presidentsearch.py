from lib2to3.pytree import convert


dic={
    "abdelmadjid tabboune" : "algeria",
    "joao lourenco" : "angola",
    "patrice talon" :"benin",
    "mokgweetsi masisi" : "botswana",
    "paul biya"  : "cameroon",
    "idriss" : "chad",
    "macky sall" : "senegal",
    "Paul kagame": "rwanda"
}
presidentname=input("enter a presidentname:") 
for a,b in dic.items():
    if a.lower()==presidentname.lower():
        print("the country is", b)
        print(a)

        

