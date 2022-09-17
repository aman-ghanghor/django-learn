<!--  

   _______views.py_______

   from django.shortcuts import render

   def function_name(request):
         Dynamic Data, if else, any python code logic

         return render(request, template_name, context=dict_name, content_type=MIME_type, status=None, using=None) 



   Example: -

   ______ views.py ______
 
   from django.shortcuts import render

   def learn_django(request):
         coursename = {'cname': 'Django'}

         return render(request, 'course/courseone.html', context=coursename)
         
         return render(request, 'course/courseone.html', coursename)

         return render(request, 'course/courseone.html', {'cname': 'Django'})


-->


