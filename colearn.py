import darknet
import cv2

imagename = "data/0a3a99129a9e37253f49c2b25283d2fb.jpg"

networkspp, _, _ = darknet.load_network('cfg/anprspp.cfg','test.data','weights/anprspp_final.weights')
networktiny, _, _ = darknet.load_network('cfg/anprtiny.cfg','test.data','weights/anprtiny_final.weights')
networkyv3, _, _ = darknet.load_network('cfg/anpryolov3.cfg','test.data','weights/anpryolov3_final.weights')
networkplate, _, _ = darknet.load_network('cfg/plate.cfg','test.data','weights/plate_final.weights')

img = darknet.load_image(imagename.encode("ascii"),0,0)

rspp = darknet.detect_image(networkspp, ["plate"], img)
rtiny = darknet.detect_image(networktiny, ["plate"], img)
ryv3 = darknet.detect_image(networkyv3, ["plate"], img)
rplate = darknet.detect_image(networkplate, ["plate"], img)

print("rssp", rspp)
print("rtiny", rtiny)
print("ryv3" ,ryv3)
print("rplate", rplate)

img = cv2.imread(imagename)

img = darknet.draw_boxes(rspp,img,{"plate":(255,0,0)})
img = darknet.draw_boxes(rtiny,img,{"plate":(0,255,0)})
img = darknet.draw_boxes(ryv3,img,{"plate":(0,0,255)})
img = darknet.draw_boxes(rplate, img,{"plate":(0,255,255)})

cv2.imwrite("result.jpg",img)