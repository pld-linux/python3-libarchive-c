#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python interface to libarchive
Summary(pl.UTF-8):	Pythonowy interfejs do libarchive
Name:		python3-libarchive-c
Version:	5.3
Release:	1
License:	CC0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/libarchive-c/
Source0:	https://files.pythonhosted.org/packages/source/l/libarchive-c/libarchive_c-%{version}.tar.gz
# Source0-md5:	0f6b2d96b936c9b7f26dfec3255f7aaf
URL:		https://pypi.org/project/libarchive-c/
# for libarchive>=3.8 it expects all digests support
BuildRequires:	libarchive-devel >= 3.8.1-2
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	libarchive >= 3.8.1-2
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to libarchive. It uses the standard ctypes module
to dynamically load and access the C library.

%description -l pl.UTF-8
Pythonowy interfejs do libarchive. Wykorzystuje standardowy moduł
ctypes do dynamicznego ładowania i dostępu do biblioteki C.

%prep
%setup -q -n libarchive_c-%{version}

%build
%py3_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.rst
%{py3_sitescriptdir}/libarchive
%{py3_sitescriptdir}/libarchive_c-%{version}-py*.egg-info
