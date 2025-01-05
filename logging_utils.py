import os
import sys
from typing import IO, AnyStr

def open_log(path, **kwargs):
    """
    Opens the log file at `path`, with the provided kwargs being given to
    `open`.
    """
    # Disable buffering, see test_advanced_3.py::test_logging_to_driver
    kwargs.setdefault("buffering", 1)
    kwargs.setdefault("mode", "a")
    kwargs.setdefault("encoding", "utf-8")
    stream = open(path, **kwargs)
    return stream

def configure_log_file(out_file: IO[AnyStr], err_file: IO[AnyStr]):
    """Configure stdout and stderr to be the given streams."""

    # Redirect stdout and stderr via file descriptor rather than sys.stdout and
    # sys.stderr, so all languages runtime is affected.
    if out_file:
        stdout_fileno = sys.stdout.fileno()
        os.dup2(out_file.fileno(), stdout_fileno)
        sys.stdout = open_log(stdout_fileno)

    if err_file:
        stderr_fileno = sys.stderr.fileno()
        os.dup2(err_file.fileno(), stderr_fileno)
        sys.stderr = open_log(stderr_fileno)
