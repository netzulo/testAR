TestAR - Automatic Reporting
============================


.. image:: https://img.shields.io/github/issues/netzulo/testAR.svg
  :alt: Issues on Github
  :target: https://github.com/netzulo/testAR/issues

.. image:: https://img.shields.io/github/issues-pr/netzulo/testAR.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/netzulo/testAR/issues

.. image:: https://img.shields.io/github/release/netzulo/testAR.svg
  :alt: Release version on Github
  :target: https://github.com/netzulo/testAR/releases/latest

.. image:: https://img.shields.io/github/release-date/netzulo/testAR.svg
  :alt: Release date on Github
  :target: https://github.com/netzulo/testAR/releases/latest

+-----------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Branch                | Linux Deploy                                                      | Windows Deploy                                                                                 | CircleCI - Docker                                                                                                         | CodeClimate                                                                            |
+=======================+===================================================================+================================================================================================+===========================================================================================================================+========================================================================================+
|  master               | .. image:: https://travis-ci.org/netzulo/testAR.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true | .. image:: https://circleci.com/gh/netzulo/testAR.svg?&style=shield&circle-token=80384cb2233d112dc0785278d5b7c3d8c6a5686c | .. image:: https://api.codeclimate.com/v1/badges/46279cf9a6a47ed583d6/maintainability  |
+-----------------------+-----------------------+-------------------------------------------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+


Python tested versions
----------------------

+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|  **3.6**          |  **3.5**          |  **3.4**          |  **3.3**          |  **3.2**          |  **2.7**          |
+===================+===================+===================+===================+===================+===================+
|    *Supported*    |    *Supported*    |  *Not Supported*  |  *Not Supported*  |  *Not Supported*  |  *Not Supported*  |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+

TestAR is a web based test management and test execution system. It enables quality assurance teams to create and manage their test cases as well as to organize them into test plans. These test plans allow team members to execute test cases and track test results dynamically.

TestAR is a GPL licensed open source project. All of the source code behind TestAR is freely available for download via GitHub. If you are interested in contributing to the TestAR effort feel free to contact us. There is no hidden fee - 100% free for using!

In an ideal world, testing would be a pretty straightforward process. A test team takes the product requirements, writes a test specification document, reviews the tests, and then runs them all for each version of the product. The team is composed of full-time staff, and everyone knows exactly what is expected of them.

In practice, few organisations have that luxury. There is not time to run all the tests on every product version - especially on fix-releases that need to be rolled out quickly. Requirements are constantly changing, and the tests have to be changed in step. Test staff come and go. There are misunderstandings over who was supposed to run which tests, so some get missed. Management suddenly wants a status update at seven in the evening.

In these situations you need the support of a test management tool, such as TestAR. The purpose of TestAR is to answer questions such as:

* For which requirements do we still need to write or update test cases?
* Which tests do you want me to run for this version?
* How much progress have we made on testing this release?
* Which test cases are currently failing, and what are the errors?
* On which version was this group of test cases last run, and is it time we ran them again?
* And ultimately: is this version of the product fit for release?

TestAR helps you to keep the test process under control. It forms a repository for requirements and test cases, and relates these to builds, platforms and staff. You allocate tests to staff who carry them out and record the results. A wide variety of reports provide information on what has been done and what still needs to be done.


How to install ?
----------------

+ Install from PIP : ``pip install testar``

+ Install from setup.py file : ``python setup.py install``


Documentation
-------------

+ How to use library, searching for `Usage Guide`_.


How to exec tests ?
-------------------

+ Tests from setup.py file : ``python setup.py test``

+ Install from PIP file : ``pip install tox``
+ Tests from tox : ``tox -l && tox -e TOX_ENV_NAME`` ( *see tox.ini file to get environment names* )


+---------------------+--------------------------------+
| TOX Env name        | Env description                |
+=====================+================================+
| py27,py34,py35,py36 | Python supported versions      |
+---------------------+--------------------------------+
| flake8              | Exec linter in testar/ tests/  |
+---------------------+--------------------------------+
| coverage            | Generate XML and HTML reports  |
+---------------------+--------------------------------+
| docs                | Generate doc HTML in /docs     |
+---------------------+--------------------------------+

Configuration File
~~~~~~~~~~~~~~~~~~


::

    {}


Getting Started
~~~~~~~~~~~~~~~

*Just starting example of usage before read* `Usage Guide`_.


.. _Usage Guide: USAGE.rst
