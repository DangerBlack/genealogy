from gents import Gents
from readTree import *

def printAll(persons):
    for p in persons:
        print("*"+str(p)+"*")

def mark(p,level):
    if(p!=None):
        if(p.level=="x"):
            p.level = level
            for q in p.childrens:
                mark(q,level - 1)
            mark(p.father,level + 1)
            mark(p.mother,level + 1)
            '''if(p.father!=None):
                p.slot = p.father.childrens.index(p)
            else
                p.slot = 0'''

def familyOrder(item):
    return item.surname+" "+item.name

def generateWeightTree(persons):
    for p in persons:
        p.level = "x"
    mark(persons[0],1)
    marked = []
    for p in persons:
        if(p.level != "x"):
            marked.append(p)
        #else:
        #    print("Scarto:"+str(p)) #TODO remove print

    slots = {}
    maxLevel = 0
    minLevel = 1000
    for p in marked:
        add(slots,p.level,p)
        if(p.level>maxLevel):
            maxLevel = p.level #TODO controllo per livelli negativi
        if(p.level<minLevel):
            minLevel = p.level

    print("MaxL:"+str(maxLevel))
    print("MinL:"+str(minLevel))
    for p in marked:
        #print(""+str(p.level)+" + "+str(abs(minLevel))+" = "+str(p.level+maxLevel)+" - "+str(maxLevel)+" - "+str(abs(minLevel))+" = "+str(-p.level+maxLevel-abs(minLevel)))
        p.level = (maxLevel+abs(minLevel))-(p.level)#(maxLevel+abs(minLevel)+1)-(abs(p.level)+1)+1
    maxSlot = 0
    for level in slots:
        i = 0
        #print("prima della cura "+str(level))
        #printAll(slots[level])
        slots[level] = sorted(slots[level],key=familyOrder)
        #print("dopo la cura "+str(level))
        #printAll(slots[level])
        for p in slots[level]:
            p.slots = len(slots[level])
            p.slot = p.slot*p.slots
            p.slot = i #TODO sistemare il posizionamento cosi random fa schifo e rompe tutto deve dipende da figli!!!
            i = i + 1
        if len(slots[level])>maxSlot:
            maxSlot=len(slots[level])

        #print(str(level)+" "+str(len(slots[level])))


    #for p in marked:
        #print(p)

    return [marked,maxSlot,maxLevel,minLevel]


def readAndBuildTree(filename):
    persons = readFullTree(filename)
    return generateWeightTree(persons)
