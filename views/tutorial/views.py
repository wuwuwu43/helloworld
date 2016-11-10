from pyramid.response import Response
from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home')
def home(request):
    #this view has a hyperlink--hello which can link to another view whose url is 127.0.0.1:6543/howdy
    #in this case , the url is in the same WSIG server so ip and port can be omitted , the view points to hello veiw
    return Response('<body>Visit <a href="/howdy">hello</a></body>')


# /howdy
@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')