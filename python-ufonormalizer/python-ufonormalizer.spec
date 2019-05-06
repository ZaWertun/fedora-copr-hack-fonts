%global srcname ufoNormalizer
%global pkgname ufonormalizer

Name:           python-%{pkgname}
Version:        0.3.6
Release:        1%{?dist}
Summary:        A tool that will normalize the XML and other data inside of a UFO

License:        BSD
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/unified-font-object/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Provides a standard formatting so that there are meaningful diffs in version
control rather than formatting noise.


%package -n python2-%{pkgname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{pkgname}
Provides a standard formatting so that there are meaningful diffs in version
control rather than formatting noise.


%package -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pkgname}
Provides a standard formatting so that there are meaningful diffs in version
control rather than formatting noise.


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
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/%{pkgname}-*.egg-info
%{python2_sitelib}/%{pkgname}.*

%files -n python3-%{pkgname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pkgname}-*.egg-info
%{python3_sitelib}/%{pkgname}.*
%{python3_sitelib}/__pycache__/*
%{_bindir}/%{pkgname}

%changelog
* Sat Feb 09 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.3.6-1
- First spec for version 0.3.6


