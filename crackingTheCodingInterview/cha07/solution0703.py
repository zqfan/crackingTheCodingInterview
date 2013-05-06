#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""Design a musical juke box using object oriented principles."""

import time
import threading


class CD(object):
    def __init__(self, songs):
        self.songs = songs


class Song(object):
    def __init__(self, name, artist, albulm, length):
        self.name = name
        self.artist = artist
        self.albulm = albulm
        self.length = length


class SongPlayer(threading.Thread):
    def __init__(self):
        super(SongPlayer, self).__init__()
        self.daemon = True
        self.song = None
        self.pos = 0

    def run(self):
        # move to song's pos
        start = self.pos
        # play this song
        for i in range(start, self.song.length):
            time.sleep(1)
            self.pos += 1


class CDPlayer(object):
    def __init__(self):
        self.is_playing = False
        self.playing_song = None
        self.play_time = 0
        self.song_player = SongPlayer()
        self.cd = None

    def insert_cd(self, cd):
        self.cd = cd

    def play(self):
        if not self.cd:
            return
        self.is_playing = True
        if not self.playing_song:
            self.playing_song = self.cd.songs[0]
        # play this song
        self.song_player.song = self.playsing_song
        self.song_player.pos = self.play_time
        self.song_player.start()

    def pause(self):
        self.is_playing = False
        self.song_player.stop()
        self.play_time = self.song_player.pos

    def play_next(self):
        if not self.cd:
            return
        if not self.playing_song:
            index = 0
        else:
            index = self.cd.songs.index(self.playing_song) + 1
        self.song_player.stop()
        self.song_player.pos = 0
        self.song_player.song = self.cd.songs[index]
        self.song_player.start()
