%global srcname skia-pathops
%global pkgname skiapathops
%global eggname skia_pathops
%global dirname pathops

Name:    python-%{pkgname}
Version: 0.2.0.post2
Release: 1%{?dist}
Summary: Python bindings for the Skia library's Path Ops

License: BSD
URL:     https://pypi.org/project/%{srcname}
Source0: https://files.pythonhosted.org/packages/10/16/a7f05773cdd9bbff6fd322a941e969f1b5fd525c99f7f173513fdd9b8576/%{srcname}-%{version}.zip

%description
Python bindings for the Google Skia library's Path Ops module, performing
boolean operations on paths (intersection, union, difference, xor).


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires: gcc-c++
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-setuptools_scm
BuildRequires: python2-pytest-runner
BuildRequires: python2-Cython

%description -n python2-%{pkgname}
Python bindings for the Google Skia library's Path Ops module, performing
boolean operations on paths (intersection, union, difference, xor).


%package -n python3-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-pytest-runner
BuildRequires: python3-Cython

%description -n python3-%{pkgname}
Python bindings for the Google Skia library's Path Ops module, performing
boolean operations on paths (intersection, union, difference, xor).


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pkgname}
%license LICENSE
%doc README.md
%{python2_sitearch}/%{eggname}-*.egg-info
%{python2_sitearch}/%{dirname}

%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{eggname}-*.egg-info
%{python3_sitearch}/%{dirname}

%changelog
* Fri Feb 08 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.2.0.post2-1
- First spec for version 0.2.0.post2


