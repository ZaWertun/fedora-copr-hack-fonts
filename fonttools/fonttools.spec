%global pypi_name fonttools
%global desc \
FontTools/TTX is a library to manipulate font files from Python. It supports \
reading and writing of TrueType/OpenType fonts, reading and writing of AFM \
files, reading (and partially writing) of PS Type 1 fonts. The package also \
contains a tool called “TTX” which converts TrueType/OpenType fonts to and \
from an XML-based format.

Name:           fonttools
Version:        3.37.3
Release:        2%{?dist}
Summary:        Tools to manipulate font files
License:        MIT
URL:            https://github.com/%{name}/%{name}/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz

Requires:       python3-fonttools
BuildArch:      noarch
Provides:       ttx = %{version}-%{release}

%description
%{desc}

%package -n python2-fonttools
Summary:        Python 2 fonttools library
%{?python_provide:%python_provide python2-%{name}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools_scm
BuildRequires:  numpy
BuildRequires:  python2-unicodedata2
BuildArch:      noarch
Requires:       numpy
Requires:       python2-fs
Requires:       python2-unicodedata2

%description -n python2-fonttools
%{desc}

%package -n python3-fonttools
Summary:        Python 3 fonttools library
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-unicodedata2
BuildArch:      noarch
Requires:       python3-fs
Requires:       python3-numpy
Requires:       python3-unicodedata2

%description -n python3-fonttools
%{desc}

%prep
%autosetup
rm -rf *.egg-info

sed -i '1d' Lib/fontTools/mtiLib/__init__.py

%build
%py2_build
%py3_build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files
%{_bindir}/pyftinspect
%{_bindir}/pyftmerge
%{_bindir}/pyftsubset
%{_bindir}/ttx
%{_bindir}/fonttools
%{_mandir}/man1/ttx.1.gz

%files -n python2-fonttools
%license LICENSE
%doc NEWS.rst README.rst
%{python2_sitelib}/fontTools
%{python2_sitelib}/%{name}-%{version}-py2.?.egg-info

%files -n python3-fonttools
%license LICENSE
%doc NEWS.rst README.rst
%{python3_sitelib}/fontTools
%{python3_sitelib}/%{name}-%{version}-py3.?.egg-info

%changelog
* Thu Feb 07 2019 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.37.3-2
- Version 3.37.3

* Sat Jul 28 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.29.0-1
- Update to 3.29.0 version (#1609078)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.28.0-2
- Rebuilt for Python 3.7

* Sat Jun 23 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.28.0-1
- Update to 3.28.0 version
- License corrected to MIT as upstream changed it since 3.21.0 release

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.27.1-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.27.1-1
- Update to 3.27.1 version (#1591522)

* Mon May 07 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.26.0-1
- Update to 3.26.0 version (#1575168)

* Wed Apr 04 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.25.0-1
- Update to 3.25.0 version (#1563434)

* Tue Mar 27 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.24.2-1
- Update to 3.24.2 version (#1560987)

* Wed Mar 07 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.24.1-1
- Update to 3.24.1 version (#1552589)

* Fri Mar 02 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.24.0-1
- Update to 3.24.0 version (#1550749)

* Tue Feb 27 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.23.0-1
- Update to 3.23.0 version (#1549339)

* Thu Feb 08 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.22.0-1
- Update to 3.22.0 version (#1542272)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.21.2-1
- Update to 3.21.2 version (#1532417)

* Sun Jan 07 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.21.1-1
- Update to 3.21.1 version (#1530999)

* Thu Dec 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.21.0-1
- Update to 3.21.0 version (#1528078)

* Wed Nov 22 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.20.0-1
- Update to 3.20.0 version (#1515794)

* Wed Nov 08 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.19.0-1
- Update to 3.19.0 version (#1510218)

* Wed Nov 01 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.18.0-1
- Update to 3.18.0 version (#1508232)

* Tue Oct 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.16.0-1
- Update to 3.16.0 version (#1498063)

* Sun Aug 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.15.1-1
- Update to 3.15.1 version

* Tue Aug 01 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.14.0-1
- Update to 3.14.0 version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.13.1-1
- Update to 3.13.1 version

* Thu May 25 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.13.0-1
- Update to 3.13.0 version

* Wed May 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.11.0-1
- Update to 3.11.0 version

* Sun Apr 16 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.10.0-1
- Update to 3.10.0 version

* Sun Apr 09 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.9.2-1
- Update to 3.9.2 version

* Tue Mar 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.9.1-1
- Update to 3.9.1 version

* Tue Mar 14 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.9.0-1
- Update to 3.9.0 version

* Mon Mar 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.8.0-1
- Update to 3.8.0 version

* Sat Feb 18 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.7.2-1
- Update to 3.7.2 version

* Fri Feb 17 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.7.1-1
- Update to 3.7.1 version

* Sun Feb 12 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.7.0-1
- Update to 3.7.0 version

* Mon Feb 06 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.6.2-1
- Update to 3.6.2 version

* Sun Jan 29 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.6.1-1
- Update to 3.6.1 version

* Fri Jan 27 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.6.0-1
- Update docs file names
- Update to 3.6.0 version

* Mon Jan 16 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.5.0-1
- Update to 3.5.0 version

* Thu Dec 22 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.4.0-1
- Update to 3.4.0 version

* Tue Dec 20 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.3.1-1
- Update to version 3.3.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Rebuild for Python 3.6

* Wed Dec 07 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.3.0-1
- Update to version 3.3.0
- This release removed top level sstruct and xmlWriter

* Mon Dec 05 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.3-1
- Update to version 3.2.3

* Tue Nov 29 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.2-2
- Resolves: rh#1278201 - ImportError: No module named 'pygtk' 

* Fri Nov 25 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.2-1
- Update to version 3.2.2

* Tue Nov 08 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.1-1
- Update to version 3.2.1

* Thu Nov 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.2.0-1
- Update to version 3.2.0

* Mon Oct 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.1.2-1
- Update to version 3.1.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar 06 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0-4
- Resolves:rh#1240265- fonttools 2.5 takes too much memory

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 02 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.0-1
- Updated to version 3.0

* Mon Jul 13 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.5-4
- Fix ttx execution backtrace (rh#1242549)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Parag <pnemade AT redhat DOT com> - 2.5-2
- Upstream dropped file eexecOp.so so make this package noarch
- Change %%{python2_sitearch} to %%{python2_sitelib} python2 macros
- Fix URL tag (rh#1164448)

* Sat Nov 15 2014 Peter Oliver <rpm@mavit.org.uk> - 2.5-1
- Changed upstream to https://github.com/behdad/fonttools.
- Updated to version 2.5.
- Use python2 macros (Parag Nemade)
- Use released tarball (Parag Nemade)
- Remove optional group tag (Parag Nemade)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Parag <pnemade AT redhat DOT com> - 2.4-1
- New upstream release 2.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Parag <pnemade AT redhat DOT com> - 2.3-6
- Resolves:rh#880063 - BR: python2-devel required

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Akira TAGOH <tagoh@redhat.com> - 2.3-2
- Rebuild.

* Fri Jul 23 2010 Akira TAGOH <tagoh@redhat.com> - 2.3-1
- New upstream release. (Paul Williams, #599281)
  - drop upstreamed patch.
  - correct man page location.
- Update the spec file to keep consistensy of usage in the macro as far as possible.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Oct 02 2009 Caolán McNamara <caolanm@redhat.com> - 2.2-7
* Resolves: rhbz#525444 as is a reserved keyword in python

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Roozbeh Pournader <roozbeh@gmail.com> - 2.2-5
* Change dependency on python-numeric to numpy

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2-3
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2-2
- Rebuild for Python 2.6

* Tue Sep 16 2008 Matt Domsch <mdomsch@fedoraproject.org> - 2.2-1
- update to 2.2, drop upstreamed patch, fix FTBFS BZ#434409

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0-0.12.20060223cvs
- Autorebuild for GCC 4.3

* Sat Dec 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.11.20060223cvs
- Rebuild for Python 2.5

* Fri Dec 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.10.20060223cvs
- Update the Unicode names file to Unicode 5.0.0

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.9.20060223cvs
- Update to newer CVS snapshot dated 2006-02-23
- Cleanup based on latest Python packaging guidelines

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.8.20050624cvs
- De-ghost .pyo files

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.7.20050624cvs
- Rebuild to get into Rawhide

* Mon May 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.6.20050624cvs
- Change specification of ulUnicodeRange1-4 to unsigned long

* Mon Feb 13 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.5.20050624cvs
- Rebuild for Fedora Extras 5

* Thu Feb 02 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.4.20050624cvs
- Provide ttx

* Wed Feb 01 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.3.20050624cvs
- Use upstream snapshots, moving the difference into a patch
- Change alphatag time to the latest change in CVS
- Use %%{python_sitearch} instead of %%{python_sitelib} (for x86_86)
- Use sed instead of a patch to remove shebang

* Sun Jan 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.2.20060103cvs
- Add %%{?dist} tag

* Fri Jan 06 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 2.0-0.1.20060103cvs
- Initial packaging
