from configparser import ConfigParser
import json
import yaml
from common.logger import logger


class MyConfigParser(ConfigParser):

    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr: str) -> str:
        # 解决 .ini 文件中的 键option 自动转为小写的问题
        return optionstr


class ReadFileData():

    def load_yaml(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        logger.info(f"读取数据为：{data}")
        return data

    def load_json(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"读取数据为：{data}")
        return data

    def load_ini(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        conf = MyConfigParser()
        conf.read(file_path, encoding="utf-8")
        data = dict(conf._sections)
        return data


data = ReadFileData()
