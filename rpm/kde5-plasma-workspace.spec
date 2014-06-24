# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kde5-plasma-workspace

# >> macros
# << macros

Summary:    Plasma 5 workspace applications and applets
Version:    4.97.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source1:    kde.pam
Source100:  kde5-plasma-workspace.yaml
Source101:  kde5-plasma-workspace-rpmlintrc
Requires:   kde5-filesystem
Requires:   kf5-kinit
Requires:   kf5-kded
Requires:   kf5-kdoctools
Requires:   qt5-qtquickcontrols
Requires:   qt5-qttools-paths
Requires:   qt5-qttools-qdbus
Requires:   coreutils
Requires:   dbus-x11
Requires:   xorg-x11-apps
Requires:   xorg-x11-utils
Requires:   xorg-x11-server-utils
Requires:   socat
Requires:   systemd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-screensaver)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xevie)
BuildRequires:  pkgconfig(xcb-xf86dri)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xprint)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcb-xvmc)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-property)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-reply)
BuildRequires:  kf5-rpm-macros
BuildRequires:  kde5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  libGL-devel
BuildRequires:  boost-devel
BuildRequires:  pam-devel
BuildRequires:  phonon-qt5-devel
BuildRequires:  kf5-umbrella
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-kjsembed-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-baloo-devel
BuildRequires:  kde5-libksysguard-devel
BuildRequires:  libkscreen-devel
BuildRequires:  kde5-kwin-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

%description
Plasma 5 libraries and runtime components.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%package -n sddm-theme-breeze
Summary:    SDDM "Breeze" theme
Group:      Applications/System
BuildArch:  noarch
Requires:   sddm
Requires:   kde5-oxygen-icon-theme

%description -n sddm-theme-breeze
This package contains the "Breeze" theme for SDDM.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kde5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kde5_make_install
# << install pre

# >> install post
mkdir -p %{buildroot}/%{_kde5_sysconfdir}/profile.d
cat > %{buildroot}/%{_kde5_sysconfdir}/profile.d/plasma5.sh <<EOF
export QT_PLUGIN_PATH="%{_kde5_plugindir}:%{_kf5_plugindir}:%{_kf5_qtplugindir}"
export QML2_IMPORT_PATH="%{_kf5_qmldir}:%{_libdir}/qml"
export LD_LIBRARY_PATH="%{_kde5_libdir}/kde5:%{_libdir}"
export LIBEXEC_PATH="%{_kf5_libexecdir}:%{_kde5_libexecdir}"

# XDG
# Refer to http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
export XDG_ICON_DIRS="%{_datadir}/icons"
export XDG_DATA_DIRS="%{_kf5_datadir}/kf5:%{_kde5_datadir}/kde5:%{_datadir}"
export XDG_CONFIG_HOME="\$HOME/.config"
export XDG_CACHE_HOME="\$HOME/.cache"
EOF

chrpath --delete %{buildroot}/%{_kde5_plugindir}/phonon_platform/kde.so

mv -f %{buildroot}%{_datadir}/apps/sddm %{buildroot}%{_datadir}
rm -rf %{buildroot}%{_datadir}/apps

# Makes kcheckpass work
install -m455 -p -D %{SOURCE1} %{buildroot}%{_kde5_sysconfdir}/pam.d/kde
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_kde5_sysconfdir}/profile.d/plasma5.sh
%{_kde5_bindir}/*
%{_kde5_libdir}/*.so.*
%{_kde5_libdir}/libkdeinit5_*.so
%{_kde5_plugindir}/*
%{_kde5_libdir}/qml/org/kde/*
%{_kde5_libexecdir}/*
%{_kde5_datadir}/ksmserver
%{_kde5_datadir}/ksplash
%{_kde5_datadir}/plasma/plasmoids
%{_kde5_datadir}/plasma/services
%{_kde5_datadir}/plasma/shareprovider
%{_kde5_datadir}/plasma/wallpapers
%{_kde5_datadir}/plasma/look-and-feel
%{_kde5_datadir}/solid
%{_kde5_datadir}/kstyle
%{_kde5_datadir}/drkonqi/debuggers/external/*
%{_kde5_datadir}/drkonqi/debuggers/internal/*
%{_kde5_datadir}/drkonqi/mappings
%{_kde5_datadir}/drkonqi/pics/*.png
%{_kde5_sysconfdir}/xdg/*.knsrc
%{_kde5_sysconfdir}/xdg/autostart/*.desktop
%{_kde5_sysconfdir}/pam.d/kde
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservices5/kded/*.desktop
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/applications/*.desktop
%{_datadir}/xsessions/plasma.desktop
%{_datadir}/config.kcfg
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kde5_libdir}/libweather_ion.so
%{_kde5_libdir}/libtaskmanager.so
%{_kde5_libdir}/libkworkspace.so
%{_kde5_libdir}/libplasma-geolocation-interface.so
%{_kde5_includedir}/*
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/ScreenSaverDBusInterface
%{_datadir}/dbus-1/interfaces/*.xml
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/HTML/en/*
# >> files doc
# << files doc

%files -n sddm-theme-breeze
%defattr(-,root,root,-)
%{_datadir}/sddm/themes/breeze
# >> files sddm-theme-breeze
# << files sddm-theme-breeze
