#!/bin/bash

Z=~t-names/Zones
export PYTHONPATH=$PYTHONPATH:$Z

cd ~t-names/Run/dns

authbind --deep /srv/pypy/bin/pypy /usr/bin/twistd dns \
    --pyzone $Z/twistedmatrix.com \
    --pyzone $Z/divunal.com \
    --pyzone $Z/intarweb.us \
    --pyzone $Z/ynchrono.us \
    --pyzone $Z/divmod.com \
    --pyzone $Z/divmod.org
