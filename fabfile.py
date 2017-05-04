# -*- coding: utf-8 -*-


import os

from fabric.api import *
from cabric.api import *


@task
def rpm_import():
    run('sudo rpm --import http://packages.elastic.co/GPG-KEY-elasticsearch')
    pass


@task
def kibana_dashboards():
    # 加载kibana仪表盘
    run("cd ~ && curl -L -O https://download.elastic.co/beats/dashboards/beats-dashboards-1.1.0.zip")
    run("cd ~ && unzip beats-dashboards-*.zip")
    run("cd ~/beats-dashboards-1.1.0 && ./load.sh")
    # 配置仪表盘
    run("cd ~ && curl -O https://gist.githubusercontent.com/thisismitch/3429023e8438cc25b86c/raw/d8c479e2a1adcea8b1fe86570e42abab0f10f364/filebeat-index-template.json")
    run("cd ~ && curl -XPUT 'http://localhost:9200/_template/filebeat?pretty' -d@filebeat-index-template.json")
    # 删除安装文件
    run("sudo rm -rf ~/beats-dashboards-* ~/beats-dashboards-*.zip ~/filebeat-index-template.json")
    pass