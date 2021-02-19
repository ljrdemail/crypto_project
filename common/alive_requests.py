import os
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError


__author__ = "Pan Xianmin"


# 基于长连接的、进程安全的requests
class AliveRequests:

    # 会话池
    session_pool = {}

    def __enter__(self):
        self.session()
        return self

    def __exit__(self, *excinfo):
        pass

    @staticmethod
    def session():
        cur_pid = os.getpid()
        if cur_pid not in AliveRequests.session_pool.keys():
            session = requests.session()
            session.mount('http://', HTTPAdapter(pool_maxsize=1000, pool_block=True))
            AliveRequests.session_pool[cur_pid] = session
        return AliveRequests.session_pool[cur_pid]

    @staticmethod
    def request(
            method=None,
            url=None,
            headers=None,
            files=None,
            data=None,
            params=None,
            auth=None,
            cookies=None,
            hooks=None,
            json=None,
            timeout=None):
        session = AliveRequests.session()
        request = requests.Request(method, url, headers, files, data, params, auth, cookies, hooks, json)
        while True:
            try:
                with session.send(session.prepare_request(request), timeout=(30, timeout)) as response:
                    return response
            except ConnectionError as err:
                if "BadStatusLine" in str(err) or "reset by peer" in str(err):
                    continue
                else:
                    raise err
            except Exception as ex:
                raise ex