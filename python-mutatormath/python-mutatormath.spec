%global srcname MutatorMath
# upstream is not consistent on uppercase usage
%global libname mutatorMath
%global pkgname mutatormath

Name:           python-%{pkgname}
Version:        2.1.2
Release:        5%{?dist}
Summary:        Python library for piecewise linear interpolation in multiple dimensions

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/LettError/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
MutatorMath is a Python library for the calculation of piecewise linear
interpolations in n-dimensions with any number of masters. It was developed for
interpolating data related to fonts, but if can handle any arithmetic object.

%package -n python2-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-defcon
BuildRequires:  python2-fs
BuildRequires:  python2-fontMath
Requires: python2-defcon
Requires: python2-fontMath

%description -n python2-%{pkgname}
MutatorMath is a Python library for the calculation of piecewise linear
interpolations in n-dimensions with any number of masters. It was developed for
interpolating data related to fonts, but if can handle any arithmetic object.


%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-fs
BuildRequires:  python3-defcon
BuildRequires:  python3-fontMath
Requires: python3-defcon
Requires: python3-fontMath

%description -n python3-%{pkgname}
MutatorMath is a Python library for the calculation of piecewise linear
interpolations in n-dimensions with any number of masters. It was developed for
interpolating data related to fonts, but if can handle any arithmetic object.


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
%doc README.rst
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{srcname}-*.egg-info

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{srcname}-*.egg-info

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 2.1.2-5
- Version 2.1.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.1.0-1
- Update version

* Sat Oct 07 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.6-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.4-1
- Update version

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 2.0.3-1
- Initial package
