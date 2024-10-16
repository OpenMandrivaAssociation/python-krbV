Name: python-krbV
Version: 1.0.90
Release: 3
Summary: Python extension module for Kerberos 5


Group: Development/Python
License: LGPLv2+

URL: https://fedorahosted.org/python-krbV/
Source: http://fedorahosted.org/python-krbV/attachment/wiki/Releases/python-krbV-%{version}.tar.bz2

BuildRequires:  python-devel
BuildRequires: krb5-devel
BuildRequires: gawk

%description
python-krbV allows python programs to use Kerberos 5 authentication and
security.

%prep
%setup -q

%build
export LIBNAME="%{_lib}"
export CFLAGS="%{optflags} -Wextra"
%configure2_5x
%make

%install
%makeinstall

%files
%doc README COPYING krbV-code-snippets.py
%{py_platsitedir}/krbVmodule.so


