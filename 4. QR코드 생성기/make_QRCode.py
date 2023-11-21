import qrcode

class QRCode:
    def __init__(self):
        pass
        #self.domain = "www.google.com"
        #self.ImageFileName = "파일이름"
    def makeQRCodeImage(self, imageFileName, qr_data):

        qr_img = qrcode.make(qr_data)
        save_path = '4. QR코드 생성기\\' + qr_data + '.png'
        qr_img.save(f'{imageFileName}.png')


if __name__ == '__main__':
    q = QRCode()

    file_path = 'qr코드모음.txt'
    with open(file_path, 'rt', encoding='UTF8') as f:
        read_lines = f.readlines()

        for line in read_lines:
            line = line.strip()
            q.makeQRCodeImage(f'{line}_Test', line)
            print(line)


