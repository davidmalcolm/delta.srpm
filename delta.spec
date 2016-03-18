Name:           delta
Version:        2006.08.03
Release:        1%{?dist}
Summary:        Tool for automatically minimizing "interesting" files e.g. bug reproducers

License:        BSD
URL:            http://delta.tigris.org/
Source0:        http://delta.tigris.org/files/documents/3103/33566/delta-2006.08.03.tar.gz
Patch1:         add-install.patch

BuildRequires:  make
BuildRequires:  flex
Requires:       perl

%description
Delta assists you in minimizing "interesting" files subject to a
test of their interestingness.  For example, given a large input
file that causes your program to exhibit a bug, it can reduce
the input file to a substring that exhibits the same bug.


%prep
%setup -q
%patch1 -p1 -b .install
rm topformflat.c

%build
make %{?_smp_mflags}
make check


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
%make_install


%files
%doc Readme
%license License.txt
%{_bindir}/delta
%{_bindir}/multidelta
%{_bindir}/topformflat

%changelog
* Fri Mar 18 2016 David Malcolm <dmalcolm@redhat.com> - 2006.08.03-1
- initial package
