# Makefile.in generated by automake 1.16.2 from Makefile.am.
# Makefile.  Generated from Makefile.in by configure.

# Copyright (C) 1994-2020 Free Software Foundation, Inc.

# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.



am__is_gnu_make = { \
  if test -z '$(MAKELEVEL)'; then \
    false; \
  elif test -n '$(MAKE_HOST)'; then \
    true; \
  elif test -n '$(MAKE_VERSION)' && test -n '$(CURDIR)'; then \
    true; \
  else \
    false; \
  fi; \
}
am__make_running_with_option = \
  case $${target_option-} in \
      ?) ;; \
      *) echo "am__make_running_with_option: internal error: invalid" \
              "target option '$${target_option-}' specified" >&2; \
         exit 1;; \
  esac; \
  has_opt=no; \
  sane_makeflags=$$MAKEFLAGS; \
  if $(am__is_gnu_make); then \
    sane_makeflags=$$MFLAGS; \
  else \
    case $$MAKEFLAGS in \
      *\\[\ \	]*) \
        bs=\\; \
        sane_makeflags=`printf '%s\n' "$$MAKEFLAGS" \
          | sed "s/$$bs$$bs[$$bs $$bs	]*//g"`;; \
    esac; \
  fi; \
  skip_next=no; \
  strip_trailopt () \
  { \
    flg=`printf '%s\n' "$$flg" | sed "s/$$1.*$$//"`; \
  }; \
  for flg in $$sane_makeflags; do \
    test $$skip_next = yes && { skip_next=no; continue; }; \
    case $$flg in \
      *=*|--*) continue;; \
        -*I) strip_trailopt 'I'; skip_next=yes;; \
      -*I?*) strip_trailopt 'I';; \
        -*O) strip_trailopt 'O'; skip_next=yes;; \
      -*O?*) strip_trailopt 'O';; \
        -*l) strip_trailopt 'l'; skip_next=yes;; \
      -*l?*) strip_trailopt 'l';; \
      -[dEDm]) skip_next=yes;; \
      -[JT]) skip_next=yes;; \
    esac; \
    case $$flg in \
      *$$target_option*) has_opt=yes; break;; \
    esac; \
  done; \
  test $$has_opt = yes
am__make_dryrun = (target_option=n; $(am__make_running_with_option))
am__make_keepgoing = (target_option=k; $(am__make_running_with_option))
pkgdatadir = $(datadir)/gettext
pkgincludedir = $(includedir)/gettext
pkglibdir = $(libdir)/gettext
pkglibexecdir = $(libexecdir)/gettext
am__cd = CDPATH="$${ZSH_VERSION+.}$(PATH_SEPARATOR)" && cd
install_sh_DATA = $(install_sh) -c -m 644
install_sh_PROGRAM = $(install_sh) -c
install_sh_SCRIPT = $(install_sh) -c
INSTALL_HEADER = $(INSTALL_DATA)
transform = $(program_transform_name)
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
build_triplet = aarch64-apple-darwin23.6.0
host_triplet = aarch64-apple-darwin23.6.0
subdir = .
ACLOCAL_M4 = $(top_srcdir)/aclocal.m4
am__aclocal_m4_deps = $(top_srcdir)/configure.ac
am__configure_deps = $(am__aclocal_m4_deps) $(CONFIGURE_DEPENDENCIES) \
	$(ACLOCAL_M4)
DIST_COMMON = $(srcdir)/Makefile.am $(top_srcdir)/configure \
	$(am__configure_deps) $(am__DIST_COMMON)
am__CONFIG_DISTCLEAN_FILES = config.status config.cache config.log \
 configure.lineno config.status.lineno
mkinstalldirs = $(SHELL) $(top_srcdir)/build-aux/mkinstalldirs
CONFIG_CLEAN_FILES =
CONFIG_CLEAN_VPATH_FILES =
AM_V_P = $(am__v_P_$(V))
am__v_P_ = $(am__v_P_$(AM_DEFAULT_VERBOSITY))
am__v_P_0 = false
am__v_P_1 = :
AM_V_GEN = $(am__v_GEN_$(V))
am__v_GEN_ = $(am__v_GEN_$(AM_DEFAULT_VERBOSITY))
am__v_GEN_0 = @echo "  GEN     " $@;
am__v_GEN_1 = 
AM_V_at = $(am__v_at_$(V))
am__v_at_ = $(am__v_at_$(AM_DEFAULT_VERBOSITY))
am__v_at_0 = @
am__v_at_1 = 
depcomp =
am__maybe_remake_depfiles =
SOURCES =
DIST_SOURCES =
RECURSIVE_TARGETS = all-recursive check-recursive cscopelist-recursive \
	ctags-recursive dvi-recursive html-recursive info-recursive \
	install-data-recursive install-dvi-recursive \
	install-exec-recursive install-html-recursive \
	install-info-recursive install-pdf-recursive \
	install-ps-recursive install-recursive installcheck-recursive \
	installdirs-recursive pdf-recursive ps-recursive \
	tags-recursive uninstall-recursive
am__can_run_installinfo = \
  case $$AM_UPDATE_INFO_DIR in \
    n|no|NO) false;; \
    *) (install-info --version) >/dev/null 2>&1;; \
  esac
RECURSIVE_CLEAN_TARGETS = mostlyclean-recursive clean-recursive	\
  distclean-recursive maintainer-clean-recursive
am__recursive_targets = \
  $(RECURSIVE_TARGETS) \
  $(RECURSIVE_CLEAN_TARGETS) \
  $(am__extra_recursive_targets)
AM_RECURSIVE_TARGETS = $(am__recursive_targets:-recursive=) TAGS CTAGS \
	cscope distdir distdir-am dist dist-all distcheck
