# ------------------- BIRTHDAY WISHING PROGRAM -------------------
import datetime
import pandas as pd
import random as r
import smtplib # Module used for connecting to server and sending email

# ------------------- DATES ------------------------
t=datetime.datetime.today() # Getting today's date
today=(t.month,t.day) # Extracting the month and day from current date

# ------------------ BIRTHDAY FILE WORK --------------------

birthday_file=pd.read_csv("birthdays.csv") # Reading CSV file

# Converting data frame to dictionary for future iteration using dictionary comprehension
birthdays_dict={
    (int(row.month),int(row.day)) : (row['name'], row['email']) for (index,row) in birthday_file.iterrows()
}
print(birthdays_dict) # Used for debugging purposes

'''
The program is made for handling two birthday entries. User can easily expand it by adding more entries in the CSV.
For the coding portion, simply follow the structure as above to accommodate the new entries in the dictionary
'''

# -------------------- MATCHING DATE & EMAIL CONNECTIONS ---------------------
# Iterating through birthday dictionary with (month, day) format as key
for key in birthdays_dict:
    if key==today: # Comparing today's date to date in dictionary
        random_selection=r.randint(1,3)
        if random_selection==1:
            with open("letter_templates/letter_1.txt","r+") as file:
                file_content=file.readlines()
                first_line_with_placeholder=file_content[0]
                seperated_first_line=first_line_with_placeholder.split(" ")
                old_name = (seperated_first_line[1].strip().rstrip(",")) # Separating only the name
                new_first_line = first_line_with_placeholder.replace(old_name, birthdays_dict[key][0])
                file_content[0]=new_first_line
                file.seek(0) # Positions cursor to the start of the letter file
                file.truncate() # Removes original content from letter file
                file.flush()
                new_file_with_receiver_name=file.writelines(file_content)
                file.seek(0)
                my_email = "t61419743@gmail.com"
                my_app_password = "qafd vdvb ecee ibmz"
                '''
                This gmail account was made solely for testing purposes. Usually a user should  not hardcode their
                passwords due to security purposes.
                '''
                with smtplib.SMTP("smtp.gmail.com") as connection: # Establishing connection between email servers
                    connection.starttls()
                    connection.login(user=my_email, password=my_app_password)
                    connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[key][1],
                                        msg=f"Subject:Happy Birthday\n\n{file.read()}")


        elif random_selection==2:
            with open("letter_templates/letter_2.txt", "r+") as file2:
                file_content2 = file2.readlines()
                first_line_with_placeholder2 = file_content2[0]
                seperated_first_line2 = first_line_with_placeholder2.split(" ")
                old_name2 = (seperated_first_line2[1].strip().rstrip(","))
                new_first_line2 = first_line_with_placeholder2.replace(old_name2, birthdays_dict[key][0])
                file_content2[0] = new_first_line2
                file2.seek(0)
                file2.truncate()
                file2.flush()
                new_file_with_receiver_name2 = file2.writelines(file_content2)
                file2.seek(0)
                my_email = "t61419743@gmail.com"
                my_app_password = "qafd vdvb ecee ibmz"
                with smtplib.SMTP("smtp.gmail.com") as connection: # Establishing connection between email servers
                    connection.starttls()
                    connection.login(user=my_email, password=my_app_password)
                    connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[key][1],
                                        msg=f"Subject:Happy Birthday\n\n{file2.read()}")
        elif random_selection==3:
            with open("letter_templates/letter_3.txt","r+") as file3:
                file_content3=file3.readlines()
                first_line_with_placeholder3=file_content3[0]
                seperated_first_line3=first_line_with_placeholder3.split(" ")
                old_name3 = (seperated_first_line3[1].strip().rstrip(","))
                new_first_line3 = first_line_with_placeholder3.replace(old_name3, birthdays_dict[key][0])
                file_content3[0]=new_first_line3
                file3.seek(0)
                file3.truncate()
                file3.flush()
                new_file_with_receiver_name3=file3.writelines(file_content3)
                file3.seek(0)
                my_email = "t61419743@gmail.com"
                my_app_password = "qafd vdvb ecee ibmz"
                with smtplib.SMTP("smtp.gmail.com") as connection: # Establishing connection between email servers
                    connection.starttls()
                    connection.login(user=my_email, password=my_app_password)
                    connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[key][1],
                                        msg=f"Subject:Happy Birthday\n\n{file3.read()}")


