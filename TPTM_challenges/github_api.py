# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:31:09 2019

@author: grant
"""

import os
from github import Github

githoj = github.Github()

calls_left, allowed = githoj.rate_limiting

print(calls_left)

mystuff = githoj.get_user('grant-king')
repos = mystuff.get_repos()

_ = [print(f'{repo.name} ') for repo in repos]

[]