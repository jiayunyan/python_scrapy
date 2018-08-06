from PIL import Image
im=Image.open("F://data/jongsuk.jpg")
size=im.size
print(size)
width=im.size[0]
height=im.size[1]
print(width)
print(height)
color=im.getpixel((1,9))
print(color)


im2=Image.open("F://data/3.jpg")
fh=open("F:/data/3.txt","a")
width=im2.size[0]
height=im2.size[1]
for j in range(0,height):
    for i in range(0,width):
        cl=im2.getpixel((i,j))
        print(cl)
        clall=cl[0]+cl[1]+cl[2]
        if(clall==0):
            #黑色
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()