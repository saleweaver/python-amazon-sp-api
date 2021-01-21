from __future__ import print_function
import os
import datetime
import hashlib
import hmac
import logging
import urllib.parse
from collections import OrderedDict
from requests.auth import AuthBase
from requests.compat import urlencode, quote, urlparse

__version__ = '0.4'

log = logging.getLogger(__name__)


def sign_msg(key, msg):
    ''' Sign message using key '''
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()


class AWSSigV4(AuthBase):

    def __init__(self, service, **kwargs):
        ''' Create authentication mechanism

        :param service: AWS Service identifier, for example `ec2`.  This is required.
        :param region:  AWS Region, for example `us-east-1`.  If not provided, it will be set using
            the environment variables `AWS_DEFAULT_REGION` or using boto3, if available.
        :param session: If boto3 is available, will attempt to get credentials using boto3,
            unless passed explicitly.  If using boto3, the provided session will be used or a new
            session will be created.

        '''
        # Set Service
        self.service = service

        # First, get credentials passed explicitly
        self.aws_access_key_id = kwargs.get('aws_access_key_id')
        self.aws_secret_access_key = kwargs.get('aws_secret_access_key')
        self.aws_session_token = kwargs.get('aws_session_token')
        # Next, try environment variables or use boto3

        # Last, fail if still not found
        if self.aws_access_key_id is None or self.aws_secret_access_key is None:
            raise KeyError("AWS Access Key ID and Secret Access Key are required")

        # Get Region passed explicitly
        self.region = kwargs.get('region')
        # Next, try environment variables or use boto3
        if self.region is None:
            self.region = os.environ.get('SP_AWS_REGION', 'us-east-1')

    def __call__(self, r):
        ''' Called to add authentication information to request

        :param r: `requests.models.PreparedRequest` object to modify

        :returns: `requests.models.PreparedRequest`, modified to add authentication

        '''
        # Create a date for headers and the credential string
        t = datetime.datetime.utcnow()
        self.amzdate = t.strftime('%Y%m%dT%H%M%SZ')
        self.datestamp = t.strftime('%Y%m%d')
        log.debug("Starting authentication with amzdate=%s", self.amzdate)

        # Parse request to get URL parts
        p = urlparse(r.url)

        host = p.hostname
        uri = urllib.parse.quote(p.path)

        if len(p.query) > 0:
            qs = dict(map(lambda i: i.split('='), p.query.split('&')))
        else:
            qs = dict()

        canonical_querystring = "&".join(map(lambda x: '='.join(x), sorted(qs.items())))
        headers_to_sign = {'host': host, 'x-amz-date': self.amzdate}
        if self.aws_session_token is not None:
            headers_to_sign['x-amz-security-token'] = self.aws_session_token

        ordered_headers = OrderedDict(sorted(headers_to_sign.items(), key=lambda t: t[0]))
        canonical_headers = ''.join(map(lambda h: ":".join(h) + '\n', ordered_headers.items()))
        signed_headers = ';'.join(ordered_headers.keys())

        if r.method == 'GET':
            payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()
        else:
            if r.body:
                payload_hash = hashlib.sha256(r.body.encode('utf-8')).hexdigest()
            else:
                payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()

        canonical_request = '\n'.join([r.method, uri, canonical_querystring,
                                       canonical_headers, signed_headers, payload_hash])

        credential_scope = '/'.join([self.datestamp, self.region, self.service, 'aws4_request'])
        string_to_sign = '\n'.join(['AWS4-HMAC-SHA256', self.amzdate,
                                    credential_scope, hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()])
        log.debug("String-to-Sign: '%s'", string_to_sign)

        kDate = sign_msg(('AWS4' + self.aws_secret_access_key).encode('utf-8'), self.datestamp)
        kRegion = sign_msg(kDate, self.region)
        kService = sign_msg(kRegion, self.service)
        kSigning = sign_msg(kService, 'aws4_request')
        signature = hmac.new(kSigning, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = "AWS4-HMAC-SHA256 Credential={}/{}, SignedHeaders={}, Signature={}".format(
            self.aws_access_key_id, credential_scope, signed_headers, signature)
        r.headers.update({
            'host': host,
            'x-amz-date': self.amzdate,
            'Authorization': authorization_header,
            'x-amz-security-token': self.aws_session_token
        })
        return r

