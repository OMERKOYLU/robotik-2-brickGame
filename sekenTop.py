import sys
import pygame

pygame.init()
ekran=pygame.display.set_mode((400,400))
#1##############################<YENİ>
zorlukSeviyesi=0
####################################
x=200
y=200
xRaket=200
yRaket=300
Vx=0.1
Vy=0.2
puan=0
mod="menu"
RaketHiz=0 #1#raketHiz yeni değişken
REKORKONTROL=False

#1#####################################################<YENİ 08.05>
yuksekSkorlar=open("./HighScores.txt","r")
skorlar=yuksekSkorlar.readlines()
for sira,skor in enumerate(skorlar):
    skorlar[sira]=skor[:-1]
print(skorlar)
yuksekSkorlar.close()
####################################################################


class menu():
    menuPencere=pygame.Rect(50,20,300,350)
    pygame.font.init()
    menuFont=pygame.font.SysFont("Times New Roman", 20)
    def update(self,ekran):
        pygame.draw.rect(ekran,(255,255,255),self.menuPencere)
        girisYazi=self.menuFont.render("başlamak için boşluk tuşuna basın!",(0,0,0),(0,0,0))
        ekran.blit(girisYazi,(60,50))
        girisYazi = self.menuFont.render("1: zorluk seviyesi seçimi", (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 100))
        girisYazi = self.menuFont.render("2: Yüksek skorlar", (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 125))
#2####################################<YENİ>
class zorluk():
    menuPencere=pygame.Rect(50,20,300,350)
    pygame.font.init()
    menuFont=pygame.font.SysFont("Times New Roman", 20)
    def update(self,ekran):
        pygame.draw.rect(ekran,(255,255,255),self.menuPencere)
        girisYazi=self.menuFont.render("Zorluk seviyesi seçin!",(0,0,0),(0,0,0))
        ekran.blit(girisYazi,(60,50))
        girisYazi = self.menuFont.render("x: Kolay", (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 100))
        girisYazi = self.menuFont.render("y: Orta", (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 125))
        girisYazi = self.menuFont.render("z: Zor", (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 150))

#2#################################################################<YENİ 08.05>###
class skorlarPencere():
    menuPencere = pygame.Rect(50, 20, 300, 350)
    pygame.font.init()
    menuFont = pygame.font.SysFont("Times New Roman", 20)
    def update(self,ekran):
        pygame.draw.rect(ekran,(255,255,255),self.menuPencere)
        girisYazi=self.menuFont.render("İşte Rekortmenler!",(0,0,0),(0,0,0))
        ekran.blit(girisYazi,(60,50))
        girisYazi = self.menuFont.render(skorlar[0], (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 100))
        girisYazi = self.menuFont.render(skorlar[1], (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 125))
        girisYazi = self.menuFont.render(skorlar[2], (0, 0, 0), (0, 0, 0))
        ekran.blit(girisYazi, (60, 150))
################################################################################
######################################################
class tugla:
    def __init__(self,x,y):
        self.rect=pygame.Rect(x,y,23,13)
tuglalar=[] #tuglalar adında bir liste tanımladık

for sutun in range(16):
    for satir in range(8):
        tuglalar.append(tugla(sutun * 25, 15 * satir))
# game over yazısı ###################################################################
pygame.font.init()
font=pygame.font.SysFont("Times New Roman",65)
goText=font.render("GAME OVER",(0,0,0),(255,0,0))
bitti=False
#######################################################################

