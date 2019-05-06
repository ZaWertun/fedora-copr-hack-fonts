%global srcname backports.os
%global pkgname backports-os

Name:           python-%{pkgname}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Backport of new features in Python's os module

License:        Python
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/pjdelport/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This package provides backports of new features in Python's os module under
the backports namespace.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-future
Requires: python2-future
Requires: python2-backports

%description -n python2-%{pkgname}
This package provides backports of new features in Python's os module under
the backports namespace.


%prep
%autosetup -n %{srcname}-%{version}

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py2_build

%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py2_install
rm -v %{buildroot}%{python2_sitelib}/backports/__init__.*

%check
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{__python2} setup.py test

%files -n python2-%{pkgname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/backports/os.*

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.1.1-1
- First spec for version 0.1.1



