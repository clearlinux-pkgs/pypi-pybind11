#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : pypi-pybind11
Version  : 2.13.6
Release  : 73
URL      : https://github.com/pybind/pybind11/archive/v2.13.6/pybind11-2.13.6.tar.gz
Source0  : https://github.com/pybind/pybind11/archive/v2.13.6/pybind11-2.13.6.tar.gz
Summary  : Seamless operability between C++11 and Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pybind11-bin = %{version}-%{release}
Requires: pypi-pybind11-data = %{version}-%{release}
Requires: pypi-pybind11-license = %{version}-%{release}
Requires: pypi-pybind11-python = %{version}-%{release}
Requires: pypi-pybind11-python3 = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : eigen-data
BuildRequires : eigen-dev
BuildRequires : glibc-dev
BuildRequires : pypi-pytest
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-pybind11-config-script.patch

%description
.. figure:: https://github.com/pybind/pybind11/raw/master/docs/pybind11-logo.png
:alt: pybind11 logo

%package bin
Summary: bin components for the pypi-pybind11 package.
Group: Binaries
Requires: pypi-pybind11-data = %{version}-%{release}
Requires: pypi-pybind11-license = %{version}-%{release}

%description bin
bin components for the pypi-pybind11 package.


%package data
Summary: data components for the pypi-pybind11 package.
Group: Data

%description data
data components for the pypi-pybind11 package.


%package dev
Summary: dev components for the pypi-pybind11 package.
Group: Development
Requires: pypi-pybind11-bin = %{version}-%{release}
Requires: pypi-pybind11-data = %{version}-%{release}
Provides: pypi-pybind11-devel = %{version}-%{release}
Requires: pypi-pybind11 = %{version}-%{release}

%description dev
dev components for the pypi-pybind11 package.


%package license
Summary: license components for the pypi-pybind11 package.
Group: Default

%description license
license components for the pypi-pybind11 package.


%package python
Summary: python components for the pypi-pybind11 package.
Group: Default
Requires: pypi-pybind11-python3 = %{version}-%{release}

%description python
python components for the pypi-pybind11 package.


%package python3
Summary: python3 components for the pypi-pybind11 package.
Group: Default
Requires: python3-core
Provides: pypi(pybind11)

%description python3
python3 components for the pypi-pybind11 package.


%prep
%setup -q -n pybind11-2.13.6
cd %{_builddir}/pybind11-2.13.6
%patch -P 1 -p1
pushd ..
cp -a pybind11-2.13.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730215642
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1730215642
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pybind11
cp %{_builddir}/pybind11-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pybind11/3dbd61e2b2c71dcc658c3da90bacf2e15958075a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
install -D -m 00755 pybind11-config %{buildroot}/usr/bin/pybind11-config
python3 setup.py install --root=%{buildroot}
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybind11-config

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/pybind11/attr.h
/usr/include/pybind11/buffer_info.h
/usr/include/pybind11/cast.h
/usr/include/pybind11/chrono.h
/usr/include/pybind11/common.h
/usr/include/pybind11/complex.h
/usr/include/pybind11/detail/class.h
/usr/include/pybind11/detail/common.h
/usr/include/pybind11/detail/cpp_conduit.h
/usr/include/pybind11/detail/descr.h
/usr/include/pybind11/detail/exception_translation.h
/usr/include/pybind11/detail/init.h
/usr/include/pybind11/detail/internals.h
/usr/include/pybind11/detail/type_caster_base.h
/usr/include/pybind11/detail/typeid.h
/usr/include/pybind11/detail/value_and_holder.h
/usr/include/pybind11/eigen.h
/usr/include/pybind11/eigen/common.h
/usr/include/pybind11/eigen/matrix.h
/usr/include/pybind11/eigen/tensor.h
/usr/include/pybind11/embed.h
/usr/include/pybind11/eval.h
/usr/include/pybind11/functional.h
/usr/include/pybind11/gil.h
/usr/include/pybind11/gil_safe_call_once.h
/usr/include/pybind11/iostream.h
/usr/include/pybind11/numpy.h
/usr/include/pybind11/operators.h
/usr/include/pybind11/options.h
/usr/include/pybind11/pybind11.h
/usr/include/pybind11/pytypes.h
/usr/include/pybind11/stl.h
/usr/include/pybind11/stl/filesystem.h
/usr/include/pybind11/stl_bind.h
/usr/include/pybind11/type_caster_pyobject_ptr.h
/usr/include/pybind11/typing.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/attr.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/buffer_info.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/cast.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/chrono.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/common.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/complex.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/class.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/common.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/cpp_conduit.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/descr.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/exception_translation.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/init.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/internals.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/type_caster_base.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/typeid.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/detail/value_and_holder.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/eigen.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/eigen/common.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/eigen/matrix.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/eigen/tensor.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/embed.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/eval.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/functional.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/gil.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/gil_safe_call_once.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/iostream.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/numpy.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/operators.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/options.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/pybind11.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/pytypes.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/stl.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/stl/filesystem.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/stl_bind.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/type_caster_pyobject_ptr.h
/usr/lib/python3.13/site-packages/pybind11/include/pybind11/typing.h
/usr/lib64/pkgconfig/pybind11.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pybind11/3dbd61e2b2c71dcc658c3da90bacf2e15958075a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
