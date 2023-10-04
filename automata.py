#! python3

import pyautogui
import argparse

import miner
import fisher

FEATURES = [miner, fisher]

def global_parser() :
    parser = argparse.ArgumentParser(
            prog='automata.py',
            description='A Set of automation tools for minecraft farming in Frenchsky server')

    sub = parser.add_subparsers()
    sub.required = True
    for feature in FEATURES :
        feature.parser(sub)
    return parser

if __name__ == '__main__' :
    p = global_parser()

    args = p.parse_args()
    args.fun(args)


