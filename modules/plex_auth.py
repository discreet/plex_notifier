#!/usr/bin/env python

from plexapi.myplex import MyPlexAccount

def connect_to_plex(username, password, server):
    account = MyPlexAccount(username, password)
    my_plex = account.resource(server).connect()
    return my_plex

