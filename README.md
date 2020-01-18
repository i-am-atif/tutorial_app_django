# tutorial_app_django

## This is a Tutorial WEB App written in python using the Django Framework.

### Installation :
 - **step 1**: Requirements : SYSTEM MUST HAVE Python 3.7 and Django 2.1.4 INSTALLED
   ``` pip install django==2.1.4 ```

 - **step 2**: WE START OUR PROJECT "mysite" USING THE COMMAND
   ``` django-admin startproject mysite ```

 - **step 3**: AFTER WE HAVE STARTED OUR PROJECT THEN WE WILL USE "manage.py" , TO ADD OUR FIRST ACTUAL APP TO OUR PROJECT
  ``` python3 manage.py startapp main ```

 - **step 4**: TO RUN THE SERVER DO:
 ``` python3 manage.py runserver ```

### WE CAN SEE THAT OUR DEVELOPMENT SERVER IS NOW RUNNING AT http://127.0.0.1:8000. OPEN A BROWSER AND HEAD TO THIS ADDRESS.

 - **step 5**: THEN WE ADD ANOTHER APP "TinyMCE-4 lite" WHICH PROVIDES US WITH SOME PREDEFINED FEATURES
 ``` python -m pip install django-tinymce4-lite ```

 ``` THEN ADD SOME FILES TO mysite/mysite/settings.py
     FIRST ADD 'tinymce', TO OUR INSTALLED_APPS
     AND THEN ADD SOMEWHERE IN THE settings.py
```    

```
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
```

- **step 6**: WE THEN ADD A "NAVBAR" IN OUR WEBSITE THE CONTENT OF WHICH IS PRESENT IN 
``` C:\Users\atifr\Desktop\mysite\main\templates\main\includes ``` THIS "NAVBAR" FILE IS IMPLICITLY INCLUDED IN THE BODY OF "header.html"

- **step 7**: AFTER WHICH WE START OUR HTML AND CSS PART WE JUST ADD HTML TEMPLATES IN OUR MAIN APP AND USE "Materialize CSS" TO DOWNLOAD SOME STYLING CONTENT. AND THEN INSTALL "koala" WHIS IS A "Sass compiler" TO NAVIGATE OUR "mayterialize" FILE.

- **step 8**: IN THS STEP WE ADD PYTHON TUTORIAL DATA IN OUR WEBSITE UNDER "tutorials ,series and category" OR YOU CAN INCLUDE YOUR OWN DATA IN YOUR WEBSITE AND NAME IT ACCORDINGLY.

- **step 9**: THEN WE INCLUDE SOME FUNCTIONS IN mysite/mysite/models.py AND mysite/mysite/views.py, IN ORDER TO ORGANIZE OUR DATA UNDER TUTORIAL,SERIES AND CATEGORY USING FOREIGN KEYS AND MODELS AND USING A SINGLE SLUG FUNCTION IN "views.py" TO FILTER OUR CONTENT USING TWO HTML FILES NAMED "categories.html" AND "category.html" TO DISPLAY OUR FILTERED DATA.

- **step 10**: NOW AT LAST WE ADD A "Dynamic Sidebar" IN OUR WEBSITE WHICH POINTS TO SPECIFIC TUTORIALS

- **step 11**: DEPLOY THE FINAL WEBSITE TO A SERVER USING SOME WEB HOSTING.



