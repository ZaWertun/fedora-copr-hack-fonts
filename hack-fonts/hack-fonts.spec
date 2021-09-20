%global priority 60
%global fontname hack

%define catalogue %{_sysconfdir}/X11/fontpath.d

Name:    hack-fonts
Version: 3.003
Release: 1%{?dist}
Summary: A typeface designed for source code

License: MIT
URL:     https://sourcefoundry.org/hack
Source0: https://github.com/source-foundry/Hack/archive/v%{version}.tar.gz
Source1: hack.metainfo.xml
Source2: hack-fonts.conf
Patch0:  build-ttf_python3.patch
Patch1:  ttfautohint_deprecated_options.patch
Patch2:  ttfautohint_invalid_glyph_name.patch
BuildArch: noarch

BuildRequires: make
BuildRequires: mkfontscale
BuildRequires: ttfautohint
BuildRequires: libappstream-glib
BuildRequires: fontpackages-devel >= 1.13, xorg-x11-font-utils

%description
%{summary}.


%prep
%setup -q -n Hack-%{version}
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

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{priority}-%{fontname}.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/hack.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{priority}-%{fontname}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{priority}-%{fontname}.conf

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}


%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/appdata/hack.metainfo.xml


%files
%dir %{_datadir}/fonts/%{fontname}
%{_datadir}/fonts/%{fontname}/Hack-*.ttf
%{_datadir}/appdata/hack.metainfo.xml
%{_datadir}/fontconfig/conf.avail/*-%{fontname}.conf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*-%{fontname}.conf
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}


%changelog
* Thu Dec 06 2018 Yaroslav Sidlovsky <zawertun@gmail.com> - 3.003-1
- first spec for version 3.003


