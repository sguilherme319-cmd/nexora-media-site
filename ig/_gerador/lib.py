"""Gerador de artes Instagram — Imperial Parfums e Nexora Media."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
HERE=os.path.dirname(os.path.abspath(__file__))
G='/usr/share/fonts/truetype/google-fonts/'
GOLD=(201,162,92); CREAM=(240,228,205); BLACK=(10,9,8); SOFT=(190,180,160)
NGOLD=(212,175,95); WHITE=(245,242,235); GREY=(150,146,138)

def P(w,s): return ImageFont.truetype(G+'Poppins-'+w+'.ttf',s)
def L(s,bold=True):
    f=ImageFont.truetype(G+'Lora-Variable.ttf',s); f.set_variation_by_name('Bold' if bold else 'Regular'); return f

def ctext(d,W,y,t,font,fill):
    w=d.textlength(t,font=font); d.text(((W-w)/2,y),t,font=font,fill=fill)

def wrap(d,text,font,maxw):
    out=[]
    for para in text.split('\n'):
        line=''
        for wd in para.split():
            t=(line+' '+wd).strip()
            if d.textlength(t,font=font)<=maxw: line=t
            else: out.append(line); line=wd
        out.append(line)
    return out

def hero(src,crop,W,H):
    """Recorte do produto ajustado pela altura, laterais preenchidas com desfoque."""
    im=Image.open(src).convert('RGB').crop(crop)
    bg=im.resize((W,int(im.height*W/im.width)) if im.width/im.height<W/H else (int(im.width*H/im.height),H))
    bg=bg.crop(((bg.width-W)//2,(bg.height-H)//2,(bg.width-W)//2+W,(bg.height-H)//2+H)).filter(ImageFilter.GaussianBlur(40))
    bg=ImageEnhance.Brightness(bg).enhance(0.45)
    fg=im.resize((int(im.width*H/im.height),H),Image.LANCZOS)
    if fg.width>W: fg=fg.crop(((fg.width-W)//2,0,(fg.width-W)//2+W,H))
    m=Image.new('L',fg.size,255)
    e=60
    md=ImageDraw.Draw(m)
    for i in range(e):
        a=int(255*i/e); md.line((i,0,i,H),fill=a); md.line((fg.width-1-i,0,fg.width-1-i,H),fill=a)
    bg.paste(fg,((W-fg.width)//2,0),m); return bg

def fade_bottom(img,start,end,color=BLACK):
    W=img.width; h=end-start
    f=Image.new('L',(W,h)); d=ImageDraw.Draw(f)
    for y in range(h): d.line((0,y,W,y),fill=min(255,int(255*(y/h)**1.2)))
    img.paste(Image.new('RGB',(W,h),color),(0,start),f)
    if end<img.height: img.paste(color,(0,end,W,img.height))

def imperial_badge(img,x=48,y=44):
    logo=Image.open(os.path.join(HERE,'imperial_logo.jpg')).resize((140,178),Image.LANCZOS)
    m=Image.new('L',logo.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,139,177),22,fill=255)
    img.paste(logo,(x,y),m); ImageDraw.Draw(img).rounded_rectangle((x,y,x+140,y+178),22,outline=GOLD,width=2)

def nexora_badge(img,x,y,size):
    lg=Image.open(os.path.join(HERE,'nexora_logo.png')).convert('RGBA').resize((size,size),Image.LANCZOS)
    img.paste(lg,(x,y),lg)

# ---------- IMPERIAL ----------
def imperial_post(page,crop,brand,name,notes,tagline,out,cta='PEÇA PELO DIRECT',badge=None):
    W,H=1080,1350
    img=Image.new('RGB',(W,H),BLACK); img.paste(hero(page,crop,W,940),(0,0))
    fade_bottom(img,680,940); d=ImageDraw.Draw(img); imperial_badge(img)
    if badge:
        f=P('Bold',30); w=d.textlength(badge,font=f)
        d.rounded_rectangle((W-48-w-44,60,W-48,116),28,fill=GOLD); d.text((W-48-w-22,68),badge,font=f,fill=BLACK)
    ctext(d,W,872,brand.upper(),L(34,False),GOLD)
    fs=112 if len(name)<=8 else (92 if len(name)<=12 else 74)
    ctext(d,W,914+(112-fs)//2+8,name.upper(),L(fs),CREAM)
    d.line((390,1062,690,1062),fill=GOLD,width=2)
    ctext(d,W,1082,'  ·  '.join(notes),P('Light',32),CREAM)
    ctext(d,W,1140,tagline,P('Regular',27),SOFT)
    d.rounded_rectangle((300,1200,780,1270),35,fill=GOLD); ctext(d,W,1217,cta,P('Bold',28),BLACK)
    ctext(d,W,1292,'IMPERIAL PARFUMS  ·  LAGES – SC',P('Regular',20),GOLD)
    img.save(out,quality=92)

def imperial_story(page,crop,kicker,question,out,foot='Responde aqui no direct'):
    W,H=1080,1920
    img=Image.new('RGB',(W,H),BLACK); img.paste(hero(page,crop,W,1050),(0,660))
    # topo
    d=ImageDraw.Draw(img); imperial_badge(img,(W-140)//2,90)
    ctext(d,W,300,kicker.upper(),P('Medium',30),GOLD)
    fq=L(62); y=350
    for ln in wrap(d,question,fq,960): ctext(d,W,y,ln,fq,CREAM); y+=78
    # faixa de topo do hero
    f=Image.new('L',(W,220)); fd=ImageDraw.Draw(f)
    for i in range(220): fd.line((0,i,W,i),fill=255-int(255*i/220))
    img.paste(Image.new('RGB',(W,220),BLACK),(0,660),f)
    fade_bottom(img,1500,1710); d=ImageDraw.Draw(img)
    d.rounded_rectangle((140,1730,940,1830),50,fill=GOLD); ctext(d,W,1756,foot.upper(),P('Bold',34),BLACK)
    ctext(d,W,1860,'@imper.ialparfums  ·  Lages – SC',P('Regular',24),GOLD)
    img.save(out,quality=92)

def imperial_cover(title_lines,sub,pages_crops,out):
    W,H=1080,1350
    img=Image.new('RGB',(W,H),BLACK)
    n=len(pages_crops); cw=W//n
    for i,(pg,cr) in enumerate(pages_crops):
        img.paste(hero(pg,cr,cw,760),(i*cw,0))
    fade_bottom(img,420,760); d=ImageDraw.Draw(img); imperial_badge(img)
    y=790
    for i,t in enumerate(title_lines):
        f=L(84) if i else L(84,False); ctext(d,W,y,t,f,GOLD if i else CREAM); y+=100
    d.line((440,y+20,640,y+20),fill=GOLD,width=2)
    ctext(d,W,y+50,sub,P('Light',32),CREAM)
    ctext(d,W,1260,'ARRASTE PARA O LADO  >>',P('Medium',26),GOLD)
    img.save(out,quality=92)

def imperial_cta(title,lines,out):
    W,H=1080,1350
    img=Image.new('RGB',(W,H),BLACK); d=ImageDraw.Draw(img)
    logo=Image.open(os.path.join(HERE,'imperial_logo.jpg')).resize((300,380),Image.LANCZOS)
    img.paste(logo,((W-300)//2,120))
    ctext(d,W,560,title,L(70),CREAM)
    y=680
    for t in lines: ctext(d,W,y,t,P('Regular',34),SOFT); y+=58
    d.rounded_rectangle((240,1000,840,1090),45,fill=GOLD); ctext(d,W,1022,'CHAME NO DIRECT',P('Bold',36),BLACK)
    ctext(d,W,1130,'Entrega grátis em Lages e região',P('Regular',26),GOLD)
    ctext(d,W,1260,'IMPERIAL PARFUMS  ·  LAGES – SC',P('Regular',22),GOLD)
    img.save(out,quality=92)

# ---------- NEXORA ----------
def _nexora_base(W,H):
    img=Image.new('RGB',(W,H),(8,8,9))
    glow=Image.new('L',(W,H),0); gd=ImageDraw.Draw(glow)
    for r in range(760,0,-10): gd.ellipse((W-200-r,320-r,W-200+r,320+r),fill=int(30*(1-r/760)))
    img.paste(Image.new('RGB',(W,H),(60,45,15)),(0,0),glow)
    return img

def nexora_post(top,gold,bullets,cta,out,H=1350,kicker=None):
    W=1080; img=_nexora_base(W,H); d=ImageDraw.Draw(img)
    nexora_badge(img,60,50,170)
    y=290
    if kicker: d.text((72,y-60),kicker.upper(),font=P('Medium',28),fill=NGOLD)
    for ln in wrap(d,top,P('Medium',60),930): d.text((72,y),ln,font=P('Medium',60),fill=WHITE); y+=78
    y+=24; fg=L(86)
    for ln in wrap(d,gold,fg,940): d.text((72,y),ln,font=fg,fill=NGOLD); y+=104
    y+=20; d.line((72,y,272,y),fill=NGOLD,width=4); y+=46
    for t in bullets:
        d.ellipse((76,y+16,92,y+32),fill=NGOLD); d.text((116,y),t,font=P('Regular',34),fill=WHITE); y+=64
    by=H-250
    f=P('Bold',34); w=d.textlength(cta,font=f)
    d.rounded_rectangle((72,by,1008,by+96),48,fill=NGOLD); d.text(((W-w)/2,by+25),cta,font=f,fill=(8,8,9))
    ctext(d,W,H-110,'@nexora_media00  ·  Lages – SC',P('Regular',24),GREY)
    img.save(out,quality=92)

def nexora_story(kicker,question,sub,out):
    W,H=1080,1920; img=_nexora_base(W,H); d=ImageDraw.Draw(img)
    nexora_badge(img,(W-260)//2,300,260)
    ctext(d,W,680,kicker.upper(),P('Medium',30),NGOLD)
    fq=L(80); y=760
    for ln in wrap(d,question,fq,940): ctext(d,W,y,ln,fq,WHITE); y+=100
    y+=40
    for ln in wrap(d,sub,P('Regular',36),900): ctext(d,W,y,ln,P('Regular',36),GREY); y+=52
    d.rounded_rectangle((140,1460,940,1560),50,fill=NGOLD); ctext(d,W,1486,'RESPONDE NO DIRECT',P('Bold',36),(8,8,9))
    ctext(d,W,1620,'@nexora_media00',P('Regular',26),GREY)
    img.save(out,quality=92)

def nexora_slide(num,title,body,out,total=None):
    W,H=1080,1350; img=_nexora_base(W,H); d=ImageDraw.Draw(img)
    nexora_badge(img,W-200,50,140)
    d.text((72,170),f'{num:02d}',font=L(200),fill=NGOLD)
    y=470; ft=P('Bold',62)
    for ln in wrap(d,title,ft,930): d.text((72,y),ln,font=ft,fill=WHITE); y+=80
    y+=30; d.line((72,y,272,y),fill=NGOLD,width=4); y+=50
    for ln in wrap(d,body,P('Regular',38),930): d.text((72,y),ln,font=P('Regular',38),fill=GREY); y+=58
    if total: ctext(d,W,1250,f'{num}/{total}   ARRASTE  >>',P('Medium',24),NGOLD)
    img.save(out,quality=92)
