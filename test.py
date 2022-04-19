import ast

project_arr = []
projects_data = open("projects.txt", "r+")
lines = projects_data.readlines()
for index, line in enumerate(lines):
        project = ast.literal_eval(line)
        project["title"] = "hamada"
        project_arr.append(str(project)+"\n")

projects_data.seek(0)
projects_data.writelines(project_arr)

