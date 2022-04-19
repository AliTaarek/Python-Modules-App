import view_projects
import create_project
import edit_project
import delete_project
import search_projects


def projects_menu():
    print("""
    1-Create new project
    2-View all projects
    3-Edit your projects
    4-Delete your projects
    5-Search projects by date
    """)


def projects_actions(email):
    projects_menu()
    selection = int(input("Choose an action : "))
    if selection == 1:
        project_data = create_project.create_project(email)
        projects_file = open("projects.txt", "a")
        projects_file.write(str(project_data) + '\n')
        projects_file.close()
        print("Thank you , your project added successfully :)")
        projects_actions(email)

    elif selection == 2:
        projects = view_projects.view_projects()
        for index, value in enumerate(projects):
            print(index+1, "-", value)
        projects_actions(email)

    elif selection == 3:
        title = input("please enter title of project to edit : ")
        edit_project.edit(email, title)
        projects_actions(email)

    elif selection == 4:
        title = input("please enter title of project to edit : ")
        delete_project.delete(email, title)
        projects_actions(email)

    elif selection == 5:
        data = search_projects.search()
        for index, project in enumerate(data):
            print(index+1, "-", project)
        projects_actions(email)

    else:
        print("please enter valid option!")
        projects_actions(email)
