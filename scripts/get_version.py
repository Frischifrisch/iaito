
import os
import re

scripts_path = os.path.dirname(os.path.realpath(__file__))
pro_file_path = os.path.join(scripts_path, "..", "src", "Iaito.pro")

with open(pro_file_path, "r") as f:
    pro_content = f.read()

def version_var_re(name):
    return f"^[ \t]*{name}[ \t]*=[ \t]*(\d+)[ \t]*$"

m = re.search(version_var_re("IAITO_VERSION_MAJOR"), pro_content, flags=re.MULTILINE)
version_major = int(m[1]) if m is not None else 0

m = re.search(version_var_re("IAITO_VERSION_MINOR"), pro_content, flags=re.MULTILINE)
version_minor = int(m[1]) if m is not None else 0

m = re.search(version_var_re("IAITO_VERSION_PATCH"), pro_content, flags=re.MULTILINE)
version_patch = int(m[1]) if m is not None else 0

print(f"{version_major}.{version_minor}.{version_patch}")
