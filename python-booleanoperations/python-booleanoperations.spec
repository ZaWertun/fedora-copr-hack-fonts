%global srcname booleanOperations
%global pkgname booleanoperations

Name:           python-%{pkgname}
Version:        0.8.2
Release:        4%{?dist}
Summary:        Boolean operations on paths

License:        MIT
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/typemytype/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Boolean operations on paths based on a super fast polygon clipper library by
Angus Johnson.

%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
BuildRequires:  python2-fonttools
BuildRequires:  python2-pyclipper
# For tests:
BuildRequires:  python2-fontpens
BuildRequires:  python2-fontparts
BuildRequires:  python2-defcon
BuildRequires:  python2-fs
Requires: python2-fonttools
Requires: python2-pyclipper

%description -n python2-%{pkgname}
Boolean operations on paths based on a super fast polygon clipper library by
Angus Johnson.

%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-fonttools
BuildRequires:  python3-pyclipper
# For tests:
BuildRequires:  python3-fontpens
BuildRequires:  python3-fontparts
BuildRequires:  python3-defcon
BuildRequires:  python3-fs
Requires: python3-fonttools
Requires: python3-pyclipper

%description -n python3-%{pkgname}
Boolean operations on paths based on a super fast polygon clipper library by
Angus Johnson.


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
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/%{srcname}

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.8.2-4
- Version 0.8.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.8.0-1
- Update version

* Mon Aug 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.1-1
- Update version
- Use lowecase string for package name

* Mon Apr 10 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.0-1
- Initial package
