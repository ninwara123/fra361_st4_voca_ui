project_path = 'C:/fra361_st4_voca_ui'
# project_path = 'D:/stu64'

from tkinter.filedialog import test
import pygame as pg
# from main_code import project_path
#### my path  'C:/fra361_st4_voca_ui/ui_photo
# my_ui_pic_path = 'C:/fra361_st4_voca_ui/ui_photo'

ui_pic_path = project_path+'/ui_photo'
tuto_pic_path = project_path+'/tutorial'
#first
first_page = pg.image.load(ui_pic_path+"/first_page.jpg")
#login
login_page = pg.image.load(ui_pic_path+'/login_page.jpg')
login_green_btn = pg.image.load(ui_pic_path+'/new_login_button.png')
regis_btn_pic = pg.image.load(ui_pic_path+'/create_account_button.png')
facelog_btn = pg.image.load(ui_pic_path+'/facelog_button.png')
register_green_btn =pg.image.load(ui_pic_path+'/new_regis_button.png')

#register
register_page = pg.image.load(ui_pic_path+'/new_register_page.jpg')
back_btn = pg.image.load(ui_pic_path+'/back_button.png')
add_pic_btn = pg.image.load(ui_pic_path+'/add_picture.png')
take_pic_btn = pg.image.load(ui_pic_path+'/take_photo_button.png')
upload_pic_btn = pg.image.load(ui_pic_path+'/upload_photo_button.png')
repic1_btn = pg.image.load(ui_pic_path+'/re1.png')
repic2_btn = pg.image.load(ui_pic_path+'/re2.png')
bgwhite = pg.image.load(ui_pic_path+'/background_pic.png')

defualt_user_pic_path = ui_pic_path+'/defualt_profile.png'

#profile
profile_page = pg.image.load(ui_pic_path+'/home_page.jpg')
lesson_green_btn = pg.image.load(ui_pic_path+'/lesson_button.png')
practice_green_btn = pg.image.load(ui_pic_path+'/lesson_button.png')
p_g_b = pg.image.load(ui_pic_path+'/practice_button.png')
practice_green_btn = pg.image.load(ui_pic_path+'/practice_button.png')
all_setting_btn = pg.image.load(ui_pic_path+'/mix_popup.png')
all_setting_btn2 = pg.image.load(ui_pic_path+'/mix_popup_2.png')

#setting
edit_profile_secl_btn = pg.image.load(ui_pic_path+'/mouseon_edit.png')
logout_profile_secl_btn = pg.image.load(ui_pic_path+'/mouseon_logout.png')

#edit_profile_page
edit_profile_page = pg.image.load(ui_pic_path+'/edit_profile_page.jpg')
save_green_btn =  pg.image.load(ui_pic_path+'/save_button.png')

#back
back_page_green_btn = pg.image.load(ui_pic_path+'/back_button.png')
back_home_green_btn = pg.image.load(ui_pic_path+'/home_button.png')



m_O_piccc =  pg.image.load(ui_pic_path+'/mouse_on_word.png')
#lesson_page

lesson_page =  pg.image.load(ui_pic_path+'/lesson_page.jpg')

#animal_lesson_page
animal_lesson_page = pg.image.load(ui_pic_path+'/lesson_animal.jpg')
a1_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Starfish.png')
a2_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Jellyfish.png')
a3_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Seahorse.png')
a4_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Octopus.png')
a5_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Turtle.png')
#classroon_lesson_page
classroon_lesson_page = pg.image.load(ui_pic_path+'/lesson_classroom.jpg')
p1_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Notice Board.png')
p2_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Scissors.png')
p3_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Calculator.png')
p4_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Magnifying Glass.png')
p5_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Calendar.png')
#food_lesson_page
food_lesson_page = pg.image.load(ui_pic_path+'/food_lesson.jpg')
n1_mouseon = pg.image.load(ui_pic_path+'/mouse_on_spa.png')
n2_mouseon = pg.image.load(ui_pic_path+'/mouse_on_egg.png')
n3_mouseon = pg.image.load(ui_pic_path+'/mouse_on_cookie.png')
n4_mouseon = pg.image.load(ui_pic_path+'/mouse_on_Croissant.png')
n5_mouseon = pg.image.load(ui_pic_path+'/mouse_on_lemon.png')

