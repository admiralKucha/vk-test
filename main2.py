import tkinter as tk
import re, os

root = tk.Tk()
w_h = [root.winfo_screenwidth(), root.winfo_screenheight()]

with open(r'D:\SteamLibrary\steamapps\common\Underlords\game\dac\cfg\video.txt', "r") as f:
    string = re.sub(r"setting\.defaultres\"\s{2}\"\d+\"", f"setting.defaultres\"		\"{w_h[0]}\"", f.read())
    string = re.sub(r"setting\.defaultresheight\"\s{2}\"\d+\"", f"setting.defaultresheight\"		\"{w_h[1]}\"", string)

with open(r'D:\SteamLibrary\steamapps\common\Underlords\game\dac\cfg\video.txt', "w") as f:
    f.write(string)

os.system(r'D:\SteamLibrary\steamapps\common\Underlords\game\bin\win64\underlords.exe')

