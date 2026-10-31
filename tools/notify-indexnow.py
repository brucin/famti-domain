"""Notify participating search engines after the public site has been updated.

The ownership proof is intentionally served as a public text file. It is not a
GitHub credential. Its location scopes submissions to this project directory.
"""
from pathlib import Path
import json
import re
import urllib.request

root = Path(__file__).resolve().parents[1]
proofs = [p for p in root.glob('*.txt') if re.fullmatch(r'[a-f0-9]{32}', p.stem)]
assert len(proofs) == 1, 'Expected one project-scoped ownership proof'
proof = proofs[0]
key = proof.read_text().strip()
assert key == proof.stem
url = 'https://brucin.github.io/famti-domain/'
location = url + proof.name
with urllib.request.urlopen(location, timeout=30) as response:
    assert response.status == 200 and response.read().decode().strip() == key
payload = {'host': 'brucin.github.io', 'key': key, 'keyLocation': location, 'urlList': [url]}
endpoint = 'https://api.indexnow.org/indexnow'
request = urllib.request.Request(endpoint, data=json.dumps(payload).encode(), method='POST',
    headers={'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Famti-SEO-Publisher'})
with urllib.request.urlopen(request, timeout=30) as response:
    assert response.status in (200, 202)
    print(json.dumps({'endpoint': endpoint, 'http_status': response.status, 'url': url,
        'result': 'URL received; key validation pending' if response.status == 202 else 'URL submitted successfully',
        'note': 'Submission does not guarantee indexing or ranking.'}, indent=2))
