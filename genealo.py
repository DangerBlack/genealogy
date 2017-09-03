from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from gents import Gents
from weightTree import *





couple = readAndBuildTree();

persons = couple[0]
maxS = couple[1]
maxL = couple[2]


n = 800
m = 600


temp = Gents(".",".",".",None,None)

n = 200*maxS+200
m = (35+temp.padding)*maxL+200

out_file = "out.png"
source_img = Image.new('RGB', (n, m))

draw = ImageDraw.Draw(source_img)
draw.rectangle(((0, 00), (n, m)), fill="white")

for p in persons:
    p.addOnDraw(draw,n)

#draw.rectangle(((0, 00), (100, 100)), outline="black")
#draw.text((20, 70), "something123", font=ImageFont.truetype("/usr/share/fonts/truetype/liberation/Liberation/LiberationSerif-Regular.ttf"),fill="black")

source_img.save(out_file, "PNG")
source_img.show()
