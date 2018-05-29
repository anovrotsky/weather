from wsgiref.simple_server import make_server
import get_weather as gw


def get_client_address(environ):
    try:
        return environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()
    except KeyError:
        return environ['REMOTE_ADDR']


def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    client_ip = get_client_address(environ)
    city_name = gw.get_city_name(client_ip)
    answer = "Current temperature is %s degrees Celsius in %s" % (gw.get_weather_in_city(city_name), city_name)
    return [answer.encode()]


with make_server('', 8080, simple_app) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()
