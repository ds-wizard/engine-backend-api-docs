import pathlib


def get_versions(specs_dir: pathlib.Path):
    files = [spec.name.replace('.json', '') for spec in specs_dir.glob('*.json')]
    strings = map(lambda version: version.split('.'), files)
    versions = list(map(lambda version: (int(version[0]), int(version[1]), int(version[2])), strings))
    sorted_versions = sorted(versions)
    return sorted_versions


def compute_diff_versions(versions):
    major = 3

    minors = set()
    for (_, minor, _) in versions:
        minors.add(minor)
    minors = list(minors)

    diffs = []
    for minor in minors:
        if (minor - 1) in minors:
            diffs.append((f'{major}.{minor - 1}.0', f'{major}.{minor}.0'))

    for minor in minors:
        patches = []
        for (_, v_minor, v_patch) in versions:
            if minor == v_minor:
                patches.append(v_patch)

        for patch in patches:
            if (patch - 1) in patches:
                diffs.append((f'{major}.{minor}.{patch - 1}', f'{major}.{minor}.{patch}'))

        last_patch = patches[-1]
        if last_patch != 0 and (minor + 1) in minors:
            diffs.append((f'{major}.{minor}.{last_patch}', f'{major}.{minor + 1}.0'))

    return diffs
