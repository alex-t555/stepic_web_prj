"""
WSGI приложение должно возвращать документ с MIME-типом text/plain, содержащий все GET параметры, по одному на каждую строку.

Например при запросе  /?a=1&a=2&b=3 приложение должно вернуть такой текст
    a=1
    a=2
    b=3
"""
################################################################################
def app(environ, start_response):
    """ web application """
    body = ''.join([(s + '\n') for s in environ['QUERY_STRING'].split('&')]).encode()
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, headers)
    return [body]
