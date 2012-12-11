
Name: python-krbV
Version: 1.0.90
Release: 1
Summary: Python extension module for Kerberos 5

Group: Development/Python
License: LGPLv2+

URL: http://fedorahosted.org/python-krbV/
Source: http://fedorahosted.org/python-krbV/attachment/wiki/Releases/python-krbV-%{version}.tar.bz2

%py_requires -d
BuildRequires: krb5-devel
BuildRequires: gawk

%description
python-krbV allows python programs to use Kerberos 5 authentication and security.

%prep
%setup -q

%build
export LIBNAME="%{_lib}"
export CFLAGS="%{optflags} -Wextra"
%configure2_5x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%doc README COPYING krbV-code-snippets.py
%{python_sitearch}/krbVmodule.so


%changelog
* Wed Aug 29 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.90-1
+ Revision: 816013
- Update previous package import.

  + Antoine Ginies <aginies@mandriva.com>
    - import python-krbV

