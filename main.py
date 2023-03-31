import os
import subprocess

from templates import indexTemplate
from versions import compute_diff_versions, get_versions


def create_diff(old_version, new_version):
    with open(f'./output/diffs/{old_version}-{new_version}-original.html', encoding="utf-8", mode='w+') as f:
        subprocess.call(["java",
                         "-jar", "./bin/swagger-diff.jar",
                         "-old", f'./specifications/{old_version}.json',
                         "-new", f'./specifications/{new_version}.json',
                         "-v", "2.0",
                         "-output-mode", "html"],
                        stdout=f)
    print(f'✅ {old_version} -> {new_version}')


def adjust_styles(old_version, new_version):
    with open(f'./output/diffs/{old_version}-{new_version}-original.html', encoding="utf-8", mode='rt') as f_in:
        with open(f'./output/diffs/{old_version}-{new_version}.html', encoding="utf-8", mode='wt') as f_out:
            for line in f_in:
                f_out.write(
                    line
                    .replace('<header><h1>Changelog</h1></header>',
                             '<header style="background: #f4f4f4; color: #4D4948;"><h1 style="display: flex; align-items: center; margin: auto; max-width: 960px;"><img class="logo" src="../assets/dsw-logo-horizontal-color-transparent.svg" style="height: 30px; margin-right: 10px;"></img>| API Changelog</h1></header>'
                             )
                    .replace('<body>',
                             '<body style="font-family: Open-Sans, sans-serif">'
                             )
                    .replace('<ol id="new">',
                             '<ol id="new" style="font-family: monospace">'
                             )
                    .replace('<ol id="deprecated">',
                             '<ol id="deprecated" style="font-family: monospace">'
                             )
                    .replace('<ol id="changed">',
                             '<ol id="changed" style="font-family: monospace">'
                             )
                )
    os.remove(f'./output/diffs/{old_version}-{new_version}-original.html')


def create_api_docs_html(versions):
    api_docs_rows = ""
    for (major, minor, patch) in reversed(versions):
        api_docs_rows += f'<tr><td scope="row">{major}.{minor}.{patch}</td><td><a href="specifications/{major}.{minor}.{patch}.json">swagger.json</a></td></tr>'
    return api_docs_rows


def create_changes_html(diff_versions):
    changes_rows = ""
    for (old_version, new_version) in reversed(diff_versions):
        changes_rows += f'<tr><td>{old_version}</td><td>{new_version}</td><td><a href="diffs/{old_version}-{new_version}.html">View Changes</a></td></tr>'
    return changes_rows


def create_index_html(versions, diff_versions):
    api_docs_rows = create_api_docs_html(versions)
    changes_rows = create_changes_html(diff_versions)

    with open('./output/index.html', encoding='utf-8', mode='w+') as f:
        f.write(indexTemplate.substitute({
            'apiDocsRows': api_docs_rows,
            'changesRows': changes_rows
        }))


if __name__ == '__main__':
    versions = get_versions()
    diff_versions = compute_diff_versions(versions)
    # for (old_version, new_version) in diff_versions:
    #     create_diff(old_version, new_version)
    #     adjust_styles(old_version, new_version)
    create_index_html(versions, diff_versions)
