# image is whole capture image webcam from openCV

def write_tt_text(image,x,y,text):
    win_text=''
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
            kk=kk-160
            win_text=win_text+unichr(0x0E00 + kk)
        else:
            win_text=win_text+unichr(0x0000 + kk)
    win_text=win_text+unichr(0x0020)+unichr(0x0020)
    Font1 = ImageFont.truetype("angsau_0.ttf", 14)
    image_pil = Image.new("RGB",(150,26),(0,0,0))
    draw = ImageDraw.Draw(image_pil)
    draw.text((5,5),win_text,(255,255,255),font=Font1)
    del draw
    # from StackOverflow Q# 14134892 Answer by Abhishek Thakur 3 Jan 2013
    cv_image = np.array(image_pil) 
    cv_image = cv_image[:, :, ::-1].copy() 
    imageout = image.copy()    
    if y>=0 and x>=0:
        if x+150<=imageout.shape[1] and y+26<=imageout.shape[0]:
            imageout[0+y:0+y+26 , 0+x:0+x+150] = cv_image
    return imageout
