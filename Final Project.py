import sqlite3
import tkinter as tk
import tkinter.messagebox as tkmb
from tkinter import Label, Frame, Button, StringVar, Entry, OptionMenu, W, E, N, CENTER, END, BOTH, LEFT, RIGHT, Y
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import customtkinter as ctk
from tkinter import filedialog

from trytrytry import choose_file, save_employee, FirstName1, DateOfBirth, gender_var, nationality_var, \
    civil_status_var, qualified_dep_var, EmployeeStatus, PayDate, Contact, Email, social_media_var, StateProvince, \
    PicturePath, ZipCode, SocialMediaAccID, Address1, Address2, CityMunicipality, country_var, window

# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")
# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x700")
app.title("Final Project")

# Global variable to store username
logged_in_username = None

# Function to handle login logic
def login():
    global logged_in_username
    username = "202314103"
    password = "12345"

    if user_entry.get() == username and user_pass.get() == password:
        logged_in_username = username
        show_home_page()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong Password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong Username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and Password")

# Function to show the login page
def show_login_page():
    for widget in app.winfo_children():
        widget.destroy()

    # Set up the background image
    image = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\background.jpg')
    bck_pic = ImageTk.PhotoImage(image.resize((900, 700)))
    background_label = Label(app, image=bck_pic)
    background_label.image = bck_pic  # Keep a reference to avoid garbage collection
    background_label.place(x=0, y=0)

    # Create frame for login section
    frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    label = ctk.CTkLabel(master=frame, text='Login Page', font=('Helvetica', 20, 'bold'))
    label.pack(pady=20)

    global user_entry
    user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=200)
    user_entry.pack(pady=12, padx=10)

    global user_pass
    user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*", width=200)
    user_pass.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Login', command=login, width=200)
    button.pack(pady=12, padx=10)

    checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
    checkbox.pack(pady=12, padx=10)

    # Sign Up section
    sign_up_text = ctk.CTkLabel(master=frame, text="Not registered?", font=('Helvetica', 10))
    sign_up_text.pack(pady=(20, 5))

    sign_up_button = ctk.CTkButton(master=frame, text='Sign Up', command=sign_up, width=200, fg_color='transparent', text_color='#57a1f8')
    sign_up_button.pack(pady=(0, 10))

# Function to show the home page
def show_home_page():
    for widget in app.winfo_children():
        widget.destroy()

    welcome_label = ctk.CTkLabel(master=app, text=f'Welcome, {logged_in_username}', font=('Helvetica', 24, 'bold'))
    welcome_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    # Payroll button
    payroll_button = ctk.CTkButton(master=app, text='Payroll', command=show_payroll, width=200, height=100)
    payroll_button.place(relx=0.5, rely=0.3, anchor=CENTER)

    # User Account Information button
    user_info_button = ctk.CTkButton(master=app, text='User Account Information', command=show_user_account_info, width=200, height=100)
    user_info_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Log Out button
    logout_button = ctk.CTkButton(master=app, text='Log Out', command=show_login_page, width=200, height=100)
    logout_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# Function to show user account information
