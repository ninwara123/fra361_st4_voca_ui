import pygame as pg
from object import Text, Button,InputBox,pic
pg.init()


# def run_setting():
print("hellooooooooooooooooooooooooo")
def resize(Profile_pic):
    pg.transform.scale(Profile_pic,(50,50))

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

startpg = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/first_page.jpg')
pg3 = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/lesson_page.jpg')
fade = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/new_login_page.jpg')
login = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/new_login_button.png')
regis = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/new_regis_button.png')
ui3 = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/new_register_page.jpg')
pgpf = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/home_page.jpg')
pgpf2 = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/home_page.png')
setting = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/popup_setting.png')
setting_btn = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/setting_button.png')
bgwhite = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/background_pic.png')
add_p = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/add_picture.png')
take_p = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/take_photo_button.png')
upload_p = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/upload_photo_button.png')
defualt_p_path = 'iC:/fra361_st4_voca_ui/UIPHOTO/photo/defualt_profile.png'
all_p = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/all.png')
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
lession_pic = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/lesson_page.jpg')

############################################ lesson


############################################ practice
practice_pic = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/practice_page.jpg')

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
lession_box_pic = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/lesson_button.png')
practice_box_pic = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/practice_button.png')
############################################ pgpf

############################################ setting
edit_profile = Button(1036,120,1256-1036,176-120)
logout_profile = Button(1036,187,1256-1036,241-187)
edit_profile_pic = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/edit_profile_button.png')
logout_profile_pic = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/log_out_button.png')
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
backpiconmouse = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/back_button.png')
repic1 = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/re1.png')
repic2 = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/re2.png')

############################################ edit
edit_profile_ui2 = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/edit_profile_page.jpg')
edit_profile_ui = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/edit_profile_page.png')
save_btn =  pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/save_button.png')
############################################ edit

########################################### back
backpiconmouse = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/back_button.png')
backtohome = Button(93,12,59,59)
homepiconmouse = pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/home_button.png')

################################### practice animal
btn_animal_pact = Button(123,50,374,310)
animal_practice_1= pg.image.load('iC:/fra361_st4_voca_ui/UIPHOTO/photo/animal_pract_1.jpg')










wrong =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]