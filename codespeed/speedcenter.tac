##
# Copyright (c) 2010 Apple Inc. All rights reserved.
# Copyright (c) 2011 Twisted Matrix Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from twisted.python.modules import getModule
from twisted.application.service import Application
from twisted.application.internet import TCPServer
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from twisted.web.resource import Resource
from twisted.internet import reactor

speedcenter = getModule("speedcenter").filePath
django = speedcenter.sibling("wsgi").child("django.wsgi")
namespace = {"__file__": django.path}
execfile(django.path, namespace, namespace)

class _HostResource(Resource):

    def __init__(self, wrapped):
        Resource.__init__(self)
        self.wrapped = wrapped


    def getChild(self, path, request):
        if ':' in path:
            host, port = path.split(':', 1)
            port = int(port)
        else:
            host, port = path, 80
        request.setHost(host, port)
        prefixLen = request.uri.find(path) + len(path)
        request.path = '/'+'/'.join(request.postpath)
        request.uri = request.uri[prefixLen:]
        del request.prepath[:3]
	return self.wrapped



class VHostMonsterResource(Resource):
    def __init__(self, wrapped):
        Resource.__init__(self)
        self.wrapped = wrapped


    def getChild(self, path, request):
        if path == 'http':
            request.isSecure = lambda: 0
        elif path == 'https':
            request.isSecure = lambda: 1
        return _HostResource(self.wrapped)



application = Application("SpeedCenter")
resource = VHostMonsterResource(
    WSGIResource(reactor, reactor.getThreadPool(), namespace["application"]))
site = Site(resource, 'httpd.log')
TCPServer(8123, site, interface='127.0.0.1').setServiceParent(application)