def show_user_account_info():
    for widget in app.winfo_children():
        widget.destroy()

    heading = ctk.CTkLabel(master=app, text="User Account Information", font=('Helvetica', 20, 'bold'))
    heading.pack(pady=20)

    user_frame = Frame(app, padx=20, pady=20)
    user_frame.pack()

    global FirstName, MiddleName, LastName, Suffix, Department, Designation, Username, Password, ConfirmPassword, UserType, UserStatus, EmployeeNumber

    # Labels and Entry Widgets for user account info
    Label(user_frame, text="First Name:").grid(row=0, column=0, sticky=W, pady=(5, 0))
    FirstName = Entry(user_frame)
    FirstName.grid(row=0, column=1, pady=5, padx=5)

    Label(user_frame, text="Middle Name:").grid(row=0, column=2, sticky=W, pady=(5, 0))
    MiddleName = Entry(user_frame)
    MiddleName.grid(row=0, column=3, pady=5, padx=5)

    Label(user_frame, text="Last Name:").grid(row=0, column=4, sticky=W, pady=(5, 0))
    LastName = Entry(user_frame)
    LastName.grid(row=0, column=5, pady=5, padx=5)

    Label(user_frame, text="Suffix:").grid(row=1, column=0, sticky=W, pady=(5, 0))
    Suffix = Entry(user_frame)
    Suffix.grid(row=1, column=1, pady=5, padx=5)

    Label(user_frame, text="Department:").grid(row=1, column=2, sticky=W, pady=(5, 0))
    Department = Entry(user_frame)
    Department.grid(row=1, column=3, pady=5, padx=5)

    Label(user_frame, text="Designation:").grid(row=2, column=0, sticky=W, pady=(5, 0))
    Designation = Entry(user_frame)
    Designation.grid(row=2, column=1, pady=5, padx=5)

    Label(user_frame, text="Username:").grid(row=2, column=2, sticky=W, pady=(5, 0))
    Username = Entry(user_frame)
    Username.grid(row=2, column=3, pady=5, padx=5)

    Label(user_frame, text="Password:").grid(row=2, column=4, sticky=W, pady=(5, 0))
    Password = Entry(user_frame, show="*")
    Password.grid(row=2, column=5, pady=5, padx=5)

    Label(user_frame, text="Confirm Password:").grid(row=3, column=0, sticky=W, pady=(5, 0))
    ConfirmPassword = Entry(user_frame, show="*")
    ConfirmPassword.grid(row=3, column=1, pady=5, padx=5)

    Label(user_frame, text="User Type:").grid(row=3, column=2, sticky=W, pady=(5, 0))
    UserType = Entry(user_frame)
    UserType.grid(row=3, column=3, pady=5, padx=5)

    Label(user_frame, text="User Status:").grid(row=3, column=4, sticky=W, pady=(5, 0))
    UserStatus = Entry(user_frame)
    UserStatus.grid(row=3, column=5, pady=5, padx=5)

    Label(user_frame, text="Employee Number:").grid(row=4, column=0, sticky=W, pady=(5, 0))
    EmployeeNumber = Entry(user_frame)
    EmployeeNumber.grid(row=4, column=1, pady=5, padx=5)

    # Buttons for user account actions
    Button(user_frame, text="Insert", bg="light green", command=insert_user).grid(row=5, column=0, pady=20, padx=10)
    Button(user_frame, text="Update", bg="light blue", command=update_user).grid(row=5, column=1, pady=20, padx=10)
    Button(user_frame, text="Delete", bg="light yellow", command=delete_user).grid(row=5, column=2, pady=20, padx=10)
    Button(user_frame, text="Cancel", bg="white", command=cancel_operation).grid(row=5, column=3, pady=20, padx=10)

    # Function to show payroll information (placeholder)
