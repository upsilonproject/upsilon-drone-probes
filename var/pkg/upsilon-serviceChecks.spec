%include SPECS/.buildid.rpmmacro

Name:		upsilon-serviceChecks
Version:	%{version_formatted_short}
Release:	%{timestamp}.%{?dist}
Summary:	Monitoring software
BuildArch: 	noarch

Group:		Applications/System
License:	GPLv2
URL:		http://upsilon-project.co.uk
Source0:	upsilon-serviceChecks.zip

BuildRequires:	python
Requires:	python upsilon-pycommon

%description
Monitoring software

%prep
rm -rf $RPM_BUILD_DIR/*
%setup -q -n upsilon-serviceChecks-%{tag}

%build
mkdir -p {%buildroot}/usr/sbin
cp src/* %{buildroot}/usr/sbin/

%files
/usr/sbin/*

%changelog
* Mon Jun 06 2016 James Read <contact@jwread.com> 1.0.0-1
	Initial version.

