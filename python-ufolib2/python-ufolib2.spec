%global srcname ufoLib2
%global pkgname ufolib2

Name:    python-%{pkgname}
Version: 0.3.0
Release: 1%{?dist}
Summary: ufoLib2 is a UFO font library

License: ASL 2.0
URL:     https://pypi.python.org/pypi/%{srcname}
Source0: https://github.com/fonttools/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
ufoLib2 is a UFO font library.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-setuptools_scm
BuildRequires: python2-lxml
BuildRequires: python2-enum34
BuildRequires: python2-attrs >= 18.2.0
BuildRequires: python2-typing >= 3.6.4
BuildRequires: python2-fonttools >= 3.34.0
BuildRequires: python2-singledispatch >= 3.4.0.3
Requires: python2-lxml
Requires: python2-enum34
Requires: python2-attrs >= 18.2.0
Requires: python2-typing >= 3.6.4
Requires: python2-fonttools >= 3.34.0
Requires: python2-singledispatch >= 3.4.0.3

%description -n python2-%{pkgname}
ufoLib2 is a UFO font library.


%package -n python3-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-lxml
BuildRequires: python3-attrs >= 18.2.0
BuildRequires: python3-fonttools >= 3.34.0
Requires: python3-lxml
Requires: python3-attrs >= 18.2.0
Requires: python3-fonttools >= 3.34.0

%description -n python3-%{pkgname}
ufoLib2 is a UFO font library.


%prep
%autosetup -n %{srcname}-%{version}

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
%dir %{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/%{srcname}

%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%dir %{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Fri Feb 08 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3.0-1
- First spec for version 0.3.0

