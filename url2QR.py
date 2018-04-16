# author : Mohit Narula

import subprocess
import os
import sys

python_major = sys.version_info.major
python_minor = sys.version_info.minor
python_path = "C:\\Python"+str(python_major)+str(python_minor)

try:
    import pyqrcode
except ImportError:
    print("\npyqrcode module is not installed. Installing now..!\n")
    p = subprocess.Popen("pip install pyqrcode", cwd=python_path)
    p.wait()
    import pyqrcode
    print("\nNow installing pypng. Please wait..!")
    p1 = subprocess.Popen("pip install pypng", cwd=python_path)
    p1.wait()

output_path = "C:\\temp2"


if os.path.exists(output_path) is False:
    os.mkdir(output_path)
    print("Temp directory created @ {}".format(output_path))
    if os.path.exists(output_path) is True:
        print("QRcode PNG file will be saved @ {}".format(output_path))

if python_major >= 3:
    input_url = input("\nEnter the URL "
                      "for which you need the QR code PNG file = ")
else:
    input_url = raw_input("\nEnter the URL "
                          "for which you need the QR code PNG file = ")
QRCode_name = "my_QR.png"


def maker():

    try:
        qr_object = pyqrcode.create(input_url,
                                    error='L', version=5, mode='binary')
    except ValueError:
        qr_object = pyqrcode.create(input_url,
                                    error='L', version=10, mode='binary')

    qr_object.png(output_path+"\\"+QRCode_name,
                  scale=6, module_color=[0, 0, 0, 128],
                  background=[0xff, 0xff, 0xcc])
    print("\n{} is generated @ {}".format(QRCode_name, output_path))


if __name__ == "__main__":
    maker()
