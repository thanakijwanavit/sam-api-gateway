from awsSchema.apigateway import Response, Event

def add(event, *args):
    return Response.getReturn(body = {'method':'add'})
def get(event, *args):
    return Response.getReturn(body = {'method':'get'})
def remove(event, *args):
    return Response.getReturn(body = {'method':'remove'})
def edit(event, *args):
    return Response.getReturn(body = {'method':'edit'})