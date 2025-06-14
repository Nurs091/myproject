#!/bin/sh
# Execute a C# program.

# Copyright (C) 2003-2020 Free Software Foundation, Inc.
# Written by Bruno Haible <bruno@clisp.org>, 2003.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This uses the same choices as csharpexec.c, but instead of relying on the
# environment settings at run time, it uses the environment variables
# present at configuration time.
#
# This is a separate shell script, because the various C# interpreters have
# different command line options.
#
# Usage: /bin/sh csharpexec.sh [OPTION] program.exe [ARGUMENTS]
# Options:
#   -L DIRECTORY      search for C# libraries also in DIRECTORY

sed_quote_subst='s/\([|&;<>()$`"'"'"'*?[#~=% 	\\]\)/\\\1/g'
libdirs_mono=
prog=
while test $# != 0; do
  case "$1" in
    -L)
      libdirs_mono="${libdirs_mono:+$libdirs_mono:}$2"
      shift
      ;;
    -*)
      echo "csharpexec: unknown option '$1'" 1>&2
      exit 1
      ;;
    *)
      prog="$1"
      break
      ;;
  esac
  shift
done
if test -z "$prog"; then
  echo "csharpexec: no program specified" 1>&2
  exit 1
fi
case "$prog" in
  *.exe) ;;
  *)
    echo "csharpexec: program is not a .exe" 1>&2
    exit 1
    ;;
esac

if test -n ""; then
  CONF_MONO_PATH=''
  if test -n "$libdirs_mono"; then
    MONO_PATH="$libdirs_mono${CONF_MONO_PATH:+:$CONF_MONO_PATH}"
  else
    MONO_PATH="$CONF_MONO_PATH"
  fi
  export MONO_PATH
  test -z "$CSHARP_VERBOSE" || echo mono "$@"
  exec mono "$@"
else
  if test -n ""; then
    CONF_CLIX_PATH=''
    if test -n "$libdirs_mono"; then
      ="$libdirs_mono${CONF_CLIX_PATH:+:$CONF_CLIX_PATH}"
    else
      ="$CONF_CLIX_PATH"
    fi
    export 
    test -z "$CSHARP_VERBOSE" || echo clix "$@"
    exec clix "$@"
  else
    echo 'C# virtual machine not found, try installing mono, then reconfigure' 1>&2
    exit 1
  fi
fi
