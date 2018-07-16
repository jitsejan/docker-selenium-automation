# docker-selenium-automation
Using Docker with Selenium using different automation options.

## Set development environment

```bash
jitsejan at MacBook in ~/code
$ git clone https://github.com/jitsejan/docker-selenium-automation.git
jitsejan at MacBook in ~/code
$ cd docker-selenium-automation/
jitsejan at MacBook in ~/code/docker-selenium-automation on master [?]
$ conda create -n docker-selenium-automation-env
jitsejan at MacBook in ~/code/docker-selenium-automation on master [?]
$ source activate docker-selenium-automation-env
```

## Create Scrapy project
(docker-selenium-automation-env) 
jitsejan at MacBook in ~/code/docker-selenium-automation on master [?]
$ git checkout -b scaffold
jitsejan at MacBook in ~/code/docker-selenium-automation on scaffold [!?]
$ pip install scrapy
jitsejan at MacBook in ~/code/docker-selenium-automation on scaffold [!?]
$ scrapy startproject nintendoscreenshot
jitsejan at MacBook in ~/code/docker-selenium-automation on scaffold [!?]
$ tree
.
├── README.md
└── nintendoscreenshot
    ├── nintendoscreenshot
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── spiders
    │       ├── __init__.py
    │       └── __pycache__
    └── scrapy.cfg

5 directories, 8 files
jitsejan at MacBook in ~/code/docker-selenium-automation/nintendoscreenshot on scaffold [!?]
$ scrapy genspider nintendomain www.nintendo.com
Created spider 'nintendomain' using template 'basic' in module:
  nintendoscreenshot.spiders.nintendomain
(docker-selenium-automation-env) 
jitsejan at MacBook in ~/code/docker-selenium-automation/nintendoscreenshot on scaffold [!?]
$ tree
.
├── nintendoscreenshot
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-36.pyc
│       └── nintendomain.py
└── scrapy.cfg

4 directories, 11 filesm
```