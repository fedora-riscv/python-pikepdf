%global srcname pikepdf

Name:           python-%{srcname}
Version:        2.8.0
Release:        1%{?dist}
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
BuildRequires:  (python3dist(hypothesis) >= 5 with python3dist(hypothesis) < 6)
BuildRequires:  python3dist(psutil) >= 5
BuildRequires:  (python3dist(pytest) >= 6 with python3dist(pytest) < 7)
BuildRequires:  python3dist(pytest-timeout) >= 1.4.2
BuildRequires:  (python3dist(pytest-xdist) >= 1.28 with python3dist(pytest-xdist) < 3)
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
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt


%changelog
* Sun Feb 28 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.8.0-1
- Update to latest version (#1933531)

* Sat Feb 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.0-1
- Update to latest version (#1933453)

* Sat Feb 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.6.0-1
- Update to latest version (#1933209)

* Sat Feb 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.2-1
- Update to latest version
- Fixes rhbz#1920753
- Fixes rhbz#1923549

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-1
- Update to latest version (#1916969)

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version (#1912665)

* Tue Dec 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.4-1
- Update to latest version (#1911403)

* Tue Dec 29 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.3-1
- Update to latest version (#1911403)

* Wed Dec 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.2-1
- Update to latest version (#1910311)

* Wed Dec 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-1
- Update to latest version (#1891776)

* Wed Dec 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.19.4-1
- Update to latest version

* Wed Sep 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.19.3-1
- Update to latest version (#1877068)

* Mon Sep 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.19.1-1
- Update to latest version (#1876202)

* Wed Aug 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.19.0-1
- Update to latest version (#1869556)
- Allow latest pytest and pytest-xdist

* Tue Aug 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.18.0-1
- Update to latest version (rhbz#1867536)

* Sun Jul 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17.3-1
- Update to latest version

* Fri Jul 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17.2-1
- Update to latest version

* Tue Jul 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17.1-1
- Update to latest version

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
