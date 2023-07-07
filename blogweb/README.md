
MIGRATIONS COMMAND

    python manage.py makemigrations 
    This command will give me a file in which all columns and data type and constraints will be defined
        python manage.py migrate 

        Add Data in 4 Ways:
            1. Using Database shell
            2. Using Admin Panel
                localhost/admin/
                To create password and username from admin, Use following
                    a. python manage.py createsuperuser
                    b. register you model in admin.py file to showcase it on admin panel
            3. Using Django Shell 
                python manage.py shell 
            4. In views file
