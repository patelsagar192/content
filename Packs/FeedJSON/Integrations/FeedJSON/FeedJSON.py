import demistomock as demisto
from CommonServerPython import *

from JSONFeedApiModule import *  # noqa: E402


def main():
    params = {k: v for k, v in demisto.params().items() if v is not None}

    params['feed_name_to_config'] = {
        params.get('indicator_type'): {
            'url': params.get('url'),
            'extractor': "prefixes[]",
            'indicator': 'ip_prefix',
            'indicator_type': params.get('indicator_type'),
        }
    }

    feed_main(params, 'JSONFeed', 'json')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
