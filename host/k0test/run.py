import os
import sys
import importlib.util
from k0test.target import make_target_from_argv


def _run_test(target, fullname, outfilename):
    print("Running %s" % os.path.basename(fullname))
    spec = importlib.util.spec_from_file_location("module.name", fullname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    with open(outfilename, 'w') as outfile:
        try:
            mod.test(target, outfile)
        except Exception as exc:
            msg = "ERROR: %r\n" % exc
            print(msg)
            outfile.close()
            os.remove(outfilename)


def _run_all(target, what):
    here = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures'))
    for filename in sorted(os.listdir(here)):
        if not filename.startswith('test_') or not filename.endswith('.py'):
            continue
        fullname = os.path.join(here, filename)
        basename = os.path.basename(filename).split('.')[0] + '.txt'
        outfilename = os.path.abspath(os.path.join(here, '..', 'results', what, basename))

        if os.path.exists(outfilename):
            print("Skipping %s (report exists)" % filename)
        else:
            _run_test(target, fullname, outfilename)


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('hardware', 'emulator'):
        sys.stderr.write("Usage: k0test-run <hardware|emulator> [test_name.py]\n")
        sys.exit(1)

    what = sys.argv[1]
    target = make_target_from_argv()

    if len(sys.argv) > 2:
        test_name = sys.argv[2]
        if not test_name.endswith('.py'):
            test_name += '.py'
        here = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures'))
        fullname = os.path.join(here, test_name)
        if not os.path.exists(fullname):
            sys.stderr.write("Test not found: %s\n" % test_name)
            sys.exit(1)
        basename = os.path.basename(test_name).split('.')[0] + '.txt'
        outfilename = os.path.abspath(os.path.join(here, '..', 'results', what, basename))
        _run_test(target, fullname, outfilename)
    else:
        _run_all(target, what)


if __name__ == '__main__':
    main()
