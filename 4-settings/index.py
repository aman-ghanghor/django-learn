#  =============  settings.py  ==============
#
#   | from pathlib import Path
#   | BASE_DIR = Path(__file__).resolve().parent.parent
#
#     - BASE_DIR is a variable which contains absolute path of base directory/project folder.
#
#
#   | SECRET_KEY = 'django-insecure-3jp^=eiaw4ig591c2_hdv)wd_$t6l$o+0ymgvc%nq*g9(*)fd-'
#
#     - This is used to provide cryptographic signing, and should be set to a unique,
#       unpredictable value. django-admin startproject automatically adds a randomly-generated
#       SECRET_KEY to each new project.
# 
#     -------- The secret key is used for : --------
#     
#     *  All sessions if you are using any other session backend than 
#        django.contrib.sessions.backend.cache, or are using the default get_session_auth_hash(). 
#     
#     *  All messages if you are using CookieStorage or FallbackStorage.
#
#     *  All PasswordResetView tokens
#
#     *  Any usage of cryptographic signing, unless a different key is provided.
#
#
#   | DEBUG = True
#  
#     - A Boolean (True/False) that turns on/off debug mode.
#     - Never deploy a site into production with DEBUG turned on.
#     - One of the main features of debug mode is the display of detailed error pages.
#     - If DEBUG is False, you also need to properly set the ALLOWED_HOSTS setting.
#       Failing to do so will result in all requests being returned as "Bad Request (400)"
#
#
#   | ALLOWED_HOSTS = []
#
#     - A list of string representing the host/domain names that this Django site can serve.
#       Values in this list can be fully qualified names (e.g. 'www.example.com'), in which case
#       they will be matched against the request's Host header exactly (case-insensitive, not 
#       including port).
#   
#     - A value beginning with a period can be used as subdomain wildcart: '.example.com' will
#       match example.com, www.example.com, and any other subdomain of example.com
#
#     - A value of '*' will match anything; in this case you are responsible to provide your own
#       validation of the Host header.
#
#
#
#   | INSTALLED_APPS = [
#   |   'django.contrib.admin',                 ______
#   |   'django.contrib.auth',                        |
#   |   'django.contrib.contenttypes',                |
#   |   'django.contrib.sessions',                    |____ Built-in Application
#   |   'django.contrib.messages',                    |
#   |   'django.contrib.staticfiles',          _______|
#   | ]
#
#     - A list of string designating all applications that are enabled in this Django installation.
#       Each string should be a dotted Python path to an application configuration class(preferred) 
#       or a package containing an application.
#     - Application names and labels must be unique in INSTALLED_APPS.
#     - Application names - The dotted Python path to the application package must be unique. There 
#                           is no way to include the same application twice, short of duplicating its
#                           code under another name.
#     - Application labels - By default the final part of the name must be unique too. For example, 
#                            you can't include both django.contrib.auth and myproject.auth
#
#
#
#   | MIDDLEWARE = [
#   |     'django.middleware.security.SecurityMiddleware',
#   |     'django.contrib.sessions.middleware.SessionMiddleware',
#   |     'django.middleware.common.CommonMiddleware',
#   |     'django.middleware.csrf.CsrfViewMiddleware',
#   |     'django.contrib.auth.middleware.AuthenticationMiddleware',
#   |     'django.contrib.messages.middleware.MessageMiddleware',
#   |     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#   | ]
#
#      - A list of middleware to use.
#
#
#
#
#   | ROOT_URLCONF = 'schoolproject.urls'
#
#      - A string representing the full Python import path to your root URLconf, for example
#        "mydjangoapps.urls" can be overridden on a per-request basis by setting the attribute
#        urlconf on the incoming HttpRequest object.
#
#
#
#
#   | TEMPLATES = [
#   |  {
#   |    'BACKEND': 'django.template.backends.django.DjangoTemplates',
#   |    'DIRS': [],                                    -----------------------> Directories where the engine should look for templates source files, in search order.
#   |    'APP_DIRS': True,                              ----------> Whether the engine should look for template source files inside installed applications.
#   |    'OPTIONS': {                                   ------------------> Extra parameters to pass to the template backend. Available parameters vary depending on the template backend.
#   |        'context_processors': [
#   |            'django.template.context_processors.debug',
#   |            'django.template.context_processors.request',
#   |            'django.contrib.auth.context_processors.auth',
#   |            'django.contrib.messages.context_processors.messages',
#   |        ],
#   |     },
#   |   },
#   | ]
#
#      - A list containing the settings for all template engines to be used with Django. Each item
#        of the list is a dictionary containing the options for an individiual engine.
#
#
#
#
#   | WSGI_APPLICATION = 'schoolproject.wsgi.application'
#
#      - The full Python path of the WSGI application object that Django's built-in servers
#        (e.g. runserver) will use. The django-admin startproject management command will create a 
#        standard wsgi.py file with an application callable in it, and point this setting to that
#        application.
#      - If not set, the return value of django.core.wsgi.get_wsgi_application() will be used.
#
#
#
#
#   | DATABASES = {
#   |   'default': {
#   |      'ENGINE': 'django.db.backends.sqlite3',
#   |      'NAME': BASE_DIR / 'db.sqlite3',
#   |    }
#   | }
#
#     - A dictionary containing the settings for all databases to be used with Django.
#     - It is a nested dictionary whose contents map a database alias to a dictionary 
#       containing the options for an individual database.
#     - The DATABASES setting must configure a default database; any number of additional
#       databases may also be specified.
#
#       Example :-
#             
#          :  DATABASE = {
#          :      'default': {
#          :          'ENGINE': 'django.db.backends.postgresql',
#          :          'NAME': 'mydatabase',
#          :          'USER': 'mydatabaseuser', 
#          :          'PASSWORD': 'mypassword',
#          :          'HOST': '127.0.0.1',
#          :          'PORT': '5432',
#          :      }
#          :  }
#          
#
#
#
#   | AUTH_PASSWORD_VALIDATORS = [
#   |     {
#   |        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#   |     },
#   |     {
#   |        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#   |     },
#   |     {
#   |        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#   |     },
#   |     {
#   |        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#   |     },
#   |  ]
#   |
#
#     - The list of validators that are used to check the strength of user's passwords.
#
#
#
#
#   | LANGUAGE_CODE = 'en-us'
#
#     - A string representing the language code for this installation. This should be in 
#       standard language ID format. For example, U.S. English is 'en-us'
#
#
#
#
#   | TIME_ZONE = 'UTC'
#
#     - A string representing the time zone for this application.
#
#
#
#
#   | USE_I18N = True
#
#     - A boolean that specifies whether Django's translation system should be enabled. This 
#       provides a way to turn it off, for performance. If this is set to False, Django will
#       make some optimizations so as not to load the translation machinery.
#
#
#
#
#   | USE_LION = True
#
#     - A boolean that specifies if loclized formatting of data will be enbaled by default or not. 
#       If this is set to True, e.g. Django will display numbers and dates using the format of
#       the current locale.
#
#
#
#
#   | USE_TZ = True
#
#     - A boolean that specifies if datetimes will be the timezone aware by default or not. If 
#       this is set to True, Django will use timezone-aware internally. Otherwise Django will
#       use naive datetimes in local time.
#
#
#
#
#   | STATIC_URL = '/static/'
#
#     - URL to use when referring to static files to located in STATIC_ROOT.
#
#       Exmaple:-        "/static/" or "http://static.example.com/"
#              
#     - If not None, this will be used as the base path for asset definitions (the Medium class)
#       and the staticfiles app.
#     - It must end in a slash if set to a non-empty value.
#     - You may need to configure these files to be served in development and will definitely 
#       need to do so in production.
#
#
#
#