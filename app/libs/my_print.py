class MyPrint(object):

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(func):
            self.mound.append((func, rule, options))
            return func

        return decorator

    def register(self, blueprint, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for func, rule, options in self.mound:
            endpoint = options.pop("endpoints", func.__name__)
            blueprint.add_url_rule(url_prefix + rule, endpoint, func, **options)
