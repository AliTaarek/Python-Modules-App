import ast
import create_project


def edit(email, title):
    projects_data = open("projects.txt", "r+")
    lines = projects_data.readlines()
    for index, line in enumerate(lines):
        project = ast.literal_eval(line)
        if project["owner"] == email and project["title"] == title:
            data = create_project.create_project(email)
            lines[index] = str(data) + '\n'
            projects_data.truncate(0)
            projects_data.seek(0)
            projects_data.writelines(lines)
            print("Your project edited successfully")
            break
        elif project["title"] == title and project["owner"] != email:
            print("This project belong to another user , sorry you can edit in your projects only!")
            break
    else:
        print("There is no project with this title!")
