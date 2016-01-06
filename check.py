# -*- coding: cp936 -*-
import json
f = file("notify.json")
s = json.load(f)

print "规则条数：" + str(len(s["content"]))

for i in range(len(s["content"])):
    print "包名:" + str(s["content"][i]["pkg"]) + "--->对应规则条数:" +str(len(s["content"][i]["rule"]))
    val = len(s["content"][i]["rule"])
    rules = s["content"][i]["rule"]
    for j in range(val):
        #print rules[j]
        if(rules[j]["type"] == 0):
            if("hcode" in rules[j].keys() or "size" in rules[j].keys() or "key" in rules[j].keys()):
                print "规则错误"
                print "这是一条软件白的规则"
                print str(s["content"][i]["pkg"]) + "+++++" + str(rules[j]["id"])
        if(rules[j]["type"] == 1):
            if("hcode" not in rules[j].keys() or "size" not in rules[j].keys() or "key" in rules[j].keys()):
                print "规则错误"
                print "这是一条文案白的规则"
                print str(s["content"][i]["pkg"]) + "+++++" + str(rules[j]["id"])
            #print rules[j]["size"] == len(rules[j]["notifytext"])
        if("hcode" in rules[j].keys() or "size" in rules[j].keys() or "key" not in rules[j].keys()):
            if("key" in rules[j].keys()):
                print "规则错误"
                print "这是一条关键词白的规则"
                print str(s["content"][i]["pkg"]) + "+++++" + str(rules[j]["id"])
        
        

    

#print s.keys()
