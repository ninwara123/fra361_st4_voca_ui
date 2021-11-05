# project_path = 'C:/fra361_st4_voca_ui'
project_path = 'C:/fra361_st4_voca_ui'

# from os import name
from os import path, read
import os
from tkinter.constants import E
import pygame as pg
from pygame.draw import rect
from object import Text, Button,InputBox
import time
from tkinter import filedialog, mainloop
import shutil
import cv2
import upload_pic as ulp
from function import resize,pic
import face_recognition as face
import numpy as np
import csv

### init ###################################################################################################
pg.init()
win_x, win_y = 1280, 720
screen = pg.display.set_mode((win_x, win_y))

### color ###################################################################################################                                                                                                                                                   
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
light_gray = (230, 230, 230)
green = (0, 200, 0)
red = (200, 0, 0)
mint = (120,255,255)
orange = (242,157,0)

### creat object ###########################################################################################
#global

#login_page
register_btn = Button(729, 388 , 217, 87)
login_btn = Button(969, 388, 217, 87)
distance_box = InputBox(723, 273.3, 471,60,45,17)  # distance input box

#register_page
firstname_register = InputBox(695, 170, 472,49,35,12)  # distance input box
surname_register = InputBox(695, 257, 472,49,35,12)  # distance input box
nickname_register = InputBox(695, 351, 472, 49,35,12)  # spinner's speed input box
username_register = InputBox(695, 439, 472,49,35,12)  # distance input box
regis_sub_btn = Button(823, 533, 217,60)

uploadpic = Button(167,180,500-167,548-180)
take_pic = Button(225,291,200,68)
add_pic = Button(225,395,200,68)
repic_btn = Button(550,180,45,45)
clear_pic = Button(0,670,100,50)

# profile_page
option = Button(1202,13,63,63)
lesson_btn = Button(597,487,268,106)
practice_btn = Button(904,487,268,106)

#setting_page
a1 = Button(0,0,1023,720)
a2 = Button(1265,79,15,720)
a3 = Button(1023,0,242,112)
a4 = Button(1023,252,242,468)
edit_profile_btn = Button(1036,120,1256-1036,176-120)
logout_profile_btn = Button(1036,187,1256-1036,241-187)

#edit_profile_page
save_sub_btn = Button(823, 533, 217,60)

#back
back_page_btn = Button(13,13,59,59)
back_home_btn = Button(93,13,59,59)

#animal
animal_btn = Button(123,50,375,310)

#classroon
classroon_btn = Button(455,50,375,310)

#food
food_btn = Button(860,50,375,310)

#test
back_test_btn = Button(1130,100,63,63)
next_test_btn = Button(1200,100,63,63)
correct_btn = Button(800,250,400,400)

### variables #############################################################################################
enter_press = 0
click = 0
regis_click = 0
login_click = 0
progress_percent = 0.00
progress_point = 0

#list

wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
input_registor = [surname_register,firstname_register,nickname_register,username_register]
input_boxes = [distance_box]
Article = [0,0] # no.Article , check change Article

memprofile = []            # 'username', 'firstname', 'surname', 'nickname','type_of_pic'
hold_p = []                # 'animal_hold_p','classroom_hold_p','food_hold_p'
test_pass =['','','']      # 'animal_pass','classroom_pass','food_pass'
csv_member_list = []

# state variables
page = 'start'
newstatus = 0
take_pic_state = 0
add_pic_state = 0
user_status = 'nohave' 
pass_test_flag = 0
mark_pass = ''
#path
filepath = ""
# user_data_path = 'C:/fra361_st4_voca_ui/user_data'
user_data_path = project_path +'/user_data'

#words
animal_word_pack = [0,['Turtle','Starfish','Octopus','Jellyfish','Seahorse']]
classroon_word_pack  =  [1,['Calculator','Calendar','Magnifying Glass','Notice Board','Scissors']]
food_word_pack =  [2,['Noodle','Spaghetti','Cookies','Croissant','Lamonade']]
word_test = [] #no.set , word 



