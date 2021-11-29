%global srcname pikepdf

Name:           python-%{srcname}
Version:        4.0.2
Release:        %autorelease
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPLv2.0
URL:            https://github.com/pikepdf/pikepdf
Source0:        %pypi_source

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel >= 10.3.2
BuildRequires:  python3-devel
# Tests:
BuildRequires:  poppler-utils

%description
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n python-%{srcname}-doc
Summary:        pikepdf documentation

# Not autorequired because it's a Fedora-specific subpackage.
BuildRequires:  python3-ipython-sphinx

%description -n python-%{srcname}-doc
Documentation for pikepdf


%prep
%autosetup -n %{srcname}-%{version} -p1

# Allow new pybind11
sed -i -e '/pybind11/s/, <= 2.8.0//' pyproject.toml

# Drop coverage requirements
sed -i -e '/coverage/d' -e '/pytest-cov/d' setup.cfg

# We don't build docs against the installed version, so force the version.
sed -i -e "s/release = .\+/release = '%{version}'/g" docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -r -x docs -x test


%build
%if 0%{fedora} && 0%{fedora} < 36
export PIP_USE_FEATURE="in-tree-build"
%endif
%pyproject_wheel

# generate html docs
pushd docs
PYTHONPATH="${PWD}/../build/lib.%{python3_platform}-%{python3_version}" sphinx-build-3 . ../html
popd
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%{pytest} -ra


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
%autochangelog