def show_payroll():
    # Collect all widgets and destroy them after the loop
    widgets = app.winfo_children()
    for widget in widgets:
        widget.destroy()

    # Create main frame for payroll section using pack
    main_frame = Frame(app)
    main_frame.pack(fill=BOTH, expand=True)

    # Create payroll frame within the main frame
    payroll_frame = Frame(main_frame, padx=20, pady=20)
    payroll_frame.pack(side=LEFT, fill=BOTH, expand=True)

    # Create search frame within the main frame
    search_frame = Frame(main_frame, padx=20, pady=0)
    search_frame.pack(side=RIGHT, fill=Y, expand=False)

    # Load and resize the image
    image = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\Default.jpg')
    resized_image = image.resize((150, 150))
    employee_image = ImageTk.PhotoImage(resized_image)

    # Keep a reference to the image to prevent it from being garbage collected
    payroll_frame.image = employee_image

    # Labels and Entry Widgets for basic employee info
    Label(payroll_frame, text="Firstname:").grid(row=1, column=2, sticky=E, padx=(150, 10), pady=(30, 5))
    Label(payroll_frame, text="Middle Name:").grid(row=2, column=2, sticky=E, pady=5)
    Label(payroll_frame, text="Surname:").grid(row=3, column=2, sticky=E, pady=5)
    Label(payroll_frame, text="Civil Status:").grid(row=4, column=2, sticky=E, pady=5)
    Label(payroll_frame, text="Qualified Dependents Status:").grid(row=5, column=2, sticky=E, pady=5)
    Label(payroll_frame, text="Paydate:").grid(row=6, column=2, sticky=E, pady=5)
    Label(payroll_frame, text="Employee Status:").grid(row=7, column=2, sticky=E, pady=5)
    Label(payroll_frame, text="Designation:").grid(row=8, column=2, sticky=E, pady=(5, 20))

    # Entry widgets
    Entry(payroll_frame, textvariable=first_name).grid(row=1, column=3, pady=(30, 5))
    Entry(payroll_frame, textvariable=middle_name).grid(row=2, column=3, pady=5)
    Entry(payroll_frame, textvariable=last_name).grid(row=3, column=3, pady=5)
    Entry(payroll_frame, textvariable=civil_status).grid(row=4, column=3, pady=5)
    Entry(payroll_frame, textvariable=qualified_dep_status).grid(row=5, column=3, pady=5)
    Entry(payroll_frame, textvariable=pay_date).grid(row=6, column=3, pady=5)
    Entry(payroll_frame, textvariable=employee_status).grid(row=7, column=3, pady=5)
    Entry(payroll_frame, textvariable=designation).grid(row=8, column=3, pady=(5, 20))

    Label(payroll_frame, text="REGULAR DEDUCTIONS:", font=("Arial", 10, "bold")).grid(row=9, column=2, sticky=E, pady=5)

    # Placeholder entries for Contributions, Loans, and Deductions
    Label(payroll_frame, text="SSS Contribution:").grid(row=10, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=sss_contribution).grid(row=10, column=3, pady=5)
    Label(payroll_frame, text="Philhealth Contribution:").grid(row=11, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=philhealth_contribution).grid(row=11, column=3, pady=5)
    Label(payroll_frame, text="Pagibig Contribution:").grid(row=12, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=pagibig_contribution).grid(row=12, column=3, pady=5)
    Label(payroll_frame, text="Income Tax Contribution:").grid(row=13, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=income_tax_contribution).grid(row=13, column=3, pady=5)

    Label(payroll_frame, text="OTHER DEDUCTIONS:", font=("Arial", 10, "bold")).grid(row=14, column=2, sticky=E, pady=5)

    Label(payroll_frame, text="SSS Loan:").grid(row=15, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=sss_loan).grid(row=15, column=3, pady=5)
    Label(payroll_frame, text="Pag-ibig Loan:").grid(row=16, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=pagibig_loan).grid(row=16, column=3, pady=5)
    Label(payroll_frame, text="Faculty Savings Deposit:").grid(row=17, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=faculty_savings_deposit).grid(row=17, column=3, pady=5)
    Label(payroll_frame, text="Faculty Savings Loan:").grid(row=18, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=faculty_savings_loan).grid(row=18, column=3, pady=5)
    Label(payroll_frame, text="Salary Loan:").grid(row=19, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=salary_loan).grid(row=19, column=3, pady=5)
    Label(payroll_frame, text="Other Loan:").grid(row=20, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=other_loan).grid(row=20, column=3, pady=5)

    Label(payroll_frame, text="DEDUCTION SUMMARY:", font=("Arial", 10, "bold")).grid(row=21, column=2, sticky=E, pady=5)

    Label(payroll_frame, text="Total Deduction:").grid(row=22, column=2, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=total_deduction).grid(row=22, column=3, pady=5)

    # Add employee image with padding
    Label(payroll_frame, image=employee_image).grid(row=1, column=0, rowspan=6, columnspan=2, padx=(0, 10), pady=(30, 0), sticky=N)

    Label(payroll_frame, text="Department:").grid(row=8, column=0, sticky=E, pady=(20, 5))
    Entry(payroll_frame).grid(row=8, column=1, padx=(0, 50), pady=(20, 5))

    # Search Frame Widgets
    Label(payroll_frame, text="Employee Number:").grid(row=7, column=0, sticky=E, pady=(10, 5), padx=(10.5))
    Entry(payroll_frame, textvariable=search_employee_number).grid(row=7, column=1, padx=(0, 50), pady=(20, 5))
    Button(payroll_frame, text="Search", command=search_employee, bg="Red").grid(row=8, column=1, padx=(0, 80), pady=(5,50),
                                                                                 sticky=W)

    # Basic Income Section
    Label(payroll_frame, text="BASIC INCOME:", font=("Arial", 10, "bold")).grid(row=9, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Rate/ Hour:").grid(row=10, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="No of Hours/ Cut off:").grid(row=11, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Income/ Cut off:").grid(row=12, column=0, sticky=E, pady=5)

    Entry(payroll_frame, textvariable=basic_rate_hour).grid(row=10, column=1, padx=(0, 50), pady=5)
    Entry(payroll_frame, textvariable=basic_no_of_hours_cutoff).grid(row=11, column=1, padx=(0, 50), pady=5)
    Entry(payroll_frame, textvariable=basic_income_compute_both).grid(row=12, column=1, padx=(0, 50), pady=5)

    # Honorarium Section
    Label(payroll_frame, text="HONORARIUM INCOME:", font=("Arial", 10, "bold")).grid(row=13, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Rate/ Hour:").grid(row=14, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="No of Hours/ Cut off:").grid(row=15, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Income/ Cut off:").grid(row=16, column=0, sticky=E, pady=5)

    Entry(payroll_frame, textvariable=honorarium_rate_hour).grid(row=14, column=1, padx=(0, 50), pady=5)
    Entry(payroll_frame, textvariable=honorarium_no_of_hours_cutoff).grid(row=15, column=1, padx=(0, 50), pady=5)
    Entry(payroll_frame, textvariable=honorarium_income_compute_both).grid(row=16, column=1, padx=(0, 50), pady=5)

    # Other Income Section
    Label(payroll_frame, text="OTHER INCOME:", font=("Arial", 10, "bold")).grid(row=17, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Rate/ Hour:").grid(row=18, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="No of Hours/ Cut off:").grid(row=19, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Income/ Cut off:").grid(row=20, column=0, sticky=E, pady=5)

    Entry(payroll_frame, textvariable=other_rate_hour).grid(row=18, column=1, padx=(0, 50), pady=5)
    Entry(payroll_frame, textvariable=other_no_of_hours_cutoff).grid(row=19, column=1, padx=(0, 50), pady=5)
    Entry(payroll_frame, textvariable=other_income_compute_both).grid(row=20, column=1, padx=(0, 50), pady=5)

    # Summary Section
    Label(payroll_frame, text="SUMMARY INCOME:", font=("Arial", 10, "bold")).grid(row=21, column=0, sticky=E, pady=5)
    Label(payroll_frame, text="Gross Income:").grid(row=22, column=0, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=gross_income_var).grid(row=22, column=1, pady=5)
    Label(payroll_frame, text="Net Income:").grid(row=23, column=0, sticky=E, pady=5)
    Entry(payroll_frame, textvariable=net_income_var).grid(row=23, column=1, pady=5)

    # Labels and Entry Widgets for payroll info
    Label(payroll_frame, text="Bianca's Choice Payroll", font=("Times New Roman", 30, "bold")).grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

    # Additional Buttons
    Button(payroll_frame, text="GROSS INCOME", command=calculate_gross_income, bg="sky blue").grid(row=23, column=2, padx=(30, 5), pady=5, sticky=W)
    Button(payroll_frame, text="NET INCOME", command=calculate_net_income, bg="sky blue").grid(row=23, column=2, padx=(130, 0), pady=5, sticky=W)
    Button(payroll_frame, text="SAVE", command=save_payroll_data, bg="light green").grid(row=23, column=3, padx=(0, 0), pady=5, sticky=W)
    Button(payroll_frame, text="UPDATE", command=update_payroll_data, bg="light green").grid(row=23, column=3, padx=(40, 0), pady=5, sticky=W)
    Button(payroll_frame, text="DEDUCTIONS", command=calculate_deductions, bg="light yellow").grid(row=23, column=3, padx=(100, 0), pady=5, sticky=W)


