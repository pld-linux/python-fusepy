%define 	module	fusepy

Summary:	Python interface to FUSE (Filesystem in USErspace)
Summary(pl.UTF-8):	Pythonowy interfejs do FUSE (systemu plików w przestrzeni użytkownika)
Name:		python-%{module}
# it's svn revision
Version:	0.r20
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://fusepy.googlecode.com/svn/trunk/fuse.py
# Source0-md5:	6dcd2fc3caa6495a34dcdaf4135c495e
URL:		http://fusepy.googlecode.com/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	iconv
Requires:	libfuse
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to FUSE (Filesystem in USErspace).

%description -l pl.UTF-8
Pythonowy interfejs do FUSE (Filesystem in USErspace - systemu plików
w przestrzeni użytkownika).

%prep
%setup -q -T -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{py_sitescriptdir}/fuse.py

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
