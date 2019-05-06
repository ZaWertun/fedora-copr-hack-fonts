%global srcname fontPens
%global pkgname fontpens

Name:           python-%{pkgname}
Version:        0.2.4
Release:        1%{?dist}
Summary:        A collection of classes implementing the pen protocol for manipulating glyphs

License:        BSD
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/robotools/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A collection of classes implementing the pen protocol for manipulating glyphs.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests:
BuildRequires:  python2-fonttools >= 3.32.0
BuildRequires:  python2-pytest-runner

Requires: python2-fonttools >= 3.32.0

%description -n python2-%{pkgname}
A collection of classes implementing the pen protocol for manipulating glyphs.


%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For tests:
BuildRequires:  python3-fonttools >= 3.32.0
BuildRequires:  python3-pytest-runner

Requires: python3-fonttools >= 3.32.0

%description -n python3-%{pkgname}
A collection of classes implementing the pen protocol for manipulating glyphs.


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
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/%{srcname}

%files -n python3-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.2.4-1
- First spec for version 0.2.4

