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

To get the image, link, release date and the name of the game, we add the following code to the spider:

```python
# -*- coding: utf-8 -*-
import scrapy

BASE_URL = 'http://www.nintendo.com/'

class NintendomainSpider(scrapy.Spider):
    name = 'nintendomain'
    allowed_domains = ['www.nintendo.com']
    start_urls = [BASE_URL]

    def parse(self, response):
        for elem in response.css('section.new-releases li a'):
            yield {
               'name': elem.css('div[itemprop="name"]::text').extract_first(),
               'releasedate': elem.css('.date::text').extract_first().strip(),
               'link': BASE_URL + elem.xpath('@href').extract_first(),
               'image': elem.css('img::attr(src)').extract_first()
            }
```

```bash
j.waterschoot at MI-Mac011 in ~/code/docker-selenium-automation/nintendoscreenshot on spider [!]
$ scrapy crawl nintendomain
...
2018-07-16 12:21:26 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2018-07-16 12:21:26 [scrapy.core.engine] INFO: Spider opened
2018-07-16 12:21:26 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2018-07-16 12:21:26 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2018-07-16 12:21:27 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.nintendo.com/robots.txt> from <GET http://www.nintendo.com/robots.txt>
2018-07-16 12:21:28 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://www.nintendo.com/robots.txt> (referer: None)
2018-07-16 12:21:28 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.nintendo.com/> from <GET http://www.nintendo.com/>
2018-07-16 12:21:28 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.nintendo.com/> (referer: None)
2018-07-16 12:21:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.nintendo.com/>
{'name': 'Captain Toad: Treasure Tracker ', 'releasedate': '07.13.18', 'link': 'http://www.nintendo.com//games/detail/VOEJamy4OefwooB8752-azz3ZJD3GMV1', 'image': '//media.nintendo.com/nintendo/bin/Ku68rcmSJKen7UnibJ_v3RY3RsJtfXNx/5GOXMh4vjnKWuu8fhJnquH1EABATAND7.png'}
2018-07-16 12:21:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.nintendo.com/>
{'name': 'Captain Toad: Treasure Tracker ', 'releasedate': '07.13.18', 'link': 'http://www.nintendo.com//games/detail/KCVZE6uK9Olm_8yuPpj7iLY6vCK9i7ur', 'image': '//media.nintendo.com/nintendo/bin/VEZ_l5hFMaNurdepFa1CHfzU50XxpQsK/WxKUWpV3S_EuBWzWPj4jb0qKiv8azT_T.png'}
2018-07-16 12:21:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.nintendo.com/>
{'name': 'OCTOPATH TRAVELER ', 'releasedate': '07.13.18', 'link': 'http://www.nintendo.com//games/detail/mHJ6s33Zed1xuj5BirLH3UIUmIrrr17R', 'image': '//media.nintendo.com/nintendo/bin/52yHZdow0JIT66VPGPY9xg_FUbT6hf6w/wW4hMobKdrOGg0sm8qmbjhzflpbdtf2w.png'}
2018-07-16 12:21:28 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.nintendo.com/>
{'name': 'Wolfenstein II: The New Colossus ', 'releasedate': '06.29.18', 'link': 'http://www.nintendo.com//games/detail/RX3RAfDdvgnjGbPBunPzZ-OHGPJViicE', 'image': '//media.nintendo.com/nintendo/bin/VNyVj_zZlMtmPvTEwkvnipCH6Yft9Of7/Mes9bLY1FaRfqUX_h5Sn4KGXP_bV9O2c.png'}
2018-07-16 12:21:28 [scrapy.core.engine] INFO: Closing spider (finished)
...
2018-07-16 12:21:28 [scrapy.core.engine] INFO: Spider closed (finished)
(docker-selenium-automation-env) 
