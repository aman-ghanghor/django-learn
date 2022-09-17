#  =================  How to Start/Create Application  ===================
#
#   - A Django project contains one or more applications which means we create application
#     inside project.
#
#   Syntax:-   python manage.py startapp appname
#




#   -------- Creating One Application inside Project:-  
#
#      * Go to Project Folder
#
#      * Run Command - python manage.py startapp course
#
#  
#
#   ------- Creating Multiple Applications inside Project:-
#
#      * Go to Project Folder
#
#      * Run Command - python manage.py startapp course
#      * Run Command - python manage.py startapp fees
#      * Run Command - python manage.py startapp result



#  ===========  How to Install Application in Our Project  ============
#
#  - As we know a Django project can contain multiple application so just creating 
#    application inside project is not enough we also have to install application in our project
#
#  - We install application in our project using settings.py file.
#
#  - settings.py file is available at Python Level which means we can install all the application 
#    of project
#
#  - This is compulsory otherwise Applications won't be recognized by Django.
#
# 
#        1. Open settings.py file 
# 
#                         INSTALLED_APPS = [
#                             'django.contrib.admin',
#                             'application_name1',
#                             'application_name2',
#                         ]   
#             
#                         Save settings.py File
#
#                 Example:-
#
#                         INSTALLED_APPS = [
#                             'django.contrib.admin',
#                             'course',
#                             'fees',
#                             'result'
#                          ]
#




#  =============  Geeky Steps  ==============
#
#     * Create Django Project:   django-admim startproject geekyshows
#
#     * Change Directory to Django Project:  cd geekyshows
#
#     * Create Django Application:  python manage.py startapp course
#
#     * Add/Install Application to Django Project (course to geekyshows)
#         
#              i. Open settings.py
#
#             ii. Add course
#                     INSTALLED_APPS = ['django.contrib.admim', 'course', ]
#
#            iii. Save settings.py




#  =============  Application Directory Structure  ==============
#
#     * Go to Project Folder
#
#     * Run Command: python manage.py startapp course
#
#
#       ====== course ======
#
#       migrations = This folder contains __init__.py file which means it's python package.
#                    It also contains all files which are created after running makemigration
#                    command.
#
#       __init__.py = The folder which contains __init__.py file is considered as Python Package.
#
#       admin.py = This file is used to register sql tables so we could perform CRUD operation 
#                  from Admin Application.
#                  Admin Application is provided by Django to perform CRUD operation.
#
#       apps.py = This file is used to config app.
#
#       models.py = This file is used to create our own model class later these classes will be 
#                   converted into database table by Django for our application.
#
#       tests.py = This is file is used to create tests.
#
#       views.py = This file is used to create view. We write all the business logic related code 
#                  in this file.
#