#test 
type_test_inputbox = InputBox(340,510,600,80,60,6)
animal_boxes = [type_test_inputbox]
animal_key_check_button = Button(1000,600,280,120)
animal_key_check_i = 0



### face recognition #####################################################################
capper = True
txt_member_list = []
mempicture_list = []
user_image = []
user_face_encoding = []
known_face_encodings = []
known_face_names = []
mmmmooo = []
k = 0
### run code ###############################################################################################
############################################################################################################
############################################################################################################
############################################################################################################



while(1):
    
    (pos_x, pos_y) = pg.mouse.get_pos()

##### CODE START PAGE #######################################################################################
    if page == 'start':
        screen.blit(ulp.first_page,(0,0))
        pg.display.update()
        pg.time.delay(2000)
        page = 'login'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

##### CODE SCAN PAGE #########################################################################################
    elif page == 'scan':

        filenames = os.listdir(user_data_path)
        for filename in filenames:
            if '.csv' in filename:
                txt_member_list.append(filename)
        

        for o in range(len(txt_member_list)):
            file_name,type_file = txt_member_list[o].split(".")

            user_data_file = open('user_data/'+file_name+'.csv','r', encoding="utf8")
            reader = csv.reader(user_data_file)
            for row in reader:
                memprofile = row[0:5]
                # hold_p = row[5:8]
                # test_pass = row[8:11]
                mempicture_list.append(file_name+"."+memprofile[4])
            user_data_file.close()

            # file = open(txt_member_list[o],"r")
            # for i in file:
            #     a,b,c,d,e,f = i.split(",")
            #     # memprofile = [a,b,c,d,e,f]
            #     mempicture_list.append(file_name+"."+e)
            # file.close()
        print('txt_member_list')
        print(txt_member_list)
        print('mempicture_list')
        print(mempicture_list)
        print(len(txt_member_list))
        #ใบหน้าคนที่ต้องการรู้จำเป็นreference #คนที่1

        for i in range(len(txt_member_list)):
            # print(mempicture_list[i])
            file_name,type_file = txt_member_list[i].split(".")
            # mmmmooo.append(face.load_image_file(str(mempicture_list[i])))
            # user_face_encoding = face.face_encodings(mmmmooo[i])[0]
            known_face_encodings.append(face.face_encodings(face.load_image_file("user_data/"+mempicture_list[i]))[0])
            known_face_names.append(file_name)
        face_locations = []
        face_encodings = []
        face_names = []
        face_percent = []
        # print(known_face_encodings)
        print(known_face_names)
        video_capture = cv2.VideoCapture(0) 
        while capper == True:
            k += 1 
            print(page,k)
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0,0), fx=0.3,fy=0.3)
            rgb_small_frame = small_frame[:,:,::-1]
            face_names = []
            face_percent = []
            face_locations = face.face_locations(rgb_small_frame, model="cnn")
            face_encodings = face.face_encodings(rgb_small_frame, face_locations)
            for face_encoding in face_encodings:
                face_distances = face.face_distance(known_face_encodings, face_encoding)
                best = np.argmin(face_distances)
                face_percent_value = 1-face_distances[best]
                if face_percent_value >= 0.5:
                    name = known_face_names[best]
                    
                    filenames = os.listdir(user_data_path)
                    for filename in filenames:
                        if name+'.txt' == filename:
                            user_status = 'have'
                    if  user_status == 'have' :     
                        file = open(name+".txt","r")
                        for i in file:
                            a,b,c,d,e,f = i.split(",")
                            memprofile = [a,b,c,d,e,f]
                        file.close()
                    capper = False
                    page = "profile"
                    print("findddddd")
            if k >= 5:
                page = "login"
                capper = False
                # face_names.append(name)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # else:
            #     break
        video_capture.release()
        cv2.destroyAllWindows()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

