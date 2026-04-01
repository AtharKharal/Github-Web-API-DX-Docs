import os
import sys
import re

def patch_file(file_path, search_pattern, replacement, dry_run=False):
    """
    Applies a targeted patch to a file using regex.
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(search_pattern, replacement, content, flags=re.MULTILINE)

    if new_content == content:
        print(f"No changes made to {file_path}.")
        return False

    if dry_run:
        print(f"[DRY RUN] Patching {file_path}...")
        return True

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully patched {file_path}.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python patch_docs.py <file_path> <search_pattern> <replacement> [--dry-run]")
        sys.exit(1)

    path = sys.argv[1]
    pattern = sys.argv[2]
    replace = sys.argv[3]
    dry = "--dry-run" in sys.argv

    patch_file(path, pattern, replace, dry_run=dry)
