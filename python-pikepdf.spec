%global srcname pikepdf

Name:           python-%{srcname}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPLv2.0
URL:            https://github.com/pikepdf/pikepdf
Source0:        %pypi_source

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(hypothesis) >= 3.56.9
BuildRequires:  python3dist(pillow) >= 5.0.0
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pytest) >= 3.6.0
BuildRequires:  python3dist(pytest-helpers-namespace) >= 2017.11.11
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-timeout) >= 1.3.0
BuildRequires:  python3dist(pytest-xdist) >= 1.22.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

%description
pikepdf is a Python library allowing creation, manipulation and repair of PDFs.
It provides a Pythonic wrapper around the C++ PDF content transformation
library, QPDF.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%{?python_enable_dependency_generator}

%description -n python3-%{srcname}
pikepdf is a Python library allowing creation, manipulation and repair of PDFs.
It provides a Pythonic wrapper around the C++ PDF content transformation
library, QPDF.


%package -n python-%{srcname}-doc
Summary:        pikepdf documentation

BuildRequires:  python3dist(sphinx) >= 1.4
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3-ipython-sphinx

%description -n python-%{srcname}-doc
Documentation for pikepdf


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf src/%{srcname}.egg-info

# Remove vendored code
rm -rf src/vendor

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
%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE.txt licenses/license.mpl2-no-exhibit-b.txt
%doc README.rst
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt licenses/license.mpl2-no-exhibit-b.txt


%changelog
* Tue Aug 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Initial package.
