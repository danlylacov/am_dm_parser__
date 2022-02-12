from PIL import Image, ImageDraw, ImageFont

def create_accord(accord, name):
    accord = str(accord).replace('(', '')
    accord = str(accord).replace(')', '')
    im = Image.new('RGB', (500, 400), (219, 193, 27))

    draw = ImageDraw.Draw(im)
    a = 30
    for i in range(6):

        draw.line(
        xy=(
        (30, a),
        (450, a)
    ), fill='black', width=10)
        a += 50

    a = 30
    for i in range(6):

        draw.line(
        xy=(
        (a, 30),
        (a, 280)
    ), fill='black', width=5)
        a += 100

    x = 80 + 100
    y = 30 + 50
    st = accord.split(',')[0]
    num = []
    begin = 1
    for i in range(len(st)):
        if st[i] != 'X' and st[i] != '0':
            num.append(int(st[i]))
    if max(num)>4:
        begin = min(num)

    for i in range(6):
        if st[i] == 0:
            print('')
        if st[i] == 'X':
            crest(im, draw, 15, 30 + 50 * (i))
        else:
            x = 80 + 100 * ((int(st[i]) ) - begin)
            y = 30 + i * 50
            draw.ellipse((x - 10, y - 10, x + 10, y + 10), 'red')
    if begin > 2:
        draw.text((74,2),str(begin) ,font=ImageFont.truetype("arial.ttf", size=25),  fill='Black')
    draw.text((200, 300), str(name), font=ImageFont.truetype("arial.ttf", size=50), fill='Green')

    im.save('1.jpg')

def crest(im, draw, x, y):


    draw.line(
        xy=(
            (x - 7, y - 7),
            (x+ 7, y + 7)
        ), fill='red', width=5)
    draw.line(
        xy=(
            (x + 7, y - 7),
            (x - 7, y + 7)
        ), fill='red', width=5)


