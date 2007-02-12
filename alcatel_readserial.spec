Summary:	Read call accounting and error data from an Alcatel PCX
Summary(pl.UTF-8):	Odczyt danych o połączeniach i błędach z PCX Alcatela
Name:		alcatel_readserial
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/alcatelpcxrs/%{name}-%{version}.tar.bz2
# Source0-md5:	e49e83f80d5cfbb89133aab717f42010
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read call accounting and error data from an Alcatel PCX built in
serial port, filtering along the way.

%description -l pl.UTF-8
Odczyt danych o połączeniach i błędach z centralki PCX Alcatela
poprzez wbudowany port szeregowy z filtrowaniem.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install alcatel_readserial $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README TODO
%attr(755,root,root) %{_bindir}/*
