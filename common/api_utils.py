# -*- coding: utf-8 -*-
# __author__ = 'zhouqiang'

import requests
import time
import traceback
import json
import os
import re
import urllib3
s = requests.Session()
a = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
s.mount('http://', a)
s.verify = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certfile', 'ca.pem')


class Api:
    def __init__(self, host, uri, method, body=None, log=None, log_msg_flag=False, timeout=120, protocol='http',
                 headers=None, params=None, verify=None, files=None, data=None):
        self.host = host
        self.uri = uri
        self.method = method
        self.body = {} if body is None else body
        self.data = {} if data is None else data
        self.params = {} if params is None else params
        self.timeout = timeout
        self.protocol = protocol
        if host.split(':')[-1] == '443':
            self.protocol = 'https'
        self.headers = {} if headers is None else headers
        s.verify = s.verify if verify is None else verify
        self.files = files
        self.url = None
        self.response = None
        self.response_time = None
        self.log = log
        self.status_code = None
        if self.log is None:
            self.log_flag = False
        else:
            self.log_flag = True
        self.log_msg_flag = log_msg_flag
        self.log_msg = []

    def request(self):
        t_start = time.time()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        try:
            if not isinstance(self.body, dict):
                self.url = self.protocol + '://' + self.host + self.uri.replace('{}', str(self.body))
            elif self.body == {}:
                self.url = self.protocol + '://' + self.host + self.uri
            else:
                uri_keys = re.findall(r'{(.*?)\}', self.uri)
                for key in uri_keys:
                    if key not in self.body and '[' not in key and '.' not in key:
                        self.uri = self.uri.replace('{' + key + '}', '')
                self.url = self.protocol + '://' + self.host + self.uri.format(**self.body)
            if self.method == 'GET' or self.method == 'DELETE':
                self.response = s.request(self.method, self.url, params=self.body, timeout=self.timeout,
                                          headers=self.headers, data=self.data)
            else:
                self.response = s.request(self.method, self.url, params=self.params, json=self.body, files=self.files,
                                          timeout=self.timeout, headers=self.headers, data=self.data)
        except Exception as e:
            print(e)
            self.log_msg.append('-' * 120 + '\n' + time.ctime() + '\n' + str(traceback.format_exc()) + '\n')
            if self.log_flag:
                self.log.error('\n' + str(self.method) + ' ' + str(self.url) + '\n' + str(self.body) + '\n' +
                               str(traceback.format_exc()) + '\n' + '-' * 120)
        finally:
            try:
                self.status_code = self.response.status_code
            except:
                pass
            self.response_time = time.time() - t_start
            line_break = '\n{}\n'.format('*' * 90)
            line_break_underline = '\n{}\n'.format('~' * 90)
            line_break_underline = '\n\n'#.format('~' * 90)

            base_info = '{}Request: {}, {}{}'.format(line_break, str(self.method), str(self.url), line_break_underline)
            request_info = '{}Body: {}{}'.format(base_info, json.dumps(self.body), line_break_underline)
            if {} != self.headers:
                request_info = '{}Headers: {}{}'.format(request_info, json.dumps(self.headers), line_break_underline)

            self.log_msg.insert(0, '-' * 120 + '\n' + time.ctime() + request_info)
            if self.response is not None:
                try:
                    response_info = json.dumps(self.response.json())
                except:
                    response_info = str(self.response.content)
                response_info = 'Response: ' + str(self.response.status_code) + '  ' + \
                                str(int(self.response_time * 1000)) + \
                                'ms  \n' + response_info + '\n' + '-' * 90
                self.log_msg.append(response_info)
                if self.log_flag:
                    if self.response.status_code == 200:
                        self.log.info(request_info + response_info)
                    else:
                        self.log.error(request_info + response_info)

    def get_response(self):
        self.request()
        try:
            if self.log_msg_flag:
                m = self.response.json()
                m['log_msg'] = ''.join(self.log_msg)
                return m
            else:
                return self.response.json()
        except:
            if self.log_msg_flag:
                return {'log_msg': ''.join(self.log_msg), 'error': 'not_json'}
            else:
                return None

    def get_response_with_status_code(self):
        self.request()
        try:
            if self.log_msg_flag:
                m = self.response.json()
                m['log_msg'] = ''.join(self.log_msg)
                return self.response.status_code, round(self.response.elapsed.total_seconds() * 1000, 2), m
            else:
                return self.response.status_code, round(self.response.elapsed.total_seconds() * 1000, 2), self.response.json()
        except:
            if self.log_msg_flag:
                return 0, 0, {'log_msg': ''.join(self.log_msg), 'error': 'not_json'}
            else:
                return 0, 0, {}
