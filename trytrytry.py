import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import sqlite3
from tkinter import filedialog

# Function to save employee data to SQLite database

def update_employee():
    try:
        employee_number = EmployeeNumber.get()
        if not employee_number:
            print("Please enter an employee number to update.")
            return

        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        # Update the employee record
        cursor.execute('''
            UPDATE personal_infotbl SET
            first_name=?, middle_name=?, last_name=?, suffix=?, date_of_birth=?, gender=?,
            nationality=?, civil_status=?, department=?, designation=?, qualified_dep_status=?,
            employee_status=?, pay_date=?, contact_no=?, email=?, social_media=?,
            social_media_account_id=?, address_line1=?, address_line2=?, city_municipality=?,
            state_province=?, country=?, zip_code=?, picture_path=?
            WHERE employee_number=?
            ''', (
            FirstName1.get(), MiddleName.get(), LastName.get(), Suffix.get(),
            DateOfBirth.get(), gender_var.get(), nationality_var.get(), civil_status_var.get(),
            Department.get(), Designation.get(), qualified_dep_var.get(), EmployeeStatus.get(),
            PayDate.get(), Contact.get(), Email.get(), social_media_var.get(),
            SocialMediaAccID.get(), Address1.get(), Address2.get(), CityMunicipality.get(),
            StateProvince.get(), country_var.get(), ZipCode.get(), PicturePath.get(),
            employee_number
        ))

        conn.commit()
        conn.close()

        print("Employee data has been successfully updated.")

    except Exception as e:
        print("Error updating employee data:", e)


