import datetime
import ast


def check_date(date):
    date_arr = date.split("-")
    try:
        datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
        return True
    except Exception as e:
        return False


def search():
    date = input("please enter project date as (Year-Month-Day) : ")
    while not check_date(date):
        print("Please enter a valid date as shown !")
        date = input("please enter project date as (Year-Month-Day) : ")
        check_date(date)

    array = []
    projects_data = open("projects.txt", "r")
    lines = projects_data.readlines()
    for line in lines:
        project = ast.literal_eval(line)
        if project['start_date'] == date:
            array.append(project)

    if len(array) > 0:
        return array
    else:
        print("There is no project with this date .")
        search()
