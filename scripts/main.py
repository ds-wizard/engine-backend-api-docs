import pathlib
import subprocess

from templates import INDEX_TEMPLATE
from versions import compute_diff_versions, get_versions


DIFFS_DIRNAME = 'changelogs'
SPECS_DIRNAME = 'specs'
ENCODING = 'utf-8'
ROOT_DIR = pathlib.Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / 'output'
DIFFS_DIR = OUTPUT_DIR / DIFFS_DIRNAME
SPECS_DIR = ROOT_DIR / SPECS_DIRNAME
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
                        '<title>Changelog</title>',
                        f'<title>Wizard API Changelog | {old_version} ➔ {new_version}</title>'
                    )
                    .replace(
                        '<link rel="stylesheet" href="http://deepoove.com/swagger-diff/stylesheets/demo.css">',
                        '<link rel="stylesheet" href="../assets/style.diff.css">'
                        '<link rel="shortcut icon" href="../assets/favicon.ico">'
                        '<script src="../assets/custom.js"></script>'
                    )
                    .replace(
                        '<header><h1>Changelog</h1></header>',
                        f'<header><h1>'
                        f'<img class="logo" src="../assets/logo.svg"></img>'
                        f'<div>| API Changelog ({old_version} ➔ {new_version})</div>'
                        f'<div class="back-link"><a href="/">&#128281;</a></div>'
                        f'</h1></header>'
                    )
                )
    in_file.unlink()


def create_api_docs_html(versions):
    api_docs_rows = []
    for (major, minor, patch) in reversed(versions):
        api_docs_rows.append(f'<tr>'
                             f'<td scope="row">{major}.{minor}.{patch}</td>'
                             f'<td><a href="/swagger-ui/index.html?spec=/specs/{major}.{minor}.{patch}.json" target="_blank">Swagger UI</a></td>'
                             f'<td><a href="./{SPECS_DIRNAME}/{major}.{minor}.{patch}.json" target="_blank">swagger.json</a></td>'
                             f'</tr>')
    return '\n'.join(api_docs_rows)


def create_changes_html(diff_versions):
    changes_rows = []
    for (old_version, new_version) in reversed(diff_versions):
        changes_rows.append(f'<tr>'
                            f'<td>{old_version}</td>'
                            f'<td>{new_version}</td>'
                            f'<td><a href="./{DIFFS_DIRNAME}/{old_version}-{new_version}.html">View Changes</a></td>'
                            f'</tr>')
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