def save_payroll_data():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        # Update the employee_details table
        cursor.execute('''UPDATE employee_details SET
                          first_name=?, middle_name=?, last_name=?, civil_status=?, 
                          qualified_dep_status=?, pay_date=?, employee_status=?, designation=?,
                          sss_contribution=?, philhealth_contribution=?, pagibig_contribution=?,
                          income_tax_contribution=?, sss_loan=?, pagibig_loan=?, 
                          faculty_savings_deposit=?, faculty_savings_loan=?, 
                          salary_loan=?, other_loan=?, total_deduction=?, net_income_var=?, gross_income_var=?, basic_rate_hour=?, basic_no_of_hours_cutoff=?, basic_income_compute_both=?,
                          honorarium_rate_hour=?, honorarium_no_of_hours_cutoff=?, honorarium_income_compute_both=?, other_rate_hour=?, other_no_of_hours_cutoff=?, other_income_compute_both=?
                          WHERE employee_number=?''',
                       (first_name.get(), middle_name.get(), last_name.get(), civil_status.get(),
                        qualified_dep_status.get(), pay_date.get(), employee_status.get(), designation.get(),
                        sss_contribution.get(), philhealth_contribution.get(), pagibig_contribution.get(),
                        income_tax_contribution.get(), sss_loan.get(), pagibig_loan.get(),
                        faculty_savings_deposit.get(), faculty_savings_loan.get(),
                        salary_loan.get(), other_loan.get(), total_deduction.get(), net_income_var.get(), gross_income_var.get(),basic_rate_hour.get(), basic_no_of_hours_cutoff.get(), basic_income_compute_both.get(),
                        honorarium_rate_hour.get(), honorarium_no_of_hours_cutoff.get(), honorarium_income_compute_both.get(),  other_rate_hour.get(), other_no_of_hours_cutoff.get(), other_income_compute_both.get(), search_employee_number.get()))

        # Commit changes
        conn.commit()
        conn.close()

        print("Employee data saved successfully.")
    except Exception as e:
        print("Error saving employee data:", e)


