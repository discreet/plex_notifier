#!/usr/bin/env python3

from plexapi.myplex import MyPlexAccount

def connect_to_plex(username, password, server):
    account = MyPlexAccount(username, password)
    return account.resource(server).connect()

