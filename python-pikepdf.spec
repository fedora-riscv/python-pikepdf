%global srcname pikepdf

Name:           python-%{srcname}
Version:        2.16.1
Release:        %autorelease
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPLv2.0
URL:            https://github.com/pikepdf/pikepdf
Source0:        %pypi_source
Patch0001:      0001-Relax-some-requirements.patch

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel >= 10.0.3
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

# Remove bundled egg-info
rm -rf src/%{srcname}.egg-info

# We don't build docs against the installed version, so force the version.
sed -i -e "s/release = .\+/release = '%{version}'/g" docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -r -x docs -x test


%build
%pyproject_wheel

# generate html docs
pushd docs
PYTHONPATH=$(ls -d %{_pyproject_builddir}/pip-req-build-*/build/lib.%{python3_platform}-%{python3_version}) sphinx-build-3 . ../html
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
