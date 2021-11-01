# from os import name
from os import path
import os
from tkinter.constants import E
import pygame as pg
from object import Text, Button,InputBox,pic
import time
# from tkinter import *
from tkinter import filedialog
import shutil
import cv2
#####################################function 

def resize(Profile_pic):
    pg.transform.scale(Profile_pic,(50,50))
    
#####################################function 
# import sys
pg.init()
#var
user_list=[]
password_list=[]
press =[0,0]
uuuu = 0
n = 0
#color                                                                                                                                                                     
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
light_gray = (230, 230, 230)
green = (0, 200, 0)
red = (200, 0, 0)
mint = (120,255,255)
orange = (242,157,0)
# screen
win_x, win_y = 1280, 720
screen = pg.display.set_mode((win_x, win_y))
pg.display.set_caption("VOCA")

startpg = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/first_page.jpg')
pg3 = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/lesson_page.jpg')
fade = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/new_login_page.jpg')
login = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/new_login_button.png')
regis = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/new_regis_button.png')
ui3 = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/new_register_page.jpg')
pgpf = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/home_page.jpg')
pgpf2 = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/home_page.png')
setting = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/popup_setting.png')
setting_btn = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/setting_button.png')
bgwhite = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/background_pic.png')
add_p = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/add_picture.png')
take_p = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/take_photo_button.png')
upload_p = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/upload_photo_button.png')
defualt_p_path = 'C:/UI-st4/IU64/UIPHOTO/photo/defualt_profile.png'
all_p = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/all.png')
page = 'start'

#picture 
# set box user
distance_box = InputBox(723, 273.3, 471,60,45,17)  # distance input box
firstname_registors = InputBox(695, 170, 472,49,35,12)  # distance input box
surname_registors = InputBox(695, 257, 472,49,35,12)  # distance input box
nickname_registors = InputBox(695, 351, 472, 49,35,12)  # spinner's speed input box
username_registors = InputBox(695, 439, 472,49,35,12)  # distance input box
input_boxes = [distance_box]
input_registor = [surname_registors,firstname_registors,nickname_registors,username_registors]
start_btn = Button(969, 388, 217, 87)
regis_sub_btn = Button(823, 533, 217,60)
save_sub_btn = Button(823, 533, 217,60)
regis_btn = Button(729, 388 , 217, 87)
backtomain = Button(18,15,59,59)
back = Button(167,180,500-167,548-180)
screencorider = Button(0,0,1280,720)
please = True
newstatus = 0
run = True
r_btn_status = False
filepath = ""
option_sta = 0
backpage = ""
click = 0
logout_status = 0
regis_click = 0
user_status = 'nohave' 
memprofile = ['  ','  ','  ','  ','  ','']
############################################ lesson
lession_pic = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/lesson_page.jpg')

############################################ lesson


############################################ practice
practice_pic = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/practice_page.jpg')

############################################ practice


############################################ pgpf
setting_status = 0
option = Button(1202,13,63,63)
setting_sta = Button(1202,112,242,140)
a1 = Button(0,0,1023,720)
a2 = Button(1265,79,15,720)
a3 = Button(1023,0,242,112)
a4 = Button(1023,252,242,468)
lession_box = Button(597,487,865-597,593-487)
practice_box = Button(904,487,1171-904,593-487)
lession_box_pic = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/lesson_button.png')
practice_box_pic = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/practice_button.png')
############################################ pgpf

############################################ setting
edit_profile = Button(1036,120,1256-1036,176-120)
logout_profile = Button(1036,187,1256-1036,241-187)
edit_profile_pic = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/edit_profile_button.png')
logout_profile_pic = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/log_out_button.png')
############################################ setting

############################################ regis
take_pic = Button(225,291,200,68)
add_pic = Button(225,395,200,68)
uploadpic = Button(167,180,500-167,548-180)
clear_pic = Button(0,670,100,50)
repic_button = Button(550,180,45,45)
take_p_state = 0
add_p_state = 0
re_pic = 0
backpiconmouse = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/back_button.png')
repic1 = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/re1.png')
repic2 = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/re2.png')

############################################ edit
edit_profile_ui2 = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/edit_profile_page.jpg')
edit_profile_ui = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/edit_profile_page.png')
save_btn =  pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/save_button.png')
############################################ edit

