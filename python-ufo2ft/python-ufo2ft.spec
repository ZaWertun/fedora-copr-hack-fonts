%global pkgname ufo2ft

Name:    python-%{pkgname}
Version: 2.7.0
Release: 1%{?dist}
Summary: A bridge from UFOs to FontTools objects (and therefore, OTFs and TTFs)

License: MIT
URL:     https://pypi.org/project/%{pkgname}
Source0: https://github.com/googlei18n/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildArch: noarch

%description
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to generate
OpenType font binaries from UFOs without the FDK dependency.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-setuptools_scm
BuildRequires: python2-pytest-runner
BuildRequires: python2-enum34
BuildRequires: python2-fs
BuildRequires: python2-ufolib2
BuildRequires: python2-unicodedata2
BuildRequires: python2-cu2qu >= 1.6.5
BuildRequires: python2-defcon >= 0.6.0
BuildRequires: python2-compreffor >= 0.4.6
BuildRequires: python2-skiapathops
BuildRequires: python2-booleanoperations >= 0.8.2
Requires: python2-enum34
Requires: python2-ufolib2
Requires: python2-cu2qu >= 1.6.5
Requires: python2-defcon >= 0.6.0
Requires: python2-compreffor >= 0.4.6
Requires: python2-skiapathops >= 0.2.0
Requires: python2-unicodedata2
Requires: python2-booleanoperations >= 0.8.2

%description -n python2-%{pkgname}
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to generate
OpenType font binaries from UFOs without the FDK dependency.


%package -n python3-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-pytest-runner
BuildRequires: python3-fs
BuildRequires: python3-ufolib2
BuildRequires: python3-cu2qu >= 1.6.5
BuildRequires: python3-defcon >= 0.6.0
BuildRequires: python3-compreffor >= 0.4.6
BuildRequires: python3-skiapathops
BuildRequires: python3-booleanoperations >= 0.8.2
Requires: python3-ufolib2
Requires: python3-cu2qu >= 1.6.5
Requires: python3-defcon >= 0.6.0
Requires: python3-compreffor >= 0.4.6
Requires: python3-skiapathops >= 0.2.0
Requires: python3-booleanoperations >= 0.8.2

%description -n python3-%{pkgname}
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to generate
OpenType font binaries from UFOs without the FDK dependency.


%prep
%autosetup -n %{pkgname}-%{version}

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
%ifarch x86_64
# Tests is broken on non x86_64 arch:
#   ValueError: timestamp out of range for platform time_t
#   (tests/fontInfoData_test.py:198: ValueError)
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{__python2} setup.py test
%{__python3} setup.py test
%endif

%files -n python2-%{pkgname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pkgname}
%{python2_sitelib}/%{pkgname}-*.egg-info

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{pkgname}-*.egg-info

%changelog
* Fri Feb 08 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 2.7.0-1
- First spec for version 2.7.0

