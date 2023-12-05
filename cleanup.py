import shutil
import os
#if screen shots folder dont already exist, create it
downloads_dir = "C:/Users/david/Downloads"

dictionary_directory = {}
dictionary_directory["screenshot_dir"] = "C:/Users/david/Downloads/Screenshots"
dictionary_directory["economics_dir"] = "C:/Users/david/Downloads/Economics"
dictionary_directory["videos_dir"] = "C:/Users/david/Downloads/Videos"
dictionary_directory["student_pdf_dir"] = "C:/Users/david/Downloads/Student_pdf"
dictionary_directory["computer_aided_design_dir"] = "C:/Users/david/Downloads/computer_aided_design_dir"


class File_Path:
    def __init__(self):
        pass

    def check_existence(self):
        for dir_name, directory in dictionary_directory.items():
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Creating {dir_name} Folder")


# check all the file, if its a screen shot move it to a scren shots folder

#image extensions
image_extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]
#video extensions
video_extensions = [".mkv", ".mp4", ".mpeg", ".avi", ".mov"]
#economics keywords
economics_keywords = ["economics", "finance", "Ch"]
#cad keywords
cad_extensions = [".SLDASM", ".SLDPRT"]
#student keywords
student_keywords = ["week", "student", "schedule", "aamu", "hbcu"]


# list of all the file in Downloads folder
files_on_downloads = os.listdir(downloads_dir)

class Cleanup:
    def __init__(self):
        pass

    def move(self):
        for file in files_on_downloads:
            for img_ext in image_extensions:
                if file.endswith(img_ext) or file.__contains__("screen"):
                    file_dir = downloads_dir + "/" + file
                    shutil.move(file_dir, dictionary_directory["screenshot_dir"])
                    print(f"Moving {file}...")
            for vid_ext in video_extensions:
                if file.endswith(vid_ext):
                    file_dir = downloads_dir + "/" + file
                    shutil.move(file_dir, dictionary_directory["videos_dir"])
                    print(f"Moving {file}...")
            for eco_keyword in economics_keywords:
                if file.endswith(".pdf") and file.__contains__(eco_keyword):
                    file_dir = downloads_dir + "/" + file
                    shutil.move(file_dir, dictionary_directory["economics_dir"])
                    print(f"Moving {file}...")
            for cad_ext in cad_extensions:
                if file.endswith(cad_ext):
                    file_dir = downloads_dir + "/" + file
                    shutil.move(file_dir, dictionary_directory["computer_aided_design_dir"])
                    print(f"Moving {file}...")
            for student_keyword in student_keywords:
                if file.lower().__contains__(student_keyword) and file.endswith(".pdf"):
                    file_dir = downloads_dir + "/" + file
                    shutil.move(file_dir, dictionary_directory["student_pdf_dir"])
                    print(f"Moving {file}...")

filepath = File_Path()
cleanup = Cleanup()
filepath.check_existence()
cleanup.move()
