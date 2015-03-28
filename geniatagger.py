#!/usr/bin/env python

from __future__ import print_function
import subprocess
import os.path
import fcntl


def _convert_result_to_tuple(result):
    result = result.decode('utf-8').split('\n')
    result = tuple(tuple(line.split('\t')) for line in result)
    return result


def _parse_wrapper(tagger):
    def __wrapper(self, text, raw=False):
        text = text.strip()
        if not text:
            return b'' if raw else ''
        if '\n' in text:
            raise Exception('newline in input')

        result = tagger(self, text)

        if raw:
            return result.strip()
        else:
            return _convert_result_to_tuple(result)
    return __wrapper


class GeniaTagger:

    @staticmethod
    def set_nonblock_read(output):
        fd = output.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    def __init__(self, path_to_tagger, arguments=[]):
        self._path_to_tagger = path_to_tagger
        self._dir_to_tagger = os.path.dirname(path_to_tagger)
        self._tagger = subprocess.Popen(['./' + os.path.basename(path_to_tagger)] + arguments,
                                        cwd=self._dir_to_tagger,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE)
        GeniaTagger.set_nonblock_read(self._tagger.stdout)

    @_parse_wrapper
    def parse(self, text):
        self._tagger.stdin.write((text + '\n').encode('utf-8'))
        self._tagger.stdin.flush()

        while True:
            try:
                result = self._tagger.stdout.read()
            except:
                continue
            if result and result[-2:] == b'\n\n':
                break
        return result.strip()


import socket

END_SEQUENCE = b'\nEND\n'


class GeniaTaggerClient:

    def __init__(self, address='localhost',  port=9595):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((address, port))

    @_parse_wrapper
    def parse(self, text):
        self._sock.sendall((text + "\n").encode('utf-8'))

        received = self._sock.recv(8192)

        if not END_SEQUENCE in received:
            raise Exception('no END_SEQUENCE in received data')

        received = received.rsplit(END_SEQUENCE, 1)[0]
        return received

    def __del__(self):
        self._sock.close()
