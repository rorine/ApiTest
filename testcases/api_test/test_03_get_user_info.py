from common.logger import logger
from testcases.conftest import api_data
from operation.user import get_all_user_info, get_one_user_info
import allure
import pytest
import os
import sys
parentdir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
print(parentdir)
sys.path.insert(0, parentdir)
print(sys.path)


@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有用户信息")


@allure.step("步骤1 ==>> 获取某个用户信息")
def step_2(username):
    logger.info("步骤1 ==>> 获取某个用户信息：{}".format(username))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("获取用户信息模块")
class TestGetUserInfo():
    """获取用户信息模块"""

    @allure.story("用例--获取全部用户信息")
    @allure.description("该用例是针对获取所有用户信息接口的测试")
    @pytest.mark.single
    @pytest.mark.parametrize("except_result, except_code, except_msg",
                             api_data["test_get_all_user_info"])
    def test_get_all_user_info(self, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        step_1()
        result = get_all_user_info()
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(
            except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--获取某个用户信息")
    @allure.description("该用例是针对获取单个用户信息接口的测试")
    @allure.title("测试数据：【 {username}，{except_result}，{except_code}，{except_msg} 】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, except_result, except_code, except_msg",
                             api_data["test_get_get_one_user_info"])
    def test_get_one_user_info(self, username, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        step_2(username)
        result = get_one_user_info(username)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(
            except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")
