%global srcname cu2qu

Name:           python-%{srcname}
Version:        1.6.5
Release:        5%{?dist}
Summary:        Cubic-to-quadratic bezier curve conversion

License:        ASL 2.0
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/googlei18n/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This library provides functions which take in UFO (Unified Font Object) objects
(Defcon Fonts or Robofab RFonts) and converts any cubic curves to quadratic.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  gcc
BuildRequires:  python2-Cython
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
BuildRequires:  python2-coverage
BuildRequires:  python2-defcon >= 0.6.0
BuildRequires:  python2-fonttools >= 3.32.0
BuildRequires:  python2-fs >= 2.2.0
Requires: python2-fonttools >= 3.32.0
Requires: python2-defcon >= 0.6.0

%description -n python2-%{srcname}
This library provides functions which take in UFO (Unified Font Object) objects
(Defcon Fonts or Robofab RFonts) and converts any cubic curves to quadratic.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-coverage
BuildRequires:  python3-defcon >= 0.6.0
BuildRequires:  python3-fonttools >= 3.32.0
BuildRequires:  python3-fs >= 2.2.0
Requires: python3-fonttools >= 3.32.0
Requires: python3-defcon >= 0.6.0

%description -n python3-%{srcname}
This library provides functions which take in UFO (Unified Font Object) objects
(Defcon Fonts or Robofab RFonts) and converts any cubic curves to quadratic.


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

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%{python2_sitearch}/%{srcname}-*.egg-info
%{python2_sitearch}/%{srcname}

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%{python3_sitearch}/%{srcname}-*.egg-info
%{python3_sitearch}/%{srcname}
%{_bindir}/%{srcname}

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.6.5-5
- Version 1.6.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.7

* Wed Apr 11 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.0-2
- Ship cu2qu binary

* Wed Apr 11 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.0-1
- Update version

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.0-3
- Remove test file from package

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.0-2
- Add python-defcon to BRs

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.4.0-1
- Update version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.2.0-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.1-1
- Initial package
