#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	HTML
%include	/usr/lib/rpm/macros.perl
Summary:	IO::HTML - Open an HTML file with automatic charset detection
Summary(pl.UTF-8):	IO::HTML - otwieranie pliku HTML z automatycznym wykrywaniem zestawu znaków
Name:		perl-IO-HTML
Version:	1.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fdfa3fe3d61a7fda9236c8d9776cdd65
URL:		http://search.cpan.org/dist/IO-HTML/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-Encode >= 2.10
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::HTML provides an easy way to open a file containing HTML while
automatically determining its encoding. It uses the HTML5 encoding
sniffing algorithm specified in section 8.2.2.1 of the draft standard.

%description -l pl.UTF-8
Moduł IO::HTML udostępnia łatwy sposób otwierania pliku zawierającego
HTML z automatycznym określaniem jego kodowania. Wykorzystuje algorytm
dopasowywania kodowania HTML5, opisany w sekcji 8.2.2.1 szkicu
standardu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/HTML.pm
%{_mandir}/man3/IO::HTML.3pm*
