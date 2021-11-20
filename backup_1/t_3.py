# animal_word_pack = [0,['Turtle','Starfish','Octopus','Jellyfish','Seahorse']]
# classroon_word_pack  =  [1,['Calculator','Calendar','Magnifying Glass','Notice Board','Scissors']]
# food_word_pack =  [2,['Omelete','Spaghetti','Cookies','Croissant','Lamonade']]
# word_test = [] #no.set , word 
# Article = [0,0]
# word_test = animal_word_pack
# true_answer = ("  "+word_test[1][Article[0]])
# # print(("  "+word_test[1][Article[0]]) )
# print(true_answer)
# print((("  "+word_test[1][Article[0]]) ).lower())
# print(true_answer.lower())

memprofile = ["nin2",  'waraset',  'wongsawat',  'nin123','png','1']            # 'username', 'firstname', 'surname', 'nickname','type_of_pic'
hold_p = ["4",'0','1']                # 'animal_hold_p','classroom_hold_p','food_hold_p'
test_pass =['','','']      # 'animal_pass','classroom_pass','food_pass'
row = []


memprofile_1 = []
hold_p_1 = []
test_pass_1 = []
# from tkinter.filedialog import test
from object import user
# u1 = user(memprofile[0],memprofile[1],memprofile[2],memprofile[3],memprofile[4],memprofile[5],hold_p[0],hold_p[1],hold_p[2],test_pass[0],test_pass[1],test_pass[2])
u1 = user()

u1.WriteData(memprofile,hold_p,test_pass)
print(u1.firstname)
print(u1.fullname)
memprofile_1,hold_p_1,test_pass_1 = u1.ReadData(memprofile[0])
# print(u1.ReadData(memprofile[0]))
# print(memprofile_1,hold_p_1,test_pass_1)
# print(u1.fullname)
# print(row)
# memprofile = row[0:6]
# hold_p = row[6:9]
# test_pass = row[9:12]
print(u1.firstname)
print(u1.fullname)