##### CODE LOGIN PAGE ########################################################################################

    elif page == 'login':
        screen.blit(ulp.login_page, (0,0))
        if wrong[2] == 1:
            t3 = Text(730,352, 30, "browallianewbold", (255,101,101), 1, 'Incorrect username')
            t3.draw(screen)
        if register_btn.mouse_on():
            screen.blit(ulp.register_green_btn, (728, 388))
            if pg.mouse.get_pressed()[0] == 1: #next state
                regis_click = 1
        if regis_click == 1 and pg.mouse.get_pressed()[0] == 0:
            regis_click = 0
            page = 'register'
            distance_box.text = "  "
            distance_box.txt_surface = distance_box.font.render(distance_box.text, True, pg.Color("black"))

        if distance_box.text == '  ': # ใส่เพราะแก้บัค
            t3 = Text(740, 290.3, 45, "browallianewbold", (192,192,192), 1, 'Username') #text username 
            t3.draw(screen)
        if distance_box.text == '  ' :
            login_btn_status = False
        elif distance_box.text != '  ' :
            wrong[2] = 0
            login_btn_status = True
        
        if login_btn.mouse_on() or enter_press == 1:
            screen.blit(ulp.login_green_btn, (969, 388))
            if pg.mouse.get_pressed()[0] == 1 or enter_press == 1:  # button get click
                enter_press = 0

                if login_btn_status is True:  # เพิ่มกรณีที่ไม่มีไฟล์ด้วย 
                    wrong[2] = 0
                    
                    filenames = os.listdir(user_data_path)
                    for filename in filenames:
                        if distance_box.text+'.csv' == filename:
                            user_status = 'have'
                    if  user_status == 'have' : 
                        click = 1    
                        user_data_file = open('user_data/'+distance_box.text+'.csv','r', encoding="utf8")
                        reader = csv.reader(user_data_file)
                        for row in reader:
                            memprofile = row[0:5]
                            hold_p = row[5:8]
                            test_pass = row[8:11]
                        user_data_file.close()
                    print('memprofile')
                    print(memprofile)
                    print("hold_p")
                    print(hold_p)
                    print("test pass")
                    print(test_pass)        
                    # page = 'profile'
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

        distance_box.draw(screen)

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_RETURN:    
                    enter_press = 1 
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()

