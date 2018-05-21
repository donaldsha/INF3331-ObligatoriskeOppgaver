# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:56:46 2017

@author: Donalds
"""
import re

def find_emails(text):
    email_regex = r'([\\da-zA-Z.#$%&~_’*\\+\\-\\/=?‘|{}]*?)\\@([\\da-zA-Z.#$%&~_’*\\+\\-\\/=?‘|{}]*)(?<=\\.[a-zA-Z])([a-zA-Z0-9])*(?=[a-zA-Z])[a-zA-Z]';

    email_match = re.compile(email_regex)
    find_mail = re.finditer(email_match, text)
    result = []
    for email in find_mail:
        result.append(email.group(0))

    return result


def find_hyperlinks(text):#find_urls
    url_regex = r'<a href=(\"|\')((http(s)?)?://(?:www)(?:\.)[a-zA-Z0-9\.\-\~]+\.[a-zA-Z0-9\.\-\~]+\/[a-zA-Z0-9\/.-~]*)\1>.*<\/a>';

    match_url = re.compile(url_regex)
    find_url = re.finditer(match_url, text)
    result = []
    for url in find_url:
        result.append(url.group(2))

    return result
