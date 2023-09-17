pip install deepface
from deepface import DeepFace
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

start_time = datetime.now()
analiz= "/ornekekipresmi.jpg"
objs = DeepFace.analyze(img_path = analiz, actions= ["age"], detector_backend=("retinaface"))

im1 = Image.open(analiz)
font = ImageFont.truetype("/hel.ttf",size=25)
l=len(objs)
yasbuyuk=100
yaskucuk=0
for i in range (0,l):
 if(yasbuyuk>objs[i]["age"]):
    yasbuyuk=objs[i]["age"]
    ek=i
 if(yaskucuk<objs[i]["age"]):
    yaskucuk=objs[i]["age"]
    eb=i

for i in range(0,l):
 x=objs[i]['region']['x']
 y=objs[i]['region']['y']
 w=objs[i]['region']['w']
 h=objs[i]['region']['h']

 img1 = ImageDraw.Draw(im1)
 if(i==ek):
  img1.rectangle([(x,y),(x+w,y+h)], outline ="green",width=5)
  img1.text((x, y+h+30), str(objs[i]["age"]), fill="black", font=font)
 elif(i==eb):
  img1.rectangle([(x,y),(x+w,y+h)], outline ="red",width=5)
  img1.text((x, y+h+30), str(objs[i]["age"]), fill="black", font=font)
 else:
  img1.rectangle([(x,y),(x+w,y+h)], outline ="yellow",width=5)
 #img1.text((x, y+h), objs[i]["dominant_emotion"], fill="cyan", font=font)
 #img1.text((x, y+h+30), str(objs[i]["age"]), fill="black", font=font)
 #img1.text((x, y+h+60), objs[i]["dominant_gender"], fill="red", font=font)
 #img1.text((x, y+h+90), objs[i]["dominant_race"], fill="red", font=font)
im1.show()
print("---%s seconds---"% (datetime.now() - start_time))