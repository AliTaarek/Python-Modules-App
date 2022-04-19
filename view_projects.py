import ast


def view_projects():
    project_arr = []
    projects_data = open("projects.txt", "r")
    lines = projects_data.readlines()
    for line in lines:
        project = ast.literal_eval(line)
        project_arr.append(project)

    return project_arr