##### CODE REGISTER PAGE #####################################################################################
    
    elif page == 'register':
        screen.blit(ulp.register_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_btn,(16,12))
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

        if username_register.text == '  '  or firstname_register.text == '  ' or surname_register.text == '  ' or nickname_register== '  ':
                r_btn_status = False


        if username_register.text != '  ' and firstname_register.text != '  ' \
            and surname_register.text != '  ' and nickname_register!= '  ':
            r_btn_status = True
            wrong[1] = 0
            wrong[3] = 0



        if uploadpic.mouse_on() and newstatus == 0: # ลากเม้าไปโดน blit รูป add picture
            screen.blit(ulp.add_pic_btn,(128,150))
            if take_pic.mouse_on():
                if pg.mouse.get_pressed()[0] == 1: 
                    take_pic_state = 1
                screen.blit(ulp.take_pic_btn,(224,289))
            while take_pic_state == 1:
                takephoto = cv2.VideoCapture(0)
                ret, frame = takephoto.read()
                cv2.imshow('video',frame)
                if (cv2.waitKey(1) & 0xFF == 13):
                    cv2.imwrite("temp_data/capture.png",frame)
                    take_pic_state = 0
                    newstatus = 1
                # C:/fra361_st4_voca_ui/temp_data
                    filepath = project_path+'/temp_data/capture.png'
                    takephoto.release()
                    cv2.destroyAllWindows()
            if add_pic.mouse_on():  #กดถ่ายรูปแล้ว upload รูป
                screen.blit(ulp.upload_pic_btn,(224,393))
                if pg.mouse.get_pressed()[0] == 1:
                    filepath=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",\
                    filetypes=(('JPG file','*.jpg'),('PNG file','*.png'))) # เลือกดึงรูปจาก computer เฉพาะ JPG,PNG
                    print("\n file path ########## \n")
                    print(filepath)
                    newstatus = 1
                    re_pic = 1
                    r_btn_status = True  
                    add_pic_state = 0 
                else:
                    add_pic_state = 0  
        filenames = os.listdir(user_data_path)
        for filename in filenames:
            if '.csv' in filename:
                x1,x2 = filename.split(".")
                csv_member_list.append(x1)
        if username_register.text in csv_member_list:
            wrong[3] = 1
        if username_register.text not in csv_member_list:
            wrong[3] = 0
        if wrong[3] == 1:
            t1 = Text(740, 100, 30, "browallianewbold", red, 1, 'Username is already used') #text username 
            t1.draw(screen)
        if newstatus == 1: #เปลงไฟลภาพให้พอดีกับกรอบรูป ##function
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
            screen.blit(ulp.bgwhite,(128,150))
            screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))


        if regis_sub_btn.mouse_on(): #กดปุ่ม register ทำการสร้างไฟล์ ข้อมูลของแต่ละ User
            screen.blit(ulp.register_green_btn, (823,533)) #600, 680, 260, 80
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                # wrong[1] = 0
                # wrong[3] = 0 
                # filenames = os.listdir(user_data_path)
                # for filename in filenames:
                #     if username_register.text+'.csv' == filename:
                #         # r_btn_status = False
                #         wrong[3] = 1
                #     # else:
                #     #     wrong[3] = 0
                if r_btn_status == True and wrong[3] == 0 :
                    if newstatus ==1:
                        newpath = shutil.copy(filepath,"user_data")
                        not_use , typefi = newpath.split(".")
                    if newstatus ==0:
                        typefi = 'png'
                        newpath = shutil.copy(ulp.defualt_user_pic_path,"user_data")

                    user_data_file = open('user_data/'+username_register.text+'.csv', 'x') #creat file
                    # f.close()
                    # row = ['username', 'firstname', 'surname', 'nickname','type_of_pic',
                    #         'animal_hold_p','classroom_hold_p','food_hold_p','animal_pass','classroom_pass','food_pass']
                    row = [username_register.text, firstname_register.text, surname_register.text, nickname_register.text,typefi,
                           0,0,0,'','','']
                    
                    user_data_file = open('user_data/'+username_register.text+'.csv','w', encoding='UTF8', newline='') 
                    writer = csv.writer(user_data_file)
                    writer.writerow(row)
                    user_data_file.close()

                    if newstatus == 1:
                        if typefi == 'png':
                            os.rename(newpath,'user_data/'+username_register.text+'.png') 

                        elif typefi == 'jpg':
                            os.rename(newpath,'user_data/'+username_register.text+'.jpg')

                    if newstatus == 0:
                        os.rename(newpath,'user_data/'+username_register.text+'.png') 

                   
                    newstatus = 0
                    re_pic = 0
                    click = 1
                    # wrong[1] = 0

                if r_btn_status == False:
                    wrong[1] = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                for n in range (len(input_registor)):
                    input_registor[n].text = "  "
                    input_registor[n].txt_surface = input_registor[n].font.render(input_registor[n].text, True, pg.Color("black"))

                page = "login"
                click =0

        if wrong[1] == 1: #ติดปัญหาเด้งขึ้น
            t1 = Text(800-6,503, 30, "browallianewbold", (255,101,101), 1, 'Please enter all information')
            t1.draw(screen)
        # elif wrong[3] == 1: #ติดปัญหาเด้งขึ้น
        #     # t1 = ''
        #     t1 = Text(800-6,503, 30, "browallianewbold", (255,101,101), 1, 'Username is already used')
        #     t1.draw(screen)


        for box in input_registor: 
            box.draw(screen)
        pg.display.update()
        for event in pg.event.get():
            for box in input_registor:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()