am__extra_recursive_targets = maintainer-update-po-recursive
am__tagged_files = $(HEADERS) $(SOURCES) $(TAGS_FILES) $(LISP)
# Read a list of newline-separated strings from the standard input,
# and print each of them once, without duplicates.  Input order is
# *not* preserved.
am__uniquify_input = $(AWK) '\
  BEGIN { nonempty = 0; } \
  { items[$$0] = 1; nonempty = 1; } \
  END { if (nonempty) { for (i in items) print i; }; } \
'
# Make sure the list of sources is unique.  This is necessary because,
# e.g., the same source file might be shared among _SOURCES variables
# for different programs/libraries.
am__define_uniq_tagged_files = \
  list='$(am__tagged_files)'; \
  unique=`for i in $$list; do \
    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
  done | $(am__uniquify_input)`
ETAGS = etags
CTAGS = ctags
CSCOPE = cscope
DIST_SUBDIRS = $(SUBDIRS)
am__DIST_COMMON = $(srcdir)/Makefile.in \
	$(top_srcdir)/build-aux/config.guess \
	$(top_srcdir)/build-aux/config.sub \
	$(top_srcdir)/build-aux/install-sh \
	$(top_srcdir)/build-aux/missing \
	$(top_srcdir)/build-aux/mkinstalldirs AUTHORS COPYING \
	ChangeLog INSTALL NEWS README THANKS build-aux/config.guess \
	build-aux/config.rpath build-aux/config.sub build-aux/depcomp \
	build-aux/install-sh build-aux/ltmain.sh build-aux/mdate-sh \
	build-aux/missing build-aux/mkinstalldirs \
	build-aux/texinfo.tex build-aux/ylwrap
DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)
distdir = $(PACKAGE)-$(VERSION)
top_distdir = $(distdir)
am__remove_distdir = \
  if test -d "$(distdir)"; then \
    find "$(distdir)" -type d ! -perm -200 -exec chmod u+w {} ';' \
      && rm -rf "$(distdir)" \
      || { sleep 5 && rm -rf "$(distdir)"; }; \
  else :; fi
am__post_remove_distdir = $(am__remove_distdir)
am__relativize = \
  dir0=`pwd`; \
  sed_first='s,^\([^/]*\)/.*$$,\1,'; \
  sed_rest='s,^[^/]*/*,,'; \
  sed_last='s,^.*/\([^/]*\)$$,\1,'; \
  sed_butlast='s,/*[^/]*$$,,'; \
  while test -n "$$dir1"; do \
    first=`echo "$$dir1" | sed -e "$$sed_first"`; \
    if test "$$first" != "."; then \
      if test "$$first" = ".."; then \
        dir2=`echo "$$dir0" | sed -e "$$sed_last"`/"$$dir2"; \
        dir0=`echo "$$dir0" | sed -e "$$sed_butlast"`; \
      else \
        first2=`echo "$$dir2" | sed -e "$$sed_first"`; \
        if test "$$first2" = "$$first"; then \
          dir2=`echo "$$dir2" | sed -e "$$sed_rest"`; \
        else \
          dir2="../$$dir2"; \
        fi; \
        dir0="$$dir0"/"$$first"; \
      fi; \
    fi; \
    dir1=`echo "$$dir1" | sed -e "$$sed_rest"`; \
  done; \
  reldir="$$dir2"
DIST_ARCHIVES = $(distdir).tar.gz
GZIP_ENV = --best
DIST_TARGETS = dist-gzip
distuninstallcheck_listfiles = find . -type f -print
am__distuninstallcheck_listfiles = $(distuninstallcheck_listfiles) \
  | sed 's|^\./|$(prefix)/|' | grep -v '$(infodir)/dir$$'
