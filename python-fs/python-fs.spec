%global srcname pyfilesystem2
%global pkgname fs

Name:           python-%{pkgname}
Version:        2.3.0
Release:        1%{?dist}
Summary:        Python's Filesystem abstraction layer

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/PyFilesystem/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests:
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-pytz
BuildRequires:  python2-psutil
BuildRequires:  python2-typing
BuildRequires:  python2-appdirs
BuildRequires:  python2-coverage
BuildRequires:  python2-coveralls
BuildRequires:  python2-pyftpdlib
BuildRequires:  python2-backports-os >= 0.1.1
Requires: python2-six
Requires: python2-pytz
Requires: python2-enum34
Requires: python2-typing
Requires: python2-appdirs
Requires: python2-backports-os >= 0.1.1

%description -n python2-%{pkgname}
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.


%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For tests:
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-pytz
BuildRequires:  python3-psutil
BuildRequires:  python3-appdirs
BuildRequires:  python3-coverage
BuildRequires:  python3-coveralls
BuildRequires:  python3-pyftpdlib
Requires: python3-six
Requires: python3-pytz
Requires: python3-appdirs

%description -n python3-%{pkgname}
Think of PyFilesystem's FS objects as the next logical step to Python's file
objects. In the same way that file objects abstract a single file, FS objects
abstract an entire filesystem.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
# Skipping tests for Fedora 28
%if 0%{?fedora} != 28
export LANG=C.UTF-8
%{__python2} setup.py test
%{__python3} setup.py test
%endif

%files -n python2-%{pkgname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{pkgname}-*.egg-info
%{python2_sitelib}/%{pkgname}

%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pkgname}-*.egg-info
%{python3_sitelib}/%{pkgname}

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 2.3.0-1
- First spec for version 2.3.0

