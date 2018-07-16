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

```bash
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

4 directories, 11 files
```

## Implement the spider

```bash
(docker-selenium-automation-env) 
j.waterschoot at MI-Mac011 in ~/code/docker-selenium-automation on master
$ git checkout -b spider
Switched to a new branch 'spider'
(docker-selenium-automation-env) 
j.waterschoot at MI-Mac011 in ~/code/docker-selenium-automation/nintendoscreenshot on spider [!]
$ scrapy crawl nintendomain
...
2018-07-16 11:50:09 [scrapy.core.engine] INFO: Spider closed (finished)
```

We need to parse the following HTML:

```html
<section class="column col8 col12-tab new-releases" itemscope="" itemtype="http://schema.org/Product">
    <h1 class="h3">New video game releases</h1>
    <span class="h3 divider">|</span>
    <a class="b5 text-btn-arrow" href="/games/game-guide#filter/-|new|-|-|-|-|-|-|-|-|-|-|-|-|featured|des|-">See all</a>
    <ul class="row row-2cols row-2cols-tab row-2cols-mob no-margin">
        <li class="threeDS">
            <a class="row row-2cols row-2cols-tab row-1cols-mob" data-metric="{ eVars: { 13: 'Captain Toad: Treasure Tracker' }, events: [34], props: { 26: 'page &amp; promotion' } }" href="/games/detail/KCVZE6uK9Olm_8yuPpj7iLY6vCK9i7ur">
                <div class="boxart column">
                    <img alt="Captain Toad: Treasure Tracker" itemprop="logo" src="//media.nintendo.com/nintendo/bin/VEZ_l5hFMaNurdepFa1CHfzU50XxpQsK/WxKUWpV3S_EuBWzWPj4jb0qKiv8azT_T.png">
                </div>
                <div class="info column">
                    <div class="date" itemprop="releaseDate">07.13.18</div>
                    <div class="b3" itemprop="name">Captain Toad: Treasure Tracker </div>
                    <p class="b4" itemprop="isRelatedTo">Nintendo 3DS</p>
                </div>
            </a>
        </li>
    </ul>
</section>
```