distcleancheck_listfiles = find . -type f -print
ACLOCAL = ${SHELL} /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21/build-aux/missing aclocal-1.16
AMTAR = $${TAR-tar}
AM_DEFAULT_VERBOSITY = 1
AUTOCONF = ${SHELL} /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21/build-aux/missing autoconf
AUTOHEADER = ${SHELL} /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21/build-aux/missing autoheader
AUTOMAKE = ${SHELL} /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21/build-aux/missing automake-1.16
AWK = awk
CC = 
CFLAGS = 
CPP = 
CPPFLAGS = 
CXX = 
CXXCPP = 
CXXFLAGS = 
CYGPATH_W = echo
DEFS = -DPACKAGE_NAME=\"gettext\" -DPACKAGE_TARNAME=\"gettext\" -DPACKAGE_VERSION=\"0.21\" -DPACKAGE_STRING=\"gettext\ 0.21\" -DPACKAGE_BUGREPORT=\"bug-gettext@gnu.org\" -DPACKAGE_URL=\"\" -DPACKAGE=\"gettext\" -DVERSION=\"0.21\"
ECHO_C = \c
ECHO_N = 
ECHO_T = 
EMACS = 
EMACSLOADPATH = 
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL_STRIP_PROGRAM = $(install_sh) -c -s
LDFLAGS = 
LIBOBJS = 
LIBS = 
LTLIBOBJS = 
LT_SYS_LIBRARY_PATH = 
MAKEINFO = ${SHELL} /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21/build-aux/missing makeinfo
MKDIR_P = build-aux/install-sh -c -d
PACKAGE = gettext
PACKAGE_BUGREPORT = bug-gettext@gnu.org
PACKAGE_NAME = gettext
PACKAGE_STRING = gettext 0.21
PACKAGE_TARNAME = gettext
PACKAGE_URL = 
PACKAGE_VERSION = 0.21
PATH_SEPARATOR = :
SET_MAKE = 
SHELL = /bin/sh
STRIP = 
VERSION = 0.21
YACC = 
YFLAGS = 
abs_builddir = /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21
abs_srcdir = /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21
abs_top_builddir = /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21
abs_top_srcdir = /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21
am__leading_dot = .
am__tar = ${AMTAR} chf - --format=ustar --owner=root --group=root "$$tardir"
am__untar = tar -xf -
bindir = ${exec_prefix}/bin
build = aarch64-apple-darwin23.6.0
build_alias = 
build_cpu = aarch64
build_os = darwin23.6.0
build_vendor = apple
builddir = .
datadir = ${datarootdir}
datarootdir = ${prefix}/share
docdir = ${datarootdir}/doc/${PACKAGE_TARNAME}
dvidir = ${docdir}
exec_prefix = ${prefix}
host = aarch64-apple-darwin23.6.0
host_alias = 
host_cpu = aarch64
host_os = darwin23.6.0
host_vendor = apple
htmldir = ${docdir}
includedir = ${prefix}/include
infodir = ${datarootdir}/info
install_sh = ${SHELL} /Users/nurairuslan/Desktop/projectt/myproject1/gettext-0.21/build-aux/install-sh
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/libexec
localedir = ${datarootdir}/locale
localstatedir = ${prefix}/var
mandir = ${datarootdir}/man
mkdir_p = $(MKDIR_P)
oldincludedir = /usr/include
pdfdir = ${docdir}
prefix = /usr/local
program_transform_name = s,x,x,
psdir = ${docdir}
sbindir = ${exec_prefix}/sbin
sharedstatedir = ${prefix}/com
srcdir = .
subdirs =  gettext-runtime libtextstyle gettext-tools
sysconfdir = ${prefix}/etc
target_alias = 
top_build_prefix = 
top_builddir = .
top_srcdir = .
AUTOMAKE_OPTIONS = 1.5 gnu no-dependencies
ACLOCAL_AMFLAGS = -I m4
SUBDIRS = gnulib-local gettext-runtime libtextstyle gettext-tools
changelog_etc = \
  gettext-runtime/ChangeLog.0 \
  gettext-runtime/doc/ChangeLog.0 \
  gettext-runtime/intl-csharp/ChangeLog.0 \
  gettext-runtime/intl-java/ChangeLog.0 \
  gettext-runtime/libasprintf/ChangeLog.0 \
  gettext-runtime/m4/ChangeLog.0 \
  gettext-runtime/man/ChangeLog.0 \
  gettext-runtime/src/ChangeLog.0 \
  gettext-runtime/tests/ChangeLog.0 \
  gettext-tools/ChangeLog.0 \
  gettext-tools/doc/ChangeLog.0 \
  gettext-tools/doc/ChangeLog.1 \
  gettext-tools/examples/ChangeLog.0 \
  gettext-tools/gnulib-tests/ChangeLog.0 \
  gettext-tools/libgettextpo/ChangeLog.0 \
  gettext-tools/libgrep/ChangeLog.0 \
  gettext-tools/m4/ChangeLog.0 \
  gettext-tools/man/ChangeLog.0 \
  gettext-tools/man/ChangeLog.1 \
  gettext-tools/misc/ChangeLog.0 \
  gettext-tools/projects/ChangeLog.0 \
  gettext-tools/src/ChangeLog.0 \
  gettext-tools/src/ChangeLog.1 \
  gettext-tools/styles/ChangeLog.0 \
  gettext-tools/tests/ChangeLog.0 \
  gettext-tools/tests/ChangeLog.1 \
  gnulib-local/ChangeLog.0


# OS/2 port.

# Windows support.

# Versioning based on Git release tags.
EXTRA_DIST = $(changelog_etc) DEPENDENCIES PACKAGING HACKING \
	ChangeLog.0 autogen.sh check-copyright-headers \
	build-aux/ac-help.sed build-aux/git-version-gen \
	build-aux/texi2html m4/fixautomake.m4 m4/woe32-dll.m4 \
	m4/libtool.m4 os2/README.OS2 os2/Makefile os2/backward.def \
	os2/configure.awk INSTALL.windows windows/windres-options \
	windows/gettext.rc $(top_srcdir)/.version
BUILT_SOURCES = $(top_srcdir)/.version

# Generate ChangeLog.
gen_start_date = 2015-10-13
all: $(BUILT_SOURCES)
	$(MAKE) $(AM_MAKEFLAGS) all-recursive

.SUFFIXES:
am--refresh: Makefile
	@:
$(srcdir)/Makefile.in:  $(srcdir)/Makefile.am  $(am__configure_deps)
	@for dep in $?; do \
	  case '$(am__configure_deps)' in \
	    *$$dep*) \
	      echo ' cd $(srcdir) && $(AUTOMAKE) --gnu'; \
	      $(am__cd) $(srcdir) && $(AUTOMAKE) --gnu \
		&& exit 0; \
	      exit 1;; \
	  esac; \
	done; \
	echo ' cd $(top_srcdir) && $(AUTOMAKE) --gnu Makefile'; \
	$(am__cd) $(top_srcdir) && \
	  $(AUTOMAKE) --gnu Makefile
Makefile: $(srcdir)/Makefile.in $(top_builddir)/config.status
	@case '$?' in \
	  *config.status*) \
	    echo ' $(SHELL) ./config.status'; \
	    $(SHELL) ./config.status;; \
	  *) \
	    echo ' cd $(top_builddir) && $(SHELL) ./config.status $@ $(am__maybe_remake_depfiles)'; \
	    cd $(top_builddir) && $(SHELL) ./config.status $@ $(am__maybe_remake_depfiles);; \
	esac;

