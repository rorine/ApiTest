from api.user import user
from common.logger import logger
from core.result_base import ResultBase


def register_user(username, password, telephone, sex="", address=""):
    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "sex": sex,
        "telephone": telephone,
        "address": address
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.register(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = f"接口返回码为 {res.json()['code']}, 返回信息：{res.json()['msg']}"
    result.msg = res.json()['msg']
    result.response = res
    logger.info(f"注册用户结果：{result.response.text}")
    return result


def login_user(username, password):

    result = ResultBase()
    payload = {
        "username": username,
        "password": password
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.login(data=payload, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
        result.token = res.json()["login_info"]["token"]
    else:
        result.error = f"接口返回码为 {res.json()['code']}, 返回信息：{res.json()['msg']}"
    result.msg = res.json()["msg"]
    result.response = res
    logger.info(f"登录用户结果：{result.response.text}")
    return result


def delete_user(username, admin_user, token):

    result = ResultBase()
    json_data = {
        "admin_user": admin_user,
        "token": token,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.delete(username, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = f"接口返回码为 {res.json()['code']}, 返回信息：{res.json()['msg']}"
    result.msg = res.json()["msg"]
    result.response = res
    logger.info(f"删除用户结果：{result.response.text}")
    return result


def update_user(id, admin_user, new_password, new_telephone, token, new_sex="", new_address=""):

    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    json_data = {
        "admin_user": admin_user,
        "password": new_password,
        "token": token,
        "sex": new_sex,
        "telephone": new_telephone,
        "address": new_address
    }
    res = user.update(id, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = f"接口返回码为 {res.json()['code']}, 返回信息：{res.json()['msg']}"
    result.msg = res.json()["msg"]
    result.response = res
    logger.info(f"修改用户结果：{result.response.text}")
    return result


def get_all_user_info():

    result = ResultBase()
    res = user.list_all_users()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = f"接口返回码为 {res.json()['code']}, 返回信息：{res.json()['msg']}"
    result.msg = res.json()["msg"]
    result.response = res
    return result


def get_one_user_info(username):
    result = ResultBase()
    res = user.list_one_user(username)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = f"接口返回码为 {res.json()['code']}, 返回信息：{res.json()['msg']}"
    result.msg = res.json()["msg"]
    result.response = res
    logger.info(f"单个用户结果：{result.response.text}")
    return result
