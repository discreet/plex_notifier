#!/usr/bin/env python

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

import jinja2
import json
from plex_notifier import plex_email

def test_format_body():
    json_file = open('tests/plex_email/media_data.json')
    json_str = json_file.read()
    json_dict = json.loads(json_str)
    template = 'email'
    rendered = plex_email.__format_body(json_dict, template)

    for k,v in json_dict.items():
        if k == 'movies':
            for k,v in v.items():
                assert k in rendered
                assert v['Rating'] in rendered
                assert str(v['Year']) in rendered
                assert v['Release_Date'] in rendered
                assert str(v['Stars']) in rendered
                assert v['Summary'] in rendered
        elif k == 'tv':
            for k,v in v.items():
                assert k in rendered
                for k,v in v.items():
                    assert k in rendered
                    for k,v in v.items():
                        assert k in rendered
                        assert v['Air_Date'] in rendered
                        assert v['Summary'] in rendered