#practice_page
press_enter = pg.image.load(ui_pic_path+'/press_enter.png')
back_to_lesson_pic =  pg.image.load(ui_pic_path+'/choose_button.png')
back_test_pic = pg.image.load(ui_pic_path+'/backword_green.png')
back_test_pic2 = pg.image.load(ui_pic_path+'/previous_gray.png')
next_test_pic = pg.image.load(ui_pic_path+'/nextword_green.png')
next_test_pic2 = pg.image.load(ui_pic_path+'/next_gray.png')
redu_test_pic = pg.image.load(ui_pic_path+'/reword_green.png')
practice_page =  pg.image.load(ui_pic_path+'/practice_page.jpg')
record_pic = pg.image.load(ui_pic_path+'/recording_pic.png')
corect_Ans = pg.image.load(ui_pic_path+'/spell_correct_pic.png')
incorect_Ans = pg.image.load(ui_pic_path+'/spell_incorrect_pic.png')
pro_incorrect_pic = pg.image.load(ui_pic_path+'/pronounce_incorrect_pic.png')
pro_correct_pic = pg.image.load(ui_pic_path+'/pronounce_correct_pic.png')

food_practice = pg.image.load(ui_pic_path+'/food_practice.jpg')
animal_practice = pg.image.load(ui_pic_path+'/animal_practice.jpg')
classroom_practice = pg.image.load(ui_pic_path+'/classroom_practice.jpg')
reward = pg.image.load(ui_pic_path+'/reward.png')
#practice_page
pass_chioce = pg.image.load(ui_pic_path+'/pass_pic.png')
test_page = pg.image.load(ui_pic_path+'/final_practice_game.jpg')
correct_icon = pg.image.load(ui_pic_path+'/correct.jpg')
success = pg.image.load((ui_pic_path+'/section.jpg'))

# tutorial lesson
tuto_lesson1 =  pg.image.load((tuto_pic_path+'/first_page.jpg'))
tuto_lesson2 =  pg.image.load((tuto_pic_path+'/choose_lesson.jpg'))
tuto_lesson3 =  pg.image.load((tuto_pic_path+'/choose_in_lesson.jpg'))
tuto_lesson4 =  pg.image.load((tuto_pic_path+'/show_pop_up.jpg'))
tuto_lesson5 =  pg.image.load((tuto_pic_path+'/havefunlearning.jpg'))

# tutorial practice
tuto_practice1 =  pg.image.load((tuto_pic_path+'/tp1.jpg'))
tuto_practice2 =  pg.image.load((tuto_pic_path+'/tp2.jpg'))
tuto_practice3 =  pg.image.load((tuto_pic_path+'/tp3.jpg'))
tuto_practice4 =  pg.image.load((tuto_pic_path+'/tp4.jpg'))
tuto_practice5 =  pg.image.load((tuto_pic_path+'/tp5.jpg'))
tuto_practice6 =  pg.image.load((tuto_pic_path+'/tp6.jpg'))
tuto_practice7 =  pg.image.load((tuto_pic_path+'/tp7.jpg'))
tuto_practice8 =  pg.image.load((tuto_pic_path+'/tp8.jpg'))
tuto_practice9 =  pg.image.load((tuto_pic_path+'/tp9.jpg'))
tuto_practice10 =  pg.image.load((tuto_pic_path+'/tp10.jpg'))
tuto_practice11 =  pg.image.load((tuto_pic_path+'/tp11.jpg'))
tuto_practice12 =  pg.image.load((tuto_pic_path+'/havefunplaying.jpg'))
tuto_practice13 =  pg.image.load((tuto_pic_path+'/tutorial_pratice.jpg'))
congrad = pg.image.load((tuto_pic_path+'/ccon.png'))

#########################################################################################