##### CODE PROFILE PAGE ######################################################################################

    elif page == "profile" :
        # print("profile")
        screen.blit(ulp.profile_page,(0,0))

        userFirstName = memprofile[1].replace(" ","")
        userSurName = memprofile[2].replace(" ","")
        userNickName = memprofile[3].replace(" ","")
        userFullName = userFirstName+"  "+userSurName
        t3 = Text(743, 216, 45, "browallianewbold", (0,0,0), 1, userFullName)
        t4 = Text(810, 294, 45, "browallianewbold", (0,0,0), 1, userNickName)
        filepath = user_data_path+'/'+str(memprofile[0])+"."+str(memprofile[4])
        pic_show_data = pic(filepath,400,440)

        screen.blit(pg.transform.scale(pic_show_data[4],(pic_show_data[0],pic_show_data[1])),(85+pic_show_data[2],155+pic_show_data[3])) 
        t3.draw(screen)
        t4.draw(screen)

        
        # percent_bar = pg.rect(797,361,int(355*(progress_percent/100)),48)
        pg.draw.rect(screen,green,(797,361,int(355*(progress_percent/100)),48))
        t_percent = Text(935,370, 45 , "browallianewbold", black, 1, str(progress_percent)) #text username 
        t_percent.draw(screen)
        if lesson_btn.mouse_on():
            screen.blit(ulp.lesson_green_btn,(597,487))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if practice_btn.mouse_on():
            screen.blit(ulp.practice_green_btn,(904,487))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            elif pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'practice'
                click =0
        ####################################################################################################################### 
        if option.mouse_on() :                  #---------setting
            backpage = "profile"                # แสดงรูปภาพ
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                # backpage = "profile"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "profile"
                click =0
        ####################################################################################################################### 


        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

##### CODE SETTING PAGE ######################################################################################

    elif page =="setting" :
        (pos_x, pos_y) = pg.mouse.get_pos() # ถ้าเม้ากดยังจุดใดก็ตามที่ไม่ใช้ในกล่อง setting ให้กลับไปยัง state ก่อนหน้า like : pop-up
        case1 = a1.x <= pos_x <= a1.x + a1.w and a1.y <= pos_y <= a1.y + a1.h
        case2 = a2.x <= pos_x <= a2.x + a2.w and a2.y <= pos_y <= a2.y + a2.h
        case3 = a3.x <= pos_x <= a3.x + a3.w and a3.y <= pos_y <= a3.y + a3.h
        case4 = a4.x <= pos_x <= a4.x + a4.w and a4.y <= pos_y <= a4.y + a4.h
        screen.blit(ulp.all_setting_btn,(1023,12)) 
        if (case1 or case2 or case3 or case4 ) :
            if pg.mouse.get_pressed()[0] == 1  :
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = backpage
                click =0
            # pg.time.delay(5)
        if edit_profile_btn.mouse_on() and backpage !="edit_profile" : # กดเม้าไปยัง edit profile สร้างตัวแปรของหน้า edit profile
            screen.blit(ulp.edit_profile_secl_btn,(1034,122))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                m1  = memprofile[1].replace("'","")
                m2  = memprofile[2].replace("'","")
                m3  = memprofile[3].replace("'","")
                m0  = memprofile[0].replace("'","")
                firstname_register1 = InputBox(695, 170, 472,49,35,14,m1)  # distance input box
                surname_register1 = InputBox(695, 257, 472,49,35,14,m2)  # distance input box
                nickname_register1 = InputBox(695, 351, 472, 49,35,14,m3)  # spinner's speed input box
                username_register1 = InputBox(695, 439, 472,49,35,12,m0)
                edit_member = [surname_register1,firstname_register1,nickname_register1]
                newstatus = 1
                page = "edit_profile"
                click =0
        if logout_profile_btn.mouse_on():
            screen.blit(ulp.logout_profile_secl_btn,(1034,186))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "logout"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

