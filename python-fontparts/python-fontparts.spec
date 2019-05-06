%global srcname fontParts
%global pkgname fontparts

Name:           python-%{pkgname}
Version:        0.8.5
Release:        1%{?dist}
Summary:        The replacement for RoboFab

License:        MIT
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/robotools/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An API for interacting with the parts of fonts during the font development
process. FontParts is the replacement for RoboFab.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-defcon >= 0.6.0
# For tests:
BuildRequires:  python2-fontMath >= 0.4.9

Requires: python2-fonttools >= 3.37.3
Requires: python2-defcon >= 0.6.0

%description -n python2-%{pkgname}
An API for interacting with the parts of fonts during the font development
process. FontParts is the replacement for RoboFab.


%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-defcon >= 0.6.0
# For tests:
BuildRequires:  python3-fontMath >= 0.4.9

Requires: python3-fonttools >= 3.37.3
Requires: python3-defcon >= 0.6.0

%description -n python3-%{pkgname}
An API for interacting with the parts of fonts during the font development
process. FontParts is the replacement for RoboFab.


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
# No checks because of circular dependency: fontPens <-> fontParts

%files -n python2-%{pkgname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/%{srcname}

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.8.5-1
- First spec for version 0.8.5

