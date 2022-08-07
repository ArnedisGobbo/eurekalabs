import requests_cache
import posixpath


class RestClient:
    def __init__(self, server_url, timeout):
        self.timeout = timeout
        self.server_url = server_url
        self.session = requests_cache.CachedSession('./db/demo_cache')

    def build_url(self, query_path):
        return posixpath.join(self.server_url, query_path)

    def post_request(self, query_path, data=None, json=None, params=None, files=None, headers=None):
        url = self.build_url(query_path)
        return self.session.post(url, data=data, json=json, params=params, files=files, headers=headers,
                                 timeout=self.timeout)

    def patch_request(self, query_path, data=None, params=None):
        url = self.build_url(query_path)
        return self.session.patch(url, data=data, params=params, timeout=self.timeout)

    def get_request(self, query_path, params=None):
        url = self.build_url(query_path)
        return self.session.get(url, params=params, timeout=self.timeout)

    def put_request(self, query_path, data=None, params=None, files=None, headers=None):
        url = self.build_url(query_path)
        return self.session.put(url, data=data, params=params, files=files, headers=headers,
                                timeout=self.timeout)

    def delete_request(self, query_path, json=None):
        url = self.build_url(query_path)
        return self.session.delete(url, json=json, params=None, timeout=self.timeout)
