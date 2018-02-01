#!/usr/bin/env python
"""
This module establishes the connection to the specified plex server. The
returned object is then used by other modules and functions to find the desired
media.
"""
from plexapi.myplex import MyPlexAccount

def connect_to_plex(username, password, server):
    """
    Takes the plex username, password and server name in order to
    establish a connection and retrieve data.
    """
    account = MyPlexAccount(username, password)
    my_plex = account.resource(server).connect()
    return my_plex