########################################### back
backpiconmouse = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/back_button.png')
backtohome = Button(93,12,59,59)
homepiconmouse = pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/home_button.png')

################################### practice animal
btn_animal_pact = Button(123,50,374,310)
animal_practice_1= pg.image.load('C:/UI-st4/IU64/UIPHOTO/photo/animal_pract_1.jpg')










wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


while run == True:
    if page == 'start':
        screen.blit(startpg,(0,0))
        pg.display.update()
        pg.time.delay(2000)
        page = 'login'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    elif page == 'login':

        # print(filepath)
        # print(newpath)
        screen.blit(fade, (0,0))
        # print(wrong[2])
        if wrong[2] == 1:
            t3 = Text(730,352, 30, "browallianewbold", (255,101,101), 1, 'Incorrect username')
            t3.draw(screen)
        (pos_x, pos_y) = pg.mouse.get_pos()
        if regis_btn.x <= pos_x <= regis_btn.x + regis_btn.w and regis_btn.y <= pos_y <= regis_btn.y + regis_btn.h: #mouseon()
            screen.blit(regis, (728, 388)) # แปลี่ยนสีกล่อง
        if start_btn.x <= pos_x <= start_btn.x + start_btn.w and start_btn.y <= pos_y <= start_btn.y + start_btn.h:
            screen.blit(login, (969, 388))
        if distance_box.text == '  ': # ใส่เพราะแก้บัค
            t3 = Text(740, 290.3, 45, "browallianewbold", (192,192,192), 1, 'Username') #text username 
            t3.draw(screen)
        if distance_box.text == '  ' :
            start_btn_status = False
        elif distance_box.text != '  ' :
            wrong[2] = 0
            start_btn_status = True
        if regis_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1: #next state
                regis_click = 1
        if start_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if start_btn_status is True:  # เพิ่มกรณีที่ไม่มีไฟล์ด้วย 
                    wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    path = 'C:/UI-st4/IU64'
                    filenames = os.listdir(path)
                    for filename in filenames:
                        if distance_box.text+'.txt' == filename:
                            user_status = 'have'
                    if  user_status == 'have' :     
                        file = open(distance_box.text+".txt","r")
                        for i in file:
                            a,b,c,d,e,f = i.split(",")
                            memprofile = [a,b,c,d,e,f]
                            click = 1
                        file.close()
                    if user_status == 'nohave' :  
                        wrong[2] = 1
                    
                if distance_box.text == '  ':
                    wrong[2] = 1 
                    please = True  # get error message
        if click == 1 and pg.mouse.get_pressed()[0] == 0:
            click = 0
            distance_box.text = "  "
            distance_box.txt_surface = distance_box.font.render(distance_box.text, True, pg.Color("black"))
            page = "profile"
        if regis_click == 1 and pg.mouse.get_pressed()[0] == 0:
            regis_click = 0
            page = 'register'
        for box in input_boxes:
            box.draw(screen)
        pg.display.update()
        for event in pg.event.get():
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()
    
    elif page == "register":
        screen.blit(ui3,(0,0))
        (pos_x, pos_y) = pg.mouse.get_pos()
        if backtomain.mouse_on():
            screen.blit(backpiconmouse,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                r_btn_status = False
                newstatus = 0
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "login"
                click =0
        if regis_sub_btn.mouse_on():#mouse_on
            screen.blit(regis, (823,533)) #600, 680, 260, 80
        if username_registors.text == '  '  or firstname_registors.text == '  ' \
            or surname_registors.text == '  ' or nickname_registors== '  ':
                r_btn_status = False
        if username_registors.text != '  ' and firstname_registors.text != '  ' \
            and surname_registors.text != '  ' and nickname_registors!= '  ':
            r_btn_status = True
            wrong[1] = 0
        if wrong[1] == 1:
            t1 = Text(800-10+2+2,503, 30, "browallianewbold", (255,101,101), 1, 'Please enter all information')
            t1.draw(screen)
        # if r_btn_status == True:
        if uploadpic.mouse_on() and newstatus == 0: # ลากเม้าไปโดน blit รูป add picture
            screen.blit(add_p,(128,150))
            if take_p_state == 1: #กดถ่ายรูปแล้วถ่ายรูป (ยังไม่เสร็จ)
                screen.blit(take_p,(224,289))
                if pg.mouse.get_pressed()[0] == 1: 
                    take_p_state = 0
                    pass
                else:
                    take_p_state = 0  
            if take_pic.mouse_on():
                take_p_state = 1
            if add_pic.mouse_on():
                add_p_state = 1
            if add_p_state == 1:  #กดถ่ายรูปแล้ว upload รูป
                screen.blit(upload_p,(224,393))
                if pg.mouse.get_pressed()[0] == 1:
                    filepath=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",\
                    filetypes=(('JPG file','*.jpg'),('PNG file','*.png'))) # เลือกดึงรูปจาก computer เฉพาะ JPG,PNG
                    newstatus = 1
                    re_pic = 1
                    r_btn_status = True  
                    add_p_state = 0 
                else:
                    add_p_state = 0  
        if clear_pic.mouse_on() and pg.mouse.get_pressed()[0] == 1: #กด Clear picture (ยังไม่เสร็จ)
            newstatus = 0
            filepath =''
        if newstatus == 1: #เปลงไฟลภาพให้พอดีกับกรอบรูป 
            image = cv2.imread(filepath)
            Profile_pic = pg.image.load(filepath)
            screen.blit(repic1,(550,545))
            if repic_button.mouse_on():
                screen.blit(repic2,(550,545))
                if pg.mouse.get_pressed()[0] == 1:
                    newstatus = 0
                    filepath =''
            [h,w,d] = image.shape
            if h>w:
                ww = int(398*(w/h))
                hh = 440
                jj = int((398-(398*w/h))/2)
                kk = 0
            if w>h:
                ww = int(398)
                hh = int(440*(h/w))
                jj = 0
                kk = int((440-(440*h/w))/2)
            screen.blit(bgwhite,(128,150))
            screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))
        if regis_sub_btn.mouse_on(): #กดปุ่ม register ทำการสร้างไฟล์ ข้อมูลของแต่ละ User
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True :
                    if newstatus ==1:
                        newpath = shutil.copy(filepath,"user_profile")
                        nna , typefi = newpath.split(".")
                    if newstatus ==0:
                        typefi = 'png'
                        newpath = shutil.copy(defualt_p_path,"user_profile")
                    # f = open(path_to_file, mode)
                    file = open(username_registors.text+".txt","w")
                    # shutil.copy("D:/IU64/"+username_registors.text+".txt","user_temp")
                    # os.remove(username_registors.text+".txt")
                    file = open(username_registors.text+".txt","a")
                    file.write("'"+username_registors.text+"','"+firstname_registors.text+"','"+\
                        surname_registors.text+"','"+nickname_registors.text+","+typefi+","  "\n")          
                    file.close() 
                    if newstatus == 1:
                        if typefi == 'png':
                            os.rename(newpath,'user_profile/'+username_registors.text+'.png') 
                            newpath = ("user_profile/"+username_registors.text+'.png')
                            print(newpath)
                        elif typefi == 'jpg':
                            os.rename(newpath,'user_profile/'+username_registors.text+'.jpg')
                            newpath = ("user_profile/"+username_registors.text+'.jpg')
                    if newstatus == 0:
                        os.rename(newpath,'user_profile/'+username_registors.text+'.png') 
                        newpath = ("user_profile/"+username_registors.text+'.png')
                    for n in range (len(input_registor)):
                            input_registor[n].text = "  "
                            input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                    newstatus = 0
                    re_pic = 0
                    click = 1
                if r_btn_status == False:
                    wrong[1] = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "login"
                click =0
        for box in input_registor:
            box.draw(screen)
        pg.display.update()
        for event in pg.event.get():
            for box in input_registor:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()
    # elif page == "profile": # blit รูปภาพก่อนจะไปยังหน้า profile เพื่อให้การ render เร็วขึ้น
    #     screen.blit(pgpf,(0,0))
    #     userName = memprofile[1].replace("'","").replace(" ","")
    #     userSur = memprofile[2].replace("'","").replace(" ","")
    #     nickname = memprofile[3].replace("'","").replace(" ","")
    #     fullname = userName+"  "+userSur
    #     t3 = Text(743, 215, 45, "browallianewbold", (0,0,0), 1, fullname)
    #     t4 = Text(810, 292, 45, "browallianewbold", (0,0,0), 1, nickname)
    #     filepath = 'C:/UI-st4/IU64/user_profile/'+str(memprofile[0].replace("'",""))+"."+str(memprofile[4])
    #     tttt = pic(filepath,400,440)
    #     screen.blit(pg.transform.scale(tttt[4],(tttt[0],tttt[1])),(85+tttt[2],155+tttt[3])) 
    #     pg.display.update()
    #     page = "profile"
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()

    elif page == "profile":
        # page = "profile"
        screen.blit(pgpf,(0,0))
        userName = memprofile[1].replace("'","").replace(" ","")
        userSur = memprofile[2].replace("'","").replace(" ","")
        nickname = memprofile[3].replace("'","").replace(" ","")
        fullname = userName+"  "+userSur
        t3 = Text(743, 216, 45, "browallianewbold", (0,0,0), 1, fullname)
        t4 = Text(810, 294, 45, "browallianewbold", (0,0,0), 1, nickname)
        filepath = 'C:/UI-st4/IU64/user_profile/'+str(memprofile[0].replace("'",""))+"."+str(memprofile[4])
        tttt = pic(filepath,400,440)
        screen.blit(pg.transform.scale(tttt[4],(tttt[0],tttt[1])),(85+tttt[2],155+tttt[3])) 
        t3.draw(screen)
        t4.draw(screen)
        (pos_x, pos_y) = pg.mouse.get_pos()  
        ####################################################################################################################### 
        if option.mouse_on() :                  #---------setting
            backpage = "profile"                # แสดงรูปภาพ
            screen.blit(all_p,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                backpage = "profile"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        if lession_box.mouse_on():
            screen.blit(lession_box_pic,(597,487))
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lession"
                click =0
        if practice_box.mouse_on():
            screen.blit(practice_box_pic,(904,487))
            if pg.mouse.get_pressed()[0] == 1:
                # pass
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "practiceto"
                click =0
        ####################################################################################################################### 
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    elif page =="setting" :
        (pos_x, pos_y) = pg.mouse.get_pos() # ถ้าเม้ากดยังจุดใดก็ตามที่ไม่ใช้ในกล่อง setting ให้กลับไปยัง state ก่อนหน้า like : pop-up
        case1 = a1.x <= pos_x <= a1.x + a1.w and a1.y <= pos_y <= a1.y + a1.h
        case2 = a2.x <= pos_x <= a2.x + a2.w and a2.y <= pos_y <= a2.y + a2.h
        case3 = a3.x <= pos_x <= a3.x + a3.w and a3.y <= pos_y <= a3.y + a3.h
        case4 = a4.x <= pos_x <= a4.x + a4.w and a4.y <= pos_y <= a4.y + a4.h
        screen.blit(all_p,(1023,12)) 
        if (case1 or case2 or case3 or case4 ) :
            if pg.mouse.get_pressed()[0] == 1  :
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = backpage
                click =0
            # pg.time.delay(5)
        if edit_profile.mouse_on() and backpage !="edit_profile" : # กดเม้าไปยัง edit profile สร้างตัวแปรของหน้า edit profile
            screen.blit(edit_profile_pic,(1034,122))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                m1  = memprofile[1].replace("'","")
                m2  = memprofile[2].replace("'","")
                m3  = memprofile[3].replace("'","")
                m0  = memprofile[0].replace("'","")
                firstname_registors1 = InputBox(695, 170, 472,49,35,14,m1)  # distance input box
                surname_registors1 = InputBox(695, 257, 472,49,35,14,m2)  # distance input box
                nickname_registors1 = InputBox(695, 351, 472, 49,35,14,m3)  # spinner's speed input box
                username_registors1 = InputBox(695, 439, 472,49,35,12,m0)
                edit_member = [surname_registors1,firstname_registors1,nickname_registors1]
                newstatus = 1
                page = "edit_profile"
                click =0
        if logout_profile.mouse_on():
            screen.blit(logout_profile_pic,(1034,186))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "logout"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    elif page =="logout":
        memprofile=["","","","","",""]
        wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        logout_status = 1
        page = "login"
    # elif page == "pre_edit": # blit ภาพ page edit profile
    #     screen.blit(edit_profile_ui2,(0,0))
    #     if newstatus == 1:
    #         image = cv2.imread(filepath)
    #         Profile_pic = pg.image.load(filepath)
    #         [h,w,d] = image.shape
    #         if h>w:
    #             ww = int(398*(w/h))
    #             hh = 440
    #             jj = int((398-(398*w/h))/2)
    #             kk = 0
    #         if w>h:
    #             ww = int(398)
    #             hh = int(440*(h/w))
    #             jj = 0
    #             kk = int((440-(440*h/w))/2)
    #         screen.blit(bgwhite,(128,150))
    #         screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))
    #     page = "edit_profile"
    elif page == "edit_profile": 
        
        backpage =""
        # screen.blit(edit_profile_ui,(0,0))
        screen.blit(edit_profile_ui2,(0,0))
        if newstatus == 1:
            image = cv2.imread(filepath)
            Profile_pic = pg.image.load(filepath)
            [h,w,d] = image.shape
            if h>w:
                ww = int(398*(w/h))
                hh = 440
                jj = int((398-(398*w/h))/2)
                kk = 0
            if w>h:
                ww = int(398)
                hh = int(440*(h/w))
                jj = 0
                kk = int((440-(440*h/w))/2)
            screen.blit(bgwhite,(128,150))
            screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))
        t5 = Text(695, 439+13, 35, "browallianewbold", (0,0,0), 1, m0)
        t5.draw(screen)
        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(all_p,(1023,12)) 
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                backpage = "edit_profile"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        if save_sub_btn.mouse_on():
            screen.blit(save_btn, (823,522)) #600, 680, 260, 80
        if firstname_registors1.text == '  ' or surname_registors1.text == '  ' or nickname_registors1== '  ':
                r_btn_status = False
        if firstname_registors1.text != '  ' and surname_registors1.text != '  ' and nickname_registors1 != '  ':
            r_btn_status = True
        if save_sub_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True :
                    click =1
                    mmmmm = memprofile[0].replace("'","")
                    file = open(mmmmm+".txt","r+")
                    file.write(memprofile[0]+",'"+firstname_registors1.text+"','"+surname_registors1.text+"','"+nickname_registors1.text+"',"+memprofile[4]+","''"\n")          
                    file.close() 
                    file = open(mmmmm+".txt","r")
                    for i in file:
                        a,b,c,d,e,f = i.split(",")
                        memprofile = [a,b,c,d,e,f]
                    
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        
        if backtomain.mouse_on():
            # print(" hold ")
            screen.blit(backpiconmouse,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                # for n in range (len(input_registor)):
                #     input_registor[n].text = "  "
                #     input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                # r_btn_status = False
                # newstatus = 0
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        # else :
        #     screen.blit(edit_profile_ui,(0,0))

        for box in edit_member:
            box.draw(screen)
        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(all_p,(1023,12))  
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                backpage = "edit_profile"
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        pg.display.update()
        for event in pg.event.get():
            for box in edit_member:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit() 
    elif page == "lession":
        # print("5555555555555555555555555555555555555")
        screen.blit(lession_pic,(0,0))
        if backtohome.mouse_on():
            screen.blit(homepiconmouse,(93,12))
            if pg.mouse.get_pressed()[0] == 1:
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                r_btn_status = False
                newstatus = 0
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "lession"
            screen.blit(all_p,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 
    elif page == "practiceto":
        screen.blit(practice_pic,(0,0))
        backpage = "practiceto"
        if backtohome.mouse_on():
            screen.blit(homepiconmouse,(93,12))
            if pg.mouse.get_pressed()[0] == 1:
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                r_btn_status = False
                newstatus = 0
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            screen.blit(all_p,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click=1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        if btn_animal_pact.mouse_on() :   #animal_prct
            # screen.blit(all_p,(1023,12)) 
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click=1

            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "animal_practice_1"
                click =0
        
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == "animal_practice_1":
        screen.blit(animal_practice_1,(0,0))
        backpage = "practiceto"
        if backtohome.mouse_on():
            screen.blit(homepiconmouse,(93,12))
            if pg.mouse.get_pressed()[0] == 1:
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
                r_btn_status = False
                newstatus = 0
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            screen.blit(all_p,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click=1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0

        
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 


























































































