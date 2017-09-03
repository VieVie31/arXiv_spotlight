def get_paper(request):
    f = open("template.html")
    lines = f.readlines()
    lines[1] = 'var request = "{}"; \n'.format(request)
    return ''.join(lines)

def results(fields, original_query):
    if not '~request' in fields:
        return {}
    
    request = fields['~request']
    html_paper = get_paper(request)
    return {
        "title": "Searching '{0}' on arXiv...".format(request),
        "run_args": [request],
        "html": html_paper
    }

def run(*arg, **args):
    pass

