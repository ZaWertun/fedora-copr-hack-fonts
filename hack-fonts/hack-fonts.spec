%global priority 60
%global fontname hack

%global nerd_fonts         hack-nerd-fonts
%global nerd_fontname      hack-nerd
%global nerd_fonts_version 2.3.3

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:    hack-fonts
Version: 3.003
Release: 2%{?dist}
Summary: A typeface designed for source code

License: MIT
URL:     https://sourcefoundry.org/hack
Source0: https://github.com/source-foundry/Hack/archive/v%{version}.tar.gz
Source1: hack.metainfo.xml
Source2: hack-fonts.conf
# svn export https://github.com/ryanoasis/nerd-fonts/tags/v2.3.3/patched-fonts/Hack nerd-fonts_Hack-v2.3.3 \
#  && tar -czvf nerd-fonts_Hack-v2.3.3.tar.gz nerd-fonts_Hack-v2.3.3/
Source3: nerd-fonts_Hack-v2.3.3.tar.gz
Source4: hack-nerd.metainfo.xml
Source5: hack-nerd-fonts.conf
# Patches
Patch0:  build-ttf_python3.patch
Patch1:  ttfautohint_deprecated_options.patch
Patch2:  ttfautohint_invalid_glyph_name.patch
BuildArch: noarch
Recommends: %{nerd_fonts}

BuildRequires: make
BuildRequires: mkfontscale
BuildRequires: ttfautohint
BuildRequires: libappstream-glib
BuildRequires: fontpackages-devel >= 1.13, xorg-x11-font-utils

%description
%{summary}.

%package -n %{nerd_fonts}
Summary: Hack font family patched with Nerd Fonts
BuildArch: noarch
%description -n %{nerd_fonts}
Hack font family patched with Nerd Fonts.


%prep
%setup -q -n Hack-%{version} -a3
%patch0 -p1 -b .build-ttf_python3
%patch1 -p1 -b .ttfautohint_deprecated_options
%patch2 -p1 -b .ttfautohint_invalid_glyph_name


%build
# Clean built fonts first:
#%{__rm} build/ttf/*
#%{__rm} build/web/fonts/*

#%{__make} ttf


%install
# Install *.ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p build/ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_datadir}/fonts/%{fontname} %{buildroot}%{catalogue}/%{name}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/appdata/hack.metainfo.xml

install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{priority}-%{fontname}.conf

ln -s %{_fontconfig_templatedir}/%{priority}-%{fontname}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{priority}-%{fontname}.conf

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}

# Install *.ttf for Hack Nerd Fonts
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{nerd_fontname}

find nerd-fonts_Hack-v%{nerd_fonts_version}/ -name '*Windows Compatible.ttf' -print -delete
install -m 0644 -p nerd-fonts_Hack-v%{nerd_fonts_version}/*/complete/*.ttf %{buildroot}%{_fontbasedir}/%{nerd_fontname}
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontbasedir}/%{nerd_fontname} %{buildroot}%{catalogue}/%{nerd_fonts}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} %{buildroot}%{_datadir}/appdata/hack-nerd.metainfo.xml

install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{priority}-%{nerd_fontname}.conf

ln -s %{_fontconfig_templatedir}/%{priority}-%{nerd_fontname}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{priority}-%{nerd_fontname}.conf

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontbasedir}/%{nerd_fontname}
mkfontdir %{buildroot}%{_fontbasedir}/%{nerd_fontname}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/hack.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/hack-nerd.metainfo.xml


%files
%doc CHANGELOG.md FAQ.md README.md
%license LICENSE.md
%dir %{_datadir}/fonts/%{fontname}
%{_datadir}/fonts/%{fontname}/Hack-*.ttf
%{_datadir}/appdata/hack.metainfo.xml
%{_datadir}/fontconfig/conf.avail/*-%{fontname}.conf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*-%{fontname}.conf
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}


%files -n hack-nerd-fonts
%license LICENSE.md
%dir %{_datadir}/fonts/%{nerd_fontname}
%{_datadir}/fonts/%{nerd_fontname}/Hack*.ttf
%{_datadir}/appdata/hack-nerd.metainfo.xml
%{_datadir}/fontconfig/conf.avail/*-%{nerd_fontname}.conf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*-%{nerd_fontname}.conf
%verify(not md5 size mtime) %{_fontbasedir}/%{nerd_fontname}/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/%{nerd_fontname}/fonts.scale
%{catalogue}/%{nerd_fonts}


%changelog
* Fri Mar 10 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.003-2
- added separate package for Hack fonts patched with Nerd Fonts

* Thu Dec 06 2018 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.003-1
- first spec for version 3.003


