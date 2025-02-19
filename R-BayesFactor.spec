#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-BayesFactor
Version  : 0.9.12.4.7
Release  : 56
URL      : https://cran.r-project.org/src/contrib/BayesFactor_0.9.12-4.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BayesFactor_0.9.12-4.7.tar.gz
Summary  : Computation of Bayes Factors for Common Designs
Group    : Development/Tools
License  : GPL-2.0
Requires: R-BayesFactor-lib = %{version}-%{release}
Requires: R-MatrixModels
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-coda
Requires: R-hypergeo
Requires: R-mvtnorm
Requires: R-pbapply
Requires: R-stringr
BuildRequires : R-MatrixModels
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-coda
BuildRequires : R-hypergeo
BuildRequires : R-mvtnorm
BuildRequires : R-pbapply
BuildRequires : R-stringr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
various Bayes factors for simple designs, including contingency tables,
    one- and two-sample designs, one-way designs, general ANOVA designs, and
    linear regression.

%package lib
Summary: lib components for the R-BayesFactor package.
Group: Libraries

%description lib
lib components for the R-BayesFactor package.


%prep
%setup -q -n BayesFactor
pushd ..
cp -a BayesFactor buildavx2
popd
pushd ..
cp -a BayesFactor buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737133905

%install
export SOURCE_DATE_EPOCH=1737133905
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
/usr/lib64/R/library/BayesFactor/DESCRIPTION
/usr/lib64/R/library/BayesFactor/INDEX
/usr/lib64/R/library/BayesFactor/Meta/Rd.rds
/usr/lib64/R/library/BayesFactor/Meta/data.rds
/usr/lib64/R/library/BayesFactor/Meta/features.rds
/usr/lib64/R/library/BayesFactor/Meta/hsearch.rds
/usr/lib64/R/library/BayesFactor/Meta/links.rds
/usr/lib64/R/library/BayesFactor/Meta/nsInfo.rds
/usr/lib64/R/library/BayesFactor/Meta/package.rds
/usr/lib64/R/library/BayesFactor/Meta/vignette.rds
/usr/lib64/R/library/BayesFactor/NAMESPACE
/usr/lib64/R/library/BayesFactor/NEWS
/usr/lib64/R/library/BayesFactor/R/BayesFactor
/usr/lib64/R/library/BayesFactor/R/BayesFactor.rdb
/usr/lib64/R/library/BayesFactor/R/BayesFactor.rdx
/usr/lib64/R/library/BayesFactor/data/puzzles.rda
/usr/lib64/R/library/BayesFactor/data/raceDolls.rda
/usr/lib64/R/library/BayesFactor/doc/compare_lme4.R
/usr/lib64/R/library/BayesFactor/doc/compare_lme4.Rmd
/usr/lib64/R/library/BayesFactor/doc/compare_lme4.html
/usr/lib64/R/library/BayesFactor/doc/index.R
/usr/lib64/R/library/BayesFactor/doc/index.Rmd
/usr/lib64/R/library/BayesFactor/doc/index.html
/usr/lib64/R/library/BayesFactor/doc/manual.R
/usr/lib64/R/library/BayesFactor/doc/manual.Rmd
/usr/lib64/R/library/BayesFactor/doc/manual.html
/usr/lib64/R/library/BayesFactor/doc/odds_probs.R
/usr/lib64/R/library/BayesFactor/doc/odds_probs.Rmd
/usr/lib64/R/library/BayesFactor/doc/odds_probs.html
/usr/lib64/R/library/BayesFactor/doc/priors.R
/usr/lib64/R/library/BayesFactor/doc/priors.Rmd
/usr/lib64/R/library/BayesFactor/doc/priors.html
/usr/lib64/R/library/BayesFactor/help/AnIndex
/usr/lib64/R/library/BayesFactor/help/BayesFactor.rdb
/usr/lib64/R/library/BayesFactor/help/BayesFactor.rdx
/usr/lib64/R/library/BayesFactor/help/aliases.rds
/usr/lib64/R/library/BayesFactor/help/paths.rds
/usr/lib64/R/library/BayesFactor/html/00Index.html
/usr/lib64/R/library/BayesFactor/html/R.css
/usr/lib64/R/library/BayesFactor/include/BayesFactor.h
/usr/lib64/R/library/BayesFactor/include/BayesFactor_RcppExports.h
/usr/lib64/R/library/BayesFactor/tests/run-all.R
/usr/lib64/R/library/BayesFactor/tests/test-anovaBF.R
/usr/lib64/R/library/BayesFactor/tests/test-contingencyBF.R
/usr/lib64/R/library/BayesFactor/tests/test-correlationBF.R
/usr/lib64/R/library/BayesFactor/tests/test-generalTestBF.R
/usr/lib64/R/library/BayesFactor/tests/test-proportionBF.R
/usr/lib64/R/library/BayesFactor/tests/test-regressionBF.R
/usr/lib64/R/library/BayesFactor/tests/test-specialchars.R
/usr/lib64/R/library/BayesFactor/tests/test-ttest.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/BayesFactor/libs/BayesFactor.so
/V4/usr/lib64/R/library/BayesFactor/libs/BayesFactor.so
/usr/lib64/R/library/BayesFactor/libs/BayesFactor.so
