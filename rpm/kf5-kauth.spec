%global kf5_version 5.115.0

Name: opt-kf5-kauth
Version: 5.115.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 2 integration module to perform actions as privileged user

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kauth

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros

#BuildRequires: polkit-qt5-1-devel
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-kcoreaddons

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
  -DKDE_INSTALL_LIBEXECDIR=%{_opt_kf5_libexecdir}
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kauth.*
%{_opt_kf5_libdir}/libKF5Auth.so.5*
%{_opt_kf5_libdir}/libKF5AuthCore.so.5*
%{_opt_kf5_datadir}/dbus-1/system.d/org.kde.kf5auth.conf
%{_opt_kf5_qtplugindir}/kauth/
%{_opt_kf5_datadir}/kf5/kauth/
#%{_opt_kf5_libexecdir}/kauth/
%{_opt_kf5_datadir}/locale/

%files devel
%{_opt_kf5_includedir}/KF5/KAuth/
%{_opt_kf5_includedir}/KF5/KAuthCore/
%{_opt_kf5_includedir}/KF5/KAuthWidgets/
%{_opt_kf5_libdir}/libKF5Auth.so
%{_opt_kf5_libdir}/libKF5AuthCore.so
%{_opt_kf5_libdir}/cmake/KF5Auth/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KAuth*.pri

