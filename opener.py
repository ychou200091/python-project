import tkinter
from tkinter import filedialog, Text
import os
import codecs

print("**************************")
print(os.path.basename(__file__))
print("**************************")
org_script_name = os.path.basename(__file__)
script_name = org_script_name.split(".")[0]
print(script_name)
"""
purpose:
This program allows user to choose apps as a collection.
User can choose to open all the apps/files at the same time.
The collection is automatically saved.
Next time the app runs, user can run the collection of apps/files.

"""
apps = []

if os.path.isfile(script_name + "_File Collection.txt"):

    with codecs.open(
        script_name + "_File Collection.txt", "r", encoding="utf-8"
    ) as cfile:
        tempApps = cfile.read()
        print(tempApps)
        apps = tempApps.split(",")
        apps = [app for app in apps if app.strip()]
        print(apps)


def getFilename():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(
            ("all files", "*.*"),
            ("executables", "*.exe"),
            ("powerpoint", "*.pptx"),
        ),
    )

    apps.append(filename)
    print(filename)
    # showthings in apps
    for app in apps:
        label = tkinter.Label(frame, text=app)
        label.pack()


def runFiles():
    for app in apps:
        os.startfile(app)


def clearFilename():
    apps.clear()
    for widget in frame.winfo_children():
        widget.destroy()


root = tkinter.Tk()
root.title("MY APP ༼ つ ◕‿◕ ༽つ")

a_title = tkinter.Label(root, text="APP/FILE Collection Opener", bg="white")
a_title.pack()

canvas = tkinter.Canvas(root, width=550, height=450, bg="#263D42")  # dark green
canvas.pack()


frame = tkinter.Frame(canvas, bg="grey")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

# frame.place(height=400, width=400, relx=0.01, rely=0.1)
# directly place at the desire location
# relheight,width,x,y, etc uses percentage to display

for app in apps:  # initialization
    label = tkinter.Label(frame, text=app)
    label.pack()

bottomFrame = tkinter.Frame(root, bg="grey")
bottomFrame.pack()

getFileBTN = tkinter.Button(
    bottomFrame, text="Choose file", width=10, command=getFilename
)
getFileBTN.pack(side="left")

clearBTN = tkinter.Button(bottomFrame, width=10, text="Clear", command=clearFilename)
clearBTN.pack(side="right")
runFileBTN = tkinter.Button(bottomFrame, text="RUN", width=10, command=runFiles)
runFileBTN.pack()

# when we clase the window, a file is saved to rmb to collection
root.mainloop()

with codecs.open(script_name + "_File Collection.txt", "w", encoding="utf-8") as cfile:
    for app in apps:
        cfile.write(app + ",")


"""
def main():
    root.mainloop()

if __name__ == "__main__":
    main()
"""
