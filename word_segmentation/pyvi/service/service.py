# -*- coding: utf-8 -*-
from os.path import join

import cherrypy
import json
import os

from process import preprocess_input, postprocess_output


class DataView(object):
    exposed = True

    @cherrypy.tools.accept(media='application/json')
    def POST(self):
        rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        data = json.loads(rawData)

        script_folder = join("/pyvi", "pyvi")
        input_file = join(script_folder, "input.txt")
        output_file = join(script_folder, "output.txt")

        # GET INPUT
        input = data["text"]
        open(input_file, "w").write(input.encode("utf-8"))

        # CALL ENDPOINT
        os.system("cd /pyvi/pyvi; python script.py")

        # SEND OUTPUT
        result = open(output_file, "r").read()
        return json.dumps({"result": result}, ensure_ascii=False)


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.CORS.on': True,
        }
    }
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8082})
    cherrypy.quickstart(DataView(), '/tokenize/', conf)
