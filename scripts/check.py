"""Check generated content, unique entries, and repository-local links offline."""
import json
import re
from pathlib import Path
from urllib.parse import unquote
from render import ROOT, CATEGORIES, render

projects=json.loads((ROOT/'data/projects.json').read_text())
assert len({p['full_name'].lower() for p in projects}) == len(projects), 'Duplicate project'
for p in projects:
    assert p['category'] in {c[0] for c in CATEGORIES}, p['full_name']
    for field in ['summary_en','summary_zh','evidence_url','default_branch_commit_at','commit_url','checked_on','language_checked_on']:
        assert p.get(field), (p['full_name'],field)
    assert 'language' in p and (p['language'] is None or isinstance(p['language'], str) and p['language'].strip()), p['full_name']
    assert p['html_url']=='https://github.com/'+p['full_name']
    assert isinstance(p['stargazers_count'],int) and p['stargazers_count']>=0
    assert p['default_branch_commit_at'][:10]<=p['checked_on'], 'Future commit'
for name,content in render().items():
    assert (ROOT/name).read_text()==content, f'Regenerate {name}: python3 scripts/render.py'
for f in ROOT.rglob('*.md'):
    if '.git' in f.parts: continue
    for link in re.findall(r'\]\(([^\s)]+)\)',f.read_text()):
        if '://' in link or link.startswith(('mailto:','#')): continue
        target=unquote(link.split('#')[0])
        assert (f.parent/target).exists(), f'Broken local link in {f}: {link}'
for name in ['README.md','README.zh-CN.md']:
    content=(ROOT/name).read_text()
    for anchor in re.findall(r'\]\(#([^\)]+)\)',content):
        assert f'id="{anchor}"' in content, (name,anchor)
print(f'OK: {len(projects)} unique projects; bilingual output, audit, anchors, and local links verified.')
