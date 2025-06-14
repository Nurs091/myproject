#!/bin/sh
# Compile a Java program.

# Copyright (C) 2001-2020 Free Software Foundation, Inc.
# Written by Bruno Haible <haible@clisp.cons.org>, 2001.
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

# This uses the same choices as javacomp.c, but instead of relying on the
# environment settings at run time, it uses the environment variables
# present at configuration time.
#
# This is a separate shell script, because it must be able to unset JAVA_HOME
# in some cases, which a simple shell command cannot do.
#
# The extra CLASSPATH must have been set prior to calling this script.
# Options that can be passed are -O, -g and "-d DIRECTORY".

CONF_JAVAC='javac -source 1.6'
CONF_CLASSPATH=''
if test -n ""; then
  # Combine given CLASSPATH and configured CLASSPATH.
  if test -n "$CLASSPATH"; then
    CLASSPATH="$CLASSPATH${CONF_CLASSPATH:+:$CONF_CLASSPATH}"
  else
    CLASSPATH="$CONF_CLASSPATH"
  fi
  export CLASSPATH
  test -z "$JAVA_VERBOSE" || echo "$CONF_JAVAC $@"
  exec $CONF_JAVAC "$@"
else
  unset JAVA_HOME
  if test -n ""; then
    # In this case, $CONF_JAVAC starts with "gcj -C".
    CLASSPATH="$CLASSPATH"
    export CLASSPATH
    test -z "$JAVA_VERBOSE" || echo "$CONF_JAVAC $@"
    exec $CONF_JAVAC "$@"
  else
    if test -n "1"; then
      # In this case, $CONF_JAVAC starts with "javac".
      CLASSPATH="$CLASSPATH"
      export CLASSPATH
      test -z "$JAVA_VERBOSE" || echo "$CONF_JAVAC $@"
      exec $CONF_JAVAC "$@"
    else
      if test -n ""; then
        # In this case, $CONF_JAVAC starts with "jikes".
        # Combine given CLASSPATH and configured CLASSPATH.
        if test -n "$CLASSPATH"; then
          CLASSPATH="$CLASSPATH${CONF_CLASSPATH:+:$CONF_CLASSPATH}"
        else
          CLASSPATH="$CONF_CLASSPATH"
        fi
        export CLASSPATH
        test -z "$JAVA_VERBOSE" || echo "$CONF_JAVAC $@"
        exec $CONF_JAVAC "$@"
      else
        echo 'Java compiler not found, try installing gcj or set $JAVAC, then reconfigure' 1>&2
        exit 1
      fi
    fi
  fi
fi
