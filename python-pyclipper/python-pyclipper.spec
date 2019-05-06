%global srcname pyclipper

Name:           python-%{srcname}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Cython wrapper for the C++ translation of the Angus Johnson's Clipper library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/greginvm/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Remove embedded libraries and use system ones instead
# See https://github.com/greginvm/pyclipper/issues/10
Patch0:         00-use-system-polyclipping.patch

BuildRequires:  polyclipping-devel

%description
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-runner
BuildRequires:  python2-Cython
BuildRequires:  python2-unittest2
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-setuptools_scm_git_archive

%description -n python2-%{srcname}
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-Cython
BuildRequires:  python3-unittest2
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-setuptools_scm_git_archive

%description -n python3-%{srcname}
Pyclipper is a Cython wrapper exposing public functions and classes of the C++
translation of the Angus Johnson's Clipper library.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove upstream egg-info
rm -rf pyclipper.egg-info
# Since there are no .git dir, there is no need to exclude files in MANIFEST.in
sed -i '/^exclude/d' MANIFEST.in

%build
%py2_build
# We want to cython again with cython3
rm -rf pyclipper/pyclipper.cpp
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{srcname}-*.egg-info
%{python2_sitearch}/*.so

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}-*.egg-info
%{python3_sitearch}/*.so

%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.7

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.1.0-2
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 16 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.0-1
- Update version
- Remove patch to use new polyclipping version (merged upstream)
- Fix patch to use system libraries due to new version modifications

* Mon Oct 23 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-4
- Do not Requires polyclipping
- Remove upstream egg-info before building
- Cython cpp file before each python version build

* Sun Oct 22 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-3
- Patch sources for compatibility with polyclipping 6.4.2

* Sun Jul 16 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-2
- Remove embedded libraries and use system ones instead
- Fix date format in changelog

* Wed Apr 05 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.6-1
- Initial package
