# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from scrapy.utils.project import get_project_settings

class NintendoscreenshotPipeline(object):
    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def open_spider(self, spider):
        self.items = []
        self.settings = get_project_settings()
        self.smtp = smtplib.SMTP(self.settings['MAIL_HOST'],
                                 self.settings['MAIL_PORT'])
        self.smtp.starttls()
        self.smtp.login(self.settings['MAIL_USER'],
                        self.settings['MAIL_PASS'])

    def close_spider(self, spider):
        msg = MIMEMultipart()
        msg['From'] = self.settings['MAIL_FROM']
        msg['To'] = COMMASPACE.join(self.settings['MAIL_TO'])
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.settings['MAIL_SUBJECT']

        msg.attach(MIMEText(str(self.items)))


        self.smtp.sendmail(
            from_addr=self.settings['MAIL_FROM'],
            to_addrs=self.settings['MAIL_TO'],
            msg=msg.as_string(),
        )