# ===========  Template Inheritance/Template Extending  ===========
<!--

  - Template inheritance allows you to build a base "skeleton" template that contains all the 
    common elements of your site and defines blocks that child templates can override.

  - The [extends] tag is used to inherit template.

  - extends tag tells the template engine that this template "extends" another template. 

  - When the template system evaluates this template, first it locates the parent let's assume,
    "base.html". 

  - At that point, the template engine will notice the block tags in base.html and replace those
    blocks with the contents of the child template.

  - You can use as many levels of inheritance as needed.
 
-->



**---------  extends Tag ---------**
<!--  

   {% extends %} = The extends tag is used to inherit template. It tells the template engine 
                   that this template "extends" another template. It has no end tag.

    Syntax:- 

         {% extends 'parent_template_name' %}

         {% extends variable %}


    Example: - 

         {% extends "./base1.html" %}

         {% extends "../base2.html" %}

         {% extends "./my/base3.html" %}

         {% extends something %}
          
-->




**---------  extends Tag ---------**
<!-- 

    {% block %} = The block tag is used to for overriding specific parts of a template.

    Syntax:-

          {% block blockname %} ... {% endblock %}

          {% block blockname %} ... {% endblock blockname %}

    
    Example:- 

          {% block title %} ... {% endblock %}

          {% block content %} ... {% endblock content %}


    Rules:- 

         * If We use {% extends %} in a template, it must be the first template tag in that 
           template. Template inheritance won't work, otherwise.

         * More {% block %} tags in our base templates are better.   

         * Child templates don't have to define all parent blocks, so we can fill in reasonable
           defaults in a number of blocks, then only define the ones we need later.
 
         * We can't define multiple block tags with the same name in the same template.
     
         * If We need to get the content of the block from the parent template,
           the {{ block.super }} variable will do the trick.
 
-->





**-------  Creating Base/Parent Template and Child Template -------**
<!-- 
   
   We write common codes in base template and create blocks for code which may vary page to
   page. Later this template will be inherited by child templates and child template will
   override created blocks.

   Example:-


     ---------------  base.html  ----------------------------
    |                                                        |
    | <html>                                                 |
    |  <head>                                                |
    |    <title> {% block title %} {% block %} </title>      |
    |  </head>                                               |
    |  <body>                                                |
    |    {% block content %}  {% endblock content %}         |
    |  </body>                                               |
    | </html>                                                |
    |________________________________________________________|


     ---------------  home.html  ----------------
    |                                            |
    | {% extends 'base.html' %}                  |
    |                                            |
    | {% block title %}                          |
    |  Home                                      |
    | {% endblock %}                             |
    |                                            |
    | {% block content %}                        |
    |   Hello I am Home Page                     |
    | {% endblock content %}                     |
    |                                            |
    |____________________________________________|


     ---------------  about.html  ---------------
    |                                            |
    | {% extends 'base.html' %}                  |
    |                                            |
    | {% block title %}                          |
    |  About                                     |
    | {% endblock %}                             |
    |                                            |
    | {% block content %}                        |
    |   Hello I am About Page                    |
    | {% endblock content %}                     |
    |                                            |
    |____________________________________________|



   
   Example:- 

     ---------------  base.html  ----------------------------------
    |                                                              |
    | <html>                                                       |
    |  <head>                                                      |
    |    <title> {% block title %} Other {% block %} </title>      |
    |  </head>                                                     |
    |  <body>                                                      |
    |    {% block content %}  {% endblock content %}               |
    |  </body>                                                     |
    | </html>                                                      |
    |______________________________________________________________|


     ---------------  home.html  ----------------
    |                                            |
    | {% extends 'base.html' %}                  |
    |                                            |
    | {% block title %}                          |
    |  Home                                      |
    | {% endblock %}                             |
    |                                            |
    | {% block content %}                        |
    |   Hello I am Home Page                     |
    | {% endblock content %}                     |
    |                                            |
    |____________________________________________|


     ---------------  about.html  ---------------
    |                                            |
    | {% extends 'base.html' %}                  |
    |                                            |
    | {% block content %}                        |
    |   Hello I am About Page                    |
    | {% endblock content %}                     |
    |                                            |
    |____________________________________________|


 
-->





<!--  

   - Keep Base template and append some content

   Ex:-

      {% block title %} {{block.super}} | Home {% endblock title %}


-->