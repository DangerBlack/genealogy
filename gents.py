from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random as r

class Gents:
    padding = 100


    rainbows = ["red","green","orangered","turquoise","darkviolet","slateblue","sienna","silver","lightsteelblue","darkkhaki","coral","teal"]
    #font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/Liberation/LiberationSerif-Regular.ttf",15)
    font = ImageFont.truetype("res/DancingScript-Regular.ttf",23)
    fontsm = ImageFont.truetype("res/DancingScript-Regular.ttf",12)

    def __init__(self,name,surname,date,father,mother):
        self.name = name
        self.surname = surname
        if("/" in date):
            year = date.split("/")[-1]
        else:
            year = date
        self.date = year
        self.father = father
        self.mother = mother
        #self.siblings = siblings
        self.childrens = []
        self.dx = self.font.getsize(self.getFullName())[0]+20
        self.dy = 55
        self.level = 0
        self.slots = 1
        self.slot = 0


    def getFullName(self):
        return self.name+" "+self.surname

    def getXc(self,l):
        slotsize = l/self.slots
        xc = slotsize*self.slot+slotsize/2
        return xc

    def __str__(self):
        mm =None
        if(self.mother!=None):
            mm=self.mother.getFullName()
        dd =None
        if(self.father!=None):
            dd=self.father.getFullName()
        return self.getFullName()+" ("+str(mm)+", "+str(dd)+") lv. "+str(self.level)

    def addOnDraw(self,draw,l):
        slotsize = l/self.slots
        x0 = slotsize*self.slot+slotsize/2 - self.dx/2
        y0 = self.level*(self.dy + self.padding)
        #draw.rectangle((( x0, y0), (x0 + self.dx, y0 + self.dy)), outline="black")
        draw.text((x0 + 10, y0 + 10), self.getFullName(), font=self.font,fill="black")

        datepadd = self.dx/2 - self.fontsm.getsize(self.date)[0]/2 -10
        topadd = self.font.getsize("a")[1]
        draw.text((x0 + 10 + datepadd, y0 + 10 + topadd + 2), self.date, font=self.fontsm,fill="black")

        if self.father != None and self.mother != None:
            quantum = self.padding/14

            spadding =  self.father.slot*quantum+quantum #self.padding/2 + self.father.slot*quantum
            color = self.rainbows[self.father.slot % len(self.rainbows)]
            xc = slotsize*self.slot + slotsize/2
            draw.line(((xc,y0-spadding),(xc,y0)),fill=color) #riga alto figlio
            fxc = self.father.getXc(l)
            mxc = self.mother.getXc(l)
            positionsc = [xc,fxc,mxc]

            minxc = min(positionsc)
            maxxc = max(positionsc)

            draw.line(((minxc,y0-spadding),(maxxc,y0-spadding)),fill=color) #riga orizzontale
            draw.line(((fxc,y0-self.padding),(fxc,y0-spadding)),fill=color) #riga basso mamma
            draw.line(((mxc,y0-self.padding),(mxc,y0-spadding)),fill=color) #riga basso papa
            #draw.rectangle((( x0, y0), (x0 + self.dx, y0 + self.dy)), outline=color)
