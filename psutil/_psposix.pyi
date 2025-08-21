# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Routines common to all posix systems."""

def pid_exists(pid): ...
def wait_pid(pid, timeout=None, proc_name=None,
             _waitpid=..., _timer=..., _min=...,
             _sleep=..., _pid_exists=...): ...
def disk_usage(path): ...
def get_terminal_map(): ...

__all__ = ["pid_exists", "wait_pid", "disk_usage", "get_terminal_map"]
