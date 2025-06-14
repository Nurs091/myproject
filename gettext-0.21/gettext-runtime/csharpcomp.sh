#!/bin/sh
# Compile a C# program.

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

# This uses the same choices as csharpcomp.c, but instead of relying on the
# environment settings at run time, it uses the environment variables
# present at configuration time.
#
# This is a separate shell script, because the various C# compilers have
# different command line options.
#
# Usage: /bin/sh csharpcomp.sh [OPTION] SOURCE.cs ... RES.resource ...
# Options:
#   -o PROGRAM.exe  or  -o LIBRARY.dll
#                     set the output assembly name
#   -L DIRECTORY      search for C# libraries also in DIRECTORY
#   -l LIBRARY        reference the C# library LIBRARY.dll
#   -O                optimize
#   -g                generate debugging information

# func_tmpdir
# creates a temporary directory.
# Sets variable
# - tmp             pathname of freshly created temporary directory
func_tmpdir ()
{
  # Use the environment variable TMPDIR, falling back to /tmp. This allows
  # users to specify a different temporary directory, for example, if their
  # /tmp is filled up or too small.
  : ${TMPDIR=/tmp}
  {
    # Use the mktemp program if available. If not available, hide the error
    # message.
    tmp=`(umask 077 && mktemp -d -q "$TMPDIR/gtXXXXXX") 2>/dev/null` &&
    test -n "$tmp" && test -d "$tmp"
  } ||
  {
    # Use a simple mkdir command. It is guaranteed to fail if the directory
    # already exists.  $RANDOM is bash specific and expands to empty in shells
    # other than bash, ksh and zsh.  Its use does not increase security;
    # rather, it minimizes the probability of failure in a very cluttered /tmp
    # directory.
    tmp=$TMPDIR/gt$$-$RANDOM
    (umask 077 && mkdir "$tmp")
  } ||
  {
    echo "$0: cannot create a temporary directory in $TMPDIR" >&2
    { (exit 1); exit 1; }
  }
}

sed_quote_subst='s/\([|&;<>()$`"'"'"'*?[#~=% 	\\]\)/\\\1/g'
options_mcs=
options_csc="-nologo"
sources=
while test $# != 0; do
  case "$1" in
    -o)
      case "$2" in
        *.dll)
          options_mcs="$options_mcs -target:library"
          options_csc="$options_csc -target:library"
          ;;
        *.exe)
          options_csc="$options_csc -target:exe"
          ;;
      esac
      options_mcs="$options_mcs -out:"`echo "$2" | sed -e "$sed_quote_subst"`
      options_csc="$options_csc -out:"`echo "$2" | sed -e "$sed_quote_subst"`
      shift
      ;;
    -L)
      options_mcs="$options_mcs -lib:"`echo "$2" | sed -e "$sed_quote_subst"`
      options_csc="$options_csc -lib:"`echo "$2" | sed -e "$sed_quote_subst"`
      shift
      ;;
    -l)
      options_mcs="$options_mcs -reference:"`echo "$2" | sed -e "$sed_quote_subst"`
      options_csc="$options_csc -reference:"`echo "$2" | sed -e "$sed_quote_subst"`".dll"
      shift
      ;;
    -O)
      options_csc="$options_csc -optimize+"
      ;;
    -g)
      options_mcs="$options_mcs -debug"
      options_csc="$options_csc -debug+"
      ;;
    -*)
      echo "csharpcomp: unknown option '$1'" 1>&2
      exit 1
      ;;
    *.resources)
      options_mcs="$options_mcs -resource:"`echo "$1" | sed -e "$sed_quote_subst"`
      options_csc="$options_csc -resource:"`echo "$1" | sed -e "$sed_quote_subst"`
      ;;
    *.cs)
      sources="$sources "`echo "$1" | sed -e "$sed_quote_subst"`
      ;;
    *)
      echo "csharpcomp: unknown type of argument '$1'" 1>&2
      exit 1
      ;;
  esac
  shift
done

if test -n ""; then
  # mcs prints it errors and warnings to stdout, not stderr. Furthermore it
  # adds a useless line "Compilation succeeded..." at the end. Correct both.
  sed_drop_success_line='${
/^Compilation succeeded/d
}'
  func_tmpdir
  trap 'rm -rf "$tmp"' 1 2 3 15
  test -z "$CSHARP_VERBOSE" || echo mcs $options_mcs $sources
  mcs $options_mcs $sources > "$tmp"/mcs.err
  result=$?
  sed -e "$sed_drop_success_line" < "$tmp"/mcs.err >&2
  rm -rf "$tmp"
  exit $result
else
  if test -n ""; then
    test -z "$CSHARP_VERBOSE" || echo csc $options_csc $sources
    exec csc $options_csc $sources
  else
    echo 'C# compiler not found, try installing mono, then reconfigure' 1>&2
    exit 1
  fi
fi
