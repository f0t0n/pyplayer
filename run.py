#!/usr/bin/env python


from argparse import ArgumentParser
import pygame
from pygame.mixer import music as m
from pygame.mixer import init


def main(filename):
    init()
    clock = pygame.time.Clock()
    m.load(filename)
    m.play()
    while m.get_busy():
        clock.tick(30)


if __name__ == '__main__':
    parser = ArgumentParser(description='PyPlayer')
    parser.add_argument('-f', '--file',
                        default=None,
                        help='An audio file to play')
    args = parser.parse_args()

    try:
        main(args.file)
    except KeyboardInterrupt:
        print '%sBye!\n' % ('\b\b' * 2)
