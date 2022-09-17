# ===========  Why URL Pattern inside Application  =============
<!-- 
   - So far we have learnt to define url pattern at project level for our all application. 
     This approach increases the dependency of application in project which means if we want to use a particular 
     application for our another project we may face issues.

   - Our each application should be independent or less depend on project so we could use our applications in 
     different projects easily without worrying about urls.py available in Project Folder.

-->


# =========== Following are the benefits of defining url pattern inside Application ========
<!-- 
   * Reduces the dependency of Application.

   * Enhance Application performance.

   * Reusability of application become easy.
-->



# ============ include() ===============
<!--
   - A function that takes a full Python import path to another URLconf (urls.py) module that should be 
     "included" in this place".

   - Optionally, the application namespace and instance namespace where the entries will be included into
     can also be specified.

   - include() also accepts as an argument either an iterable that returns URL pattern or a 2-tuple containing 
     such iterable plus the names of the application namespaces.

   - urlpatterns can "include" other URLconf modules.


     Syntax:-    

            include(module, namespace=None)
            include(pattern_list)
            include( (pattern_list, app_namespace), namespace=None )

      Where,
            module = URLconf module (or module name)
            namespace(str) = Instance namespace for the URL entries being included
            pattern_list = Iterable of path() and/or re_path() instances.
            app_namespace(str) = Application namespace for the URL entries being included.



      Example:- 
            
            from django.urls import include, path

            urlpatterns = [
                path('cor/', include('course.urls')),

            ]

            ------ OR

            urlpatterns = [ 
                path('cor/', include([
                    path('learndj/', views.learn_django),
                    path('learnpy/', views.learn_python)
                ]))
            ]

            ------ OR

            otherpatterns = [
                path('learndj/', views.learn_django),
                path('learnpy/', views.learn_python)
            ]
            
            urlpatterns = [
                path('cor/', include(otherpatterns)),
            ]

-->




# =============  Where URL Pattern inside Application  =============
<!--  
    
   1. Create an urls.py file inside each application (in case multiple application).

   2. Write all url patterns related to application, in urls.py file available inside application.

   3. Include Application's urls.py file inside Project's urls.py file.

-->




# ============= Geeky Steps =============
<!--  

    1. Create Django Project: django-admin startproject geekyshows

    2. Change Directory to Django: cd geekyshows

    3. Create Django Application: python manage.py startapp course

    4. Add / Install Application to Django Project using settings.py INSTALLED_APP

    5. Write View Function inside views.py file

    6. Create an urls.py file inside each application (in case multiple application).

    7. Write all url pattern related to application, in urls.py file available inside application.

    8. Include Application's urls.py file inside Project's urls.py file.

-->