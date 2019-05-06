%global srcname unicodedata2
%global pkgname unicodedata2
%global srcpost -2

Name:           python-%{pkgname}
Version:        11.0.0
Release:        1%{?dist}
Summary:        Unicodedata backport/updates

License:        ASL 2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/robotools/%{srcname}/archive/%{version}/%{srcname}-%{version}%{?srcpost}.tar.gz

%description
The versions of this package match unicode versions, so unicodedata2==11.0.0
is data from unicode 11.0.0. Additionally this backports support for named
aliases and named sequences to python2.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  gcc
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests:

%description -n python2-%{pkgname}
The versions of this package match unicode versions, so unicodedata2==11.0.0
is data from unicode 11.0.0. Additionally this backports support for named
aliases and named sequences to python2.


%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For tests:

%description -n python3-%{pkgname}
The versions of this package match unicode versions, so unicodedata2==11.0.0
is data from unicode 11.0.0. Additionally this backports support for named
aliases and named sequences to python2.


%prep
%autosetup -n %{srcname}-%{version}%{?srcpost}

%build
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py2_build
%py3_build

%install
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py2_install
%py3_install

%check
# Here we set upstream version based on setuptools_scm documentation
# this is done to avoid the following error:
# LookupError: setuptools-scm was unable to detect version
# since we are not importing a .git repository in the tarball
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pkgname}
%license LICENSE
%doc README.md
%{python2_sitearch}/%{srcname}-*.egg-info
%{python2_sitearch}/%{srcname}*.so

%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{srcname}-*.egg-info
%{python3_sitearch}/%{srcname}*.so

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 11.0.0-1
- First spec for version 11.0.0