def update_payroll_data():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''UPDATE employee_details SET
                          first_name=?, middle_name=?, last_name=?, civil_status=?, 
                          qualified_dep_status=?, pay_date=?, employee_status=?, designation=?,
                          sss_contribution=?, philhealth_contribution=?, pagibig_contribution=?,
                          income_tax_contribution=?, sss_loan=?, pagibig_loan=?, 
                          faculty_savings_deposit=?, faculty_savings_loan=?, 
                          salary_loan=?, other_loan=?, gross_income_var=?, net_income_var=?, total_deduction=? , basic_rate_hour=?, basic_no_of_hours_cutoff=?, basic_income_compute_both=?,
                          honorarium_rate_hour=?, honorarium_no_of_hours_cutoff=?, honorarium_income_compute_both=?, other_rate_hour=?, other_no_of_hours_cutoff=?, other_income_compute_both=?
                          WHERE employee_number=?''',
                       (first_name.get(), middle_name.get(), last_name.get(), civil_status.get(),
                        qualified_dep_status.get(), pay_date.get(), employee_status.get(), designation.get(),
                        sss_contribution.get(), philhealth_contribution.get(), pagibig_contribution.get(),
                        income_tax_contribution.get(), sss_loan.get(), pagibig_loan.get(),
                        faculty_savings_deposit.get(), faculty_savings_loan.get(),
                        salary_loan.get(), other_loan.get(), total_deduction.get(), net_income_var.get(), gross_income_var.get(), basic_rate_hour.get(), basic_no_of_hours_cutoff.get(), basic_income_compute_both.get(),
                        honorarium_rate_hour.get(), honorarium_no_of_hours_cutoff.get(), honorarium_income_compute_both.get(),  other_rate_hour.get(), other_no_of_hours_cutoff.get(), other_income_compute_both.get(), search_employee_number.get()))

        conn.commit()
        conn.close()
        print("Employee data updated successfully.")
    except Exception as e:
        print("Error updating employee data:", e)

# Search functionality
search_employee_number = StringVar()

def search_employee():
    employee_number = search_employee_number.get()
    if not employee_number:
        print("Please enter an employee number.")
        return

    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee_details WHERE employee_number=?', (employee_number,))
        employee = cursor.fetchone()
        conn.close()

        if employee:
            first_name.set(employee[0])
            middle_name.set(employee[1])
            last_name.set(employee[2])
            civil_status.set(employee[7])
            qualified_dep_status.set(employee[10])
            pay_date.set(employee[12])
            employee_status.set(employee[11])
            designation.set(employee[9])
            department.set(employee[8])

            basic_rate_hour.set(employee[25])
            basic_no_of_hours_cutoff.set(employee[26])
            basic_income_compute_both.set(employee[27])
            honorarium_rate_hour.set(employee[28])
            honorarium_no_of_hours_cutoff.set(employee[29])
            honorarium_income_compute_both.set(employee[30])
            other_rate_hour.set(employee[31])
            other_no_of_hours_cutoff.set(employee[32])
            other_income_compute_both.set(employee[33])

            sss_contribution.set(employee[34])
            philhealth_contribution.set(employee[35])
            pagibig_contribution.set(employee[36])
            income_tax_contribution.set(employee[37])
            sss_loan.set(employee[38])
            pagibig_loan.set(employee[39])
            faculty_savings_deposit.set(employee[40])
            faculty_savings_loan.set(employee[41])
            salary_loan.set(employee[42])
            other_loan.set(employee[43])
            total_deduction.set(employee[44])
            gross_income_var.set(employee[45])
            net_income_var.set(employee[46])


        else:
            print("Employee not found.")
    except Exception as e:
        print("Error searching for employee:", e)

# User account functions
def update_user():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE user_account_info
            SET first_name = ?, middle_name = ?, last_name = ?, suffix = ?, department = ?, 
                designation = ?, username = ?, password = ?, confirm_password = ?, user_type = ?, 
                user_status = ?
            WHERE employee_number = ?
        ''', (
            FirstName.get(), MiddleName.get(), LastName.get(), Suffix.get(), Department.get(),
            Designation.get(), Username.get(), Password.get(), ConfirmPassword.get(), UserType.get(),
            UserStatus.get(), EmployeeNumber.get()
        ))

        conn.commit()
        conn.close()
        tkmb.showinfo("Success", "User data has been successfully updated.")
        clear_fields()

    except Exception as e:
        tkmb.showerror("Error", f"Error updating user data: {e}")

