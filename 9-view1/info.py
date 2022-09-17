#  ==================  View  ==================
#
#     1. Function Based View
#     2. Class Based View
#



#  ================  Function Based View  =================
#
#   - A function based view, is a Python function that takes a Web request and returns a Web response.
#
#   - This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML
#     document, or an image or anything.
#
#   - Each view function takes a HttpRequest object as its first parameter
#  
#   - The view returns an HttpResponse object that contains the generated response.
#     Each view function is responsible for returning an HttpResponse object.
#
#   - We will call these functions as - [view function] or [view function of application] or [view].
#
#
#     Syntax:- 
#     
#         def function_name(request):
#               return HttpResponse('html/variable/text')
#     
#   -+- Where HttpResponse is class which is in [django.http] module so we have to import it before 
#       using HttpResponse. 
#
#   -+- We use views.py file of the application to write functions which may contain business logic of
#       application, later it required to define url name for this function in the urls.py file of the
#       project.
#
#   
#     Example:-
#
#         from django.http import HttpResponse
#         
#         def learn_django(request):
#                return HttpResponse('Hello Django')
#
#         def learn_python(request):
#                return HttpResponse('<h1> Hello Python </h1>')
#
#         def learn_var(request):
#                a = '<h1> Hello Variable </h1>'
#                return HttpResponse(a)
#
#         def learn_math(request):
#                a = 10 + 20
#                return HttpResponse(a)
#




#  ---------- Single Application with Single view function -----------
#
#  
#      views.py
#      ________
#
#      from django.http import HttpResponse
#      def learn_django(request):
#             return HttpResponse('Hello Django')
#
#
#      urls.py
#      ________
#
#      urlpatterns = [ 
#          path('admin/', admin.site.urls), 
#          path('learndj/', views.learn_django),
#      ]
#
#
#
#