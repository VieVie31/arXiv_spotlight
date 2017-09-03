import urllib
import webbrowser
import xml.etree.ElementTree as ET

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

def run(request):
    url = 'http://export.arxiv.org/api/query?search_query=all:{}&start=0&max_results=1'.format(request)
    data = urllib.urlopen(url).read()
    root = ET.fromstring(data)
    paper_url = root[7][0].text.replace('/abs/', '/pdf/') + '.pdf'
    webbrowser.open(paper_url)

