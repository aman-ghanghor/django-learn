#   ============ Model View Template (MVT) ==============
#
#   The MVT is an design pattern that separate an application into three main logical components :
#  
#   1. Model
#   2. View
#   3. Template
#
#   Each of these components has their own role in Project.
#


#  ================ Model =================
#
#  The Model responsible to handle database. It is a data access layer which handles the data.
#
#


#  =============== View ===============
#
#  The user can send request by interacting with template, the view handles these requests and 
#  sends to Model then get appropriate response from the Model, sends response to template.
#
#  It may also have required logics.
# 
#  It works as a mediator between Template and Model.
#


#  =============== Template =============
#
#  It represents how data should be presented to the application user. User can read or write
#  the data from template
#
#  Basically it is responsible for showing end user content, we can say it is user interface.
#
#  It may consists of HTML, CSS, JS mixed with Django Template Language.
#


# ---------------- Model -------------------- View -------------------------- Template -----------
#
#       1. Process Data               |    1. Server Side Logic        |       1. User Interface
#       2. Insert/Update DB           |    2. Process GET/POST         |       2. HTML/CSS
#       3. Communication with View    |    3. Get data from User       |       3. Get Data from View
#                                     |    4. Gets data from Model     |
#                                     |    5. Pass data to Template    |
#                                     |                                |
#                                     |                                |
#



# ==============  Why Use MVT ===============
#
#     * Organized Code
#     * Independent Block
#     * Reduce the complexity of web applications.



#  =============== Django Requirements ==============
#
#    * Python 3.0 or Higher
#           python --version
#
#    * PIP
#           pip --version
#
#    * Text/Code Editor/IDE
#
#    * Web Browser - Google Chrome, Mozilla Firefox, Edge.
#



#  ============== How to install Django ===============
#
#   (1) Separate Virtual Environment
#
#   (2) Globally 










# ============= (1) Install Django in Separate Environment =============
#
#   1. Install Virtual Environment Wrapper
#          
#            pip install virtualenvwrapper-win == This is used to install Virtual environment wrapper
#
#
#   2. Create Virtual Environment(VE)
#
#            mkvirtualenv envname = This is used to create virtual environment. It will automatically 
#                                   activate environment.
#
#
#   3. Active VE 
#
#            workon envname = This is used to activate environment.    
#
#
#   4. Install Django in Created VE 
#
#            pip install django = First activate environment then run the command to install django within
#                                 active environment. You can also specify version [pip install django==2.0]
#
#
#


# ======= What is Django Project ?? =======
#
#  - A Django Project may contain multiple Project Application, which means a group of Application and files
#    is called Django Project.
#
#  - An Application is a part of Django Project.
#
#  - Ex:
#
#              SchoolProject
#              -------------     
#                  * Registration App
#                  * Fees App
#                  * Exam App
#                  * Attendance App
#                  * Result App
#
#
#              Structure
#              ---------
#              
#                  schoolproject
#                     |
#                     |__________ schoolproject
#                     |             |
#                     |             |________ __init__.py
#                     |             | 
#                     |             |________ asgi.py
#                     |             |
#                     |             |________ settings.py
#                     |             |
#                     |             |________ urls.py
#                     |             |
#                     |             |________ wsgi.py
#                     |
#                     |
#                     |__________ manage.py
#


#  =========== Django Project Directory Structure ===========
#
#
#   __init__.py = The folder which contains __init__.py file is considered as python package.
#
#   wsgi.py = WSGI (Web Server Gateway Interface) is a specification that describes how a web 
#             server communicates with web applications, and how web applications can be chained
#             together to process one request. WSGI provided a standard for synchronous Python
#             apps. 
#
#   asgi.py = ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended
#             to provide a standard interface between async-capable Python web servers, frameworks,
#             and applications. ASGI provides standard for both asynchronous and synchronous apps.
#
#   settings.py = This file contains all the information or data about project settings.
#                 E.g:-  Database Config information, Template, Installed Application, Validators etc.
#
#   urls.py = This file contains information of url attached with application.
#
#   manage.py = manage.py is automatically created in each Django project. It is Django's 
#               command-line utility also sets the DJANGO_SETTING_MODULE environment 
#               variable so that it points to your project's setting.py file.
#               Generally, when working on a single Django project, it's easier to use 
#               manage.py than django-admim.
#               







#  ========= Uninstall Django from Separate Environment =========
#
#   1. Active Virtual Environment (VE)
#
#            workon envname = This is used to activate environment.
#
#
#   2. Uninstall Django from VE
#
#            pip uninstall django = This is used to uninstall django.
#
#
#   3. Remove Virtual Environment
#
#            rmvirtualenv envname = This is used to remove virtual environment.
#
#
#   4. Uninstall Virtual Environment Wrapper
#
#            pip uninstall virtualenvwrapper-win = This is used to uninstall Virtual environment wrapper.
#
#








