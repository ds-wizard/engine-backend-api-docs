import pathlib


def get_versions(specs_dir: pathlib.Path):
    files = [spec.name.replace('.json', '') for spec in specs_dir.glob('*.json')]
    strings = map(lambda version: version.split('.'), files)
    versions = list(map(lambda version: (int(version[0]), int(version[1]), int(version[2])), strings))
    sorted_versions = sorted(versions)
    return sorted_versions


def compute_diff_versions(versions):
    diffs = []

    for current_version in versions:
        previous_version = get_previous_version(current_version, versions)
        if previous_version is not None:
            diffs.append((
                f'{previous_version[0]}.{previous_version[1]}.{previous_version[2]}',
                f'{current_version[0]}.{current_version[1]}.{current_version[2]}'
            ))

    return diffs


def get_previous_version(current_version: (int, int, int), versions: [(int, int, int)]) -> (int, int, int):
    # 1. Define variables
    (current_major, current_minor, current_patch) = current_version
    minors = sorted([minor for (_, minor, _) in versions], reverse=True)
    patches = sorted([patch for (_, _, patch) in versions], reverse=True)

    # 2. Try decrease patch
    previous_version = (current_major, current_minor, current_patch - 1)
    if previous_version in versions:
        return previous_version

    # 3. Try decrease minor
    for patch in patches:
        previous_version = (current_major, current_minor - 1, patch)
        if previous_version in versions:
            return previous_version

    # 4. Try decrease major
    for minor in minors:
        for patch in patches:
            previous_version = (current_major - 1, minor, patch)
            if previous_version in versions:
                return previous_version

    return None
