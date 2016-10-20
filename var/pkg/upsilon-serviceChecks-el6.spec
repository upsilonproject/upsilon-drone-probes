Name:		upsilon-serviceChecks
Version:	%{buildid_version}
Release:	%{buildid_timestamp}1%{?dist}
Summary:	Monitoring software
BuildArch: 	noarch

Group:		Applications/System
License:	GPLv2
URL:		http://upsilon-project.co.uk
Source0:	upsilon-serviceChecks.py

BuildRequires:	python
Requires:	python

%description
Monitoring software

%prep
rm -rf $RPM_BUILD_DIR/*
%setup -q -n upsilon-serviceChecks-%{buildid_tag}

%build
mkdir -p {%buildroot}/usr/local/sbin
cp src/* %{buildroot}/usr/local/sbin/

%files
/usr/local/sbin/*

%changelog
* Fri Jun 06 2016 James Read <contact@jwread.com 1.0.0-1
	Initial version.

