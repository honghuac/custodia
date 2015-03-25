# Copyright (C) 2015  Custodia Project Contributors - see LICENSE file


class CSStoreError(Exception):
    pass


class CSStore(object):

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def list(self, keyfilter=None):
        raise NotImplementedError
