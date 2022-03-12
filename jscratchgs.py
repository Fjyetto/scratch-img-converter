from PIL import Image, ImageOps


def conv(nam):
    img = Image.open(nam+'.png')
    img = img.convert("LA")
    pix = img.load()
    lis = []
    for y in range(40):
        for x in range(40):
            l,a = pix[x,y]
            lis.append(l/255)

    j = '\n'.join(str(e) for e in lis) #str(lis)
    d = open(nam+".txt","w")
    d.write(j)
    d.close()

#for i in range(6):
#    name="notfish"
#    if i-1>0:
#        name=name+str(i-1)
#
#    conv(name)

conv("name") #replace name with the name of your .png image which MUST be 40x40 
