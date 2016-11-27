#encoding=utf-8

"""
一. 为什么使用包？
    1. 没有包时，需要查看文件搜索路径才知道文件的位置。包提供了更加明确的信息如：
        import utils
        import database.client.utils
    2. 所有包导入都相对于一个根目录，在搜索路径上就只需要一个单独的接入点，更好的组织项目
        - root
          - main.py
          - packages
            - __init__.py
            - module2.py
            - module3.py

二、__init__.py
    1. 如果一个目录希望python将其看做是包，则该目录必须包含__init__.py 大部分情况下这个文件为空
    2. 当一个包被导入时，会执行__init__.py里面的语句,就好比导入模块要执行模块里面的语句一样
    3. __all__: 在这个文件中指定包含的模块，在使用from packages import *时会自动导入该模块
"""
