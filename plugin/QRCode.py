from PIL import Image 
import sys, os

QR_DIR = '.'
try:
    b = u'\u2588'.encode(sys.stdin.encoding)
    sys.stdout.write(b + '\r')
    sys.stdout.flush()
except:
    BLOCK = 'MM'
else:
    BLOCK = b

class QRCode():
    def __init__(self, fileName, size, padding = 0, background = 'BLACK'):
        self.size = size
        self.padding = padding
        self.img = Image.open(fileName)
        self.times = self.img.size[0]/(size + padding * 2)
        self.rgb = self.img.convert('RGB')
        self.white = BLOCK if background == 'BLACK' else '  '
        self.black = '  ' if background == 'BLACK' else BLOCK 
    def print_qr(self):
        sys.stdout.write(' '*50 + '\r')
        sys.stdout.flush()
        print(self.white * (self.size + 2))
        startPoint = self.padding + 0.5
        for y in range(self.size):
            sys.stdout.write(self.white)
            for x in range(self.size):
                r,g,b = self.rgb.getpixel(((x + startPoint) * self.times, (y + startPoint) * self.times))
                sys.stdout.write(self.white if r > 127 else self.black)
            print(self.white)
        print(self.white * (self.size + 2))

if __name__ == '__main__':
    # 37 is for picture size without padding, 3 is padding
    q = QRCode(os.path.join(os.path.pardir, 'log', 'QR.jpg'), 37, 3, 'BLACK')
    q.print_qr()
