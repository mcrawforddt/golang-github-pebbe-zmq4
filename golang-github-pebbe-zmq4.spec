%global debug_package %{nil}
# https://github.com/pebbe/zmq4
%global goipath         github.com/pebbe/zmq4
%global common_description %{expand:
A Go interface to ZeroMQ version 4.}

Version:	1.4.0
Release:	1%{?dist}
Summary:	Minimalist go config library
License:  FIXME
%gometa
Name:     %{goname}
URL:		  https://github.com/pebbe/zmq4
Source0:	https://github.com/pebbe/zmq4/archive/%{name}-%{version}.tar.gz

%description %{common_description}

%go_generate_buildrequires

%gopkg

%prep
%goprep -A

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
