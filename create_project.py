import datetime


def check_date(date):
    date_arr = date.split("-")
    try:
        datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
        return True
    except Exception as e:
        return False


def date_compare(start, end):
    start_date = start.split("-")
    end_date = end.split("-")
    return datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2])) < \
        datetime.date(int(end_date[0]), int(end_date[1]), int(end_date[2]))


def create_project(email):
    title = input("Please enter project title : ")
    while not title.isalnum():
        print("sorry title can contain characters or numbers only!")
        title = input("Please enter project title : ")
    details = input("Please enter project details : ")
    total_target = input("please enter your project target : ")
    while not total_target.isdecimal():
        print("Target must be digits only!")
        total_target = input("please enter your project target : ")
    start_time = input("please enter your project start date as (Year-Month-Day) : ")
    while not check_date(start_time):
        print("Please enter a valid date as shown !")
        start_time = input("please enter your project start date as (Year-Month-Day) : ")
        check_date(start_time)
    end_time = input("please enter your project end date as (Year-Month-Day) : ")
    while not check_date(end_time):
        print("Please enter a valid date as shown !")
        end_time = input("please enter your project end date as (Year-Month-Day) : ")
        check_date(end_time)
    while not date_compare(start_time, end_time):
        print("End date must be after start date !")
        end_time = input("please enter your project end date as (Year-Month-Day) : ")
        check_date(end_time)
        date_compare(start_time, end_time)

    project_data = {
        'owner': email,
        'title': title,
        'details': details,
        'total_target': total_target,
        'start_date': start_time,
        'end_date': end_time
    }
    return project_data