def save_employee():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS personal_infotbl (
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            suffix TEXT,
            date_of_birth TEXT,
            gender TEXT,
            nationality TEXT,
            civil_status TEXT,
            department TEXT,
            designation TEXT,
            qualified_dep_status TEXT,
            employee_status TEXT,
            pay_date TEXT,
            employee_number TEXT PRIMARY KEY,
            contact_no TEXT,
            email TEXT,
            social_media TEXT,
            social_media_account_id TEXT,
            address_line1 TEXT,
            address_line2 TEXT,
            city_municipality TEXT,
            state_province TEXT,
            country TEXT,
            zip_code TEXT,
            picture_path TEXT
        )
        ''')

        conn.commit()
        conn.close()

        print("Employee data has been successfully saved.")

    except Exception as e:
        print("Error saving employee data:", e)

# Function to handle file selection
def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        PicturePath.delete(0, END)
        PicturePath.insert(0, file_path)

# Create the GUI
window = tk.Tk()
window.title("HAKU'S EMPLOYEE PERSONAL INFORMATION")
window.configure(bg='dark olive green')

# Create the heading label with modified properties
heading = Label(text="HAKU'S EMPLOYEE PERSONAL INFORMATION", fg='white', bg='dark olive green', font=('Times New Roman', 20, 'bold'))
heading.place(x=150, y=30, width=1190)

# Load and resize the image
image1 = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\haku.png')
resized_image = image1.resize((90, 90))
employee_image = ImageTk.PhotoImage(resized_image)

# Create frame for user account info
user_frame = Frame(window, padx=20, pady=20)
user_frame.grid(row=1, column=0, sticky="ew")

frame = Frame(window, width=1500, height=110, bg='light gray').place(x=15, y=120)
Button(frame, width=15, pady=4, text='Choose file', bg='white', fg='black', cursor='hand2', border=1).place(x=20, y=165)
NF = Label(frame, text='No File Chosen', bg='light gray', font=('black',7))
NF.place(x=40,y=200)

ContactInfo1 = Label(text='Contact Info', fg='white', bg='dark olive green', font=('black',9, 'bold'))
ContactInfo1.place(x=10,y=360)

## Add user image with padding
image_label = Label(window, image=employee_image)
image_label.place(x=25, y=60)

FN = Label(frame, text='First Name', bg='light gray', font=('black',9))
FN.place(x=150,y=130)
FirstName1=Entry(frame, width=50, border=1, fg='black', bg='white')
FirstName1.place(x=150,y=150)

MiddleName1 = Label(frame, text='Middle Name', bg='light gray', font=('black',9))
MiddleName1.place(x=460,y=130)
MiddleName=Entry(frame, width=50, border=1, fg='black', bg='white')
MiddleName.place(x=460,y=150)

LastName1 = Label(frame, text='Last Name', bg='light gray', font=('black',9))
LastName1.place(x=770,y=130)
LastName=Entry(frame, width=50, border=1, fg='black', bg='white')
LastName.place(x=770,y=150)

Suffix1 = Label(frame, text='Suffix', bg='light gray', font=('black',9))
Suffix1.place(x=1080,y=130)
Suffix=Entry(frame, width=30, border=1, fg='black', bg='white')
Suffix.place(x=1080,y=150)

DateOfBirth1 = Label(frame, text='Date of Birth', bg='light gray', font=('black',9))
DateOfBirth1.place(x=150, y=170)

DateOfBirth = DateEntry(frame, width=45, border=1, fg='black', bg='white', date_pattern="yyyy-mm-dd")
DateOfBirth.place(x=150, y=190)


Gender1 = Label(frame, text='Gender', bg='light gray', font=('black',9))
Gender1.place(x=460,y=170)
gender_var = StringVar(window)
gender_var.set("Select One")
gender_choices = ['Select One','Male', 'Female', 'Other']
Gender = OptionMenu(frame, gender_var, *gender_choices)
Gender.config(width=45, height=1, border=1, bg='white')
Gender.place(x=460, y=195)

Nationality1 = Label(frame, text='Nationality', bg='light gray', font=('black',9))
Nationality1.place(x=780,y=170)
nationality_var = StringVar(window)
nationality_var.set("Select One")
nationality_choices = ['Select One','Filipino', 'American', 'Japanese', 'Korean', 'Other']
Nationality = OptionMenu(frame, nationality_var, *nationality_choices)
Nationality.config(width=45, height=1, border=1, bg='white')
Nationality.place(x=780, y=195)

CivilStatus1 = Label(frame, text='Civil Status', bg='light gray', font=('black',9))
CivilStatus1.place(x=1100,y=170)
civil_status_var = StringVar(window)
civil_status_var.set("Select One")
civil_status_choices = ['Select One','Single', 'Married', 'Widowed', 'Divorced', 'Other']
CivilStatus = OptionMenu(frame, civil_status_var, *civil_status_choices)
CivilStatus.config(width=45, height=1, border=1, bg='white')
CivilStatus.place(x=1100, y=195)


frame2 = Frame(window, width=1500, height=110, bg='light gray').place(x=15, y=250)
Department1 = Label(frame, text='Department', bg='light gray', font=('black',9))
Department1.place(x=30,y=260)
Department=Entry(frame, width=70, border=1, fg='black', bg='white')
Department.place(x=30,y=280)

Designation1 = Label(frame, text='Designation', bg='light gray', font=('black',9))
Designation1.place(x=460,y=260)
Designation=Entry(frame, width=70, border=1, fg='black', bg='white')
Designation.place(x=460,y=280)

QualitfiedDepStatus1 = Label(frame, text='Qualified Dep. Status', bg='light gray', font=('black',9))
QualitfiedDepStatus1.place(x=900,y=260)
qualified_dep_var = StringVar(window)
qualified_dep_var.set("Select One")
qualified_dep_choices = ['Select One','Approved', 'Declined', 'Pending Review']
QualifiedDepStatus = OptionMenu(frame, qualified_dep_var, *qualified_dep_choices)
QualifiedDepStatus.config(width=70, height=1, bg='white', border=1)
QualifiedDepStatus.place(x=900, y=280)

EmployeeStatus1 = Label(frame, text='Employee Status', bg='light gray', font=('black',9))
EmployeeStatus1.place(x=30,y=305)
EmployeeStatus=Entry(frame, width=70, border=1, fg='black', bg='white')
EmployeeStatus.place(x=30,y=325)

PayDate1 = Label(frame, text='PayDate', bg='light gray', font=('black',9))
PayDate1.place(x=460, y=305)

PayDate = DateEntry(frame, width=67, border=1, fg='black', bg='white', date_pattern="yyyy-mm-dd")
PayDate.place(x=460, y=325)


EmployeeNumber1 = Label(frame, text='Employee Number', bg='light gray', font=('black',9))
EmployeeNumber1.place(x=900,y=310)
EmployeeNumber=Entry(frame, width=75, border=1, fg='black', bg='white')
EmployeeNumber.place(x=900,y=330)


frame3 = Frame(window, width=1500, height=110, bg='light gray').place(x=15, y=380)
Contact1 = Label(frame, text='Contact No.', bg='light gray', font=('black',9))
Contact1.place(x=30,y=390)
Contact=Entry(frame, width=75, border=1, fg='black', bg='white')
Contact.place(x=30,y=410)

Email1 = Label(frame, text='Email', bg='light gray', font=('black',9))
Email1.place(x=500,y=390)
Email=Entry(frame, width=110, border=1, fg='black', bg='white')
Email.place(x=500,y=410)

Other1 = Label(frame, text='Other (Social Media)', bg='light gray', font=('black',9))
Other1.place(x=30,y=435)
social_media_var = StringVar(window)
social_media_var.set("Select One")
social_media_choices = ['Select One','Instagram', 'Facebook', 'Twitter', 'Other']
Other = OptionMenu(frame, social_media_var, *social_media_choices)
Other.config(width=70, height=1, border=1, bg='white')
Other.place(x=30, y=455)

SocialMediaAccID1 = Label(frame, text='Social Media Account ID/No.', bg='light gray', font=('black',9))
SocialMediaAccID1.place(x=500,y=435)
SocialMediaAccID=Entry(frame, width=110, border=1, fg='black', bg='white')
SocialMediaAccID.place(x=500,y=455)


frame4 = Frame(window, width=1500, height=180, bg='light gray').place(x=15, y=510)
AddressInfo1 = Label(frame, text='Address', fg='white', bg='dark olive green', font=('black',9, "bold"))
AddressInfo1.place(x=10,y=490)
Address11 = Label(frame, text='Address Line 1', bg='light gray', font=('black',9))
Address11.place(x=30,y=520)
Address1=Entry(frame, width=130, border=1, fg='black', bg='white')
Address1.place(x=30,y=540)

Address21 = Label(frame, text='Address Line 2', bg='light gray', font=('black',9))
Address21.place(x=30,y=560)
Address2=Entry(frame, width=130, border=1, fg='black', bg='white')
Address2.place(x=30,y=580)

CityMunicipality1 = Label(frame, text='City/Municipality', bg='light gray', font=('black',9))
CityMunicipality1.place(x=30,y=600)
CityMunicipality=Entry(frame, width=130, border=1, fg='black', bg='white')
CityMunicipality.place(x=30,y=620)

StateProvince1 = Label(frame, text='State/Province', bg='light gray', font=('black',9))
StateProvince1.place(x=820,y=520)
StateProvince=Entry(frame, width=110, border=1, fg='black', bg='white')
StateProvince.place(x=820,y=540)

Country1 = Label(frame, text='Country', bg='light gray', font=('black',9))
Country1.place(x=820,y=600)
country_var = StringVar(window)
country_var.set("Select One")
country_choices = ['Select One','Philippines', 'US', 'Japan', 'Korea', 'Other']
Country = OptionMenu(frame, country_var, *country_choices)
Country.config(width=105, height=1, border=1, bg='white')
Country.place(x=820, y=620)

ZipCode1 = Label(frame, text='Zip Code', bg='light gray', font=('black',9))
ZipCode1.place(x=820,y=560)
ZipCode=Entry(frame, width=110, border=1, fg='black', bg='white')
ZipCode.place(x=820,y=580)

PicturePath1 = Label(frame, text='Picture Path', bg='light gray', font=('black',9))
PicturePath1.place(x=30,y=640)
PicturePath=Entry(frame, width=130, border=1, fg='black', bg='white')
PicturePath.place(x=30,y=660)


# Function to handle canceling the operation
def cancel_operation():
    window.destroy()

# Save and Cancel buttons
SaveButton = Button(window, text="Save", bg='dark green', fg='black', width=13, font=('Times New Roman', 8), command=save_employee)
SaveButton.place(x=15, y=700)

CancelButton = Button(window, text="Cancel", bg='light green', fg='black', width=13, border=1, font=('Times New Roman', 8), command=cancel_operation)
CancelButton.place(x=115, y=700)

# Add the Update and Search buttons to your employee registration interface
UpdateButton = Button(window, text="Update", bg='green', fg='black', width=13, font=('Times New Roman', 8), command=update_employee)
UpdateButton.place(x=215, y=700)

window.geometry('1550x730')
window.mainloop()
