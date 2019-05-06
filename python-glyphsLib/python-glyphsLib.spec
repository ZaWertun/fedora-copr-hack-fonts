%global srcname glyphsLib

Name:    python-%{srcname}
Version: 3.2.0
Release: 5%{?dist}
Summary: A bridge from Glyphs source files to UFOs

License: ASL 2.0
URL:     https://pypi.org/project/%{srcname}
Source0: https://github.com/googlei18n/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
This library provides a bridge from Glyphs source files (.glyphs) to UFOs
(Unified Font Object).

%package -n python2-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-setuptools_scm
BuildRequires: python2-pytest
BuildRequires: python2-pytest-runner
BuildRequires: python2-fonttools
BuildRequires: python2-mutatormath
BuildRequires: python2-mock
BuildRequires: python2-xmldiff
BuildRequires: python2-ufonormalizer >= 0.3.2
BuildRequires: python2-fs
Requires: python2-fonttools
Requires: python2-defcon
Requires: python2-mutatormath

%description -n python2-%{srcname}
This library provides a bridge from Glyphs source files (.glyphs) to UFOs
(Unified Font Object).


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-pytest
BuildRequires: python3-pytest-runner
BuildRequires: python3-fonttools
BuildRequires: python3-mutatormath
BuildRequires: python3-mock
BuildRequires: python3-xmldiff
BuildRequires: python3-ufonormalizer >= 0.3.2
BuildRequires: python3-fs
Requires: python3-fonttools
Requires: python3-defcon
Requires: python3-mutatormath

%description -n python3-%{srcname}
This library provides a bridge from Glyphs source files (.glyphs) to UFOs
(Unified Font Object).


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
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-*.egg-info

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CONTRIBUTING.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info
%{_bindir}/glyphs2ufo
%{_bindir}/ufo2glyphs

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.2.0-5
- Version 3.2.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.2.1-2
- Include new subdirectories

* Wed Feb 21 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 2.2.1-1
- Update version
- Remove patch merged upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.7.5-2
- Apply patch to remove shebangs from non-executable modules

* Thu Jul 13 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.7.5-1
- Update version
- Change package name to use upstream cammelcase

* Mon Apr 10 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.6.0-1
- Update version
- Add pythonX-mock BR

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.5.2-1
- Initial package
