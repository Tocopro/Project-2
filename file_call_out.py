
def file_access():
    with open("C:\\Users\\NEAK\\Downloads\\Patient file.txt", "r") as patient_file:
        name, age, gender = user_input()
        patient_information = patient_file.readlines()
        patient_info_output = patient_information[1]
        patient_info_output2 = patient_information[2]
        print(patient_info_output, patient_info_output2)


def user_input():
    name = str(input("Enter search Name: "))
    age = int(input("Enter search Age: "))
    gender = str(input("Enter search Gender: "))
    return name, age, gender


file_access()




from datetime import datetime

# patient name, age, and gender intake information


def intake_id():
    name, age, gender = main()
    print(name, age, gender)
    time_stamp = datetime.today()
    print(time_stamp.strftime("Date: %b %d %Y  Time: %H:%M:%S"))

    with open("C:\\Users\\NEAK\\Downloads\\Patient file.txt", "w", encoding='utf-8') as patient_file:
        patient_file.write(time_stamp.strftime("Date: %b %d %Y   Time: %H:%M:%S \n"))
        patient_file.write("Name: " + name + "\n")
        patient_file.write("Age: " + age + "\n")
        patient_file.write("Gender: " + gender + "\n")
        patient_file.close()


def main():
    name = str(input("Enter the Patients Name: "))
    name_length = len(name)
    if name_length < 30:
        pass
    else:
        print("Invalid Input")
        main()

    age = str(input("Enter the Patients Age: "))
    if age.isdigit():
        pass
    else:
        print("Invalid Input")
        main()
    gender = str(input("Enter the Patients Gender: "))
    if gender == "male" or gender == "female":
        pass
    else:
        print("Invalid Input ")
    return name, age, gender


intake_id()
