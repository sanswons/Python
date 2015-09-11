import webbrowser
import time

print("The program started at:",time.ctime())
i=1
while i<=3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=3-J0nMYAGlA")
    i=i+1

