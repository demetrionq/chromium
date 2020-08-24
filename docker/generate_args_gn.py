import os
import random
import string
import subprocess

args_gn_template_format = """
target_os = "android"
target_cpu = "{target_cpu}" # <---- can be arm, arm64, x86 or x64
is_debug = false
is_java_debug = false

android_channel = "stable"
is_official_build = true
is_component_build = false
is_chrome_branded = false
is_clang = true
symbol_level = 1
use_unofficial_version_number = false
android_default_version_code = "{android_default_version_code}"
android_default_version_name = "{android_default_version_name}"
fieldtrial_testing_like_official_build = true
icu_use_data_file = false
enable_iterator_debugging = false

enable_extensions = true
enable_plugins = true

"""

def main():
    target_cpu = os.getenv('TARGET_CPU', 'arm64')
    android_default_version_name = os.getenv('ANDROID_DEFAULT_VERSION_NAME', 'Flow')
    android_default_version_code = os.getenv('MAJOR_VERSION', 100)

    with open('args.gn', 'w') as f:
        f.write(args_gn_template_format.format(
            target_cpu=target_cpu,
            android_default_version_name=android_default_version_name,
            android_default_version_code=android_default_version_code,
        ))


if __name__ == '__main__':
    main()