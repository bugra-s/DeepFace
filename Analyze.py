pip install deepface
from deepface import DeepFace
from PIL import Image,ImageDraw,ImageFont
resim1="/messi.jpg"
result = DeepFace.analyze(resim1)


im1 = Image.open(resim1)
font = ImageFont.truetype("/hel.ttf",size=25)
img1=ImageDraw.Draw(im1)
x=result[0]['region']['x']
y=result[0]['region']['y']
w=result[0]['region']['w']
h=result[0]['region']['h']
img1.rectangle([(x,y),(x+w,y+h)], outline ="green",width=5)
img1.text((x, y+h), result[0]["dominant_emotion"], fill="black", font=font)
img1.text((x, y+h+30), str(result[0]["age"]), fill="black", font=font)
img1.text((x, y+h+60), result[0]["dominant_gender"], fill="black", font=font)
img1.text((x, y+h+90), result[0]["dominant_race"], fill="black", font=font)
im1.show()