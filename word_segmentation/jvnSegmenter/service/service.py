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
        input = data["text"]
        input = preprocess_input(input)
        open("input.txt", "w").write(input.encode("utf-8"))
        os.system("java -classpath ../JVnSegmenter/dist/JVnSegmenter.jar JVnSegmenter.JVnSegmenter -modeldir ../JVnSegmenter/models -inputfile input.txt; mv input.txt.wseg output.txt")
        result = open("output.txt", "r").read()
        result = postprocess_output(result)
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
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8081})
    cherrypy.quickstart(DataView(), '/tokenize/', conf)
