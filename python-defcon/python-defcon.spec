%global srcname defcon

Name:           python-%{srcname}
Version:        0.6.0
Release:        5%{?dist}
Summary:        A set of flexible objects for representing UFO data

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/typesupply/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Defcon is a set of UFO (Unified Font Object) based objects optimized for use in
font editing applications. Defcon implements UFO3 as described by the UFO font
format.

%package -n python2-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
BuildRequires:  python2-fonttools
BuildRequires:  python2-fs
BuildRequires:  python2-lxml
# For tests:
BuildRequires:  python2-unicodedata2
Requires: python2-lxml
Requires: python2-fonttools

%description -n python2-%{srcname}
Defcon is a set of UFO (Unified Font Object) based objects optimized for use in
font editing applications. Defcon implements UFO3 as described by the UFO font
format.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-fonttools
BuildRequires:  python3-fs
BuildRequires:  python3-lxml
# For tests:
BuildRequires:  python3-unicodedata2
Requires: python3-lxml
Requires: python3-fonttools

%description -n python3-%{srcname}
Defcon is a set of UFO (Unified Font Object) based objects optimized for use in
font editing applications. Defcon implements UFO3 as described by the UFO font
format.


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

%files -n python2-%{srcname}
%license License.txt
%doc README.rst
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/%{srcname}

%files -n python3-%{srcname}
%license License.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.6.0-5
- Added deps to run tests offline

* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.6.0-4
- Version 0.6.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.1-1
- Update version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 7 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.5-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 7 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.4-1
- Update version

* Wed May 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.3-1
- Update version

* Mon Apr 3 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.2-1
- Update version

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-3
- Depends on the lowercase version of ufolib

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-2
- Improve %%description
- Remove the sum global

* Sat Mar 18 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-1
- Initial package
