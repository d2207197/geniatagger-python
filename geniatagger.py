#!/usr/bin/env python

from __future__ import print_function
import argparse
import subprocess
import os.path


import fcntl


class GeniaTagger(object):

    """
    """
    @staticmethod
    def set_nonblock_read(output):
        fd = output.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    @staticmethod
    def convert_result(result):
        result = result.decode('utf-8').split('\n')[:-2]
        result = tuple(tuple(line.split('\t'))for line in result)
        return result

    def __init__(self, path_to_tagger):
        """

        Arguments:
        - `path_to_tagger`:
        """
        self._path_to_tagger = path_to_tagger
        self._dir_to_tagger = os.path.dirname(path_to_tagger)
        self._tagger = subprocess.Popen('./' + os.path.basename(path_to_tagger),
                                        cwd=self._dir_to_tagger,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE)
        GeniaTagger.set_nonblock_read(self._tagger.stdout)

    def parse(self, text):
        """
        Arguments:
        - `self`:
        - `text`:
        """

        if '\n' in text:
            raise Exception('newline in input')
        self._tagger.stdin.write((text + '\n').encode('utf-8'))
        self._tagger.stdin.flush()

        while True:
            try:
                result = self._tagger.stdout.read()
            except:
                continue
            if result:
                break

        return GeniaTagger.convert_result(result)


def _main():
    parser = argparse.ArgumentParser(description="GeniaTagger python binding")
    parser.add_argument('input_text')
    parser.add_argument('--tagger', help='Path to geniatagger', default='./geniatagger')
    options = parser.parse_args()

    tagger = GeniaTagger(options.tagger)
    print((tagger.parse(options.input_text)))

    pass


if __name__ == '__main__':
    _main()
