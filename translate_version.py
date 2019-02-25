import os
import argparse
import subprocess
import sys


# ARGUMENTS
parser = argparse.ArgumentParser()

parser.add_argument('-v', '--version', type=int,
                    default=3, help='Open-Signs & Python version.')
parser.add_argument('file', nargs='?', help='File to translate.')

args, _ = parser.parse_known_args()

# VERSION SWAPPING
if args.version != 2 and args.version != 3:
    print('Version should be 2 or 3.\nExiting...')
    sys.exit(-1)

current_version = 'open-signs'
version2_path = current_version + '2'
version3_path = current_version + '3'

if os.path.exists(version2_path) and \
        os.path.exists(current_version) and \
        os.path.exists(version3_path):

    print('Found a version in use besides version 2 and 3.\nExiting...')
    sys.exit(-1)

if args.version == 3:
    if os.path.exists(version2_path) and os.path.exists(current_version):
        pass
    elif os.path.exists(version3_path) and os.path.exists(current_version):
        os.rename(current_version, version2_path)
        os.rename(version3_path, current_version)
    elif os.path.exists(version3_path) and os.path.exists(version2_path):
        os.rename(version3_path, current_version)
    else:
        print('Missing one of the versions!\nExiting...')
        sys.exit(-1)
elif args.version == 2:
    if os.path.exists(version2_path) and os.path.exists(current_version):
        os.rename(current_version, version3_path)
        os.rename(version2_path, current_version)
    elif os.path.exists(version3_path) and os.path.exists(current_version):
        pass
    elif os.path.exists(version3_path) and os.path.exists(version2_path):
        os.rename(version2_path, current_version)
    else:
        print('Missing one of the versions!\nExiting...')
        sys.exit(-1)

# TRANSLATION
if args.file:
    src_path = os.path.join(current_version, 'vlibras-translate/src')
    translator_path = os.path.join(src_path, 'TraduzirArquivo.py')
    result = subprocess.run(['python' + str(args.version), translator_path, args.file])
    print(result)
