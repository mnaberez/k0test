import os
import sys

def main():
    hardware_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results/hardware'))
    emulator_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'results/emulator'))

    hardware_filenames = [ f for f in sorted(os.listdir(hardware_dir)) if f.endswith('.txt') ]
    exitcode = 0
    for basename in hardware_filenames:
        h_filename = os.path.join(hardware_dir, basename)
        e_filename = os.path.join(emulator_dir, basename)

        if os.path.exists(e_filename):
            with open(h_filename) as f:
                h_contents = f.read()
            with open(e_filename) as f:
                e_contents = f.read()

            if h_contents == e_contents:
                result = 'ok'
            else:
                exitcode = 1
                result = 'DIFFERENT'

        else:
            exitcode = 1
            result = 'MISSING'

        print("%s: %s" % (basename, result))
    sys.exit(exitcode)

if __name__ == '__main__':
    assert sys.version_info[0] >= 3
    main()
