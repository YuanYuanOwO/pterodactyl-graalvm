"""Check the updater dependencies of every yolk: python3 scripts/test-yolks.py."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
dockerfiles = sorted(root.glob('*/*/Dockerfile'))
required = {'bash', 'coreutils', 'curl', 'jq', 'sed', 'unzip'}
for dockerfile in dockerfiles:
    source = dockerfile.read_text()
    packages = set(re.search(r'apt-get install\s+(.+?)(?:&&|\n\s*RUN)', source, re.S)[1]
                   .replace('\\\n', ' ').split())
    assert required <= packages, f'{dockerfile.relative_to(root)} lacks {sorted(required - packages)}'
    assert 'USER' in source and 'container' in source
template = (root / 'CORRETTO/Dockerfile.template').read_text()
for dockerfile in root.glob('CORRETTO/*/Dockerfile'):
    assert dockerfile.read_text() == template.replace('@@JAVA_VERSION@@', dockerfile.parent.name)
workflow = (root / '.github/workflows/docker-image.yml').read_text()
assert workflow.count('no-cache: true') == 2, 'Both image builds must refresh downloaded Java releases'
assert workflow.count('pull: true') == 2, 'Both image builds must refresh base images'
assert workflow.count('run: bash scripts/smoke-test-image.sh') == 2, 'Every image must run its runtime checks'
print(f'PASS: dependencies, unprivileged user and generation for {len(dockerfiles)} yolks; CI refresh/check gates')
