sh = input('Enter hours:') 
sr = input('Enter rate:') 
fh = float(sh)
fr = float(sr)

def pay():
    w = int(fh) * int(fr)
    return w
def otp():
    reg = fr * fh 
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,otp)
    xp = reg + otp 
    return xp
if fh > 40: 
    print("Overtime pay is:", otp()) 
else: 
    print ("Regular pay is:", pay()) 

 

