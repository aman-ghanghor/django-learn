============  Django Template Language  =============
<!-- 
   * Django's template language is designed to strike a balance between power and ease. It's
     designed to feel comfortable to those used to working with HTML.


   * Jinja 2 = Jinja is a modern and designer-friendly templating language for Python, modelled
               after Django's templates. It is fast, widely used and secure with the optional
               sandboxed template execution environment.

         - python pip install jinja2

         - in settings.py:   'BACKEND': 'django.template.backends.jijna2.jinja2',

-->






**) =========  Variables  ========= (**
<!--
    Variables look like this: {{ variable }} When the template engine encounters a variable, it
    evaluates that variable and replace it with the result.

    Rules:-

      - Variable names consist of any combination of alphanumeric characters and the underscore.

      - Variable name should not start with underscore.

      - Variable name can not have spaces or punctuation characters.

      Syntax:-    {{ variable }}

      Example:-    {{ nm }},  {{name}},  {{first_name}}


-->






**) =========  Filters  ========= (**
<!-- 

    - When we need to modify variable before displaying we can use filters. Pip  '|' is used to apply
      filter.

            Syntax:-      {{ variable | filter }}

            Example:-     {{ name | upper }}

            Example:-      {{ article | truncateword:40 }}



    - Filter can be chained.

            Syntax:-      {{ variable | filter | filter }}

            Example:-     {{ article | upper | truncateword:40 }}




    1. capfirst = It capitalizes the first character of the value. If the first character is not a letter, 
                  this filter has no effect.

                  Example:-   {{ value | capfirst }}


    2. default = If value evaluates to False, uses the given default. Otherwise, uses the value.
     
                 Ex:-   {{ value|default:"nothing"}}


    3. length = It returns the length of the value. This works for both strings and lists. The filter
                return 0 for an undefined variable.
               
                Ex:   {{ value | length }}


    4. lower = It converts a string into all lowercase.

               Ex:-    {{ value | length }}


    5. upper = It converts a string into all upper.

               Ex:  {{value|upper}}


    6. truncatewords = truncate string to word provided

                      Ex:   {{value|truncatewords:40}}

    7. truncatechars = truncate string to specific characters

                       Ex:   {{value|truncatechars:30}}


    8. slice = It returns a slice of the list. Uses the same syntax as Python's list slicing.

               Ex:   {{ some_list | slice: "1:3" }}


    9. date = It formats a date according to the given format.

              Ex:    {{ value | date:"D m M Y" }}

              Ex:    {{ value | date:"SHORT_DATE_FORMAT" }}


    10. time = It formats a time according to the given format.

               Ex:  {{ value | time:"H:i" }}

               Ex:  {{ value | time: "TIME_FORMAT" }}


    11. floatformat = When used without an argument, rounds a floating-point number to one decimal
                      place but only if there's a decimal part to be displayed.
                      
                      - If used with a numeric integer argument, floatformat rounds a number to that 
                        many decimal places.

                      - Particularly useful is passing 0 (zero) as the argument  which will round the
                        float to the nearest   integer.

                      - If the argument passed to floatformat is negative, it will round a number to 
                        that many decimal places but only if there's decimal part to be desplayed.


-->





**) =========  if Tag  ========= (**
<!-- 

    {% if %} tag = The {% if %} tag evaluate a variable, and if that variable is "true"
                   (i.e. exists, is not empty, and is not a false boolean value.)
                   
    Syntax:- 

        {% if variable %}
               .............
        {% endif %}


    Example:- 

        {% if nm %}
            <h1>Hello {{nm}} </h1>
        {% endif %}


        {% if nm and st %}
            <h1> Hello {{nm}} </h1>
        {% endif %}


        {% if nm or st %}
            <h1> Seat Available </h1>
        {% endif %}


        {% if not st %}
            <h1> Seat Not Available </h1>
        {% endif %}



    ------------  if Tag with condition  ------------

     Syntax:-

         {% if condition %}
              .................
         {% endif %}


     Example:- 

         {% if nm == 'Django' %}
             <h1> Hello {{nm}} </h1>
         {% endif %}


         {% if nm=='Django' and st==5 %}
             <h1> {{nm}} Seats Available </h1>
         {% endif %}

         
         NOTE :-   If tags may also use the operations ==, !=, <, >, <=, >=, in, not in, is, is not


-->





**) =========  if else Tag  ========= (**
<!-- 

    Syntax:-

           {{ if condition }}
                ..................
                ..................
           {{ else }}
                ..................
                ..................
           {{ endif }}
          

-->





**) =========  if elif else Tag  ========= (**
<!-- 

    Syntax:- 

           {{ if condition }}
                ..................
                ..................
           {{ elif condition }}
                ..................
                ..................
           {{ elif condition }}
                ..................
                ..................
           {{ else }}
                ..................
                ..................
           {{ endif }}

-->





**) =========  if elif else Tag  ========= (**
<!--  

    Technically, when the template system encounters a dot, it tries the following lookups, 
    in this order:
        
        * Dictionary lookup
        * Attribute or method lookup
        * Numeric index lookup 

-->






**) =========  for loop Tag  ========= (**
<!--  

     Syntax:- 

           {% for variable in variables %}
                  {{variable}}
           {% endfor %}

     Syntax:- 
           
           {% for variable in variables %}
                  {{variable}}
           {% empty %}
                  Empty
           {% endfor %}



     Ex:-

           <ul>
              {% for stu in student %}
                <li> {{stu}} </li>
              {% endfor %}
           </ul>

     Ex:- 

           {% for key, value in data.items %}
                {{key}} : {{value}}
           {% endfor %}

-->


**) =========  Predefined forloop Variable  ========= (**
<!--  
    
     forloop.counter           =    The current iteration of the loop (1-indexed)
     forloop.counter()         =    The current iteration of the loop (0-indexed)
     forloop.revcounter        =    The number of iterations from the end of the loop (1-indexed)
     forloop.revcounter()      =    The number of iterations from the end of the loop (0-indexed)  
     forloop.first             =    True if this is the first time through the loop
     forloop.last              =    True if this is the last time through the loop
     forloop.parentloop        =    For nested loops, this is the loop surrounding the current one

     Example:-
           
           {% for stu in student %}
                {{forloop.counter}} {{stu}}
           {% endfor %}


-->