def delete_user():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM user_account_info WHERE employee_number = ?
        ''', (EmployeeNumber.get(),))

        conn.commit()
        conn.close()
        tkmb.showinfo("Success", "User data has been successfully deleted.")
        clear_fields()

    except Exception as e:
        tkmb.showerror("Error", f"Error deleting user data: {e}")

def cancel_operation():
    show_home_page()

def clear_fields():
    FirstName.delete(0, END)
    MiddleName.delete(0, END)
    LastName.delete(0, END)
    Suffix.delete(0, END)
    Department.delete(0, END)
    Designation.delete(0, END)
    Username.delete(0, END)
    Password.delete(0, END)
    ConfirmPassword.delete(0, END)
    UserType.delete(0, END)
    UserStatus.delete(0, END)
    EmployeeNumber.delete(0, END)

def insert_user():
    try:
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO user_account_info (
                first_name, middle_name, last_name, suffix, department, designation, 
                username, password, confirm_password, user_type, user_status, employee_number
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            FirstName.get(), MiddleName.get(), LastName.get(), Suffix.get(), Department.get(),
            Designation.get(), Username.get(), Password.get(), ConfirmPassword.get(), UserType.get(),
            UserStatus.get(), EmployeeNumber.get()
        ))

        conn.commit()
        conn.close()
        tkmb.showinfo("Success", "User data has been successfully inserted.")
        clear_fields()

    except Exception as e:
        tkmb.showerror("Error", f"Error inserting user data: {e}")

# Sign Up function
# Function to show the sign-up form

        file_path = filedialog.askopenfilename()
        if file_path:
            PicturePath.delete(0, tk.END)
            PicturePath.insert(0, file_path)

    # Function to show the sign-up form
def sign_up():
    for widget in app.winfo_children():
        widget.destroy()

    heading = ctk.CTkLabel(app, text="EMPLOYEE PERSONAL INFORMATION", fg_color='dark grey',
                           text_color='white', font=('Times New Roman', 20, 'bold'))
    heading.pack(pady=20)

    frame = ctk.CTkFrame(app, width=800, height=1000)
    frame.pack(pady=20)

    image1 = Image.open('C:\\Users\\admin\\PycharmProjects\\pythonProject6\\image\\haku.png')
    resized_image = image1.resize((1000, 1000))
    employee_image = ctk.CTkImage(resized_image)
    image_label = ctk.CTkLabel(frame, image=employee_image)
    image_label.place(x=50, y=20)

    global FirstName1, MiddleName, LastName, Suffix, DateOfBirth, gender_var, nationality_var, civil_status_var
    global Department, Designation, qualified_dep_var, EmployeeStatus, PayDate, EmployeeNumber, Contact
    global Email, social_media_var, SocialMediaAccID, Address1, Address2, CityMunicipality, StateProvince
    global country_var, ZipCode, PicturePath

    ctk.CTkLabel(frame, text='First Name').place(x=160, y=20)
    FirstName1 = ctk.CTkEntry(frame, width=200)
    FirstName1.place(x=160, y=50)

    ctk.CTkLabel(frame, text='Middle Name').place(x=380, y=20)
    MiddleName = ctk.CTkEntry(frame, width=200)
    MiddleName.place(x=380, y=50)

    ctk.CTkLabel(frame, text='Last Name').place(x=600, y=20)
    LastName = ctk.CTkEntry(frame, width=200)
    LastName.place(x=600, y=50)

    ctk.CTkLabel(frame, text='Suffix').place(x=820, y=20)
    Suffix = ctk.CTkEntry(frame, width=80)
    Suffix.place(x=820, y=50)

    ctk.CTkLabel(frame, text='Date of Birth').place(x=160, y=80)
    DateOfBirth = DateEntry(frame, width=20, date_pattern="yyyy-mm-dd")
    DateOfBirth.place(x=160, y=110)

    ctk.CTkLabel(frame, text='Gender').place(x=380, y=80)
    gender_var = tk.StringVar(frame)
    gender_var.set("Select One")
    gender_choices = ['Select One', 'Male', 'Female', 'Other']
    Gender = ctk.CTkOptionMenu(frame, variable=gender_var, values=gender_choices)
    Gender.place(x=380, y=110)

    ctk.CTkLabel(frame, text='Nationality').place(x=600, y=80)
    nationality_var = tk.StringVar(frame)
    nationality_var.set("Select One")
    nationality_choices = ['Select One', 'Filipino', 'American', 'Japanese', 'Korean', 'Other']
    Nationality = ctk.CTkOptionMenu(frame, variable=nationality_var, values=nationality_choices)
    Nationality.place(x=600, y=110)

    ctk.CTkLabel(frame, text='Civil Status').place(x=820, y=80)
    civil_status_var = tk.StringVar(frame)
    civil_status_var.set("Select One")
    civil_status_choices = ['Select One', 'Single', 'Married', 'Widowed', 'Divorced', 'Other']
    CivilStatus = ctk.CTkOptionMenu(frame, variable=civil_status_var, values=civil_status_choices)
    CivilStatus.place(x=820, y=110)

    ctk.CTkLabel(frame, text='Department').place(x=160, y=140)
    Department = ctk.CTkEntry(frame, width=400)
    Department.place(x=160, y=170)

    ctk.CTkLabel(frame, text='Designation').place(x=600, y=140)
    Designation = ctk.CTkEntry(frame, width=400)
    Designation.place(x=600, y=170)

    ctk.CTkLabel(frame, text='Qualified Dep. Status').place(x=160, y=200)
    qualified_dep_var = tk.StringVar(frame)
    qualified_dep_var.set("Select One")
    qualified_dep_choices = ['Select One', 'Approved', 'Declined', 'Pending Review']
    QualifiedDepStatus = ctk.CTkOptionMenu(frame, variable=qualified_dep_var, values=qualified_dep_choices)
    QualifiedDepStatus.place(x=160, y=230)

    ctk.CTkLabel(frame, text='Employee Status').place(x=380, y=200)
    EmployeeStatus = ctk.CTkEntry(frame, width=200)
    EmployeeStatus.place(x=380, y=230)

    ctk.CTkLabel(frame, text='PayDate').place(x=600, y=200)
    PayDate = DateEntry(frame, width=20, date_pattern="yyyy-mm-dd")
    PayDate.place(x=600, y=230)

    ctk.CTkLabel(frame, text='Employee Number').place(x=380, y=320)
    EmployeeNumber = ctk.CTkEntry(frame, width=200)
    EmployeeNumber.place(x=380, y=350)

    ctk.CTkLabel(frame, text='Contact No.').place(x=160, y=260)
    Contact = ctk.CTkEntry(frame, width=400)
    Contact.place(x=160, y=290)

    ctk.CTkLabel(frame, text='Email').place(x=600, y=260)
    Email = ctk.CTkEntry(frame, width=400)
    Email.place(x=600, y=290)

    ctk.CTkLabel(frame, text='Other (Social Media)').place(x=160, y=320)
    social_media_var = tk.StringVar(frame)
    social_media_var.set("Select One")
    social_media_choices = ['Select One', 'Instagram', 'Facebook', 'Twitter', 'Other']
    Other = ctk.CTkOptionMenu(frame, variable=social_media_var, values=social_media_choices)
    Other.place(x=160, y=350)

    ctk.CTkLabel(frame, text='Social Media Account ID/No.').place(x=600, y=320)
    SocialMediaAccID = ctk.CTkEntry(frame, width=400)
    SocialMediaAccID.place(x=600, y=350)

    ctk.CTkLabel(frame, text='Address Line 1').place(x=160, y=380)
    Address1 = ctk.CTkEntry(frame, width=840)
    Address1.place(x=160, y=410)

    ctk.CTkLabel(frame, text='Address Line 2').place(x=160, y=440)
    Address2 = ctk.CTkEntry(frame, width=840)
    Address2.place(x=160, y=470)

    ctk.CTkLabel(frame, text='City/Municipality').place(x=160, y=500)
    CityMunicipality = ctk.CTkEntry(frame, width=400)
    CityMunicipality.place(x=160, y=530)

    ctk.CTkLabel(frame, text='State/Province').place(x=600, y=500)
    StateProvince = ctk.CTkEntry(frame, width=400)
    StateProvince.place(x=600, y=530)

    ctk.CTkLabel(frame, text='Country').place(x=160, y=560)
    country_var = tk.StringVar(frame)
    country_var.set("Select One")
    country_choices = ['Select One', 'Philippines', 'US', 'Japan', 'Korea', 'Other']
    Country = ctk.CTkOptionMenu(frame, variable=country_var, values=country_choices)
    Country.place(x=160, y=590)

    ctk.CTkLabel(frame, text='Zip Code').place(x=600, y=560)
    ZipCode = ctk.CTkEntry(frame, width=400)
    ZipCode.place(x=600, y=590)

    ctk.CTkLabel(frame, text='Picture Path').place(x=160, y=620)
    PicturePath = ctk.CTkEntry(frame, width=840)
    PicturePath.place(x=160, y=650)

    choose_file_button = ctk.CTkButton(frame, text="Choose File", command=choose_file)
    choose_file_button.place(x=160, y=680)

    save_button = ctk.CTkButton(frame, text="Save", command=save_employee_data)
    save_button.place(x=160, y=720)

    cancel_button = ctk.CTkButton(frame, text="Cancel", command=cancel_operation_data)
    cancel_button.place(x=300, y=720)

    update_button = ctk.CTkButton(frame, text="Update", command=update_employee)
    update_button.place(x=430, y=720)

# Employee functions
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


def cancel_operation_data():
    show_home_page()


def save_employee_data():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('EmployeeDatabase2.db')
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute('''
            INSERT INTO employee_details (
                first_name, middle_name, last_name, suffix, date_of_birth, gender,
                nationality, civil_status, department, designation, qualified_dep_status,
                employee_status, pay_date, employee_number, contact_no, email,
                social_media, social_media_account_id, address_line1, address_line2,
                city_municipality, state_province, country, zip_code, picture_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
            FirstName1.get(), MiddleName.get(), LastName.get(), Suffix.get(),
            DateOfBirth.get(), gender_var.get(), nationality_var.get(), civil_status_var.get(),
            Department.get(), Designation.get(), qualified_dep_var.get(), EmployeeStatus.get(),
            PayDate.get(), EmployeeNumber.get(), Contact.get(), Email.get(), social_media_var.get(),
            SocialMediaAccID.get(), Address1.get(), Address2.get(), CityMunicipality.get(),
            StateProvince.get(), country_var.get(), ZipCode.get(), PicturePath.get()
        ))

        conn.commit()
        conn.close()

        print("Employee data has been successfully saved to the database.")

    except Exception as e:
        print("Error saving employee data:", e)


