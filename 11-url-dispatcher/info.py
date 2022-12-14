#  =============== URL Dispatcher ===============
#
#  - To design URLs for app, you create a Python module in informally named urls.py This module
#    is pure Python code and is a mapping between URL path expressions to view functions.
#
#  - This mapping can be as short or as long as needed.
#
#  - It can reference other mappings.
#
#  - It's pure Python code so it can be constructed dynamically.
#
#
#       urls.py
#       _______
#
#           urlpatterns = [
#              path(route, view, kwargs=None, name=None)
#           ]
#
#           ex:  path('learndj/', views.learn_django)
#
#
#
#
#      -------- path() ---------
#
#      path(route, view, kwargs=None, name=None) = It returns an element for inclusion in urlpatterns.
#
#      Where,
#
#        * The route argument should be string or gettext_lazy() that contains a URL pattern. The
#          string may contain angle brackets e.g. <username> to capture part of the URL and send
#          it as a keyword argument to the view. The angle brackets may include a converter 
#          specification like the int part of <int:id> which limits the characters matched and may
#          also change the type of the variable passed to the view. For example, <int:id> matches
#          a string of decimal digits and convert the value to an int.
#
#        * The view argument is a view function or the result of a _view() for class-based views.
#          It can also be an django.urls.include().
#
#        * The kwargs argument allow you to pass additional arguments to the view function or 
#          method. It should be a dictionary.
#
#        * name is used to perform URL reversing.
#
#          ex:)   path('learndj/', views.learn_Django, {'check': 'OK'}, name='learn_django' )        
#