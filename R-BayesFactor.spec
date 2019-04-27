#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BayesFactor
Version  : 0.9.12.4.2
Release  : 12
URL      : https://cran.r-project.org/src/contrib/BayesFactor_0.9.12-4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BayesFactor_0.9.12-4.2.tar.gz
Summary  : Computation of Bayes Factors for Common Designs
Group    : Development/Tools
License  : GPL-2.0
Requires: R-BayesFactor-lib = %{version}-%{release}
BuildRequires : R-RcppEigen
BuildRequires : R-arm
BuildRequires : R-coda
BuildRequires : R-gtools
BuildRequires : R-highr
BuildRequires : R-hypergeo
BuildRequires : R-languageR
BuildRequires : R-pbapply
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
-------------------------------------------------------------------
Flat Shadow Social Media Icons
by Lokas Software
http://www.awicons.com/

%package lib
Summary: lib components for the R-BayesFactor package.
Group: Libraries

%description lib
lib components for the R-BayesFactor package.


%prep
%setup -q -c -n BayesFactor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552714812

%install
export SOURCE_DATE_EPOCH=1552714812
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BayesFactor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BayesFactor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BayesFactor
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  BayesFactor || :


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
/usr/lib64/R/library/BayesFactor/libs/BayesFactor.so
/usr/lib64/R/library/BayesFactor/libs/BayesFactor.so.avx2
/usr/lib64/R/library/BayesFactor/libs/BayesFactor.so.avx512