def calculate_gross_income():
    try:
        # Basic Income calculation
        basic_rate_per_hour = float(basic_rate_hour.get())
        basic_no_of_hours = float(basic_no_of_hours_cutoff.get())
        basic_income_compute = float(basic_income_compute_both.get())
        basic_income = basic_rate_per_hour * basic_no_of_hours / basic_income_compute
        basic_income_var.set(basic_income)

        # Honorarium Income calculation
        honorarium_rate_per_hour = float(honorarium_rate_hour.get())
        honorarium_no_of_hours = float(honorarium_no_of_hours_cutoff.get())
        honorarium_income_compute = float(honorarium_income_compute_both.get())
        honorarium_income = honorarium_rate_per_hour * honorarium_no_of_hours / honorarium_income_compute
        honorarium_income_var.set(honorarium_income)

        # Other Income calculation
        other_rate_per_hour = float(other_rate_hour.get())
        other_no_of_hours = float(other_no_of_hours_cutoff.get())
        other_income_compute = float(other_income_compute_both.get())
        other_income = other_rate_per_hour * other_no_of_hours / other_income_compute
        other_income_var.set(other_income)

        # Gross Income calculation
        gross_income = basic_income + honorarium_income + other_income
        gross_income_var.set(gross_income)
    except ValueError:
        print("Please enter valid numbers for rate and hours.")

