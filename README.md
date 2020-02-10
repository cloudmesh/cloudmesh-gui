Documentation
=============


[![image](https://img.shields.io/travis/TankerHQ/cloudmesh-bar.svg?branch=master)](https://travis-ci.org/TankerHQ/cloudmesn-bar)

[![image](https://img.shields.io/pypi/pyversions/cloudmesh-bar.svg)](https://pypi.org/project/cloudmesh-bar)

[![image](https://img.shields.io/pypi/v/cloudmesh-bar.svg)](https://pypi.org/project/cloudmesh-bar/)

[![image](https://img.shields.io/github/license/TankerHQ/python-cloudmesh-bar.svg)](https://github.com/TankerHQ/python-cloudmesh-bar/blob/master/LICENSE)

see cloudmesh.cmd5

* https://github.com/cloudmesh/cloudmesh.cmd5


This component allows you to edit the cloudmesh.yaml file via a simple 
GUI form.

The manual page is

      gui activate
      gui profile
      gui cloud CLOUD [--show]
      gui edit KEY [--show]

If you use --show the passwords are shown in the form otherwise they are
blended out with a * 

For cloudmesh to work you need to edit

* the profile
* activate the cloud you like to use
* and add things such as usernames, passwords and other parameters

Next we provide some examples to achive these tasks and include a
screenshot:

    
```bash    
cms gui profile
```    
    
![Profile](images/profile.png)    

    
```bash
cms gui activate
```

![Activate](images/activate.png)    


```bash
cms gui edit cloud.chameleon.credentials
```

or

```bash
cms gui cloud chameleon
```

![Credentials](images/credentials.png)
    
