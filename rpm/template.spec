Name:           ros-indigo-tetris-gazebo
Version:        0.1.4
Release:        0%{?dist}
Summary:        ROS tetris_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/tetris_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-plugins
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-gazebo-ros-control
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rosbash
Requires:       ros-indigo-tetris-description
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gazebo-plugins

%description
This package contains specific ROS simulation setting for hakuto robots. Note:
&quot;models&quot; directory is temporary and should be removed once this
pullrequest to gazebo_model gets merged.

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
* Fri Nov 06 2015 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.4-0
- Autogenerated by Bloom

* Sat Apr 11 2015 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.3-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.2-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.1-0
- Autogenerated by Bloom

* Sun Mar 22 2015 Isaac I.Y. Saito <iiysaito@opensource-robotics.tokyo.jp> - 0.1.0-0
- Autogenerated by Bloom

