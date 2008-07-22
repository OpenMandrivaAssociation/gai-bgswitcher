%define name gai-bgswitcher
%define version 0.3
%define release %mkrel 8

Name: %name
Summary: A GAI applet for switching background
Version: %{version}
Release: %{release}
License: GPL
Url: http://gai.sf.net
Group: Graphics
Source: http://www.drakos7.net/%{name}-%{version}.tar.bz2
Source10:   %{name}-16.png
Source11:   %{name}-32.png
Source12:   %{name}-48.png
Patch: gai-album-0.6-rox-install.patch
BuildRoot: %{_tmppath}/build-root-%{name}
BuildRequires: libgai-devel >= 0.5

%description
A GAI applet for switching the background image.

This applet can be used in the GNOME and ROX Panels and as a
WindowMaker dockapp. Other panels and Window Managers will be
supported soon.


%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make 

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/* %buildroot%_libdir/
%endif
install -m644 %name-icon.png -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name-icon.png
install -m644 %name-icon.png -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name/%name-icon.png
install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gai-bgswitcher
Comment=Backgrund switcher
Exec=%{_bindir}/%{name}
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Graphics;Graphics;Viewer;
StartupNotify=true
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,0755)
%doc TODO CHANGELOG README README.gai
%{_bindir}/*
%{_libdir}/bonobo/servers/GNOME_%{name}Applet.server
%_datadir/applications/mandriva*
%{_datadir}/pixmaps/*
%_libdir/apps/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png

