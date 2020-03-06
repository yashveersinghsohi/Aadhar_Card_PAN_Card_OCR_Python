#importing required packages.
import cv2
import pytesseract
import re
import mysql.connector as mc

# Initializing all variables in which aadhar card details are to be stored.
user_aadhar_no = str()
user_gender = str()
user_dob = str()
user_name = str()



# Change this to your image name. Make sure the image is stored in the same working directory as this python file.
image_name = 'Aadhar_Card_Sample_1.jpg'

# Reading the image, extracting text from it, and storing the text into a list.
img = cv2.imread(image_name)
text = pytesseract.image_to_string(img)
all_text_list = re.split(r'[\n]', text)

# Process the text list to remove all whitespace elements in the list.
text_list = list()
for i in all_text_list:
    if re.match(r'^(\s)+$', i) or i=='':
        continue
    else:
        text_list.append(i)



# Extracting all the necessary details from the pruned text list.
# 1) Aadhar Card No.
aadhar_no_pat = r'^[0-9]{4}\s[0-9]{4}\s[0-9]{4}$'
for i in text_list:
    if re.match(aadhar_no_pat, i):
        user_aadhar_no = i
    else:
        continue


# 2) Gender
aadhar_male_pat = r'(Male|MALE|male)$'
aadhar_female_pat = r'[(Female)(FEMALE)(female)]$'
for i in text_list:
    if re.search('(Male|male|MALE)$', i):
        user_gender = 'MALE'
    elif re.search('(Female|FEMALE|female)$', i):
        user_gender = 'FEMALE'
    else:
        continue

# 3) DOB
aadhar_dob_pat = r'(Year|Birth|irth|YoB|YOB:|DOB:|DOB)'
date_ele = str()
for idx, i in enumerate(text_list):
    if re.search(aadhar_dob_pat, i):
        index = re.search(aadhar_dob_pat, i).span()[1]
        date_ele = i
        dob_idx = idx
    else:
        continue

date_str=''
for i in date_ele[index:]:
    if re.match(r'\d', i):
        date_str = date_str+i
    elif re.match(r'/', i):
        date_str = date_str+i
    else:
        continue
user_dob = date_str

# 4) Name
user_name = text_list[dob_idx-1]



# Commit details to a mysql database
# Change the 'database' attribute in the line below to match your database and make sure that the server is running before executing this code.
mydb = mc.connect(host='localhost', user='root', passwd='root', database='fyp_aadhar')
mycursor = mydb.cursor()

# Make sure that the table, attribute names match the ones in your database.
insert_query = "Insert into card_details(card_no, gender, dob, name) values(%s, %s, %s, %s)"
card_details = (user_aadhar_no, user_gender, user_dob, user_name)

mycursor.execute(insert_query, card_details)

mydb.commit()
