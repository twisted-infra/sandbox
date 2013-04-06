#!/bin/bash

PYTHON=~pypy/bin/pypy
TWISTD=~pypy/bin/twistd
export PYTHONPATH=Projects/frack/trunk/:Projects/Divmod/trunk/Combinator/:Projects/twisted-trac-integration/port-diffresource-to-frack/diffresource/

eval `$PYTHON ~/Projects/Divmod/trunk/Combinator/environment.py -d ~/DiffResource -p ~/DiffResource/combinator_paths`
$TWISTD web --personal --resource-script Projects/twisted-trac-integration/port-diffresource-to-frack/diffresource/diffresource.rpy 
