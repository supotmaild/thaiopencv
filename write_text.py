# write_text function for ไทย Open CV
# don't import copy this code to use in your program
# How to use
# import lcd_font
# font_data = lcd_font.font()
# del lcd_font

def write_text(image,x,y,text):
    global font_data
    dimg = np.zeros((26,100,3),np.uint8)
    h=10
    chk1=0
    chk2=0
    for k in text:
        if chk2>0:
            if chk2==1:
                kk=ord(k)+3456
            else:
                kk=ord(k)+3520
            chk1=0
            chk2=0
        else:    
            if chk1==1 and chk2==0:
                if ord(k)==184:
                    chk2=1
                elif ord(k)==185:
                    chk2=2
                continue
            if ord(k)==224:
                chk1=1
                continue
            else:
                kk=ord(k)
        vv=0
        if kk>=3584:
            kk=kk-3424
        #very upper Thai font
        if kk>=232 and kk<=238:
            vv=(-12)
            h=h-9
        #upper Thai font
        if kk==209 or (kk>=212 and kk<=215) or kk==231:
            vv=(-8)
            h=h-9
        #lower Thai font
        if kk>=216 and kk<=218:
            vv=9
            h=h-9
        for j in range(8):
            nfont=font_data[kk][j]
            v=10
            for i in range(8):
                if nfont>=(2**(7-i)):
                    vvv=v+vv
                    if vvv>=0 and vv<=26 and h>=0 and h<=90:
                        dimg[vvv][h]=[255,255,255]
                    nfont=nfont-(2**(7-i))
                v=v+1
            h=h+1
        h=h+1
    imageout = image.copy()
    if y>=0 and x>=0:
        if x+100<=imageout.shape[1] and y+26<=imageout.shape[0]:
            imageout[0+y:0+y+26 , 0+x:0+x+100] = dimg
    return imageout
