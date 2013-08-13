# -*- coding: utf-8 -*-
#
# Copyright 2012 Zhang ZY<http://idupx.blogspot.com/> 
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

'''
@feature: Config Options
'''

import sys
import os

from tornado.options import define, options

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.realpath(os.path.join(CURRENT_PATH, '..', '..'))

DEFAULT_OPTIONS_LOG_ROOT_PATH     = \
    os.path.realpath(os.path.join(PROJECT_PATH, 'log'))

define("log_level", default = 'DEBUG', 
        help = "Set Log Level")

define('log_root_path', default = DEFAULT_OPTIONS_LOG_ROOT_PATH, 
        help = 'Log file stored root path')

define('log_path',
        help = 'Log file stored path')

define('project_path', default =
        os.path.realpath(os.path.join(os.path.realpath(__file__),'..', '..', '..')),
        help = 'Set the Project Path')

define('cfg_file', default = os.path.join(options.project_path, 'etc',
        'mownfish.conf'),
        help = 'set the config file path')

define("bind_ip", default = '0.0.0.0',
        help = "Run server on a specific IP")

define("port", type = int, 
        help = 'Run server on a specific port')

define("env", default="dev", help="service run environment")
    
def _usage():
    print 'Usage: bin/mownfish -log_root_path=SpecifiedFile -port=SpecifiedPort'
    sys.exit()
    pass

def _check_dir_tail(dir_name):
    if not dir_name or '' == dir_name:
        return dir_name
    _len = len(dir_name) - 1
    if '/' == dir_name[_len:]:
        dir_name = dir_name[0:_len]

    return dir_name
    pass

def _mkdir(file_dir):
    real_path = os.path.realpath(file_dir)
    if not os.path.exists(real_path):
        os.makedirs(real_path)
        pass
    pass

def init_options():
    # maybe some options will be use before load config file
    options.parse_command_line()
    options.parse_config_file(options.cfg_file)
    if not options.log_root_path or not options.port:
        options.print_help()
        _usage()
    options.log_root_path = _check_dir_tail(options.log_root_path)
    options.log_path = '%s/%d' % (options.log_root_path, options.port)
    _mkdir(options.log_path)

