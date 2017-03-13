import cherrypy
import json
import os


class DataView(object):
    exposed = True

    @cherrypy.tools.accept(media='application/json')
    def POST(self):
        rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
        data = json.loads(rawData)
        input = data["text"]
        open("input.txt", "w").write(input.encode("utf-8"))
        # call endpoint
        os.system("cd /vnTokenizer/vntokenizer/; ./vnTokenizer.sh -i ../service/input.txt -o ../service/output.txt")
        result = open("output.txt", "r").read()
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
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(DataView(), '/tokenize/', conf)
