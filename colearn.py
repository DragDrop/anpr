import darknet
import ctypes
# net = darknet.load_net(r'cfg/anprtiny.cfg', r'weights/anprtiny_final.weights', 0)
# meta = darknet.load_meta(r"test.data")
# r = detect(net, meta, "data/IMG_20200729_134303.jpg")
# meta = darknet.load_meta(ctypes.c_char_p(b'test.data'))
# net = darknet.load_net(b'cfg/anprspp.cfg', b'weights/anprspp_final.weights', 0)

# r = darknet.detect(net, meta, b'data/IMG_20200729_134401.jpg')

network, class_names, colors = darknet.load_network('cfg/anprspp.cfg','test.data','weights/anprspp_final.weights')
darknet.load_image()
r = darknet.detect_image(network,class_names,"data/IMG_20200729_134303.jpg")
print(r)