#pip install speechrecognition
#pip sounddevice instead of pyaudio
import speech_recognition
import os, subprocess
from Persian import Convert

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

r = speech_recognition.Recognizer()

mic = speech_recognition.Microphone()

merge = ""

end = "پایان"

while True:
    with mic as mic_open:
        try:
            r.adjust_for_ambient_noise(mic_open, duration=1) #duration=[0.5-1]
            print(Convert("لطفاً صحبت کنید"))
            audio = r.listen(mic_open)
            my_text = r.recognize_google(audio, language="fa-IR")
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            merge = merge + " " + my_text
            if my_text == end:
                print("**********")
                print(Convert(merge))
                print("**********")
                print(Convert("به امید دیدار"))
                input(Convert("برای خروج، یک کلید را فشار دهید"))
                break
            print(Convert(merge))
        #except Exception as er:
            #print(type(er))
        except speech_recognition.exceptions.RequestError:
            print(Convert("لطفاً وضعیت شبکه خود را بررسی کنید"))
            input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید"))
            break
        #except Exception as er:
            #print(type(er))
        except OSError:
            print(Convert("لطفاً وضعیت میکروفون خود را بررسی کنید"))
            input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید"))
            break
        except:
            print(Convert("برنامه با شکست مواجه شد"))
            input(Convert("برای خروج، یکی از کلیدهای کیبورد را فشار دهید"))
            break