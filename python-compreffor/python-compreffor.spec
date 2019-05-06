%global pkgname compreffor

Name:    python-%{pkgname}
Version: 0.4.6.post1
Release: 1%{?dist}
Summary: A CFF table subroutinizer for FontTools

License: ASL 2.0
URL:     https://pypi.org/project/%{pkgname}
Source0: https://github.com/googlei18n/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz

%description
A CFF table subroutinizer for FontTools.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires: gcc-c++
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pytest-runner
BuildRequires: python2-fonttools >= 3.22.0
Requires: python2-fonttools >= 3.22.0

%description -n python2-%{pkgname}
A CFF table subroutinizer for FontTools.


%package -n python3-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest-runner
BuildRequires: python3-fonttools >= 3.22.0
Requires: python3-fonttools >= 3.22.0

%description -n python3-%{pkgname}
A CFF table subroutinizer for FontTools.


%prep
%autosetup -n %{pkgname}-%{version}

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
%{python2_sitearch}/%{pkgname}
%{python2_sitearch}/%{pkgname}-*.egg-info

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pkgname}
%{python3_sitearch}/%{pkgname}-*.egg-info
%{_bindir}/%{pkgname}

%changelog
* Fri Feb 08 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.4.6.post1-1
- First spec for version 0.4.6.post1


