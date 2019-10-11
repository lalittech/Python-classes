from Model import *



class main():
    def __init__(self):
        print("Inside main class")
        
    a ="1"
    b="2"
    c ="3"
    d=1
    
    if a.__contains__("1"):
        loginDetails =  (a,b,d)
        wiologinDetails_Obj = wiologinDetails() 
        wiologinDetails_Obj.login(loginDetails)
    
    if b.__contains__("2"):
        wioRule_Obj = wioRules()
    
    if c.__contains__("3"):
        wiodeviceDetails_Obj = wiodeviceDetails() 
    
