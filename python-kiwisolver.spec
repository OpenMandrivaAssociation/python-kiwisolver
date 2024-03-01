%global           pypi_name kiwisolver
%define debug_package %nil

Name:             python-kiwisolver
Version:	1.4.5
Release:          4

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/kiwisolver/
Source0:	https://github.com/nucleic/kiwi/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3dist(cppy)

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
%autosetup -p1 -n %{pypi_name}-%{version}
#rm -f pyproject.toml

%build
%py_build


%install
%py_install %{pypi_name}

%files -n python-kiwisolver
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info
%{python3_sitearch}/%{pypi_name}


