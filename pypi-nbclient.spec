#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nbclient
Version  : 0.6.6
Release  : 27
URL      : https://files.pythonhosted.org/packages/bf/53/0488846ed174a29049230be39db0fa56a699f269dfb340d1bc2491bf3536/nbclient-0.6.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/53/0488846ed174a29049230be39db0fa56a699f269dfb340d1bc2491bf3536/nbclient-0.6.6.tar.gz
Summary  : A client library for executing notebooks. Formerly nbconvert's ExecutePreprocessor.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-nbclient-bin = %{version}-%{release}
Requires: pypi-nbclient-license = %{version}-%{release}
Requires: pypi-nbclient-python = %{version}-%{release}
Requires: pypi-nbclient-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(nest_asyncio)
BuildRequires : pypi(traitlets)

%description
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter/nbclient/master?filepath=binder%2Frun_nbclient.ipynb)
[![Build Status](https://github.com/jupyter/nbclient/workflows/CI/badge.svg)](https://github.com/jupyter/nbclient/actions)
[![Documentation Status](https://readthedocs.org/projects/nbclient/badge/?version=latest)](https://nbclient.readthedocs.io/en/latest/?badge=latest)
[![image](https://codecov.io/github/jupyter/nbclient/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbclient?branch=master)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package bin
Summary: bin components for the pypi-nbclient package.
Group: Binaries
Requires: pypi-nbclient-license = %{version}-%{release}

%description bin
bin components for the pypi-nbclient package.


%package license
Summary: license components for the pypi-nbclient package.
Group: Default

%description license
license components for the pypi-nbclient package.


%package python
Summary: python components for the pypi-nbclient package.
Group: Default
Requires: pypi-nbclient-python3 = %{version}-%{release}

%description python
python components for the pypi-nbclient package.


%package python3
Summary: python3 components for the pypi-nbclient package.
Group: Default
Requires: python3-core
Provides: pypi(nbclient)
Requires: pypi(jupyter_client)
Requires: pypi(nbformat)
Requires: pypi(nest_asyncio)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-nbclient package.


%prep
%setup -q -n nbclient-0.6.6
cd %{_builddir}/nbclient-0.6.6
pushd ..
cp -a nbclient-0.6.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656688591
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nbclient
cp %{_builddir}/nbclient-0.6.6/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nbclient/8a1fbf91e5334237f0176576f8ad1a679b8135a8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/bin/jupyter-run
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-execute

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nbclient/8a1fbf91e5334237f0176576f8ad1a679b8135a8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
