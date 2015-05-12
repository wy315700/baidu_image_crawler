#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015-05-12 10:14
@author: Wang Yang <wy315700@gmail.com>
'''

import md5
import base64
import urllib2
import urllib
import json
import random
import os
import sys




def search_img(keyword):
    search_url = 'http://image.baidu.com/i?tn=baiduimagejson&width=&height=&word=%s&rn=100&pn=0' %(keyword)

    resp = urllib2.urlopen(search_url)
    resp_js = json.loads(resp.read().decode('gbk'))
    print resp_js
    if resp_js['data']:
        for x in resp_js['data']:
            url = x['objURL']
            try:
                print "downloading :" + url
                save_to_disk(url, keyword)
            except Exception, e:
                pass

    else:
        return None


def save_to_disk(url, folder):
    base_dir = os.path.dirname(__file__)
    folder = os.path.join(base_dir, folder)
    if not os.path.isdir(folder):
      print 'Creating ' + folder
      os.makedirs(folder)

    filename = url.split('/')[-1]
    fpath = os.path.join(folder, filename.encode('utf8'))
    if os.path.exists(fpath):
        return

    resp = urllib2.urlopen(url)
    data = resp.read()
    f = open(fpath, 'wb')
    f.write(data)
    f.close()


if __name__ == '__main__':
    keyword = raw_input('请输入关键词')
    search_img(keyword)