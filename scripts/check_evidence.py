# SPDX-License-Identifier: MIT
"""Validate the review register and citation structure without network access."""
from pathlib import Path
import csv
import re

root = Path(__file__).resolve().parents[1]
with (root / 'evidence/studies.csv').open(newline='', encoding='utf-8') as stream:
    rows = list(csv.DictReader(stream))
ids = [row['study_id'] for row in rows]

def require(condition, message):
    if not condition:
        raise ValueError(message)

require(bool(rows) and len(ids) == len(set(ids)), 'Missing or duplicate study IDs')
required = ['study_id', 'title', 'authors', 'year', 'scope', 'verification',
            'doi', 'url', 'access_level', 'primary_source', 'population',
            'design', 'outcome', 'limitation', 'locator', 'checked_on']
levels = {'full-text-sections', 'abstract-only', 'abstract-and-slides', 'metadata-only'}
by_id = {row['study_id']: row for row in rows}
dois = [row['doi'].strip().lower() for row in rows]
require(len(dois) == len(set(dois)), 'Duplicate DOI: check for duplicate publications')
for row in rows:
    sid = row['study_id']
    require(re.fullmatch(r'M\d{2}', sid) is not None, f'Invalid ID: {sid}')
    require(all(row[key].strip() for key in required), f'Missing appraisal field: {sid}')
    require(row['access_level'] in levels, f'Unknown access level: {sid}')
    require(row['url'] == 'https://doi.org/' + row['doi'], f'DOI link mismatch: {sid}')
    require(row['primary_source'].startswith('https://'), f'Invalid primary link: {sid}')
    for related in filter(None, row['related_studies'].split(';')):
        require(related in by_id and related != sid, f'Invalid related study: {sid}')
        require(sid in by_id[related]['related_studies'].split(';'),
                f'Nonreciprocal relationship: {sid}/{related}')
references = (root / 'REFERENCES.md').read_text(encoding='utf-8')
appraisals = (root / 'docs/study-appraisals.md').read_text(encoding='utf-8')
for sid in ids:
    require(f'## {sid}\n' in references, f'Missing reference: {sid}')
    require(f'## {sid} —' in appraisals, f'Missing appraisal: {sid}')
for path in root.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    for sid in re.findall(r'\bM\d{2}\b', text):
        require(sid in by_id, f'Unknown study citation: {path.name}/{sid}')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if not target.startswith(('https://', 'http://', '#')):
            require((path.parent / target.split('#')[0]).exists(),
                    f'Broken local link: {path.name}/{target}')
print(f'PASS: {len(rows)} distinct records; appraisal fields, DOI identities, related-study links and local citations resolve.')
print('This checks structure only, not scientific truth or copyright permissions.')