$(top_builddir)/config.status: $(top_srcdir)/configure $(CONFIG_STATUS_DEPENDENCIES)
	$(SHELL) ./config.status --recheck

$(top_srcdir)/configure:  $(am__configure_deps)
	$(am__cd) $(srcdir) && $(AUTOCONF)
$(ACLOCAL_M4):  $(am__aclocal_m4_deps)
	$(am__cd) $(srcdir) && $(ACLOCAL) $(ACLOCAL_AMFLAGS)
$(am__aclocal_m4_deps):

# This directory's subdirectories are mostly independent; you can cd
# into them and run 'make' without going through this Makefile.
# To change the values of 'make' variables: instead of editing Makefiles,
# (1) if the variable is set in 'config.status', edit 'config.status'
#     (which will cause the Makefiles to be regenerated when you run 'make');
# (2) otherwise, pass the desired values on the 'make' command line.
$(am__recursive_targets):
	@fail=; \
	if $(am__make_keepgoing); then \
	  failcom='fail=yes'; \
	else \
	  failcom='exit 1'; \
	fi; \
	dot_seen=no; \
	target=`echo $@ | sed s/-recursive//`; \
	case "$@" in \
	  distclean-* | maintainer-clean-*) list='$(DIST_SUBDIRS)' ;; \
	  *) list='$(SUBDIRS)' ;; \
	esac; \
	for subdir in $$list; do \
	  echo "Making $$target in $$subdir"; \
	  if test "$$subdir" = "."; then \
	    dot_seen=yes; \
	    local_target="$$target-am"; \
	  else \
	    local_target="$$target"; \
	  fi; \
	  ($(am__cd) $$subdir && $(MAKE) $(AM_MAKEFLAGS) $$local_target) \
	  || eval $$failcom; \
	done; \
	if test "$$dot_seen" = "no"; then \
	  $(MAKE) $(AM_MAKEFLAGS) "$$target-am" || exit 1; \
	fi; test -z "$$fail"
maintainer-update-po-local: 

ID: $(am__tagged_files)
	$(am__define_uniq_tagged_files); mkid -fID $$unique
tags: tags-recursive
TAGS: tags

tags-am: $(TAGS_DEPENDENCIES) $(am__tagged_files)
	set x; \
	here=`pwd`; \
	if ($(ETAGS) --etags-include --version) >/dev/null 2>&1; then \
	  include_option=--etags-include; \
	  empty_fix=.; \
	else \
	  include_option=--include; \
	  empty_fix=; \
	fi; \
	list='$(SUBDIRS)'; for subdir in $$list; do \
	  if test "$$subdir" = .; then :; else \
	    test ! -f $$subdir/TAGS || \
	      set "$$@" "$$include_option=$$here/$$subdir/TAGS"; \
	  fi; \
	done; \
	$(am__define_uniq_tagged_files); \
	shift; \
	if test -z "$(ETAGS_ARGS)$$*$$unique"; then :; else \
	  test -n "$$unique" || unique=$$empty_fix; \
	  if test $$# -gt 0; then \
	    $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	      "$$@" $$unique; \
	  else \
	    $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	      $$unique; \
	  fi; \
	fi
ctags: ctags-recursive

CTAGS: ctags
ctags-am: $(TAGS_DEPENDENCIES) $(am__tagged_files)
	$(am__define_uniq_tagged_files); \
	test -z "$(CTAGS_ARGS)$$unique" \
	  || $(CTAGS) $(CTAGSFLAGS) $(AM_CTAGSFLAGS) $(CTAGS_ARGS) \
	     $$unique

GTAGS:
	here=`$(am__cd) $(top_builddir) && pwd` \
	  && $(am__cd) $(top_srcdir) \
	  && gtags -i $(GTAGS_ARGS) "$$here"
cscope: cscope.files
	test ! -s cscope.files \
	  || $(CSCOPE) -b -q $(AM_CSCOPEFLAGS) $(CSCOPEFLAGS) -i cscope.files $(CSCOPE_ARGS)
clean-cscope:
	-rm -f cscope.files
cscope.files: clean-cscope cscopelist
cscopelist: cscopelist-recursive

cscopelist-am: $(am__tagged_files)
	list='$(am__tagged_files)'; \
	case "$(srcdir)" in \
	  [\\/]* | ?:[\\/]*) sdir="$(srcdir)" ;; \
	  *) sdir=$(subdir)/$(srcdir) ;; \
	esac; \
	for i in $$list; do \
	  if test -f "$$i"; then \
	    echo "$(subdir)/$$i"; \
	  else \
	    echo "$$sdir/$$i"; \
	  fi; \
	done >> $(top_builddir)/cscope.files

distclean-tags:
	-rm -f TAGS ID GTAGS GRTAGS GSYMS GPATH tags
	-rm -f cscope.out cscope.in.out cscope.po.out cscope.files

distdir: $(BUILT_SOURCES)
	$(MAKE) $(AM_MAKEFLAGS) distdir-am

