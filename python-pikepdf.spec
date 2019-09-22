%global srcname pikepdf

Name:           python-%{srcname}
Version:        1.6.4
Release:        1%{?dist}
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPLv2.0
URL:            https://github.com/pikepdf/pikepdf
Source0:        %pypi_source
Patch0001:      0001-Reduce-test-requirements.patch

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel >= 8.4.2
BuildRequires:  python3-devel
BuildRequires:  python3dist(lxml) >= 4
BuildRequires:  (python3dist(pybind11) >= 2.3 with python3dist(pybind11) < 3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
# Tests:
BuildRequires:  poppler-utils
BuildRequires:  python3dist(attrs) >= 18.2
BuildRequires:  (python3dist(hypothesis) >= 3.66.11 with python3dist(hypothesis) < 5)
BuildRequires:  python3dist(pillow) >= 5
BuildRequires:  (python3dist(pytest) >= 3.9.3 with python3dist(pytest) < 5)
BuildRequires:  python3dist(pytest-helpers-namespace) >= 2019.1.8
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-timeout) >= 1.3.3
BuildRequires:  (python3dist(pytest-xdist) >= 1.27 with python3dist(pytest-xdist) < 2)
BuildRequires:  python3dist(python-xmp-toolkit) >= 2.0.1

%description
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%{?python_enable_dependency_generator}
# Force a minimum version (same soname as 8.1.x):
Requires:       qpdf-libs >= 8.4.2

%description -n python3-%{srcname}
pikepdf is a Python library for reading and writing PDF files. pikepdf is
based on QPDF, a powerful PDF manipulation and repair library.


%package -n python-%{srcname}-doc
Summary:        pikepdf documentation

BuildRequires:  python3dist(sphinx) >= 1.4
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
%{__python3} setup.py test --addopts -ra


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
* Sun Sep 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.4-1
- Update to latest version

* Wed Sep 04 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-1
- Update to latest version

* Fri Aug 30 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.2-1
- Update to latest version

* Fri Aug 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Tue May 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version

* Tue Apr 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Sun Mar 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Tue Feb 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.5-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- Update to latest version

* Sat Jan 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.7-1
- Update to latest version

* Sat Oct 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.5-1
- Update to latest version

* Tue Sep 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-2
- Force requires to new qpdf

* Mon Sep 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version

* Tue Aug 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Initial package.
