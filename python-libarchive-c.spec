#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python interface to libarchive
Summary(pl.UTF-8):	Pythonowy interfejs do libarchive
Name:		python-libarchive-c
# keep 2.x here for python2 support
Version:	2.9
Release:	1
License:	CC0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/libarchive/
Source0:	https://files.pythonhosted.org/packages/source/l/libarchive-c/libarchive-c-%{version}.tar.gz
# Source0-md5:	083bd2cb0043c1e22a52cb9a05e31532
Patch0:		libarchive-c-mock.patch
URL:		https://pypi.org/project/libarchive-c/
BuildRequires:	libarchive-devel
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to libarchive. It uses the standard ctypes module
to dynamically load and access the C library.

%description -l pl.UTF-8
Pythonowy interfejs do libarchive. Wykorzystuje standardowy moduł
ctypes do dynamicznego ładowania i dostępu do biblioteki C.

%package -n python3-libarchive-c
Summary:	Python interface to libarchive
Summary(pl.UTF-8):	Pythonowy interfejs do libarchive
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-libarchive-c
A Python interface to libarchive. It uses the standard ctypes module
to dynamically load and access the C library.

%description -n python3-libarchive-c -l pl.UTF-8
Pythonowy interfejs do libarchive. Wykorzystuje standardowy moduł
ctypes do dynamicznego ładowania i dostępu do biblioteki C.

%prep
%setup -q -n libarchive-c-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.md README.rst
%{py_sitescriptdir}/libarchive
%{py_sitescriptdir}/libarchive_c-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-libarchive-c
%defattr(644,root,root,755)
%doc LICENSE.md README.rst
%{py3_sitescriptdir}/libarchive
%{py3_sitescriptdir}/libarchive_c-%{version}-py*.egg-info
%endif
