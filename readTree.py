import csv
from gents import Gents

def add(surd,ancestor,person):
    if(ancestor in surd):
        surd[ancestor].append(person)
    else:
        surd[ancestor]=[person]

def search(fullname, person):
    for p in person:
        if(fullname == p.getFullName()):
            return p
    return None


def getAncestor(ancestor,person):
    a = None
    if(ancestor!=""):
        a = search(ancestor,person)
        if a == None:
            name = ancestor.split(' ')
            if(len(name)>1):
                a = Gents(name[0],name[1],"?",None,None)
            else:
                a = Gents("",ancestor,"?",None,None)
            person.append(a)
    return a

def readFullTree():
    surdm = {}
    surdf = {}
    person = []
    with open('Genalogia.csv', 'rb') as csvfile:
        '''tr = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in tr:
                print '****** '.join(row)'''
        tr = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in tr:
                g = Gents(row['Nome'],row["Cognome"],row["data nascita"],None,None)
                add(surdm,row['padre'],g)
                add(surdf,row['madre'],g)
                person.append(g)

        print(len(surdm))
        for ancestor in surdm:
            a = getAncestor(ancestor,person)
            if(a!=None):
                for p in surdm[ancestor]:
                    p.father = a
                    a.childrens.append(p)
        for ancestor in surdf:
            a = getAncestor(ancestor,person)
            if(a!=None):
                for p in surdf[ancestor]:
                    p.mother = a
                    a.childrens.append(p)

        for p in person:
            print(p)

    return person

#readFullTree()