distdir-am: $(DISTFILES)
	$(am__remove_distdir)
	test -d "$(distdir)" || mkdir "$(distdir)"
	@srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	topsrcdirstrip=`echo "$(top_srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	list='$(DISTFILES)'; \
	  dist_files=`for file in $$list; do echo $$file; done | \
	  sed -e "s|^$$srcdirstrip/||;t" \
	      -e "s|^$$topsrcdirstrip/|$(top_builddir)/|;t"`; \
	case $$dist_files in \
	  */*) $(MKDIR_P) `echo "$$dist_files" | \
			   sed '/\//!d;s|^|$(distdir)/|;s,/[^/]*$$,,' | \
			   sort -u` ;; \
	esac; \
	for file in $$dist_files; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  if test -d $$d/$$file; then \
	    dir=`echo "/$$file" | sed -e 's,/[^/]*$$,,'`; \
	    if test -d "$(distdir)/$$file"; then \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -fpR $(srcdir)/$$file "$(distdir)$$dir" || exit 1; \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    cp -fpR $$d/$$file "$(distdir)$$dir" || exit 1; \
	  else \
	    test -f "$(distdir)/$$file" \
	    || cp -p $$d/$$file "$(distdir)/$$file" \
	    || exit 1; \
	  fi; \
	done
	@list='$(DIST_SUBDIRS)'; for subdir in $$list; do \
	  if test "$$subdir" = .; then :; else \
	    $(am__make_dryrun) \
	      || test -d "$(distdir)/$$subdir" \
	      || $(MKDIR_P) "$(distdir)/$$subdir" \
	      || exit 1; \
	    dir1=$$subdir; dir2="$(distdir)/$$subdir"; \
	    $(am__relativize); \
	    new_distdir=$$reldir; \
	    dir1=$$subdir; dir2="$(top_distdir)"; \
	    $(am__relativize); \
	    new_top_distdir=$$reldir; \
	    echo " (cd $$subdir && $(MAKE) $(AM_MAKEFLAGS) top_distdir="$$new_top_distdir" distdir="$$new_distdir" \\"; \
	    echo "     am__remove_distdir=: am__skip_length_check=: am__skip_mode_fix=: distdir)"; \
	    ($(am__cd) $$subdir && \
	      $(MAKE) $(AM_MAKEFLAGS) \
	        top_distdir="$$new_top_distdir" \
	        distdir="$$new_distdir" \
		am__remove_distdir=: \
		am__skip_length_check=: \
		am__skip_mode_fix=: \
	        distdir) \
	      || exit 1; \
	  fi; \
	done
	$(MAKE) $(AM_MAKEFLAGS) \
	  top_distdir="$(top_distdir)" distdir="$(distdir)" \
	  dist-hook
	-test -n "$(am__skip_mode_fix)" \
	|| find "$(distdir)" -type d ! -perm -755 \
		-exec chmod u+rwx,go+rx {} \; -o \
	  ! -type d ! -perm -444 -links 1 -exec chmod a+r {} \; -o \
	  ! -type d ! -perm -400 -exec chmod a+r {} \; -o \
	  ! -type d ! -perm -444 -exec $(install_sh) -c -m a+r {} {} \; \
	|| chmod -R a+r "$(distdir)"
dist-gzip: distdir
	tardir=$(distdir) && $(am__tar) | eval GZIP= gzip $(GZIP_ENV) -c >$(distdir).tar.gz
	$(am__post_remove_distdir)

dist-bzip2: distdir
	tardir=$(distdir) && $(am__tar) | BZIP2=$${BZIP2--9} bzip2 -c >$(distdir).tar.bz2
	$(am__post_remove_distdir)

dist-lzip: distdir
	tardir=$(distdir) && $(am__tar) | lzip -c $${LZIP_OPT--9} >$(distdir).tar.lz
	$(am__post_remove_distdir)

dist-xz: distdir
	tardir=$(distdir) && $(am__tar) | XZ_OPT=$${XZ_OPT--e} xz -c >$(distdir).tar.xz
	$(am__post_remove_distdir)

dist-zstd: distdir
	tardir=$(distdir) && $(am__tar) | zstd -c $${ZSTD_CLEVEL-$${ZSTD_OPT--19}} >$(distdir).tar.zst
	$(am__post_remove_distdir)

dist-tarZ: distdir
	@echo WARNING: "Support for distribution archives compressed with" \
		       "legacy program 'compress' is deprecated." >&2
	@echo WARNING: "It will be removed altogether in Automake 2.0" >&2
	tardir=$(distdir) && $(am__tar) | compress -c >$(distdir).tar.Z
	$(am__post_remove_distdir)

dist-shar: distdir
	@echo WARNING: "Support for shar distribution archives is" \
	               "deprecated." >&2
	@echo WARNING: "It will be removed altogether in Automake 2.0" >&2
	shar $(distdir) | eval GZIP= gzip $(GZIP_ENV) -c >$(distdir).shar.gz
	$(am__post_remove_distdir)

dist-zip: distdir
	-rm -f $(distdir).zip
	zip -rq $(distdir).zip $(distdir)
	$(am__post_remove_distdir)

dist dist-all:
	$(MAKE) $(AM_MAKEFLAGS) $(DIST_TARGETS) am__post_remove_distdir='@:'
	$(am__post_remove_distdir)

# This target untars the dist file and tries a VPATH configuration.  Then
# it guarantees that the distribution is self-contained by making another
# tarfile.
distcheck: dist
	case '$(DIST_ARCHIVES)' in \
	*.tar.gz*) \
	  eval GZIP= gzip $(GZIP_ENV) -dc $(distdir).tar.gz | $(am__untar) ;;\
	*.tar.bz2*) \
	  bzip2 -dc $(distdir).tar.bz2 | $(am__untar) ;;\
	*.tar.lz*) \
	  lzip -dc $(distdir).tar.lz | $(am__untar) ;;\
	*.tar.xz*) \
	  xz -dc $(distdir).tar.xz | $(am__untar) ;;\
	*.tar.Z*) \
	  uncompress -c $(distdir).tar.Z | $(am__untar) ;;\
	*.shar.gz*) \
	  eval GZIP= gzip $(GZIP_ENV) -dc $(distdir).shar.gz | unshar ;;\
	*.zip*) \
	  unzip $(distdir).zip ;;\
	*.tar.zst*) \
	  zstd -dc $(distdir).tar.zst | $(am__untar) ;;\
	esac
	chmod -R a-w $(distdir)
	chmod u+w $(distdir)
	mkdir $(distdir)/_build $(distdir)/_build/sub $(distdir)/_inst
	chmod a-w $(distdir)
	test -d $(distdir)/_build || exit 0; \
	dc_install_base=`$(am__cd) $(distdir)/_inst && pwd | sed -e 's,^[^:\\/]:[\\/],/,'` \
	  && dc_destdir="$${TMPDIR-/tmp}/am-dc-$$$$/" \
	  && $(MAKE) $(AM_MAKEFLAGS) distcheck-hook \
	  && am__cwd=`pwd` \
	  && $(am__cd) $(distdir)/_build/sub \
	  && ../../configure \
	    $(AM_DISTCHECK_CONFIGURE_FLAGS) \
	    $(DISTCHECK_CONFIGURE_FLAGS) \
	    --srcdir=../.. --prefix="$$dc_install_base" \
	  && $(MAKE) $(AM_MAKEFLAGS) \
	  && $(MAKE) $(AM_MAKEFLAGS) dvi \
	  && $(MAKE) $(AM_MAKEFLAGS) check \
	  && $(MAKE) $(AM_MAKEFLAGS) install \
	  && $(MAKE) $(AM_MAKEFLAGS) installcheck \
	  && $(MAKE) $(AM_MAKEFLAGS) uninstall \
	  && $(MAKE) $(AM_MAKEFLAGS) distuninstallcheck_dir="$$dc_install_base" \
	        distuninstallcheck \
	  && chmod -R a-w "$$dc_install_base" \
	  && ({ \
	       (cd ../.. && umask 077 && mkdir "$$dc_destdir") \
	       && $(MAKE) $(AM_MAKEFLAGS) DESTDIR="$$dc_destdir" install \
	       && $(MAKE) $(AM_MAKEFLAGS) DESTDIR="$$dc_destdir" uninstall \
	       && $(MAKE) $(AM_MAKEFLAGS) DESTDIR="$$dc_destdir" \
	            distuninstallcheck_dir="$$dc_destdir" distuninstallcheck; \
	      } || { rm -rf "$$dc_destdir"; exit 1; }) \
	  && rm -rf "$$dc_destdir" \
	  && $(MAKE) $(AM_MAKEFLAGS) dist \
	  && rm -rf $(DIST_ARCHIVES) \
	  && $(MAKE) $(AM_MAKEFLAGS) distcleancheck \
	  && cd "$$am__cwd" \
	  || exit 1
	$(am__post_remove_distdir)
	@(echo "$(distdir) archives ready for distribution: "; \
	  list='$(DIST_ARCHIVES)'; for i in $$list; do echo $$i; done) | \
	  sed -e 1h -e 1s/./=/g -e 1p -e 1x -e '$$p' -e '$$x'
distuninstallcheck:
	@test -n '$(distuninstallcheck_dir)' || { \
	  echo 'ERROR: trying to run $@ with an empty' \
	       '$$(distuninstallcheck_dir)' >&2; \
	  exit 1; \
	}; \
	$(am__cd) '$(distuninstallcheck_dir)' || { \
	  echo 'ERROR: cannot chdir into $(distuninstallcheck_dir)' >&2; \
	  exit 1; \
	}; \
	test `$(am__distuninstallcheck_listfiles) | wc -l` -eq 0 \
	   || { echo "ERROR: files left after uninstall:" ; \
	        if test -n "$(DESTDIR)"; then \
	          echo "  (check DESTDIR support)"; \
	        fi ; \
	        $(distuninstallcheck_listfiles) ; \
	        exit 1; } >&2
distcleancheck: distclean
	@if test '$(srcdir)' = . ; then \
	  echo "ERROR: distcleancheck can only run from a VPATH build" ; \
	  exit 1 ; \
	fi
	@test `$(distcleancheck_listfiles) | wc -l` -eq 0 \
	  || { echo "ERROR: files left in build directory after distclean:" ; \
	       $(distcleancheck_listfiles) ; \
	       exit 1; } >&2
check-am: all-am
check: $(BUILT_SOURCES)
	$(MAKE) $(AM_MAKEFLAGS) check-recursive
all-am: Makefile
installdirs: installdirs-recursive
installdirs-am:
install: $(BUILT_SOURCES)
	$(MAKE) $(AM_MAKEFLAGS) install-recursive
install-exec: install-exec-recursive
install-data: install-data-recursive
uninstall: uninstall-recursive

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-recursive
install-strip:
	if test -z '$(STRIP)'; then \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	      install; \
	else \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	    "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'" install; \
	fi
mostlyclean-generic:

clean-generic:

distclean-generic:
	-test -z "$(CONFIG_CLEAN_FILES)" || rm -f $(CONFIG_CLEAN_FILES)
	-test . = "$(srcdir)" || test -z "$(CONFIG_CLEAN_VPATH_FILES)" || rm -f $(CONFIG_CLEAN_VPATH_FILES)

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
	-test -z "$(BUILT_SOURCES)" || rm -f $(BUILT_SOURCES)
clean: clean-recursive

clean-am: clean-generic mostlyclean-am

distclean: distclean-recursive
	-rm -f $(am__CONFIG_DISTCLEAN_FILES)
	-rm -f Makefile
distclean-am: clean-am distclean-generic distclean-tags

dvi: dvi-recursive

dvi-am:

html: html-recursive

html-am:

info: info-recursive

info-am:

install-data-am:

install-dvi: install-dvi-recursive

install-dvi-am:

install-exec-am:

install-html: install-html-recursive

install-html-am:

install-info: install-info-recursive

install-info-am:

install-man:

install-pdf: install-pdf-recursive

install-pdf-am:

install-ps: install-ps-recursive

install-ps-am:

installcheck-am:

maintainer-clean: maintainer-clean-recursive
	-rm -f $(am__CONFIG_DISTCLEAN_FILES)
	-rm -rf $(top_srcdir)/autom4te.cache
	-rm -f Makefile
maintainer-clean-am: distclean-am maintainer-clean-generic

maintainer-update-po: maintainer-update-po-recursive

maintainer-update-po-am: maintainer-update-po-local

mostlyclean: mostlyclean-recursive

mostlyclean-am: mostlyclean-generic

pdf: pdf-recursive

pdf-am:

ps: ps-recursive

ps-am:

uninstall-am:

.MAKE: $(am__recursive_targets) all check install install-am \
	install-strip

.PHONY: $(am__recursive_targets) CTAGS GTAGS TAGS all all-am \
	am--refresh check check-am clean clean-cscope clean-generic \
	cscope cscopelist-am ctags ctags-am dist dist-all dist-bzip2 \
	dist-gzip dist-hook dist-lzip dist-shar dist-tarZ dist-xz \
	dist-zip dist-zstd distcheck distclean distclean-generic \
	distclean-tags distcleancheck distdir distuninstallcheck dvi \
	dvi-am html html-am info info-am install install-am \
	install-data install-data-am install-dvi install-dvi-am \
	install-exec install-exec-am install-html install-html-am \
	install-info install-info-am install-man install-pdf \
	install-pdf-am install-ps install-ps-am install-strip \
	installcheck installcheck-am installdirs installdirs-am \
	maintainer-clean maintainer-clean-generic \
	maintainer-update-po-am maintainer-update-po-local mostlyclean \
	mostlyclean-generic pdf pdf-am ps ps-am tags tags-am uninstall \
	uninstall-am

.PRECIOUS: Makefile


# Additional dependencies for configure, due to the use of autoconf --trace.
$(srcdir)/configure: $(srcdir)/gettext-runtime/configure.ac $(srcdir)/gettext-tools/configure.ac 

distcheck-hook:
# Verify that some files are the same.
	cmp -s $(srcdir)/gettext-runtime/po/Makefile.in.in $(srcdir)/gettext-tools/po/Makefile.in.in
	cmp -s $(srcdir)/gettext-runtime/po/Rules-quot $(srcdir)/gettext-tools/po/Rules-quot
	cmp -s $(srcdir)/gettext-runtime/po/boldquot.sed $(srcdir)/gettext-tools/po/boldquot.sed
	cmp -s $(srcdir)/gettext-runtime/po/quot.sed $(srcdir)/gettext-tools/po/quot.sed
	cmp -s $(srcdir)/gettext-runtime/po/en@quot.header $(srcdir)/gettext-tools/po/en@quot.header
	cmp -s $(srcdir)/gettext-runtime/po/en@boldquot.header $(srcdir)/gettext-tools/po/en@boldquot.header
	cmp -s $(srcdir)/gettext-runtime/po/insert-header.sin $(srcdir)/gettext-tools/po/insert-header.sin
	cmp -s $(srcdir)/gettext-runtime/po/remove-potcdate.sin $(srcdir)/gettext-tools/po/remove-potcdate.sin
	cmp -s $(srcdir)/gettext-runtime/po/remove-potcdate.sin $(srcdir)/gettext-tools/examples/po/remove-potcdate.sin
	cmp -s $(srcdir)/gettext-runtime/m4/fcntl-o.m4 $(srcdir)/gettext-tools/gnulib-m4/fcntl-o.m4
	cmp -s $(srcdir)/gettext-runtime/m4/flexmember.m4 $(srcdir)/gettext-tools/gnulib-m4/flexmember.m4
	cmp -s $(srcdir)/gettext-runtime/m4/gettext.m4 $(srcdir)/gettext-tools/gnulib-m4/gettext.m4
	cmp -s $(srcdir)/gettext-runtime/m4/iconv.m4 $(srcdir)/gettext-tools/gnulib-m4/iconv.m4
	cmp -s $(srcdir)/gettext-runtime/m4/intlmacosx.m4 $(srcdir)/gettext-tools/gnulib-m4/intlmacosx.m4
	cmp -s $(srcdir)/gettext-runtime/m4/inttypes_h.m4 $(srcdir)/gettext-tools/gnulib-m4/inttypes_h.m4
	cmp -s $(srcdir)/gettext-runtime/m4/nls.m4 $(srcdir)/gettext-tools/gnulib-m4/nls.m4
	cmp -s $(srcdir)/gettext-runtime/m4/po.m4 $(srcdir)/gettext-tools/gnulib-m4/po.m4
	cmp -s $(srcdir)/gettext-runtime/m4/progtest.m4 $(srcdir)/gettext-tools/gnulib-m4/progtest.m4
	cmp -s $(srcdir)/gettext-runtime/m4/size_max.m4 $(srcdir)/gettext-tools/gnulib-m4/size_max.m4
	cmp -s $(srcdir)/gettext-runtime/m4/stdint_h.m4 $(srcdir)/gettext-tools/gnulib-m4/stdint_h.m4
	cmp -s $(srcdir)/gettext-runtime/m4/xsize.m4 $(srcdir)/gettext-tools/gnulib-m4/xsize.m4
	cmp -s $(srcdir)/gettext-runtime/libasprintf/gnulib-m4/intmax_t.m4 $(srcdir)/gettext-tools/gnulib-m4/intmax_t.m4
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/arg-nonnull.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/arg-nonnull.h | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/attribute.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/attribute.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/filename.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/filename.h | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/flexmember.h | md5sum`" = "`sed 1,19d $(srcdir)/gettext-tools/gnulib-lib/flexmember.h | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/localcharset.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/localcharset.h | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/localcharset.c | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/localcharset.c | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/localename.c | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/localename.c | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/localename-table.in.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/localename-table.h | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/localename-table.c | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/localename-table.c | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/lock.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/glthread/lock.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/lock.c | md5sum`" = "`sed -e 1,15d -e 's,glthread/,,g' $(srcdir)/gettext-tools/gnulib-lib/glthread/lock.c | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/setlocale-lock.c | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/setlocale-lock.c | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/setlocale_null.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/setlocale_null.h | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/setlocale_null.c | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/setlocale_null.c | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/threadlib.c | md5sum`" = "`sed -e 1,15d $(srcdir)/gettext-tools/gnulib-lib/glthread/threadlib.c | md5sum`"
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/verify.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/verify.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-initguard.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-initguard.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-mutex.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-mutex.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-mutex.c | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-mutex.c | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-once.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-once.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-once.c | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-once.c | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-recmutex.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-recmutex.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-recmutex.c | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-recmutex.c | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-rwlock.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-rwlock.h | md5sum`"
	test "`sed 1,15d $(srcdir)/gettext-runtime/intl/windows-rwlock.c | md5sum`" = "`sed 1,15d $(srcdir)/gettext-tools/gnulib-lib/windows-rwlock.c | md5sum`"
	cmp -s $(srcdir)/gettext-runtime/intl/printf-args.h $(srcdir)/gettext-runtime/libasprintf/printf-args.h
	cmp -s $(srcdir)/gettext-runtime/intl/printf-args.c $(srcdir)/gettext-runtime/libasprintf/printf-args.c
	cmp -s $(srcdir)/gettext-runtime/intl/printf-parse.h $(srcdir)/gettext-runtime/libasprintf/printf-parse.h
	cmp -s $(srcdir)/gettext-runtime/intl/printf-parse.c $(srcdir)/gettext-runtime/libasprintf/printf-parse.c
	cmp -s $(srcdir)/gettext-runtime/intl/verify.h $(srcdir)/gettext-runtime/libasprintf/verify.h
	test "`sed 1,18d $(srcdir)/gettext-runtime/intl/relocatable.h | md5sum`" = "`sed 1,18d $(srcdir)/gettext-tools/gnulib-lib/relocatable.h | md5sum`"
	test "`sed 1,18d $(srcdir)/gettext-runtime/intl/relocatable.c | md5sum`" = "`sed 1,18d $(srcdir)/gettext-tools/gnulib-lib/relocatable.c | md5sum`"
	cmp -s $(srcdir)/gettext-runtime/intl/vasnprintf.h $(srcdir)/gettext-runtime/libasprintf/vasnprintf.h
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/vasnprintf.c | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/vasnprintf.c | md5sum`"
	cmp -s $(srcdir)/gettext-runtime/intl/vasnprintf.c $(srcdir)/gettext-runtime/libasprintf/vasnprintf.c
	cmp -s $(srcdir)/gettext-runtime/intl/xsize.h $(srcdir)/gettext-runtime/libasprintf/xsize.h
	test "`sed 1,16d $(srcdir)/gettext-runtime/intl/xsize.h | md5sum`" = "`sed 1,16d $(srcdir)/gettext-tools/gnulib-lib/xsize.h | md5sum`"
	cmp -s $(srcdir)/gettext-runtime/man/help2man $(srcdir)/gettext-tools/man/help2man
	cmp -s $(srcdir)/gettext-runtime/man/x-to-1.in $(srcdir)/gettext-tools/man/x-to-1.in
	cmp -s $(srcdir)/libtextstyle/m4/libtextstyle.m4 $(srcdir)/gettext-tools/gnulib-m4/libtextstyle.m4
	cmp -s $(srcdir)/gettext-tools/examples/hello-java-awt/m4/TestAWT.java $(srcdir)/gettext-tools/examples/hello-java-swing/m4/TestAWT.java
	cmp -s $(srcdir)/gettext-tools/examples/hello-java-awt/m4/TestAWT.class $(srcdir)/gettext-tools/examples/hello-java-swing/m4/TestAWT.class
	test "`sed 1,15d $(srcdir)/gnulib-local/lib/alloca.in.h | md5sum`" = "`sed 1,15d $(srcdir)/gettext-runtime/libasprintf/alloca.in.h | md5sum`"
