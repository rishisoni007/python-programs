hindi = float(input("Enter your marks in hindi :"))
english = float(input("Enter your marks in english :"))
math = float(input("Enter your marks in math :"))

if(0 > hindi or hindi > 100 and 0 > english or english > 100 and 0 > math or math > 100):
    print("Enter valid markes !!")
else: 
    mper = (math/100)*100
    hper = (hindi/100)*100
    eper = (english/100)*100
    total = ((math+english+hindi)/300)*100
    if(hper<33):
        print("-----You are fail in hindi with percentage ",hper,"-----")
        print("-----Total percentages are ",total,"-----")
    elif(mper<33):
        print("-----You are fail in math with percentage ",mper,"-----")
        print("-----Total percentages are ",total,"-----")
    elif(eper<33):
        print("-----You are fail in english with percentage ",eper,"-----")
        print("-----Total percentages are ",total,"-----")
    elif(total<40):
        print("-----You are fail in all subjects with percentage ",total,"-----")
    else:
        print("-----You are pass in all subject with percentage ",total,"-----")
