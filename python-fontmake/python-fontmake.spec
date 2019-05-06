%global pkgname fontmake

Name:    python-%{pkgname}
Version: 1.9.1
Release: 1%{?dist}
Summary: Compile fonts from sources (UFO, Glyphs) to binary (OpenType, TrueType)

License: ASL 2.0
URL:     https://pypi.org/project/%{pkgname}
Source0: https://github.com/googlei18n/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildArch: noarch

%description
This library provides a wrapper for several other Python libraries which
together compile fonts from various sources (.glyphs, .ufo) into binaries
(.otf, .ttf).


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-setuptools_scm
BuildRequires: python2-mock
BuildRequires: python2-lxml
BuildRequires: python2-defcon
BuildRequires: python2-ufo2ft >= 2.7.0
BuildRequires: python2-glyphsLib >= 3.2.0
BuildRequires: python2-mutatormath >= 2.1.2
BuildRequires: python2-booleanoperations >= 0.8.2
Requires: python2-lxml
Requires: python2-cu2qu >= 1.6.5
Requires: python2-defcon >= 0.6.0
Requires: python2-ufo2ft >= 2.7.0
Requires: python2-fonttools >= 3.37.3
Requires: python2-glyphsLib >= 3.2.0
Requires: python2-setuptools
Requires: python2-mutatormath >= 2.1.2
Requires: python2-booleanoperations >= 0.8.2

%description -n python2-%{pkgname}
This library provides a wrapper for several other Python libraries which
together compile fonts from various sources (.glyphs, .ufo) into binaries
(.otf, .ttf).


%package -n python3-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-lxml
BuildRequires: python3-defcon
BuildRequires: python3-ufo2ft >= 2.7.0
BuildRequires: python3-glyphsLib >= 3.2.0
BuildRequires: python3-mutatormath >= 2.1.2
BuildRequires: python3-booleanoperations >= 0.8.2
Requires: python3-lxml
Requires: python3-cu2qu >= 1.6.5
Requires: python3-defcon >= 0.6.0
Requires: python3-ufo2ft >= 2.7.0
Requires: python3-fonttools >= 3.37.3
Requires: python3-glyphsLib >= 3.2.0
Requires: python3-setuptools
Requires: python3-mutatormath >= 2.1.2
Requires: python3-booleanoperations >= 0.8.2

%description -n python3-%{pkgname}
This library provides a wrapper for several other Python libraries which
together compile fonts from various sources (.glyphs, .ufo) into binaries
(.otf, .ttf).


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
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pkgname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%{python2_sitelib}/%{pkgname}
%{python2_sitelib}/%{pkgname}-*.egg-info

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{pkgname}-*.egg-info
%{_bindir}/%{pkgname}

%changelog
* Fri Feb 08 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.9.1-1
- First spec for version 1.9.1

