#判斷key是否存在的應用-2
#有一筆新的rap list,紀錄各種rap詞,請更新進rap頻率字典中,印出新的rap頻率字典

dic={"Skr": 100, "Check it out": 20, "Yo": 80, "Diss": 90}

L=["Skr","Skr","Yo","Yo","Wow","Wow","Wow","Yo","Oh my God","Oh my God","Yo","Check it out","Diss","Diss","Oh my God","Oh my God","Diss","Diss","Check it out","Skr","Skr","Skr","Yo","Yo","Skr","Skr","Skr","Yo","Yo","Skr","Skr","Skr","Skr","Skr","Skr"]

for rap in L:
    if rap not in dic.keys():
        dic[rap]=0
    dic[rap]+=1

print(dic)
