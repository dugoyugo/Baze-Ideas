import qrcode
from pyzbar.pyzbar import decode
from PIL import image



myq = qrcode.make("https://www.youtube.com/watch?v=K35zrOk98co")

                                                                                                                                                                                                                                                                                                                
myq.save("myq.png", scale = 8)