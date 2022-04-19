import ast


def delete(email, title):
    projects_data = open("projects.txt", "r+")
    lines = projects_data.readlines()
    for index, line in enumerate(lines):
        project = ast.literal_eval(line)
        if project["owner"] == email and project["title"] == title:
            lines.pop(index)
            projects_data.truncate(0)
            projects_data.seek(0)
            projects_data.writelines(lines)
            print("Your project deleted successfully")
            break
        elif project["title"] == title and project["owner"] != email:
            print("This project belong to another user , sorry you can delete your projects only!")
            break
    else:
        print("There is no project with this title!")