##### CODE LOGOUT PAGE #######################################################################################

    elif page =="logout":
        memprofile=[]
        wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        page = "start"
        logout_status = 1
        txt_member_list = []
        mempicture_list = []
        known_face_encodings = []
        known_face_names = []
        txt_member_list = []
        mempicture_list = []
        k = 0
        capper = True

##### CODE EDIT_PROFILE PAGE #################################################################################

    elif page == "edit_profile":  
        
        # backpage =""
        # screen.blit(edit_profile_ui,(0,0))
        screen.blit(ulp.edit_profile_page,(0,0))
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
            screen.blit(ulp.bgwhite,(128,150))
            screen.blit(pg.transform.scale(Profile_pic,(ww,hh)),(134+jj,155+kk))

        t5 = Text(695, 439+13, 35, "browallianewbold", (0,0,0), 1, m0)
        t5.draw(screen)

        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            # pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                # backpage = "edit_profile"
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                click =0
        
            
        if firstname_register1.text == '  ' or surname_register1.text == '  ' or nickname_register1== '  ':
                r_btn_status = False
        if firstname_register1.text != '  ' and surname_register1.text != '  ' and nickname_register1 != '  ':
            r_btn_status = True

        if save_sub_btn.mouse_on():
            screen.blit(ulp.save_green_btn, (823,522)) #600, 680, 260, 80
            if pg.mouse.get_pressed()[0] == 1:  # button get click
                if r_btn_status == True :
                    click =1
                    user_file_name = memprofile[0]

                    row = [memprofile[0], firstname_register1.text, surname_register1.text, nickname_register1.text,memprofile[4],
                            hold_p[0],hold_p[1],hold_p[2],test_pass[0],test_pass[1],test_pass[2]]

                    user_data_file = open('user_data/'+user_file_name+'.csv','w', encoding='UTF8', newline='') 
                    writer = csv.writer(user_data_file)
                    writer.writerow(row)
                    user_data_file.close()

                    user_data_file = open('user_data/'+user_file_name+'.csv','r', encoding="utf8")
                    reader = csv.reader(user_data_file)
                    for row in reader:
                        memprofile = row[0:5]
                        hold_p = row[5:8]
                        test_pass = row[8:11]
                    user_data_file.close()

                    print('memprofile')
                    print(memprofile)
                    print("hold_p")
                    print(hold_p)
                    print("test pass")
                    print(test_pass)   

            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        
        if back_page_btn.mouse_on():
            # print(" hold ")
            screen.blit(ulp.back_page_green_btn,(16,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page =  back_page_state
                # page = "profile"
                click =0
        # else :
        #     screen.blit(edit_profile_ui,(0,0))

        for box in edit_member:
            box.draw(screen)
            
        if option.mouse_on() :   #---------setting
            backpage = "edit_profile"
            screen.blit(ulp.all_setting_btn,(1023,12))  
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

##### CODE LESSON PAGE #######################################################################################

    elif page == 'lesson':
        screen.blit(ulp.lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "lesson"
                click =0

        if animal_btn.mouse_on():
            # print('animal_btn')
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'animal_lesson'
                click =0


        if classroon_btn.mouse_on():
            # print('classroon_btn')
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'classroon_lesson'
                click =0

        if food_btn.mouse_on():
            # print('food_btn')
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'food_lesson'
                click =0

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'animal_lesson':
        print('animal_lesson')
        screen.blit(ulp.animal_lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "animal_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "animal_lesson"
                click =0

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'classroon_lesson':
        print('classroon_lesson')
        screen.blit(ulp.classroon_lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "classroon_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "classroon_lesson"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'food_lesson':
        print('food_lesson')
        screen.blit(ulp.food_lesson_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "lesson"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "food_lesson"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "food_lesson"
                click =0
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

##### CODE PRACTICE PAGE #####################################################################################

    elif page == 'practice':
        screen.blit(ulp.practice_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "practice"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "practice"
                click =0

        if animal_btn.mouse_on():
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                
                page = 'test_practice'
                word_test = animal_word_pack
                Article[0] = int(hold_p[word_test[0]])
                click =0


        if classroon_btn.mouse_on():
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'test_practice'
                word_test = classroon_word_pack
                Article[0] = int(hold_p[word_test[0]])
                click =0

        if food_btn.mouse_on():
            #?
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = 'test_practice'
                word_test = food_word_pack
                Article[0] = int(hold_p[word_test[0]])
                click =0

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 

    elif page == 'test_practice':
        
        screen.blit(ulp.test_page, (0,0))
        if back_page_btn.mouse_on():
            screen.blit(ulp.back_page_green_btn,(15,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "practice"
                click =0
        if back_home_btn.mouse_on():
            screen.blit(ulp.back_home_green_btn,(94,12))
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "profile"
                click =0
        if option.mouse_on() :   #---------setting
            backpage = "test_practice"
            screen.blit(ulp.all_setting_btn,(1023,12)) 
            pg.display.update()
            if pg.mouse.get_pressed()[0] == 1:
                click = 1
                option_sta =1
            if pg.mouse.get_pressed()[0] == 0 and click ==1:
                page = "setting"
                back_page_state = "test_practice"
                click =0

        if Article[0] > 0:
            if back_test_btn.mouse_on():
                if pg.mouse.get_pressed()[0] == 1:
                    click = 1
                if pg.mouse.get_pressed()[0] == 0 and click ==1:
                    Article[1] = 1
                    Article[0] -= 1
                    
                    click =0
        if Article[0] < 4:
            if next_test_btn.mouse_on():
                if pg.mouse.get_pressed()[0] == 1:
                    click = 1
                if pg.mouse.get_pressed()[0] == 0 and click ==1:
                    
                    Article[1] = 1
                    Article[0] += 1
                    
                    click =0

        screen.blit(ulp.pic_i_test_object[word_test[0]][Article[0]],(528,165))

        # if animal_key_check_button.mouse_on() and pg.mouse.get_pressed()[0] == 1 and type_test_inputbox.text != "  "+word_test[1][Article[0]] :
        if enter_press == 1:
            # if type_test_inputbox.text != "  "+word_test[1][Article[0]]:
            # #     print(type_test_inputbox.text)
            # #     type_test_inputbox.text = "  "
            # #     type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))
            # #     print(word_test[1][Article[0]])
            #     print("wrong answer")

        # if animal_key_check_button.mouse_on() and pg.mouse.get_pressed()[0] == 1 and type_test_inputbox.text == "  "+word_test[1][Article[0]] :
            if type_test_inputbox.text == "  "+word_test[1][Article[0]]:
                print("true answer")
                Article[1] = 1
                pass_test_flag = 1  

            else :
                print("wrong answer")
            enter_press = 0
            type_test_inputbox.text = "  "
            type_test_inputbox.txt_surface = type_test_inputbox.font.render(type_test_inputbox.text, True, pg.Color("black"))

        for box in animal_boxes:
            box.draw(screen)


        #save change
        if Article[1] == 1 :
            Article[1] = 0
            hold_p[word_test[0]] = str(Article[0])
            
            user_file_name = memprofile[0]
            row = [memprofile[0],memprofile[1],memprofile[2],memprofile[3],memprofile[4],
                    hold_p[0],hold_p[1],hold_p[2],test_pass[0],test_pass[1],test_pass[2]]

            user_data_file = open('user_data/'+user_file_name+'.csv','w', encoding='UTF8', newline='') 
            writer = csv.writer(user_data_file)
            writer.writerow(row)
            user_data_file.close()

            user_data_file = open('user_data/'+user_file_name+'.csv','r', encoding="utf8")
            reader = csv.reader(user_data_file)
            for row in reader:
                memprofile = row[0:5]
                hold_p = row[5:8]
                test_pass = row[8:11]
            user_data_file.close()

            print('memprofile')
            print(memprofile)
            print("hold_p")
            print(hold_p)
            print("test pass")
            print(test_pass)   



        t3 = Text(500,300, 80, "browallianewbold", red, 1, word_test[1][Article[0]]) #text username 
        t3.draw(screen)


        #for beta
        # screen.blit(ulp.correct_icon,(800,250))
        # if correct_btn.mouse_on():
        #     # print("mouse on")
        #     if pg.mouse.get_pressed()[0] == 1:
        #         click = 1
        #     if pg.mouse.get_pressed()[0] == 0 and click ==1:
        #         pass_test_flag = 1
        #         click =0

        # for point
        if pass_test_flag == 1 :
            Article[1] = 1
            pass_test_flag = 0
            if Article[0] == 0 and test_pass[word_test[0]].find("A") == -1 : mark_pass = "A"
            elif Article[0] == 1 and test_pass[word_test[0]].find("B") == -1 : mark_pass = "B"
            elif Article[0] == 2 and test_pass[word_test[0]].find("C") == -1 : mark_pass = "C"
            elif Article[0] == 3 and test_pass[word_test[0]].find("D") == -1 : mark_pass = "D"
            elif Article[0] == 4 and test_pass[word_test[0]].find("E") == -1 : mark_pass = "E"
            test_pass[word_test[0]] = test_pass[word_test[0]] + mark_pass
            mark_pass = ''
            if Article[0] < 4 :
                Article[0] += 1

        if Article[0] == 0 and test_pass[word_test[0]].find("A") != -1 :
            t4 = Text(90,250, 80, "browallianewbold", green, 1, "PASS") 
            t4.draw(screen)
        elif Article[0] == 1 and test_pass[word_test[0]].find("B") != -1 :
            t4 = Text(90,250, 80, "browallianewbold", green, 1, "PASS") 
            t4.draw(screen)
        elif Article[0] == 2 and test_pass[word_test[0]].find("C") != -1 :
            t4 = Text(90,250, 80, "browallianewbold", green, 1, "PASS") 
            t4.draw(screen)
        elif Article[0] == 3 and test_pass[word_test[0]].find("D") != -1 :
            t4 = Text(90,250, 80, "browallianewbold", green, 1, "PASS") 
            t4.draw(screen)
        elif Article[0] == 4 and test_pass[word_test[0]].find("E") != -1 :
            t4 = Text(90,250, 80, "browallianewbold", green, 1, "PASS") 
            t4.draw(screen)
        else :
            t4 = Text(90,250, 80, "browallianewbold", green, 1, "")
            t4.draw(screen)

        # pg.display.update()
        # for event in pg.event.get():
        #     if event.type == pg.QUIT:
        #         pg.quit()

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:    
                if event.key == pg.K_RETURN:    
                    enter_press = 1 
            for box in animal_boxes:
                box.handle_event(event)
            if event.type == pg.QUIT:
                pg.quit()         



##### CALCULATE PERCENT PROGRESS #############################################################################
    # if test_pass[0] != '' or test_pass[1] != '' or test_pass[2] != '':
    progress_percent = 0.00
    progress_point = 0
    for n in range(3):
        if test_pass[n].find("A") != -1 :
            progress_point += 1
        if test_pass[n].find("B") != -1 :
            progress_point += 1
        if test_pass[n].find("C") != -1 :
            progress_point += 1
        if test_pass[n].find("D") != -1 :
            progress_point += 1
        if test_pass[n].find("E") != -1 :
            progress_point += 1
    progress_percent = round(((progress_point/15)*100),2)
            
    #if event.type==pygame.KEYDOWN:
    #   if event.key==pygame.K_KP_ENTER: