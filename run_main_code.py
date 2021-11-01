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

# from initial_setting import run_setting
# from initial_setting import run
import initial_setting as ins
from initial_setting import regis_click,newstatus
# run_setting()
page = 'start'
while ins.run == True:
    # pass
    if page == 'start':
        ins.screen.blit(ins.startpg,(0,0))
        pg.display.update()
        pg.time.delay(2000)
        page = 'login'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    elif page == 'login':

        # print(filepath)
        # print(newpath)
        ins.screen.blit(ins.fade, (0,0))
        # print(wrong[2])
        if ins.wrong[2] == 1:
            t3 = Text(730,352, 30, "browallianewbold", (255,101,101), 1, 'Incorrect username')
            t3.draw(ins.screen)
        (pos_x, pos_y) = pg.mouse.get_pos()
        if ins.regis_btn.x <= pos_x <= ins.regis_btn.x + ins.regis_btn.w and ins.regis_btn.y <= pos_y <= ins.regis_btn.y + ins.regis_btn.h: #mouseon()
            ins.screen.blit(ins.regis, (728, 388)) # แปลี่ยนสีกล่อง
        if ins.start_btn.x <= pos_x <= ins.start_btn.x + ins.start_btn.w and ins.start_btn.y <= pos_y <= ins.start_btn.y + ins.start_btn.h:
            ins.screen.blit(ins.login, (969, 388))
        if ins.distance_box.text == '  ': # ใส่เพราะแก้บัค
            t3 = Text(740, 290.3, 45, "browallianewbold", (192,192,192), 1, 'Username') #text username 
            t3.draw(ins.screen)
        if ins.distance_box.text == '  ' :
            start_btn_status = False
        elif ins.distance_box.text != '  ' :
            ins.wrong[2] = 0
            start_btn_status = True
        if ins.regis_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1: #next state
                regis_click = 1
        if ins.start_btn.mouse_on():
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if start_btn_status is True:  # เพิ่มกรณีที่ไม่มีไฟล์ด้วย 
                    ins.wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    path = 'iC:/fra361_st4_voca_ui'
                    filenames = os.listdir(path)
                    for filename in filenames:
                        if ins.distance_box.text+'.txt' == filename:
                            user_status = 'have'
                    if  user_status == 'have' :     
                        file = open(ins.distance_box.text+".txt","r")
                        for i in file:
                            a,b,c,d,e,f = i.split(",")
                            memprofile = [a,b,c,d,e,f]
                            ins.click = 1
                        file.close()
                    if user_status == 'nohave' :  
                        ins.wrong[2] = 1
                    
                if ins.distance_box.text == '  ':
                    ins.wrong[2] = 1 
                    please = True  # get error message
        if ins.click == 1 and pg.mouse.get_pressed()[0] == 0:
            ins.click = 0
            ins.distance_box.text = "  "
            ins.distance_box.txt_surface = ins.distance_box.font.render(ins.distance_box.text, True, pg.Color("black"))
            page = "profile"
        if regis_click == 1 and pg.mouse.get_pressed()[0] == 0:
            regis_click = 0
            page = 'register'
        for box in ins.input_boxes:
            box.draw(ins.screen)
        pg.display.update()
        for event in pg.event.get():
            for box in ins.input_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()
    
    elif page == "register":
        ins.screen.blit(ins.ui3,(0,0))
        (pos_x, pos_y) = pg.mouse.get_pos()
        if ins.backtomain.mouse_on():
            ins.screen.blit(ins.backpiconmouse,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                for n in range (len(ins.input_registor)):
                    ins.input_registor[n].text = "  "
                    ins.input_registor[n].txt_surface = ins.input_registor[n].font.render(ins.input_registor[n].text, True, pg.Color("black"))
                r_btn_status = False
                newstatus = 0
                ins.click = 1
            if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
                page = "login"
                ins.click =0
        if ins.regis_sub_btn.mouse_on():#mouse_on
            ins.screen.blit(ins.regis, (823,533)) #600, 680, 260, 80
        if ins.username_registors.text == '  '  or ins.firstname_registors.text == '  ' \
            or ins.surname_registors.text == '  ' or ins.nickname_registors== '  ':
                r_btn_status = False
        if ins.username_registors.text != '  ' and ins.firstname_registors.text != '  ' \
            and ins.surname_registors.text != '  ' and ins.nickname_registors!= '  ':
            r_btn_status = True
            ins.wrong[1] = 0
        if ins.wrong[1] == 1:
            t1 = Text(800-10+2+2,503, 30, "browallianewbold", (255,101,101), 1, 'Please enter all information')
            t1.draw(ins.screen)
        # if r_btn_status == True:
        if ins.uploadpic.mouse_on() and newstatus == 0: # ลากเม้าไปโดน blit รูป add picture
            ins.screen.blit(ins.add_p,(128,150))
            if take_p_state == 1: #กดถ่ายรูปแล้วถ่ายรูป (ยังไม่เสร็จ)
                ins.screen.blit(ins.take_p,(224,289))
                if pg.mouse.get_pressed()[0] == 1: 
                    take_p_state = 0
                    pass
                else:
                    take_p_state = 0  
            if ins.take_pic.mouse_on():
                take_p_state = 1
            if ins.add_pic.mouse_on():
                add_p_state = 1
            if add_p_state == 1:  #กดถ่ายรูปแล้ว upload รูป
                ins.screen.blit(ins.upload_p,(224,393))
                if pg.mouse.get_pressed()[0] == 1:
                    filepath=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",\
                    filetypes=(('JPG file','*.jpg'),('PNG file','*.png'))) # เลือกดึงรูปจาก computer เฉพาะ JPG,PNG
                    newstatus = 1
                    re_pic = 1
                    r_btn_status = True  
                    add_p_state = 0 
                else:
                    add_p_state = 0  
        if ins.clear_pic.mouse_on() and pg.mouse.get_pressed()[0] == 1: #กด Clear picture (ยังไม่เสร็จ)
            newstatus = 0
            filepath =''
        if newstatus == 1: #เปลงไฟลภาพให้พอดีกับกรอบรูป 
            image = cv2.imread(filepath)
            Profile_pic = pg.image.load(filepath)
            ins.screen.blit(ins.repic1,(550,545))
            if ins.repic_button.mouse_on():
                ins.screen.blit(ins.repic2,(550,545))
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
            ins.screen.blit(ins.bgwhite,(128,150))
            ins.screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))
        if ins.regis_sub_btn.mouse_on(): #กดปุ่ม register ทำการสร้างไฟล์ ข้อมูลของแต่ละ User
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True :
                    if newstatus ==1:
                        newpath = shutil.copy(filepath,"user_profile")
                        nna , typefi = newpath.split(".")
                    if newstatus ==0:
                        typefi = 'png'
                        newpath = shutil.copy(ins.defualt_p_path,"user_profile")
                    # f = open(path_to_file, mode)
                    file = open(ins.username_registors.text+".txt","w")
                    # shutil.copy("D:/IU64/"+username_registors.text+".txt","user_temp")
                    # os.remove(username_registors.text+".txt")
                    file = open(ins.username_registors.text+".txt","a")
                    file.write("'"+ins.username_registors.text+"','"+ins.firstname_registors.text+"','"+\
                        ins.surname_registors.text+"','"+ins.nickname_registors.text+","+typefi+","  "\n")          
                    file.close() 
                    if newstatus == 1:
                        if typefi == 'png':
                            os.rename(newpath,'user_profile/'+ins.username_registors.text+'.png') 
                            newpath = ("user_profile/"+ins.username_registors.text+'.png')
                            print(newpath)
                        elif typefi == 'jpg':
                            os.rename(newpath,'user_profile/'+ins.username_registors.text+'.jpg')
                            newpath = ("user_profile/"+ins.username_registors.text+'.jpg')
                    if newstatus == 0:
                        os.rename(newpath,'user_profile/'+ins.username_registors.text+'.png') 
                        newpath = ("user_profile/"+ins.username_registors.text+'.png')
                    for n in range (len(ins.input_registor)):
                            ins.input_registor[n].text = "  "
                            ins.input_registor[n].txt_surface = ins.input_registor[n].font.render(ins.input_registor[n].text, True, pg.Color("black"))
                    newstatus = 0
                    re_pic = 0
                    ins.click = 1
                if r_btn_status == False:
                    ins.wrong[1] = 1
            if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
                page = "login"
                ins.click =0
        for box in ins.input_registor:
            box.draw(ins.screen)
        pg.display.update()
        for event in pg.event.get():
            for box in ins.input_registor:
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
    #     filepath = 'iC:/fra361_st4_voca_ui/user_profile/'+str(memprofile[0].replace("'",""))+"."+str(memprofile[4])
    #     tttt = pic(filepath,400,440)
    #     screen.blit(pg.transform.scale(tttt[4],(tttt[0],tttt[1])),(85+tttt[2],155+tttt[3])) 
    #     pg.display.update()
    #     page = "profile"
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()

    elif page == "profile":
        # page = "profile"
        ins.screen.blit(ins.pgpf,(0,0))
        userName = memprofile[1].replace("'","").replace(" ","")
        userSur = memprofile[2].replace("'","").replace(" ","")
        nickname = memprofile[3].replace("'","").replace(" ","")
        fullname = userName+"  "+userSur
        t3 = Text(743, 216, 45, "browallianewbold", (0,0,0), 1, fullname)
        t4 = Text(810, 294, 45, "browallianewbold", (0,0,0), 1, nickname)
        filepath = 'iC:/fra361_st4_voca_ui/user_profile/'+str(memprofile[0].replace("'",""))+"."+str(memprofile[4])
        tttt = pic(filepath,400,440)
        ins.screen.blit(pg.transform.scale(tttt[4],(tttt[0],tttt[1])),(85+tttt[2],155+tttt[3])) 
        t3.draw(ins.screen)
        t4.draw(ins.screen)
        (pos_x, pos_y) = pg.mouse.get_pos()  
        ####################################################################################################################### 
        if ins.option.mouse_on() :                  #---------setting
            backpage = "profile"                # แสดงรูปภาพ
            ins.screen.blit(ins.all_p,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                backpage = "profile"
                ins.click = 1
            if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
                page = "setting"
                ins.click =0
        if ins.lession_box.mouse_on():
            ins.screen.blit(ins.lession_box_pic,(597,487))
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                ins.click = 1
            if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
                page = "lession"
                ins.click =0
        if ins.practice_box.mouse_on():
            ins.screen.blit(ins.practice_box_pic,(904,487))
            if pg.mouse.get_pressed()[0] == 1:
                # pass
                ins.click = 1
            if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
                page = "practiceto"
                ins.click =0
        ####################################################################################################################### 
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    # elif page =="setting" :
    #     (pos_x, pos_y) = pg.mouse.get_pos() # ถ้าเม้ากดยังจุดใดก็ตามที่ไม่ใช้ในกล่อง setting ให้กลับไปยัง state ก่อนหน้า like : pop-up
    #     case1 = a1.x <= pos_x <= a1.x + a1.w and a1.y <= pos_y <= a1.y + a1.h
    #     case2 = a2.x <= pos_x <= a2.x + a2.w and a2.y <= pos_y <= a2.y + a2.h
    #     case3 = a3.x <= pos_x <= a3.x + a3.w and a3.y <= pos_y <= a3.y + a3.h
    #     case4 = a4.x <= pos_x <= a4.x + a4.w and a4.y <= pos_y <= a4.y + a4.h
    #     screen.blit(all_p,(1023,12)) 
    #     if (case1 or case2 or case3 or case4 ) :
    #         if pg.mouse.get_pressed()[0] == 1  :
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = backpage
    #             ins.click =0
    #         # pg.time.delay(5)
    #     if edit_profile.mouse_on() and backpage !="edit_profile" : # กดเม้าไปยัง edit profile สร้างตัวแปรของหน้า edit profile
    #         screen.blit(edit_profile_pic,(1034,122))
    #         if pg.mouse.get_pressed()[0] == 1:
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             m1  = memprofile[1].replace("'","")
    #             m2  = memprofile[2].replace("'","")
    #             m3  = memprofile[3].replace("'","")
    #             m0  = memprofile[0].replace("'","")
    #             firstname_registors1 = InputBox(695, 170, 472,49,35,14,m1)  # distance input box
    #             surname_registors1 = InputBox(695, 257, 472,49,35,14,m2)  # distance input box
    #             nickname_registors1 = InputBox(695, 351, 472, 49,35,14,m3)  # spinner's speed input box
    #             username_registors1 = InputBox(695, 439, 472,49,35,12,m0)
    #             edit_member = [surname_registors1,firstname_registors1,nickname_registors1]
    #             newstatus = 1
    #             page = "edit_profile"
    #             ins.click =0
    #     if logout_profile.mouse_on():
    #         screen.blit(logout_profile_pic,(1034,186))
    #         if pg.mouse.get_pressed()[0] == 1:
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "logout"
    #             ins.click =0
    #     pg.display.update()
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()
    # elif page =="logout":
    #     memprofile=["","","","","",""]
    #     wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #     logout_status = 1
    #     page = "login"
    # # elif page == "pre_edit": # blit ภาพ page edit profile
    # #     screen.blit(edit_profile_ui2,(0,0))
    # #     if newstatus == 1:
    # #         image = cv2.imread(filepath)
    # #         Profile_pic = pg.image.load(filepath)
    # #         [h,w,d] = image.shape
    # #         if h>w:
    # #             ww = int(398*(w/h))
    # #             hh = 440
    # #             jj = int((398-(398*w/h))/2)
    # #             kk = 0
    # #         if w>h:
    # #             ww = int(398)
    # #             hh = int(440*(h/w))
    # #             jj = 0
    # #             kk = int((440-(440*h/w))/2)
    # #         screen.blit(bgwhite,(128,150))
    # #         screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))
    # #     page = "edit_profile"
    # elif page == "edit_profile": 
        
    #     backpage =""
    #     # screen.blit(edit_profile_ui,(0,0))
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
    #     t5 = Text(695, 439+13, 35, "browallianewbold", (0,0,0), 1, m0)
    #     t5.draw(screen)
    #     if option.mouse_on() :   #---------setting
    #         backpage = "edit_profile"
    #         screen.blit(all_p,(1023,12)) 
    #         # pg.display.update()
    #         if pg.mouse.get_pressed()[0] == 1:
    #             backpage = "edit_profile"
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "setting"
    #             ins.click =0
    #     if save_sub_btn.mouse_on():
    #         screen.blit(save_btn, (823,522)) #600, 680, 260, 80
    #     if firstname_registors1.text == '  ' or surname_registors1.text == '  ' or nickname_registors1== '  ':
    #             r_btn_status = False
    #     if firstname_registors1.text != '  ' and surname_registors1.text != '  ' and nickname_registors1 != '  ':
    #         r_btn_status = True
    #     if save_sub_btn.mouse_on():
    #         if pg.mouse.get_pressed()[0] == 1:  # button get ins.click
    #             if r_btn_status == True :
    #                 ins.click =1
    #                 mmmmm = memprofile[0].replace("'","")
    #                 file = open(mmmmm+".txt","r+")
    #                 file.write(memprofile[0]+",'"+firstname_registors1.text+"','"+surname_registors1.text+"','"+nickname_registors1.text+"',"+memprofile[4]+","''"\n")          
    #                 file.close() 
    #                 file = open(mmmmm+".txt","r")
    #                 for i in file:
    #                     a,b,c,d,e,f = i.split(",")
    #                     memprofile = [a,b,c,d,e,f]
                    
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "profile"
    #             ins.click =0
        
    #     if backtomain.mouse_on():
    #         # print(" hold ")
    #         screen.blit(backpiconmouse,(16,12))
    #         if pg.mouse.get_pressed()[0] == 1:
    #             # for n in range (len(input_registor)):
    #             #     input_registor[n].text = "  "
    #             #     input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
    #             # r_btn_status = False
    #             # newstatus = 0
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "profile"
    #             ins.click =0
    #     # else :
    #     #     screen.blit(edit_profile_ui,(0,0))

    #     for box in edit_member:
    #         box.draw(screen)
    #     if option.mouse_on() :   #---------setting
    #         backpage = "edit_profile"
    #         screen.blit(all_p,(1023,12))  
    #         # pg.display.update()
    #         if pg.mouse.get_pressed()[0] == 1:
    #             backpage = "edit_profile"
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "setting"
    #             ins.click =0
    #     pg.display.update()
    #     for event in pg.event.get():
    #         for box in edit_member:
    #             box.handle_event(event)
    #         if event.type == pg.QUIT:
    #             pg.quit() 
    # elif page == "lession":
    #     # print("5555555555555555555555555555555555555")
    #     screen.blit(lession_pic,(0,0))
    #     if backtohome.mouse_on():
    #         screen.blit(homepiconmouse,(93,12))
    #         if pg.mouse.get_pressed()[0] == 1:
    #             for n in range (len(input_registor)):
    #                 input_registor[n].text = "  "
    #                 input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
    #             r_btn_status = False
    #             newstatus = 0
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "profile"
    #             ins.click =0
    #     if option.mouse_on() :   #---------setting
    #         backpage = "lession"
    #         screen.blit(all_p,(1023,12)) 
    #         pg.display.update()
    #         if pg.mouse.get_pressed()[0] == 1:
    #             ins.click = 1
    #             option_sta =1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "setting"
    #             ins.click =0
    #     pg.display.update()
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit() 
    # elif page == "practiceto":
    #     screen.blit(practice_pic,(0,0))
    #     backpage = "practiceto"
    #     if backtohome.mouse_on():
    #         screen.blit(homepiconmouse,(93,12))
    #         if pg.mouse.get_pressed()[0] == 1:
    #             for n in range (len(input_registor)):
    #                 input_registor[n].text = "  "
    #                 input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
    #             r_btn_status = False
    #             newstatus = 0
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "profile"
    #             ins.click =0
    #     if option.mouse_on() :   #---------setting
    #         screen.blit(all_p,(1023,12)) 
    #         pg.display.update()
    #         if pg.mouse.get_pressed()[0] == 1:
    #             ins.click=1
    #             option_sta =1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "setting"
    #             ins.click =0
    #     if btn_animal_pact.mouse_on() :   #animal_prct
    #         # screen.blit(all_p,(1023,12)) 
    #         # pg.display.update()
    #         if pg.mouse.get_pressed()[0] == 1:
    #             ins.click=1

    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "animal_practice_1"
    #             ins.click =0
        
    #     pg.display.update()
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit() 

    # elif page == "animal_practice_1":
    #     screen.blit(animal_practice_1,(0,0))
    #     backpage = "practiceto"
    #     if backtohome.mouse_on():
    #         screen.blit(homepiconmouse,(93,12))
    #         if pg.mouse.get_pressed()[0] == 1:
    #             for n in range (len(input_registor)):
    #                 input_registor[n].text = "  "
    #                 input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))
    #             r_btn_status = False
    #             newstatus = 0
    #             ins.click = 1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "profile"
    #             ins.click =0
    #     if option.mouse_on() :   #---------setting
    #         screen.blit(all_p,(1023,12)) 
    #         pg.display.update()
    #         if pg.mouse.get_pressed()[0] == 1:
    #             ins.click=1
    #             option_sta =1
    #         if pg.mouse.get_pressed()[0] == 0 and ins.click ==1:
    #             page = "setting"
    #             ins.click =0

        
    #     pg.display.update()
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit() 