#puan için ##############################################################
fontpuan=pygame.font.SysFont("Times New Roman",24)
puanText = fontpuan.render("puan:" +str(puan), (0, 0, 0), (255, 255, 255))
oyunSonuPuan=pygame.font.SysFont("Times New Roman",50)
oyunSonuPuanText = oyunSonuPuan.render(str(puan), (0, 0, 0), (255, 255, 255))
#########################################################################
while True:
    ekran.fill((0, 0, 255))
    for olay in pygame.event.get():  #for yer değiştirdi
        if olay.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #3#################################<YENİ>
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        mod="oyun"
    if pygame.key.get_pressed()[pygame.K_1]:
        mod="zorluk seçim"
    #3#######################################<YENİ 08.05>
    if pygame.key.get_pressed()[pygame.K_2]:
        mod="yuksek skorlar"
    #####################################################
    ############################################
    if mod=="oyun":
        if not bitti: #<2>## burdan sonraki kısımlar display flipe kadar bir sekme sağa
            for a in tuglalar:
                pygame.draw.rect(ekran,(255,255,0),a)
            if (y>390) or (y<10):
                Vy=-Vy
            if (x>390) or (x<10):
                Vx=-Vx
            #2##########################Raket hareket komutları
            if pygame.key.get_pressed()[pygame.K_LEFT] and xRaket>0:
                if (RaketHiz>-2):
                    RaketHiz-=0.3
            elif pygame.key.get_pressed()[pygame.K_RIGHT] and xRaket<300:
                if (RaketHiz<2):
                    RaketHiz+=0.3
            else: RaketHiz=0.0
            xRaket+=RaketHiz
            ##########################################################
            x+=Vx
            y+=Vy

            rect=pygame.draw.rect(ekran,(0,255,0),(xRaket,yRaket,100,5)) #raketi çizer
            rectTop=pygame.draw.circle(ekran,(255,255,255),(x,y),10.0)  #topu çizer

            if rect.colliderect(rectTop):
                Vy=-Vy
                Vx+=RaketHiz/2 #####top raketin hızından etkilensin

            for tgl in tuglalar:
                if (rectTop.colliderect(tgl.rect)):
                    puan+=(zorlukSeviyesi+1)*5  #5#####################puan kazancını değiştirdik
                    puanText = fontpuan.render("puan:" + str(puan), (0, 0, 0), (255, 255, 255))
                    oyunSonuPuanText = oyunSonuPuan.render(str(puan), (0, 0, 0), (255, 255, 255))
                    ###########################################################
                    if tgl.rect.x-10<rectTop.x+10<tgl.rect.x or tgl.rect.x+13<rectTop.x<tgl.rect.x+23:
                        Vx=-Vx
                    if tgl.rect.y<rectTop.y+10<tgl.rect.y or tgl.rect.y+3<rectTop.y<tgl.rect.y+13:
                        Vy=-Vy
                    tuglalar.remove(tgl)
                    break
            print(rectTop.y)
            #oyun bitiş kontrolü########################################################################
            if rectTop.y>365:
                bitti=True
            ############################################################################################
            ekran.blit(puanText,(10,360))
        if bitti: #####oyun bitti yazısını burası yazıyor
            ekran.blit(goText,(10,200))
            ekran.blit(oyunSonuPuanText, (180, 150))
            #<1>##########################################<29-MAYIS>####
            if not REKORKONTROL:
                REKORKONTROL=True
                index=0
                sira=-1
                for s in skorlar:
                    if puan>=int(s.split(",")[1]):
                        sira=index
                        break
                    index+=1
                print(sira)
                if sira != -1:
                    sTemp = skorlar[sira]
                    skorlar[sira] = "Ömer," + str(puan)
                    for i in range(3):
                        if (i>sira):
                            sTemp2 = skorlar[i]
                            skorlar[i] = sTemp
                            sTemp = sTemp2
                    # <1>#######################################<05.06.2021>###
                    f = open("./HighScores.txt", "w")
                    for s in skorlar:
                        f.write(s + "\n")
                    f.close()
                    ##########################################################
            print(skorlar)
        #######################################################
    #2###################################################
    elif mod=="menu":
        m=menu()
        m.update(ekran)
    #4#############################################<YENİ>
    elif mod=="zorluk seçim":
        pencere=zorluk()
        pencere.update(ekran)
        if pygame.key.get_pressed()[pygame.K_x]:
            zorlukSeviyesi=0
            mod="menu"
        if pygame.key.get_pressed()[pygame.K_y]:
            zorlukSeviyesi=1
            mod = "menu"
        if pygame.key.get_pressed()[pygame.K_z]:
            zorlukSeviyesi=2
            mod = "menu"
        Vx += (zorlukSeviyesi * 0.15)
        Vy += (zorlukSeviyesi * 0.15)
    ######################################################
    #4###################################################<YENİ 08.05>
    elif mod=="yuksek skorlar":
        pencere=skorlarPencere()
        pencere.update(ekran)
    #################################################################
    pygame.display.flip()