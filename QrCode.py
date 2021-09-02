import pyqrcode
from pyqrcode import QRCode

s = input("Enter the url: ")

url = pyqrcode.create(s)

url.svg("myyoutube.svg", scale = 8)