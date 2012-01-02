%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-curses
Version:        1.0.3
Release:        6.1%{?dist}
Summary:        OCaml bindings for ncurses

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://savannah.nongnu.org/projects/ocaml-tmk/
Source0:        http://download.savannah.gnu.org/releases/ocaml-tmk/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 3.10.2
BuildRequires:  ocaml-findlib-devel, ncurses-devel
BuildRequires:  gawk

# Doesn't include a configure script, so we have to make one.
BuildRequires:  autoconf, automake, libtool


%description
OCaml bindings for ncurses.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q

autoreconf


%build
%configure --enable-widec
make all opt

strip dllcurses_stubs.so


%install
rm -rf $RPM_BUILD_ROOT

export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocamlfind install curses META *.cmi *.cmx *.cma *.cmxa *.a *.so *.mli


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/ocaml/curses
%if %opt
%exclude %{_libdir}/ocaml/curses/*.a
%exclude %{_libdir}/ocaml/curses/*.cmxa
%exclude %{_libdir}/ocaml/curses/*.cmx
%endif
%exclude %{_libdir}/ocaml/curses/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%defattr(-,root,root,-)
%doc COPYING
%if %opt
%{_libdir}/ocaml/curses/*.a
%{_libdir}/ocaml/curses/*.cmxa
%{_libdir}/ocaml/curses/*.cmx
%endif
%{_libdir}/ocaml/curses/*.mli


%changelog
* Mon Jan 11 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-6.1
- Replace %%define with %%global.
- Use upstream RPM 4.8 OCaml dependency generator.

* Tue Oct  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-6.fc12.1
- Use ncursesw for wide character support.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-5
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-3
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-2
- Rebuild for OCaml 3.11.0

* Mon Nov 17 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-1
- Major version leap to the latest, supported, released version.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.1-8
- Rebuild for OCaml 3.10.2

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 0.1-7.20020319
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.1-6.20020319
- Rebuild for OCaml 3.10.1

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.1-5.20020319
- Force rebuild because of updated requires/provides scripts in OCaml.

* Thu Aug 30 2007 Richard W.M. Jones <rjones@redhat.com> - 0.1-4.20020319
- Force rebuild because of changed BRs in base OCaml.

* Mon Aug 24 2007 Richard W.M. Jones <rjones@redhat.com> - 0.1-3.20020319
- License is LGPL 2.1 or any later version.

* Mon Aug  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.1-2.20020319
- The archive is called 'mlcurses.*'.

* Mon Aug  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.1-1.20020319
- Initial RPM release.
