import random
import logging
from scrapy.exceptions import NotConfigured
from urllib.request import _parse_proxy

<<<<<<< HEAD

logger = logging.getLogger()

=======
logger = logging.getLogger()


>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
def reform_url(url):
    proxy_type, user, password, hostport = _parse_proxy(url)
    return '%s://%s' % (proxy_type, hostport)

<<<<<<< HEAD
class RandomProxyMiddleware(object):

=======

class RandomProxyMiddleware(object):
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
    def __init__(self, settings):
        self.proxies = settings.getlist('PROXIES')
        self.max_failed = settings.getint('PROXY_MAX_FAILED', 3)
        self.stats = {}.fromkeys(map(reform_url, self.proxies), 0)

    def random_proxy(self):
        return random.choice(self.proxies)

    @classmethod
<<<<<<< HEAD
    def from_crawler(cls,crawler):
=======
    def from_crawler(cls, crawler):
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        if not crawler.settings.getlist('PROXIES'):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self, request, spider):
        if 'proxy' not in request.meta:
            request.meta['proxy'] = self.random_proxy()

    def process_response(self, request, response, spider):
        cur_proxy = request.meta['proxy']
        if response.status >= 400:
            self.stats[cur_proxy] += 1
        if self.stats[cur_proxy] >= self.max_failed:
            for proxy in self.proxies:
                if reform_url(proxy) == cur_proxy:
                    self.proxies.remove(proxy)
                    break
            logger.warning('proxy %s remove from proxies list' % cur_proxy)
        return response


<<<<<<< HEAD
=======

>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
