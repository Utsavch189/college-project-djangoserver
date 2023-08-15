from core.middleware.validation.validate_factory import Factory


class ValidateMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        ob=Factory().middleware(request=request)
        if ob:
            ob.validates(request=request)
        response = self.get_response(request)
        return response