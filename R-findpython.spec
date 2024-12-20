#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-findpython
Version  : 1.0.9
Release  : 54
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/findpython_1.0.9.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/findpython_1.0.9.tar.gz
Summary  : Functions to Find an Acceptable Python Binary
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# findpython
[![CRAN Status Badge](https://www.r-pkg.org/badges/version/findpython)](https://cran.r-project.org/package=findpython)
[![R-CMD-check](https://github.com/trevorld/findpython/workflows/R-CMD-check/badge.svg)](https://github.com/trevorld/findpython/actions)
[![Coverage Status](https://codecov.io/github/trevorld/findpython/branch/master/graph/badge.svg)](https://app.codecov.io/gh/trevorld/findpython)
[![RStudio CRAN mirror downloads](https://cranlogs.r-pkg.org/badges/findpython)](https://cran.r-project.org/package=findpython)

%prep
%setup -q -n findpython
pushd ..
cp -a findpython buildavx2
popd
pushd ..
cp -a findpython buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732028858

%install
export SOURCE_DATE_EPOCH=1732028858
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/findpython/DESCRIPTION
/usr/lib64/R/library/findpython/INDEX
/usr/lib64/R/library/findpython/LICENSE
/usr/lib64/R/library/findpython/Meta/Rd.rds
/usr/lib64/R/library/findpython/Meta/features.rds
/usr/lib64/R/library/findpython/Meta/hsearch.rds
/usr/lib64/R/library/findpython/Meta/links.rds
/usr/lib64/R/library/findpython/Meta/nsInfo.rds
/usr/lib64/R/library/findpython/Meta/package.rds
/usr/lib64/R/library/findpython/NAMESPACE
/usr/lib64/R/library/findpython/NEWS.md
/usr/lib64/R/library/findpython/R/findpython
/usr/lib64/R/library/findpython/R/findpython.rdb
/usr/lib64/R/library/findpython/R/findpython.rdx
/usr/lib64/R/library/findpython/help/AnIndex
/usr/lib64/R/library/findpython/help/aliases.rds
/usr/lib64/R/library/findpython/help/findpython.rdb
/usr/lib64/R/library/findpython/help/findpython.rdx
/usr/lib64/R/library/findpython/help/paths.rds
/usr/lib64/R/library/findpython/html/00Index.html
/usr/lib64/R/library/findpython/html/R.css
/usr/lib64/R/library/findpython/tests/run-all.R
/usr/lib64/R/library/findpython/tests/testthat/test-findpython.r
