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

#确保命令按顺序展示
class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()

@click.group(cls=NaturalOrderGroup)
@click.version_option()
def cli():
    """
    将Poetry run 的长命令+参数缩写为短命令 ，便于记忆和使用。
    可以在独立的Spder内使用，也可以启动集成环境里的Spyder IDE。

    """


@cli.command()
def new():
    """用内置的dsproj模版创建数据科学标准项目

    """
    cookiecutter(DSTEMPLATE)


@cli.command()
def install():
    """按当前项目的pyproject.toml依赖管理，配置含Spyder的的虚拟环境
    """
    os.system("poetry install")

@cli.command()
def spyder():
    """弹出当前数据科学项目环境中的内置Spyder，开启数据科学之旅

    """
    os.system("nohup poetry run spyder --window-title=数据科学工作台 --opengl=gles -p . > logs/spyder.log 2>&1 &")


@cli.command()
def clean():
    """清理Python运行时的字节码文件
    """
    cmd = """
    find . -type f -name "*.py[co]" -delete
    find . -type d -name "__pycache__" -delete
    """
    os.system(cmd)

@cli.command()
def git():
    """弹出Git界面，可交互式操作常规Git动作
    """
    os.system("nohup poetry run git cola  > logs/git-cola.log 2>&1 &")


@cli.command()
def monitor():
    """在默认端口8501运行当前数据科学项目环境中的指标监控仪
    """
    os.system("nohup poetry run streamlit run  analysis/monitor.py --server.port 8501 > logs/report.log 2>&1 &")


@cli.command()
def report():
    """在默认端口8502运行当前数据科学项目环境中的分析仪
    """
    os.system("nohup poetry run streamlit run  analysis/report.py --server.port 8502 > logs/monitor.log 2>&1 &")


@cli.command()
def run(py_path):
    """用数据科学虚拟环境中的Python执行项目内的给定路径的py文件
    """
    os.system(f"poetry run pyhon3 {py_path}")


@cli.command()
def update():
    """按pyproject.toml升级当前数据科学项目的虚拟环境
    """
    os.system("poetry update")


@cli.command()
def shell():
    """激活poetry的虚拟环境，通常是做某些简单的验证
    """
    os.system("poetry shell")


@cli.command()
def remote():
    """ 通常在服务器上执行，启动当前数据科学项目环境中的Spyder-kernles，用于本地Spyder远程连接

    """
    os.system("""nohup poetry run python3 -m spyder_kernels.console --matplotlib="inline"  -f=connect.json > logs/spyderkernels.log 2>&1 &""")

@cli.command()
def pypi():
    """ 通常在服务器上执行，启动当前数据科学项目环境中的piserver，用于托管私有pip包
    """
    os.system("nohup poetry run pypi-server -p 8585 ~/pypipkgs &")




if __name__ == "__main__":
    cli()
