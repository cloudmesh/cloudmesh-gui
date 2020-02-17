# Cloudmesh Configuration with a GUI 


[![image](https://img.shields.io/travis/TankerHQ/cloudmesh-gui.svg?branch=master)](https://travis-ci.org/TankerHQ/cloudmesn-gui)

[![image](https://img.shields.io/pypi/pyversions/cloudmesh-gui.svg)](https://pypi.org/project/cloudmesh-gui)

[![image](https://img.shields.io/pypi/v/cloudmesh-gui.svg)](https://pypi.org/project/cloudmesh-gui/)

[![image](https://img.shields.io/github/license/TankerHQ/python-cloudmesh-gui.svg)](https://github.com/TankerHQ/python-cloudmesh-gui/blob/master/LICENSE)

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
    
In case you like to edit all parameters for a compute cloud you can use


```bash
cms gui edit cloud.chameleon
```