%global           pypi_name kiwisolver
%define debug_package %nil

Name:             python-kiwisolver
Version:	1.5.0
Release:          1

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/kiwisolver/
Source0:	https://github.com/nucleic/kiwi/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cppy)

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

%files
%doc README.rst
%{python_sitearch}/%{pypi_name}-%{version}.dist-info
%{python_sitearch}/%{pypi_name}
