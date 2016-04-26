Name:           ros-indigo-tetris-launch
Version:        0.1.6
Release:        0%{?dist}
Summary:        ROS tetris_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/tetris_launch
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosbridge-server
Requires:       ros-indigo-teleop-twist-keyboard
Requires:       ros-indigo-tetris-gazebo
BuildRequires:  ros-indigo-catkin

%description
Launch files (batch files that start processes and set parameters) for hakuto
robots. This package also contains document for the Hakuto ROS package suite.
Notes: Some images included in the instruction to be applied to Gazebo runtime
are publicly provided by JAXA, Japan Aerospace Exploration Agency, for science
and educational purposes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Apr 27 2016 TORK <dev@opensource-robotics.tokyo.jp> - 0.1.6-0
- Autogenerated by Bloom

* Wed Apr 27 2016 TORK <dev@opensource-robotics.tokyo.jp> - 0.1.5-0
- Autogenerated by Bloom

* Fri Nov 06 2015 TORK <dev@opensource-robotics.tokyo.jp> - 0.1.4-0
- Autogenerated by Bloom

* Sat Apr 11 2015 TORK <dev@opensource-robotics.tokyo.jp> - 0.1.3-0
- Autogenerated by Bloom

* Thu Apr 09 2015 TORK <dev@opensource-robotics.tokyo.jp> - 0.1.2-0
- Autogenerated by Bloom

* Thu Apr 09 2015 TORK <dev@opensource-robotics.tokyo.jp> - 0.1.1-0
- Autogenerated by Bloom

* Sun Mar 22 2015 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.0-0
- Autogenerated by Bloom

