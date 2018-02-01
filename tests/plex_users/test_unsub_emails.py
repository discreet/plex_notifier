#!/usr/bin/env python

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')

from plex_notifier import plex_users

def test_unsub_emails():
    test_list = ['foo', 'bar', 'baz', 'bip', 'bop']
    test_unsub_list1 = 'bar, baz'
    test_unsub_list2 = 'bar,baz'
    returned_list1 = plex_users.unsub_emails(test_unsub_list1, test_list)
    returned_list2 = plex_users.unsub_emails(test_unsub_list2, test_list)

    assert type(returned_list1) is list
    assert type(returned_list2) is list
    assert 'bar' not in returned_list1 or 'bar' not in  returned_list2
    assert 'baz' not in returned_list1 or 'bar' not in returned_list2
    assert 'foo' in returned_list1 or 'bar' in returned_list2
    assert 'bip' in returned_list1 or 'bar' in returned_list2
    assert 'bop' in returned_list1 or 'bar' in returned_list2
