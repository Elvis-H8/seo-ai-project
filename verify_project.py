#!/usr/bin/env python3
"""Offline, read-only verification of this export. No account or network access."""
from pathlib import Path, PurePosixPath
import json, hashlib, re, urllib.parse
P=Path(__file__).resolve().parent
errors=[]
def local_path(rel):
 q=PurePosixPath(rel)
 if q.is_absolute() or '..' in q.parts:raise ValueError('unsafe manifest path')
 t=(P/rel).resolve()
 if not t.is_relative_to(P):raise ValueError('out of project')
 return t
M=json.loads((P/'manifest.json').read_text())
for r in M['files']:
 try:
  f=local_path(r['path'])
  if not f.is_file() or f.is_symlink():errors.append('missing or symlink: '+r['path']);continue
  if f.stat().st_size!=r['bytes'] or hashlib.sha256(f.read_bytes()).hexdigest()!=r['sha256']:errors.append('checksum: '+r['path'])
 except ValueError:errors.append('unsafe manifest path')
skip_parts={'.git','__pycache__'}
actual={str(f.relative_to(P)) for f in P.rglob('*') if f.is_file() and skip_parts.isdisjoint(f.relative_to(P).parts)}
expected={r['path'] for r in M['files']}|{'manifest.json'}
if actual!=expected:errors.append('unexpected/missing package files')
rows=[json.loads(l) for l in (P/'01_KNOWLEDGE/SOURCES.jsonl').read_text().splitlines()]
ids=[r['document_id'] for r in rows]
if len(ids)!=len(set(ids)):errors.append('duplicate source IDs')
disk={p.stem for p in (P/'01_KNOWLEDGE/summaries').glob('*.md')}
if disk!=set(ids):errors.append('summary/source mapping')
for r in rows:
 if not local_path(r['summary_path']).is_file():errors.append('missing summary')
for f in P.rglob('*.md'):
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()):
  if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',target) or target.startswith('#'):continue
  q=urllib.parse.urlsplit(target);t=(f.parent/urllib.parse.unquote(q.path)).resolve()
  if not t.is_relative_to(P) or not t.exists():errors.append('bad link: '+str(f.relative_to(P)))
a=json.loads((P/'04_GAPS_AND_AUDIT/coverage_audit.json').read_text())
if a['unique_document_ids']!=len(ids) or sum(a['status_counts'].values())!=len(ids):errors.append('coverage count')
print(json.dumps({'ok':not errors,'files':len(actual),'summaries':len(disk),'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
