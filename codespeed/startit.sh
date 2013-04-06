#!/bin/bash

cd ~/Run
export PYTHONPATH=:~/.local/lib/python2.5/site-packages/:~/Twisted/:~/codespeed/
twistd -y speedcenter.tac
