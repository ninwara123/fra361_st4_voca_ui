# project_path = 'C:/fra361_st4_voca_ui'
project_path = 'C:/fra361_st4_voca_ui'

from tkinter.filedialog import test
import pygame as pg
# from main_code import project_path
#### my path  'C:/fra361_st4_voca_ui/ui_photo
# my_ui_pic_path = 'C:/fra361_st4_voca_ui/ui_photo'

ui_pic_path = project_path+'/ui_photo'

#first
first_page = pg.image.load(ui_pic_path+'/first_page.jpg')
#login
login_page = pg.image.load(ui_pic_path+'/login_page.jpg')
login_green_btn = pg.image.load(ui_pic_path+'/new_login_button.png')
register_green_btn = pg.image.load(ui_pic_path+'/new_regis_button.png')


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
# p_g_b = pg.image.load('C:/fra361_st4_voca_ui/ui_photo/practice_button.png')
practice_green_btn = pg.image.load(ui_pic_path+'/practice_button.png')

all_setting_btn = pg.image.load(ui_pic_path+'/all.png')


#setting
edit_profile_secl_btn = pg.image.load(ui_pic_path+'/edit_profile_button.png')
logout_profile_secl_btn = pg.image.load(ui_pic_path+'/log_out_button.png')

#edit_profile_page
edit_profile_page = pg.image.load(ui_pic_path+'/edit_profile_page.jpg')
save_green_btn =  pg.image.load(ui_pic_path+'/save_button.png')

#back
back_page_green_btn = pg.image.load(ui_pic_path+'/back_button.png')
back_home_green_btn = pg.image.load(ui_pic_path+'/home_button.png')



#lesson_page

lesson_page =  pg.image.load(ui_pic_path+'/lesson_page.jpg')

#animal_lesson_page
animal_lesson_page = pg.image.load(ui_pic_path+'/animal_lesson_page.jpg')
#classroon_lesson_page
classroon_lesson_page = pg.image.load(ui_pic_path+'/classroon_lesson_page.jpg')

#food_lesson_page
food_lesson_page = pg.image.load(ui_pic_path+'/food_lesson_page.jpg')
#practice_page
practice_page =  pg.image.load(ui_pic_path+'/practice_page.jpg')

#practice_page
test_page = pg.image.load(ui_pic_path+'/practice_in.jpg')
correct_icon = pg.image.load(ui_pic_path+'/correct.jpg')

animal_test_pic_1 = pg.image.load(ui_pic_path+'/test_pic/animal_test_1.jpg')
animal_test_pic_2 = pg.image.load(ui_pic_path+'/test_pic/animal_test_2.jpg')
animal_test_pic_3 = pg.image.load(ui_pic_path+'/test_pic/animal_test_3.jpg')
# animal_test_pic_4 = pg.image.load(ui_pic_path+'/test_pic/animal_test_4.jpg')
# animal_test_pic_5 = pg.image.load(ui_pic_path+'/test_pic/animal_test_5.jpg')
# classroom_test_pic_1 = pg.image.load(ui_pic_path+'/test_pic/classroom_1.jpg')
# classroom_test_pic_2 = pg.image.load(ui_pic_path+'/test_pic/classroom_2.jpg')
# classroom_test_pic_3 = pg.image.load(ui_pic_path+'/test_pic/classroom_3.jpg')
# # classroom_pic_4 = pg.image.load(ui_pic_path+'/test_pic/classroom_4.jpg')
# # classroom_pic_5 = pg.image.load(ui_pic_path+'/test_pic/classroom_5.jpg')
# food_test_pic_1 = pg.image.load(ui_pic_path+'/test_pic/food_test_1.jpg')
# food_test_pic_2 = pg.image.load(ui_pic_path+'/test_pic/food_test_2.jpg')
# food_test_pic_3 = pg.image.load(ui_pic_path+'/test_pic/food_test_3.jpg')
# food_test_pic_4 = pg.image.load(ui_pic_path+'/test_pic/animal_test_4.jpg')
# food_test_pic_5 = pg.image.load(ui_pic_path+'/test_pic/animal_test_5.jpg')

animal_list_test_pic = [animal_test_pic_1,animal_test_pic_2,animal_test_pic_3,animal_test_pic_1,animal_test_pic_2]
# classroom_list_test_pic = [classroom_test_pic_1,classroom_test_pic_2,classroom_test_pic_3,classroom_test_pic_4,classroom_test_pic_5]
# food_list_test_pic = [food_test_pic_1,food_test_pic_2,food_test_pic_3,food_test_pic_4,food_test_pic_5]
pic_i_test_object = [animal_list_test_pic,animal_list_test_pic,animal_list_test_pic]







#########################################################################################



