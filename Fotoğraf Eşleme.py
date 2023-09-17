pip install deepface
from deepface import DeepFace
from PIL import Image,ImageDraw
 
result = DeepFace.verify(img1_path = "/beckham.jpg", img2_path = "/messi.jpg")
print(result)

im1 = Image.open("/beckham.jpg")
img1=ImageDraw.Draw(im1)
x=result['facial_areas']['img1']['x']
y=result['facial_areas']['img1']['y']
w=result['facial_areas']['img1']['w']
h=result['facial_areas']['img1']['h']
img1.rectangle([(x,y),(x+w,y+h)], outline ="yellow",width=5)
im1.show()

im2 = Image.open("/messi.jpg")
img2=ImageDraw.Draw(im2)
x=result['facial_areas']['img2']['x']
y=result['facial_areas']['img2']['y']
w=result['facial_areas']['img2']['w']
h=result['facial_areas']['img2']['h']
img2.rectangle([(x,y),(x+w,y+h)], outline ="yellow",width=5)
im2.show()
