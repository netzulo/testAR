Usage Guide
===========

*This project it's oriented to all testers wich need an open source web application*.
*Manage all testing data for a Quality Assurance deparment*

Developers
~~~~~~~~~~

Prerequisites
-------------

+ Create virtualenv : ``mkvirtualenv testar``
+ Enter your existing virtualenv : ``workon testar``
+ Install package : ``python setup.py clean build install test``
+ Regenerate database scripts : ``python www/manage.py makemigrations testar-base``
+ Apply database scripts : ``python www/manage.py migrate``
+ Create new superuser : ``python www/manage.py createsuperuser`` ( *by default is* ``admin`` / ``adminadmin``)

Startup
-------

+ Can start development webserver with : ``python www/manage.py runserver 0.0.0.0:8000``
+ You can handle data from code with : ``python www/manage.py shell``

.. code:: python


    # Introduce some models to start
    from testproject.models import TestProject

    tp = TestProject(name="MyTestProject")
    tp.save()
    # end
    exit()


ToDo list
~~~~~~~~~

+ **mysql server** trought **docker image** configuration
+ **django** admin database

  + Will need to use bootstraped template ( *https://djangopackages.org/packages/p/django-admin-bootstrapped/* )
  + App : **testar-base**
      
      + CRUD for ``TestProject`` ( *group of testplans* )
      + CRUD for ``TestPlan`` ( *group of testsuites* )
      + CRUD for ``TestSuite`` ( *group of testcases* )
      + CRUD for ``TestCase`` ( *group of specs validated trought test steps* )
      + CRUD for ``Environment`` ( *group of conditions to be applied ``n - n`` to TestProject* )
      + CRUD for ``Milestone`` ( *group of conditions to manage reporting status for each testproyect for each model levels* )
      + CRUD for ``Report`` ( *data about reporting over some testar-base models* )
      + CRUD for ``ReportTemplate`` ( *group of report conditions, vars to be replaced at* )
      + CRUD for ``ContinuousIntegration`` ( *allow to configure integration with different systems using app* : **testar-ci** )
      + CRUD for ``IssueTracker`` ( *allow to configure integration with different reporting systems using app* : **testar-tracker** )
  + App : **testar-ci**

      + CRUD for ``GitlabCi`` ( *allow to configure integration with gitlab* )

          + CRUD for ``GitlabPipeline`` ( *allow to access Gitlab pipelines using API calls* )
          + CRUD for ``GitlabJob`` ( *allow to access Gitlab pipelines using API calls* )
  
  + App : **testar-tracker**

      + CRUD for ``RedmineTracker`` ( *allow to configure integration with gitlab* )
      + CRUD for ``JiraTracker`` ( *allow to configure integration with gitlab* )
  

.. code:: python


    # some python code 