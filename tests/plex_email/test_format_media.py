#!/usr/bin/env python

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from modules import plex_email

def test_format_email():
    test_list = ['foo', 'bar', 'baz']
    returned_string = plex_email.__format_media(test_list)

    assert type(returned_string) is str
    assert 'foo\n' in returned_string
    assert 'bar\n' in returned_string
    assert 'baz' in returned_string
