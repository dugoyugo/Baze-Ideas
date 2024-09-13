import qrcode
from pyzbar.pyzbar import decode
from PIL import image


myqrc = qrcode.make("https://www.youtube.com/watch?v=K35zrOk98co")
myqrc1 = qrcode.make("https://learn.microsoft.com/en-gb/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package")

myqrc.save("myqrc.png", scale = 8)
myqrc1.save("myqrc1.png")


b = decode(Image.open("myqrc.png"))
print(b[0].data.decode("ascii"))
