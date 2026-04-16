k0test
======

Test harness for `k0emu <https://github.com/mnaberez/k0emu>`_, a Renesas (NEC) 78K/0 emulator.  It runs the same test programs on both the emulator and on a real uPD78F0831Y, then compares the results to verify that the emulator behaves like the real hardware.

Structure
---------

- ``firmware/`` - Debugger firmware for the uPD78F0831Y.  Provides a serial protocol for reading/writing memory and calling code on the real hardware.  Assembled with `asxxxx <https://shop-pdp.net/ashtml/asxxxx.php>`_.

- ``host/`` - Python package that communicates with the debugger firmware (``HardwareTarget``) or the k0emu emulator (``EmulatorTarget``) to run the test programs and compare results.

Installation
------------

::

    cd host
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -e .

Usage
-----

Run all test programs on the emulator::

    k0test-run emulator

Run all test programs on real hardware::

    k0test-run hardware

Compare results from hardware and emulator::

    k0test-diff

The ``FTDI_DEVICE`` environment variable can be set to specify the serial port.  If not set, the first available port is used.
