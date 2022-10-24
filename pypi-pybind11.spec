#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pybind11
Version  : 2.10.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/59/f6/aafe0b7e798f25632b199523cce98552fde53e8c552b9d96765426532d5f/pybind11-2.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/f6/aafe0b7e798f25632b199523cce98552fde53e8c552b9d96765426532d5f/pybind11-2.10.0.tar.gz
Summary  : Seamless operability between C++11 and Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pybind11-bin = %{version}-%{release}
Requires: pypi-pybind11-license = %{version}-%{release}
Requires: pypi-pybind11-python = %{version}-%{release}
Requires: pypi-pybind11-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pytest

%description
.. figure:: https://github.com/pybind/pybind11/raw/master/docs/pybind11-logo.png
:alt: pybind11 logo

%package bin
Summary: bin components for the pypi-pybind11 package.
Group: Binaries
Requires: pypi-pybind11-license = %{version}-%{release}

%description bin
bin components for the pypi-pybind11 package.


%package dev
Summary: dev components for the pypi-pybind11 package.
Group: Development
Requires: pypi-pybind11-bin = %{version}-%{release}
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
%setup -q -n pybind11-2.10.0
cd %{_builddir}/pybind11-2.10.0
pushd ..
cp -a pybind11-2.10.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658094775
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pybind11
cp %{_builddir}/pybind11-2.10.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pybind11/3dbd61e2b2c71dcc658c3da90bacf2e15958075a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pybind11-config

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/attr.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/buffer_info.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/cast.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/chrono.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/common.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/complex.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/class.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/common.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/descr.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/init.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/internals.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/type_caster_base.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/detail/typeid.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/eigen.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/embed.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/eval.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/functional.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/gil.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/iostream.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/numpy.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/operators.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/options.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/pybind11.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/pytypes.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/stl.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/stl/filesystem.h
/usr/lib/python3.10/site-packages/pybind11/include/pybind11/stl_bind.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pybind11/3dbd61e2b2c71dcc658c3da90bacf2e15958075a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