# Verify that all files have appropriate copyright headers.
	if test -d '$(distdir)'; then $(srcdir)/check-copyright-headers '$(distdir)'; fi
$(top_srcdir)/.version:
	echo $(VERSION) > $@-t && mv $@-t $@
dist-hook: gen-ChangeLogs
	echo $(VERSION) > $(distdir)/.tarball-version
.PHONY: gen-ChangeLogs
gen-ChangeLogs:
	$(AM_V_GEN)if test -d .git; then				\
	  log_fix="$(srcdir)/build-aux/git-log-fix";			\
	  test -e "$$log_fix"						\
	    && amend_git_log="--amend=$$log_fix"			\
	    || amend_git_log=;						\
	  for d in . gettext-runtime/intl gettext-runtime/po		\
		gettext-tools/po; do					\
	    test "$$d" = "."						\
	      && cldir="$(distdir)"					\
	      || cldir="$(distdir)/$$d";				\
	    $(top_srcdir)/build-aux/gitlog-to-changelog			\
	      $$amend_git_log --since=$(gen_start_date) -- "$$d"	\
		> "$$cldir/cl-t" &&					\
	    { rm -f "$$cldir/ChangeLog" &&				\
	      mv "$$cldir/cl-t" "$$cldir/ChangeLog"; };			\
	  done;								\
	fi

# PO files update.

maintainer-update-po-local: $(top_builddir)/config.status

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
