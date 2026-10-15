#pip sounddevice instead of pyaudio
import speech_recognition
import os, subprocess
import time
from Persian import Convert

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

r = speech_recognition.Recognizer()

file = speech_recognition.AudioFile(r"D:\Learning\Programing\Sample Project\Speech to Text\Sounds\20241120_093341.wav") #Instead of "r" before Location Address, Use \\ or / in location

try:
    #time_hour = int(input("Duration of Voice File (Hours): "))

    time_min = int(input("Duration of Voice File (Minutes): "))
except ValueError:
    print("*************************************************************")
    print(Convert("لطفاً مقدار دقیقه را به صورت عدد وارد کنید."))
    print("*************************************************************")
    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
    exit()

try:
    time_sec = int(input("Duration of Voice File (Seconds): "))
except ValueError:
    print("**************************************************************")
    print(Convert("لطفاً مقدار ثانیه را به صورت عدد وارد کنید."))
    print("**************************************************************")
    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
    exit()

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
total_time = (time_min*60) + time_sec
#total_time(based on hours) = (time_hour*60) + (time_min*60) + time_sec
print(str(total_time) + "s")

merge = ""

offs = 0

try:
    while offs <= total_time:
        with file as file_open:
            r.adjust_for_ambient_noise(file_open, duration=1) #duration=[0.5-1]
            audio = r.record(file_open, offset= offs , duration=20) #duration = {20, 40, 60}
            #audio = r.record(file_open, offset= offs, duration= int(input("Type your selected Duration for Processing (based on Seconds): ")))
            try:
                print(Convert("در حال تبدیل صدا به متن..."))
                my_text = r.recognize_google(audio, language = "fa-IR")
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                merge = merge + " " + my_text
                print("**********************************************")
                print(Convert(merge))
                print("**********************************************")
                offs = offs + 20
                #offs = offs + duration

                if offs <= total_time:
                    print(str(offs) + "s" + "/" + str(total_time) + "s")
                else:
                    print(Convert("عملیات با موفقیت انجام شد."))

            #except Exception as ex:
                #print(type(ex))
            except speech_recognition.exceptions.UnknownValueError:
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                print(Convert("در حال تلاش مجدد..."))
                time.sleep(1)
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                print("**********************************************")
                print(Convert(merge))
                print("**********************************************")
                offs = offs + 20
                #offs = offs + duration

                if offs <= total_time:
                    print(str(offs) + "s" + "/" + str(total_time) + "s")
                else:
                    print(Convert("عملیات با موفقیت انجام شد."))
                    print("*********************************************************")
                    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))

            except speech_recognition.exceptions.RequestError:
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                print(Convert("متن، ذخیره شده است."))
                print("*********************************************")
                print(Convert(merge))
                print("*********************************************")
                print(Convert("لطفاً وضعیت شبکه را بررسی کنید."))
                print("-------------------------------------------------")
                print(Convert("در حال تلاش مجدد..."))
                print("-------------------------------------------------")
                time.sleep(2)

            except:
                print(Convert("برنامه با خطا مواجه شد."))
                print("=============================================================")
                input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
                break
            
#except Exception as ex:
    #print(type(ex))
except FileNotFoundError:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("-------------------------------------------------------------")
    print(Convert("فایل یافت نشد"))
    print("-------------------------------------------------------------")
    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
    exit()

#except Exception as ex:
    #print(type(ex))
except ValueError:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("----------------------------------------------------------------")
    print(Convert("فرمت فایل صوتی توسط این برنامه، پشتیبانی نمی شود"))
    print("----------------------------------------------------------------")
    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
    exit()

except PermissionError:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("-------------------------------------------------------------")
    print(Convert("لطفاً مسیر فایل را بررسی کنید."))
    print("-------------------------------------------------------------")
    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
    exit()

except:
    print(Convert("برنامه با خطا مواجه شد."))
    print("=============================================================")
    input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید."))
    exit()