#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:27:40 2022

@author: genghis
"""

import os
import click
from cookiecutter.main import cookiecutter


DSTEMPLATE = 'git@github.com:jonzhaopeng/dsproj-template.git'


@click.group()
@click.version_option()
def cli():
    """
    将Poetry run 的长命令+参数缩写为短命令 ，便于记忆和使用。
    可以在独立的Spder内使用，也可以启动集成环境里的Spyder IDE。

    """


@cli.command()
def new():
    """用模版创建数据科学标准项目

    """
    cookiecutter(DSTEMPLATE)



@cli.command()
def install():
    """创建当前数据科学项目需要的虚拟环境
    """
    os.system("poetry install")



@cli.command()
def update():
    """升级当前数据科学项目需要的虚拟环境
    """
    os.system("poetry update")


@cli.command()
def shell():
    """激活poetry的虚拟环境
    """
    os.system("poetry shell")


@cli.command()
def spyder():
    """启动当前数据科学项目环境中的Spyder

    """
    os.system("poetry run spyder --window-title=数据科学工作台 --opengl=gles -p . > logs/spyder.log 2>&1 &")

@cli.command()
def remote():
    """ 通常在服务器上，启动当前数据科学项目环境中的Spyder-kernles

    """
    os.system("""poetry run python3 -m spyder_kernels.console --matplotlib="inline"  -f=connect.json > logs/spyderkernels.log 2>&1 &""")

@cli.command()
def pypi():
    """ 通常在服务器上，启动当前数据科学项目环境中的remoteypiserver

    """
    os.system("poetry run pypi-server -p 8585 ~/pypipkgs &")



@cli.command()
def monitor():
    """启动当前数据科学项目环境中的指标监控仪,会自动弹出浏览器请求默认端口8501。
    """
    os.system("poetry run streamlit run  analysis/monitor.py --server.port 8501 > logs/report.log 2>&1 &")


@cli.command()
def report():
    """当前数据科学项目环境中的分析仪,会自动弹出浏览器请求默认端口8502。
    """
    os.system("poetry run streamlit run  analysis/report.py --server.port 8502 > logs/monitor.log 2>&1 &")


@cli.command()
def run(py_path):
    """用数据科学的Python虚拟环境执行项目内的py文件
    """
    os.system(f"poetry run pyhon3 {py_path}")


@cli.command()
def clean():
    """清理Python运行时的动态文件
    """
    cmd = """
    find . -type f -name "*.py[co]" -delete
    find . -type d -name "__pycache__" -delete
    """
    os.system(cmd)


def git():
    """启动cola 完成git 操作和commit模版
    """
    os.system("poetry run git cola &")

