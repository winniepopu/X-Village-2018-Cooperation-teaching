#判斷key是否存在的應用-1
#有一個詞語是"Wow"，請更新進字典，印出新的rap頻率字典。

dic={"Skr":100,"Check it out":20,"Yo":80,"Diss":90}

key="Wow"
if key not in dic.keys():    
    dic[key]=0
dic[key]+=1

print(dic)
