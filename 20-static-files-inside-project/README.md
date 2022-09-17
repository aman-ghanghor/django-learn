=============  Static Files  ==============
<!-- 

   CSS files, JavaScript Files, image files, video files etc are considered as static files in
   Django.

   Django provides django.contrib.staticfiles to help you manage them.

   django.contrib.staticfiles collects static files from each of your applications (and any other 
   places you specify) into a single location that can easily be served in production. 

   
   - We create [static] folder inside Root Project Folder then inside [static] folder we create 
     required folders. which will contain all static files respectively like css folder will contain 
     all css files, image folder will contain all images and so on.


     schoolproject
           
           static
                
                css 
                    style.css
                    custom.css

                image
                    love.jpg
                    pic.jpg
    
            templates

            schoolproject

            manage.py

            course

            fees
 
-->


 
**|--------------   Add Static in settings.py -------------- |**

Settings.py:)

     TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

     STATIC_DIR = os.path.join(BASE_DIR, 'static')




**|--------------  Use Static Files in Template Files -------------- |**

    1. First Load Static Files

    2. Reference Static Files

[template/course]
     
course.html
<!-- 
   <!DOCTYPE html>
   {% load static %}        // Loading Static files
   <html>
      <link href='{% static "css/style.css" %}' >
      
      <body>
          ...
      </body>

   </html>

 -->





**|--------------  Load Template Tag  -------------- |**
<!--  

    1.  {% load module_name %} = It loads a custom template tag set.

            Example:-         {% load emotags %}
            
            Example:-         {% load geek.mytags %}

            Example:-         {% load emotags geeky.mytags %}  

                              Template would load all the tags and filters registered in emotags and mytags located 
                              in package geek.



    ***  You can also selectively load individual filters or tags from a library or module,
         using the from argument. 

         Ex:-     {% load cry lol from emotags %}

         The template tags/filters named cry and lol will be loaded from emotags.



-->




**|--------------  Static Template Tag  -------------- |**
<!-- 

   {% static filename %} = This tag is used to link to static files that are saved in STATIC_ROOT.
                           If the django.contrib.staticfiles app is installed, the tag will serve 
                           files using url() method of the storage specified by STATICFILES_STORAGE.
    
    Syntax:- 

        {% load static %}

        {% static filename %}

        {% static path/filename %}     

        {% static path/filename as variable %} 


    Example:- 

        <link rel="stylesheet" href="{% static 'style.css' %}"> 

        <link rel="stylesheet" href="{% static 'css/style.css' %}"> 
 
        <img src="{% static 'love.jpg' %}"> 

        <img src="{% static 'images/love.jpg' %}"> 

        {% static "images/love.jpg" as mylove %}
        <img src="{{ mylove }}" >


-->




**|--------------  get_static_prefix  Template Tag  -------------- |**
<!-- 

   {% get_static_prefix %} =  We should prefer the static template tag, but if you need more
                              control over exactly where and how STATIC_URL is injected into the 
                              template, you can use the get_static_prefix template tag.
 
    Example:- 

         {% load static %}

         <img src="{% get_static_prefix %}images/love.jpg" >


    
         *** There's also a second form you can use to avoid extra processing if you need the 
             value multiple times.

            {% load static %}
            {% get_static_prefix as STATIC_PREFIX %}
            <img src="{{ STATIC_PREFIX }}images/love.jpg">
            <img src="{{ STATIC_PREFIX }}images/pic1.jpg">



      NOTE - 
       
        STATIC_URL (in settings.py) = This is the URL to use when referring to static file located 
                                      in STATIC_ROOT.
                                      It must end in a slash if set to a non-empty value.

                                        Example:-     "/static/"
                                        Example:-     "http://static.example.com/"
       
       
       
        STATIC_ROOT = This is absolute path to the directory where [collectstatic] will collect static
                      files for deployment. It is by default None.
                      
                Ex:  "/var/www/example.com/static/"     -> on live server
                Ex:  os.path.join(BASE_URL, 'static/')  -> on local server
        
        
          
        STATICFILES_DIRS = This setting defines the additional locations the [staticfiles] app will 
                           traverse if the [FilesSystemFinder] finder is enabled, e.g. If you use the
                           [collectstatic] or [findstatic] management command or use the static file 
                           serving view. It is by default an empty list.

                           ex- 

                           STATICFILES_DIRS = [
                               "/home/special.geek.com/geek/static",
                               "/home/geek.com/geek/static",
                               "/opt/webfiles/common",
                           ]
                           
        
        
        STATICFILES_STORAGE = The file storage engine to use when collecting static files with the 
                              collectstatic management command.


-->












