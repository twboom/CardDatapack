import shutil
import argparse

parser = argparse.ArgumentParser(description='Build a new release.')
parser.add_argument('-v', '--version', help='The version to build.')

args = parser.parse_args()

if not args.version:
    print('Please specify a version to build.')
    exit(1)

print(f'Starting build of CardMaker with version {args.version}')
shutil.make_archive(f'CardMaker-{args.version}', "zip", "src")
print(f'Finished build')