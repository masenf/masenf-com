# generate.py -- assemble the pieces
import os

TEMPLATE_DIR = "template"
OUTPUT_DIR = "output"

class WebComponent(object):
    _pages = {}
    _current = {}
    _templates = {}
    _generate = []

class Generator(WebComponent):
    def _scan(self, container, scan_dir, store_content=False):
        """Scan scan a folder and collect metadata"""
        for filename in os.listdir(scan_dir):
            # read the metadata
            if filename.startswith('.'):
                continue
            path = os.path.join(scan_dir,filename)
            with open(path,'r') as f:
                content = f.read()
            file_info = {}
            if store_content:
                file_info['content'] = content
            file_info['name'] = filename
            file_info['relpath'] = path
            file_info['metadata'] = {}
            # pick out the metadata directives
            metadata = filter(lambda x: x.startswith(":"), content.split("\n"))
            for md in metadata:
                mds = md.split(' ')
                mds[0] = mds[0].strip(':')
                if mds[0] == 'generate':
                    WebComponent._generate.append((mds[1],mds[2],filename))
                if mds[0] not in file_info['metadata']:
                    file_info['metadata'][mds[0]] = []
                file_info['metadata'][mds[0]].append(mds[1:])
            container[filename] = file_info
    def ScanTemplates(self):
        self._scan(WebComponent._templates, TEMPLATE_DIR, store_content=True)
    def ScanContent(self):
        for gen in WebComponent._generate:
            WebComponent._pages[gen[0]] = {}
            self._scan(WebComponent._pages[gen[0]], gen[0])
