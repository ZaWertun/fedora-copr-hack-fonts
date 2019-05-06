%global srcname xmldiff

Name:           python-%{srcname}
Version:        2.2
Release:        1%{?dist}
Summary:        A library and command line utility for diffing xml

License:        MIT
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/Shoobx/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
xmldiff is a library and a command-line utility for making diffs out of XML.


%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-lxml
# For tests:
BuildRequires:  python2-six
Requires: python2-lxml

%description -n python2-%{srcname}
xmldiff is a library and a command-line utility for making diffs out of XML.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-lxml
# For tests:
BuildRequires:  python3-six
Requires: python3-lxml

%description -n python3-%{srcname}
xmldiff is a library and a command-line utility for making diffs out of XML.


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
%license LICENSE.txt
%doc README.txt
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-*.egg-info

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info
%{_bindir}/%{srcname}

%changelog
* Sat Feb 09 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 2.2-1
- First spec for version 2.2

