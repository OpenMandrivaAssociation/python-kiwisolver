%global           pypi_name kiwisolver
%define srcname   kiwi
%define debug_package %nil

Name:             python-kiwisolver
Version:	1.1.0
Release:          4

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

%prep
%setup -q -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build


%install
%py3_install

%files -n python-kiwisolver
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py*.*.egg-info
%{python3_sitearch}/%{pypi_name}*.so


