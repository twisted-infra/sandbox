#!/bin/bash
cd ~commit-bot/Projects/twisted-trac-integration/branches/local-config/commit-bot
/srv/pypy/bin/pypy /usr/bin/twistd -y commit_bot.tac

