from cornice import Service

hello_service = Service(
    "hello",
    path="/api/hello",
    description="Say hello")

@hello_service.get()
def get_hello(request):
    return {"data" : "hello"}
