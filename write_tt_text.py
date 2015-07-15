# image is whole capture image webcam from openCV
# Thai char from fill form and Database are in form of UTF-8 already
# upside and downside char of Thai can not be display with double space in to bottom line
def write_tt_text(image,x,y,text):
    try:
        win_text=text.decode('UTF-8')
        win_text=win_text+unichr(0x0020)+unichr(0x0020)
    except:
        win_text=text+'  '
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
