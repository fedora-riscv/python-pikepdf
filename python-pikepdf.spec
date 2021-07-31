%global srcname pikepdf

Name:           python-%{srcname}
Version:        2.15.1
Release:        %autorelease
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPLv2.0
URL:            https://github.com/pikepdf/pikepdf
Source0:        %pypi_source
Patch0001:      0001-Relax-some-requirements.patch

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel >= 10.0.3
BuildRequires:  python3-devel
BuildRequires:  python3dist(lxml) >= 4
BuildRequires:  (python3dist(pillow) >= 7 with python3dist(pillow) < 9)
BuildRequires:  (python3dist(pybind11) >= 2.6 with python3dist(pybind11) < 3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm[toml]) >= 4.1
BuildRequires:  python3dist(setuptools-scm-git-archive)
# Tests:
BuildRequires:  poppler-utils
BuildRequires:  python3dist(attrs) >= 20.2
BuildRequires:  (python3dist(hypothesis) >= 5 with python3dist(hypothesis) < 7)
BuildRequires:  python3dist(psutil) >= 5
BuildRequires:  (python3dist(pytest) >= 6 with python3dist(pytest) < 7)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-timeout) >= 1.4.2
BuildRequires:  (python3dist(pytest-xdist) >= 1.28 with python3dist(pytest-xdist) < 3)
BuildRequires:  python3dist(python-dateutil) >= 2.8
BuildRequires:  python3dist(python-xmp-toolkit) >= 2.0.1

%description
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n     python3-%{srcname}
Summary:        %{summary}

# Force a minimum version (same soname as 8.1.x):
Requires:       qpdf-libs >= 8.4.2

%description -n python3-%{srcname}
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n python-%{srcname}-doc
Summary:        pikepdf documentation

BuildRequires:  python3dist(sphinx) >= 3
BuildRequires:  python3dist(sphinx-issues)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3-ipython-sphinx

%description -n python-%{srcname}-doc
Documentation for pikepdf


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf src/%{srcname}.egg-info

# We don't build docs against the installed version, so force the version.
sed -i -e "s/release = .\+/release = '%{version}'/g" docs/conf.py


%build
%py3_build

# generate html docs
pushd docs
PYTHONPATH=$(ls -d ${PWD}/../build/lib*) sphinx-build-3 . ../html
popd
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%{pytest} -ra


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
%autochangelog
