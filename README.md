# README
## Prepare the project environment

First, create a virtualenv using python native functionality
The purpose is to hold imports and other package dependencies:

```$ python3 -m venv py_env ```

Activate the new virtualenv by doingL

```source py_env/bin/activate```

While the py_dev is active you'll notice the label "py_dev" on the os prompt.

Now, install the dependencies.
In this case, Django.

```
pip3 install django
pip3 install djangorestframework
pip3 install django-filter
pip3 install markdown
```

Now use `django-admin` to setup the project,
```
django-admin startproject py_clean_arch_rest_api .
```
and the app

```
cd py_clean_arch_rest_api
django-admin startapp theapp
```

From now on implement the app inside "theapp" directory.