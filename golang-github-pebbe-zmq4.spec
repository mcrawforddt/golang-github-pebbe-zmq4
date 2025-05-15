# Define backup go macros
%if %{rhel} == 8
%global gopkg %package -n %{goname}-devel \
Summary:	%{summary} \
BuildArch:  noarch \
%description -n %{goname}-devel \
%{common_description}
%global goprep(A) %setup -q
%global generate_buildrequires echo "Need more specific macro on rhel8"
%global gopkginstall for file in $(find . -iname "*.go" \! -iname "*_test.go" \! -iname "main.go" ) ; do \
    echo "%%dir %%{gopath}/src/%%{goipath}/$(dirname $file)" >> devel.file-list ;\
    install -d -p %{buildroot}/%{gopath}/src/%{goipath}/$(dirname $file) ;\
    cp -pav $file %{buildroot}/%{gopath}/src/%{goipath}/$file ;\
    echo "%%{gopath}/src/%%{goipath}/$file" >> devel.file-list ;\
done ;\
sort -u -o devel.file-list devel.file-list
%global gopkgfiles %files -n %{goname}-devel -f devel.file-list
%global gocheck echo "skipping gocheck on rhel8"
# Specific BuildRequires macro
%global go_generate_buildrequires BuildRequires:	%{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%endif

%global debug_package %{nil}
# https://github.com/pebbe/zmq4
%global goipath         github.com/pebbe/zmq4
%global common_description %{expand:
A Go interface to ZeroMQ version 4.}

Version:	1.4.0
Release:	1%{?dist}
Summary:	Minimalist go config library
License:    FIXME
%gometa
Name:       %{goname}
URL:		https://github.com/pebbe/zmq4
Source0:	https://github.com/pebbe/zmq4/archive/%{name}-%{version}.tar.gz

%description %{common_description}

%go_generate_buildrequires

%gopkg

%prep
# goprep -A fails on rocky9 looking for tarball named zmq4
%setup -q

%install
for file in $(find . -iname "*.go" \! -iname "*_test.go" \! -iname "main.go" ) ; do
    echo "%%dir %%{gopath}/src/%%{goipath}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{goipath}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{goipath}/$file
    echo "%%{gopath}/src/%%{goipath}/$file" >> devel.file-list
done
sort -u -o devel.file-list devel.file-list

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
