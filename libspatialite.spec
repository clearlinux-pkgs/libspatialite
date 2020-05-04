#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libspatialite
Version  : 4.3.0a
Release  : 3
URL      : http://www.gaia-gis.it/gaia-sins/libspatialite-4.3.0a.tar.gz
Source0  : http://www.gaia-gis.it/gaia-sins/libspatialite-4.3.0a.tar.gz
Summary  : Spatial SQL database engine based on SQLite
Group    : Development/Tools
License  : GPL-2.0 MPL-1.1
Requires: libspatialite-lib = %{version}-%{release}
Requires: libspatialite-license = %{version}-%{release}
BuildRequires : geos-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)
BuildRequires : proj-dev
BuildRequires : sqlite-autoconf-dev

%description
--------------------- libspatialite ------------------------
PLEASE read the following information.

%package dev
Summary: dev components for the libspatialite package.
Group: Development
Requires: libspatialite-lib = %{version}-%{release}
Provides: libspatialite-devel = %{version}-%{release}
Requires: libspatialite = %{version}-%{release}

%description dev
dev components for the libspatialite package.


%package lib
Summary: lib components for the libspatialite package.
Group: Libraries
Requires: libspatialite-license = %{version}-%{release}

%description lib
lib components for the libspatialite package.


%package license
Summary: license components for the libspatialite package.
Group: Default

%description license
license components for the libspatialite package.


%prep
%setup -q -n libspatialite-4.3.0a
cd %{_builddir}/libspatialite-4.3.0a

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588614089
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-freexl CFLAGS="$CFLAGS -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H"
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1588614089
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libspatialite
cp %{_builddir}/libspatialite-4.3.0a/COPYING %{buildroot}/usr/share/package-licenses/libspatialite/fac7e08b00d48464e5cff0180701395569184413
cp %{_builddir}/libspatialite-4.3.0a/src/control_points/COPYING %{buildroot}/usr/share/package-licenses/libspatialite/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/spatialite.h
/usr/include/spatialite/control_points.h
/usr/include/spatialite/debug.h
/usr/include/spatialite/gaiaaux.h
/usr/include/spatialite/gaiaexif.h
/usr/include/spatialite/gaiageo.h
/usr/include/spatialite/gaiamatrix.h
/usr/include/spatialite/geopackage.h
/usr/include/spatialite/gg_advanced.h
/usr/include/spatialite/gg_const.h
/usr/include/spatialite/gg_core.h
/usr/include/spatialite/gg_dxf.h
/usr/include/spatialite/gg_dynamic.h
/usr/include/spatialite/gg_formats.h
/usr/include/spatialite/gg_mbr.h
/usr/include/spatialite/gg_structs.h
/usr/include/spatialite/gg_wfs.h
/usr/include/spatialite/gg_xml.h
/usr/include/spatialite/spatialite.h
/usr/include/spatialite/sqlite.h
/usr/lib64/libspatialite.so
/usr/lib64/mod_spatialite.so
/usr/lib64/pkgconfig/spatialite.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspatialite.so.7
/usr/lib64/libspatialite.so.7.1.0
/usr/lib64/mod_spatialite.so.7
/usr/lib64/mod_spatialite.so.7.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libspatialite/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libspatialite/fac7e08b00d48464e5cff0180701395569184413
