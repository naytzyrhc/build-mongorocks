Name:           rocks-strata-oss
Version:        0.0
Release:        %(date '+%Y%m%d%H%M%s')%{?dist}
Summary:        Backup tool for mongorocks using oss

License:        BSD
URL:            https://github.com/facebookgo/rocks-strata
# Source0:

BuildRequires:  golang
# Requires:

%description
rocks-strata is a framework for managing incremental backups of databases that use the RocksDB storage engine. Current drivers support MongoDB with the RocksDB storage engine ("MongoRocks") and use Aliyun OSS for remote storage.

# %prep
# true
# %setup -q


%build
export GOPATH="%{_tmppath}/gopath"
mkdir -p $GOPATH
for PROJECT in github.com/naytzyrhc/rocks-strata/strata github.com/facebookgo/rocks-strata/strata github.com/PinIdea/oss-aliyun-go github.com/facebookgo/mgotest gopkg.in/mgo.v2 gopkg.in/mgo.v2/bson code.google.com/p/go.crypto/ssh/terminal github.com/kr/pty; do
	go get $PROJECT
done

cd $GOPATH/src/github.com/naytzyrhc/rocks-strata/strata/cmd/mongo/lreplica_ossstorage_driver/strata
go install
cd $GOPATH/src/github.com/naytzyrhc/rocks-strata/strata/cmd/mongo/lreplica_ossstorage_driver/mongoq
go install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

cp $GOPATH/bin/* $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/*

%changelog


%changelog
