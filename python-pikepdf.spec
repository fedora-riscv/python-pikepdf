%global srcname pikepdf

Name:           python-%{srcname}
Version:        1.17.0
Release:        1%{?dist}
Summary:        Read and write PDFs with Python, powered by qpdf

License:        MPLv2.0
URL:            https://github.com/pikepdf/pikepdf
Source0:        %pypi_source
Patch0001:      0001-Reduce-some-requirements.patch

BuildRequires:  gcc-c++
BuildRequires:  qpdf-devel >= 8.4.2
BuildRequires:  python3-devel
BuildRequires:  python3dist(lxml) >= 4
BuildRequires:  python3dist(pillow) >= 6
BuildRequires:  (python3dist(pybind11) >= 2.4.3 with python3dist(pybind11) < 3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
# Tests:
BuildRequires:  poppler-utils
BuildRequires:  python3dist(attrs) >= 19.1
BuildRequires:  (python3dist(hypothesis) >= 4.23.8 with python3dist(hypothesis) < 6)
BuildRequires:  python3dist(psutil) >= 5
BuildRequires:  (python3dist(pytest) >= 4.4.0 with python3dist(pytest) < 6)
BuildRequires:  python3dist(pytest-helpers-namespace) >= 2019.1.8
BuildRequires:  python3dist(pytest-timeout) >= 1.3.3
BuildRequires:  (python3dist(pytest-xdist) >= 1.28 with python3dist(pytest-xdist) < 2)
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
%{pytest} -ra


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
* Mon Jul 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17.0-1
- Update to latest version

* Thu Jul 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.1-1
- Update to latest version

* Sat Jun 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15.1-1
- Update to latest version

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14.0-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13.0-1
- Update to latest version

* Fri May 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.0-1
- Update to latest version

* Mon May 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.2-1
- Update to latest version

* Fri Apr 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.1-1
- Update to latest version

* Tue Apr 14 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.11.0-2
- rebuilt for qpdf-10.0.1

* Mon Apr 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.0-1
- Update to latest version

* Thu Apr 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.4-1
- Update to latest version

* Tue Mar 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.3-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.2-1
- Update to latest version

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.1-1
- Update to latest version

* Tue Jan 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.0-1
- Update to latest version

* Mon Jan 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.3-1
- Update to latest version

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.2-1
- Update to latest version

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.1-1
- Update to latest version

* Tue Nov 19 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.7.0-2
- rebuilt for qpdf-9.1.0

* Mon Nov 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.0-1
- Update to latest version

* Mon Oct 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.5-1
- Update to latest version

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
