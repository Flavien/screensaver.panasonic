Panasonic TV Screensaver
========================

This Kodi screensaver add-on turns off a Panasonic TV when it activates.

Instructions
------------

Before using this screensaver, you must configure the hostname of the TV. Create a ``settings.xml`` file in the ``userdata\addon_data\screensaver.panasonic`` folder with the following content:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<settings>
  <host>HOSTNAME</host>
</settings>
```

Replace ``HOSTNAME`` with the hostname of the TV, for example ``192.168.0.10``.

License
-------

Copyright 2016 Flavien Charlon

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
