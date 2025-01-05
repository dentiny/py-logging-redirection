import logging_utils
import pipe_logging
import sys
import os
import time

_ROTATION_MAX_BYTE = 1
_ROTATION_FILE_NUM = 2
_LOG_STDOUT_FNAME = "/tmp/dentiny.out"
_LOG_STDERR_FNAME = "/tmp/dentiny.err"

stdout_stream = pipe_logging.open_pipe_with_rotation(
    _LOG_STDOUT_FNAME, _ROTATION_MAX_BYTE, _ROTATION_FILE_NUM)
stderr_stream = pipe_logging.open_pipe_with_rotation(
    _LOG_STDERR_FNAME, _ROTATION_MAX_BYTE, _ROTATION_FILE_NUM)

logging_utils.configure_log_file(stdout_stream, stderr_stream)

sys.stdout.write("Hello, World 1 for stdout!\n")
sys.stdout.write("Hello, World 2 for stdout!\n")
sys.stdout.write("Hello, World 3 for stdout!\n")
sys.stdout.write("Hello, World 4 for stdout!\n")

sys.stderr.write("Hello, World 1 for stderr!\n")
sys.stderr.write("Hello, World 2 for stderr!\n")
sys.stderr.write("Hello, World 3 for stderr!\n")
sys.stderr.write("Hello, World 4 for stderr!\n")
