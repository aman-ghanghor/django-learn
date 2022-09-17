# ============== Template ===============
<!--  
   
   - A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.).

   - A template contains variables, which get replaced with values when the template is evaluated, 
     and tags, which control the logic of the template.

   - Template is used by view function to represent the data to user.

   - User sends request to view then view contact template afterthat view get information from the
     template and then view gives response to the users.

-->




# ============= Create Template Folder and Files ===============
<!-- 
   
   - We create [template] folder inside Project Folder. templates folder will contain all HTML files.

   * FOLDER STRUCTURE :- 


     geekyshows
        |
        |
        |________ templates
        |             |
        |             |__________ courseone.html            ----
        |             |                                         | 
        |             |__________ coursetwo.html                |
        |             |                                         |------- Template Files
        |             |__________ feesone.html                  |
        |             |                                         |
        |             |__________ feestwo.html              ----
        |

        |________ course
        |
        |________ fees
        |
        |________ exam
        |               
        |          
        |________ geekyshows
        |             |
        |             |__________ __init__.py
        |             |
        |             |__________ settings.py
        |             | 
        |             |__________ urls.py
        |             |
        |             |__________ wsgi.py
        |             |
        |             |__________ asgi.py
        |

        |________ manage.py




   _-_-_-_-_-_-_ settings.py _-_-_-_-_-_-_


        TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

        INSTALLED_APP = [
            'course',
            'fees',
            'exam'                       ________________________________
        ]                     _________ | Directories where the engine   |
                             |          | should look for template       |  
        TEMPLATES = [        |          | source files, in search order. | 
            {                |          |________________________________|   
              'DIRS': [TEMPLATE_DIR],
            }
        ]



-->




# =============  Write Templates Files  =============
<!--  
   
   - When we create Template file for application we separate business logic and 
     presentation from the application views.py file.

   - Now we will write business logic in views.py file and presentation code in 
     template file.

-->




# ========= Rendering Templates Files =========
<!-- 

   - By creating Template file for application we separate business logic and presentation
     from the application views.py file. Now we will write business logic in views.py file 
     and presentation code in HTML file,

     Still views.py will be responsible to process the template files for this we will use
     render() function in views.py file.

   
    _______ views.py _______

    from django.shortcuts import render

    def function_name(request):
         Dynamic Data, if else, any python code logic

         return render(request, template_name, context=dict_name, content_type=MIME_type, 
                       status=None, using=None)

    
    Example:-

       def learn_django(request):
             return render(request, 'course.html')
           
-->




# ===========  render()  ===========
<!-- 

   render() Function = It combines a given template with a given context dictionary and 
   returns an HttpResponse object with that rendered text.

   Syntax:-

   render(request, template_name, context=dict_name, content_type=MIME_type, status=None, using=None)

   WHERE,

      * request = Required, The request object used to generate response
      
      * template_name = Required, The full name of a template to use or sequence of template 
                        names. If a sequence is given, the first template that exists will
                        be used.

      * context = A dictionary of values to add to the template context. By default, this
                  is an empty dictionary. If a value in the dictionary is callable,
                  the view will call it just before rendering the template.
      
      * content_type = The MIME type to use for the resulting document. Defaults to 'text/html'

      * status = The status code for the response. Default to 200.

      * using = The NAME of a template engine to use for loading the template.


-->
















