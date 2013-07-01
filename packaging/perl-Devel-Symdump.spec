#
# spec file for package perl-Devel-Symdump
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           perl-Devel-Symdump
Version:        2.08
Release:        11
License:        Artistic-1.0
%define cpan_name Devel-Symdump
Summary:        Dump symbol names or the symbol table
Url:            http://cpan.org/modules/by-module/Devel/
Group:          Development/Libraries/Perl
Source:         %{cpan_name}-%{version}.tar.gz
Source1001: 	perl-Devel-Symdump.manifest
BuildRequires:  perl
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl-macros
Requires:       perl(Carp)

%description
%{cpan_name} module for perl
This little package serves to access the symbol table of perl.

%prep
%setup -q -n %{cpan_name}-%{version}
cp %{SOURCE1001} .

%build
CFLAGS="%{optflags}" perl Makefile.PL
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%manifest %{name}.manifest
# normally you only need to check for doc files
%defattr(-,root,root)
%doc ChangeLog SIGNATURE

%changelog