def calculate_deductions():
    try:
        # Regular Deduction from provided fields
        regular_deduction = (
                float(sss_contribution.get()) +
                float(philhealth_contribution.get()) +
                float(pagibig_contribution.get()) +
                float(income_tax_contribution.get())
        )

        # Other Deduction from provided fields
        other_deduction = (
                float(sss_loan.get()) +
                float(pagibig_loan.get()) +
                float(faculty_savings_deposit.get()) +
                float(faculty_savings_loan.get()) +
                float(salary_loan.get()) +
                float(other_loan.get())
        )

        # Set the calculated values
        regular_deduction_var.set(regular_deduction)
        other_deduction_var.set(other_deduction)

        # Total Deduction calculation
        total_deduction_value = regular_deduction + other_deduction
        total_deduction.set(total_deduction_value)
    except ValueError:
        print("Please enter valid numbers for deductions.")

def calculate_net_income():
    try:
        gross_income = float(gross_income_var.get())
        total_deductions = float(total_deduction.get())
        net_income = gross_income - total_deductions
        net_income_var.set(net_income)
    except ValueError:
        print("Please enter valid numbers for income and deductions.")


# Labels and Entry Widgets for basic employee info
first_name = StringVar()
middle_name = StringVar()
last_name = StringVar()
civil_status = StringVar()
qualified_dep_status = StringVar()
pay_date = StringVar()
employee_status = StringVar()
designation = StringVar()
department = StringVar()
sss_contribution = StringVar()
philhealth_contribution = StringVar()
pagibig_contribution = StringVar()
income_tax_contribution = StringVar()
sss_loan = StringVar()
pagibig_loan = StringVar()
faculty_savings_deposit = StringVar()
faculty_savings_loan = StringVar()
salary_loan = StringVar()
other_loan = StringVar()
total_deduction = StringVar()
basic_rate_hour = StringVar()
basic_no_of_hours_cutoff = StringVar()
honorarium_rate_hour = StringVar()
honorarium_no_of_hours_cutoff = StringVar()
other_rate_hour = StringVar()
basic_income_compute = StringVar()
basic_income_compute_both = StringVar()
honorarium_income_compute = StringVar ()
honorarium_income_compute_both = StringVar()
other_income_compute = StringVar()
other_income_compute_both = StringVar()
other_no_of_hours_cutoff = StringVar()
income_cutoff = StringVar()
gross_income_var= StringVar()
gross_income_compute = StringVar()
net_income_var = StringVar()
basic_income_var = StringVar()
honorarium_income_var = StringVar()
other_income_var = StringVar()
regular_deduction_var = StringVar()
other_deduction_var = StringVar()


# Show the login page initially
show_login_page()

app.mainloop()
