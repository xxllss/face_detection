#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
import json
import re


def face_detection(environ, start_response):
    from face_detection import FaceDetection
    face = FaceDetection()
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status,headers)

    params = environ['params']
    image = params.get('image')

    try:
        faces = face.face_detection(image)
        if isinstance(faces,numpy.ndarray):
            data = faces.tolist()
            return [json.dumps(dict(status = 0,data = data)).encode('utf-8')]
        else:
            return ['{"status":0,"data":[]}'.encode('utf-8')]
    except Exception as error:
        res = '{"status":-1,"data":"%s"}' %(str(error))
        return [res.encode('utf-8')]
    
def root(environ, response):
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    status = '200 OK'
    response(status,headers)
    respose = '{"status":0,"data":"请指定uri"}'
    return [respose.encode('utf-8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    from resty import PathDispatcher

    d = PathDispatcher()
    d.register('GET', '/face_detection', face_detection)
    d.register('GET', '/',root)

    # 指定服务器端口
    port = 8080
    httpd = make_server('', port, d)
    print('Serving on port {0}...'.format(port))
    httpd.serve_forever()

