%global           pypi_name kiwisolver
%define srcname   kiwi

Name:             python-kiwisolver
Version:	1.1.0
Release:          2

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/kiwisolver/
Source0:	https://github.com/nucleic/kiwi/archive/%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)

%description
Kiwi is an efficient C++ implementation of the Cassowary
constraint solving algorithm. Kiwi is an implementation of the
algorithm based on the seminal Cassowary paper. It is not a
refactoring of the original C++ solver. Kiwi has been designed from
the ground up to be lightweight and fast. Kiwi ranges from 10x to 500x
faster than the original Cassowary solver with typical use cases
gaining a 40x improvement. Memory savings are consistently > 5x. In
addition to the C++ solver, Kiwi ships with hand-rolled Python
bindings.

%package -n python2-kiwisolver
Summary:        Python3 implementation of Kiwi
Group:          Development/Python
BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)


%description -n python2-kiwisolver
%{summary}.


%prep
%setup -q -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

cp -a . %{py3dir}

%build

%py2_build
pushd %{py3dir} 
%py3_build
popd


%install
%py2_install
pushd %{py3dir} 
%py3_install
popd

%files -n python2-kiwisolver
%doc README.rst
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitearch}/%{pypi_name}*.so

%files -n python-kiwisolver
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitearch}/%{pypi_name}*.so


