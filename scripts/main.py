import pathlib
import subprocess

from templates import INDEX_TEMPLATE
from versions import compute_diff_versions, get_versions


ENCODING = 'utf-8'
ROOT_DIR = pathlib.Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / 'output'
DIFFS_DIR = OUTPUT_DIR / 'diffs'
SPECS_DIR = ROOT_DIR / 'specs'
JAR_FILE = ROOT_DIR / 'bin' / 'swagger-diff.jar'


def create_diff(old_version, new_version):
    diff_file = DIFFS_DIR / f'{old_version}-{new_version}-original.html'
    with diff_file.open(encoding=ENCODING, mode='w+') as f:
        subprocess.call(['java',
                         '-jar', JAR_FILE.as_posix(),
                         '-old', (SPECS_DIR / f'{old_version}.json').as_posix(),
                         '-new', (SPECS_DIR / f'{new_version}.json').as_posix(),
                         '-v', '2.0',
                         '-output-mode', 'html'],
                        stdout=f)
    print(f'✅ {old_version} ➔ {new_version}')


def adjust_styles(old_version, new_version):
    in_file = DIFFS_DIR / f'{old_version}-{new_version}-original.html'
    out_file = DIFFS_DIR / f'{old_version}-{new_version}.html'
    with in_file.open(encoding=ENCODING, mode='rt') as f_in:
        with out_file.open(encoding=ENCODING, mode='wt') as f_out:
            for line in f_in:
                f_out.write(
                    line
                    .replace(
                        '<header><h1>Changelog</h1></header>',
                        '<header style="background: #f4f4f4; color: #4D4948;"><h1 style="display: flex; align-items: center; margin: auto; max-width: 960px;"><img class="logo" src="../assets/dsw-logo-horizontal-color-transparent.svg" style="height: 30px; margin-right: 10px;"></img>| API Changelog</h1></header>'
                    )
                    .replace(
                        '<body>',
                        '<body style="font-family: Open-Sans, sans-serif">'
                    )
                    .replace(
                        '<ol id="new">',
                        '<ol id="new" style="font-family: monospace">'
                    )
                    .replace(
                        '<ol id="deprecated">',
                        '<ol id="deprecated" style="font-family: monospace">'
                    )
                    .replace(
                        '<ol id="changed">',
                        '<ol id="changed" style="font-family: monospace">'
                    )
                )
    in_file.unlink()


def create_api_docs_html(versions):
    api_docs_rows = []
    for (major, minor, patch) in reversed(versions):
        api_docs_rows.append(f'<tr><td scope="row">{major}.{minor}.{patch}</td><td><a href="specifications/{major}.{minor}.{patch}.json">swagger.json</a></td></tr>')
    return '\n'.join(api_docs_rows)


def create_changes_html(diff_versions):
    changes_rows = []
    for (old_version, new_version) in reversed(diff_versions):
        changes_rows.append(f'<tr><td>{old_version}</td><td>{new_version}</td><td><a href="diffs/{old_version}-{new_version}.html">View Changes</a></td></tr>')
    return '\n'.join(changes_rows)


def create_index_html(versions, diff_versions):
    api_docs_rows = create_api_docs_html(versions)
    changes_rows = create_changes_html(diff_versions)

    out_file = OUTPUT_DIR / 'index.html'
    with out_file.open(encoding=ENCODING, mode='w+') as f:
        f.write(INDEX_TEMPLATE.substitute({
            'apiDocsRows': api_docs_rows,
            'changesRows': changes_rows
        }))


if __name__ == '__main__':
    versions = get_versions(SPECS_DIR)
    diff_versions = compute_diff_versions(versions)
    for (old_version, new_version) in diff_versions:
        create_diff(old_version, new_version)
        adjust_styles(old_version, new_version)
    create_index_html(versions, diff_versions)
