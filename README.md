# Automatic_Desktop/Downloads_Cleaner
python script to help Organize Desktop space for improved efficiency

# Downloads Cleanup

Downloads Cleanup is a Python script designed to organize files in your Downloads folder into specific directories based on file types and keywords. This script is particularly useful for keeping your downloads folder tidy and well-organized.

## Prerequisites

- Python 3.x installed on your machine.

## How to Use

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/your-username/downloads-cleanup.git
    ```

2. Navigate to the project directory.

    ```bash
    cd downloads-cleanup
    ```

3. Run the script.

    ```bash
    python cleanup.py
    ```

   This will organize the files in your Downloads folder into subdirectories such as "Screenshots," "Economics," "Videos," "Student_pdf," and "Computer_Aided_Design."

## Customization

You can customize the script according to your preferences. Here's what you can modify:

- **Directories:**
    - Open the script (`cleanup.py`) and update the `dictionary_directory` dictionary with your desired directory names and paths.

- **File Categories:**
    - Customize the file categories and associated keywords/extensions by modifying the lists in the script.
        - `image_extensions` for image files.
        - `video_extensions` for video files.
        - `economics_keywords` for economics-related files.
        - `cad_extensions` for computer-aided design files.
        - `student_keywords` for student-related files.
## Note

- If the specified directories do not exist, the script will create them for you.

- **Antivirus Considerations:**
    - Some antivirus programs, such as AVG, may trigger alerts when downloading and running scripts. This is a common behavior for scripts that manipulate files.
    - To avoid triggering antivirus alerts, consider adding an exception for the project directory or temporarily disabling your antivirus while running the script.
    - Always ensure that you are downloading scripts from reliable sources.

- Make sure to run the script from the same directory where it is located.

Feel free to fork this project, make changes, and adapt it to suit your specific needs. Contributions are welcome!

Happy cleaning!
